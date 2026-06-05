---
layout: post
title: "Backstage the NixOS way: a portal for 71 repos, declared"
date: 2026-06-05 12:30:00 +0100
permalink: /blog/backstage-the-nixos-way/
tags: [nixos, backstage, infrastructure, agenix, podman, tailscale]
comments: true
excerpt: >-
  I installed Spotify's Backstage on p510 yesterday. The interesting bit
  isn't that it works — Backstage works fine anywhere — it's that the
  whole thing is one PR in `nixos_config`, every secret is encrypted at
  rest with agenix, the image is SHA-pinned through CI, the URL is
  HTTPS-terminated by Tailscale Serve, and all 71 of my GitHub repos
  onboard themselves via a daily PR-bot. No `nix-env`. No `:latest`.
  No certbot. Notes on what fought back.
---

I wanted [Backstage](https://backstage.io) — Spotify's developer
portal — running on my home lab. The "why" is small: I have 71 repos
across personal + Freundcloud and I keep losing the thread of which one
does what. Backstage's software catalog is the canonical answer: one
page that says "here are your things, here's who owns them, here's
where the docs live."

The catch: Backstage has effectively **zero first-class NixOS support**.
There's an [open package
request](https://github.com/NixOS/nixpkgs/issues/379438) and one
abandoned community flake with a single star. Nothing usable. And
Backstage isn't a binary — it's a Yarn 4 monorepo you scaffold per
deployment, customize with plugins, and bake into a Docker image.

So this is a write-up of the "NixOS way" install: declarative, version-
controlled, no hidden state, no manual `docker run` invocations to
forget. Plus the four things that fought back hardest.

## The shape

```text
                          https://p510.tail833f7.ts.net/backstage
                                         ▲
                                         │  Tailscale Serve
                                         │  (HTTPS terminates here)
                                         ▼
       ┌─────────────────────────────────────────────────────┐
       │ p510                                                │
       │                                                     │
       │  ┌────────────┐    backstage-net    ┌────────────┐  │
       │  │ podman:    │◀──────podman───────▶│ podman:    │  │
       │  │ backstage  │     bridge DNS      │ backstage- │  │
       │  │ :7007 (lo) │                     │ postgres   │  │
       │  └────────────┘                     └────────────┘  │
       │         ▲                                           │
       │         │ EnvironmentFile=/run/backstage/env-*      │
       │         │                                           │
       │  ┌──────┴──────────┐                                │
       │  │ backstage-env-  │ ← agenix at activation         │
       │  │ setup (oneshot) │                                │
       │  └─────────────────┘                                │
       └─────────────────────────────────────────────────────┘
```

Three systemd units, two containers, one shared podman bridge network,
four agenix-encrypted secrets, one Tailscale Serve path. Everything
declared in `modules/services/backstage.nix` (~250 lines) and toggled
by a single `features.backstage.enable = true` on p510.

## The app repo: scaffolded, CI'd, ghcr-published

The Backstage app itself lives in a separate repo,
[`olafkfreund/backstage`](https://github.com/olafkfreund/backstage).
It's the standard `@backstage/create-app` scaffold with two changes:

- `app-config.production.yaml` overrides for Postgres connection,
  GitHub OAuth, and `auth.allowGuestAccess: true` for read-only browsing
- `.github/workflows/build.yml` that yarn-installs, type-checks, lints,
  tests, builds the backend bundle, and publishes a multi-tag image to
  `ghcr.io/olafkfreund/backstage` (both `:latest` and `:sha-<commit>`)

The CI job's final step is the bit that matters for NixOS:

```bash
echo "ghcr.io/olafkfreund/backstage@sha256:e0284ab..."
```

That **SHA digest** — not `:latest` — is what the NixOS module pins.
Updates are explicit `nixos_config` commits. A leaked GHCR token can't
quietly swap the running image; the worst it can do is push to a tag
nothing references.

## The NixOS module: secrets at runtime, never in the store

The module structure mirrors my existing
[`skill-pool`](https://github.com/olafkfreund/nixos_config/blob/main/modules/services/skill-pool.nix)
pattern. Two containers, one secret-to-env bridge, all hardening
inherited from the systemd defaults plus a `--memory=2G` cap so a
Backstage memory leak can't fight Plex transcoding for RAM.

The interesting part is the agenix wiring. Backstage's container reads
env vars for its Postgres password, GitHub OAuth client ID/secret, and
catalog PAT. I do NOT want those values in the Nix store — anyone who
can read `/nix/store/*` would see them. So the pattern is:

```nix
# 1. Declare the secrets — agenix decrypts to /run/agenix/* at boot
age.secrets.backstage-github-token = {
  file = ../../secrets/backstage-github-token.age;
  mode = "0400";
};

# 2. One-shot service that reads agenix files and writes
#    /run/backstage/env-* on tmpfs (cleared every boot)
systemd.services.backstage-env-setup = {
  before = [ "podman-backstage.service" "podman-backstage-postgres.service" ];
  serviceConfig = { Type = "oneshot"; RemainAfterExit = true; };
  script = ''
    set -euo pipefail
    umask 077
    mkdir -p /run/backstage
    GH_TOKEN=$(cat /run/agenix/backstage-github-token)
    # ... cat the others, write env-postgres + env-backstage ...
    chmod 0400 /run/backstage/env-postgres /run/backstage/env-backstage
  '';
};

# 3. Containers consume the env files via EnvironmentFile
virtualisation.oci-containers.containers.backstage = {
  image = "ghcr.io/olafkfreund/backstage@sha256:49f4e8e...";
  environmentFiles = [ "/run/backstage/env-backstage" ];
  # ...
};
```

End result: the only place the plaintext PAT exists at rest is in
`/run/agenix/` (tmpfs, root-only, mode 0400) and `/run/backstage/env-*`
(same). Both gone on reboot. The Nix store contains zero secret bytes.

## The four things that fought back

### 1. Backstage's seed `yarn.lock` is a lie

CI's `yarn install --immutable` rejected the install on the first run:
"The lockfile would have been modified by this install, which is
explicitly forbidden." The scaffolder ships a *seed* lockfile that needs
materializing on first install. Fix: run `yarn install` locally once,
commit the resulting `yarn.lock` (31,513 line diff), push. Then CI's
`--immutable` is happy. Annoying, but understandable.

### 2. `yarn build:backend --config X` resolves X from packages/backend/

I passed `--config app-config.production.yaml` to the build step.
Backstage looked for it at `packages/backend/app-config.production.yaml`
and failed with "Config file does not exist." Production overrides are
applied at *runtime* via the Dockerfile `CMD`, not bundled at build
time. Dropping the flag fixed it.

### 3. GHA `cache-to: type=gha,mode=max` needs buildx

GitHub-hosted runners ship with Docker's default driver, which doesn't
support cache export to GHA. The fix is one line: add
`docker/setup-buildx-action@v3` before the build step. It swaps in the
`docker-container` driver which does. CI went from 1m48s to a cached
3m51s and now ~3m for subsequent builds.

### 4. `agenix.service` doesn't exist (this one bit me at deploy time)

My module declared `requires = [ "agenix.service" ]` on the env-setup
unit. The deploy succeeded, but starting the service failed with "Unit
agenix.service not found." Reason: **agenix runs in the NixOS
*activation phase*, not as a systemd unit.** `/run/agenix/*` is
populated before systemd reaches `multi-user.target`. So the dep is
implicit; no explicit ordering needed. Removing the two lines fixed it.

There was also a podman container-to-container networking gotcha —
the backstage container couldn't reach `host.containers.internal:5435`
because Postgres was bound to the host's `127.0.0.1`, which the podman
bridge gateway can't see. Fix: create a shared `backstage-net` bridge
network at activation, put both containers on it, drop the host port
mapping on Postgres entirely, and address Postgres by container name
(`backstage-postgres:5432`). Cleaner anyway — Postgres no longer
appears in the host's `ss -tlnp` output at all.

## Importing 71 repos without touching each one (much)

Backstage's `GithubEntityProvider` scans a GitHub account for
`catalog-info.yaml` files. Repos without one are silent. With 71 repos
spread across personal + Freundcloud + assorted forks, I wasn't going
to hand-add catalog files to each.

Two cooperating mechanisms ship with the install:

1. **`GithubEntityProvider`** scans `olafkfreund/*` every hour. Any
   repo with `catalog-info.yaml` gets pulled into the catalog.
2. **`.github/workflows/catalog-onboard.yml`** runs daily at 06:17 UTC.
   It lists repos missing `catalog-info.yaml`, picks the first 10, and
   opens a PR adding a templated file. Lifecycle is derived from repo
   state (`archived` → `deprecated`, `fork` → `experimental`, otherwise
   `production`); tier from visibility; tags from repo topics. The bot
   is idempotent — it skips repos with open onboarding PRs.

At 10 PRs/day the full 71 repos onboard in ~8 days. With
`-f max_prs=80` it's one workflow run. Up to my future self how
aggressively to ship.

The bot needs a separate fine-grained PAT — `BOT_PAT` — with
`Contents: Read and write` and `Pull requests: Read and write` across
all my repos. The PAT Backstage uses for *discovery* is read-only by
design and intentionally can't be reused for writes. Read/write
separation: if the discovery PAT leaks, the worst case is information
disclosure; if the bot PAT leaks, the worst case is malicious PRs.
Different blast radii, different rotation cadences.

## What "the NixOS way" actually bought me

A few things:

- **One PR to land it all.** Module + secrets + docs + host enable
  flag, all in
  [PR #737](https://github.com/olafkfreund/nixos_config/pull/737).
  Reviewable end-to-end. Revertable end-to-end. No "remember to run
  `docker compose up -d` on the box" step.

- **Atomic rollback.** If something turns out to be wrong on p510,
  `sudo nixos-rebuild switch --rollback` puts the previous generation
  back. Backstage containers stop, network gets torn down,
  `/run/backstage` clears. No leftover bridges, no orphan volumes.

- **Reproducible from scratch.** `git clone nixos_config` →
  `just quick-deploy p510` rebuilds the same Backstage with the same
  image SHA, the same Postgres password (encrypted in the repo, so any
  authorized host key can decrypt), the same Tailscale path. The whole
  setup is in the repo or in a single GitHub OAuth App I registered
  once.

- **Honest secret handling.** `grep -ri 'github_pat_' .` returns
  nothing. `grep -ri 'postgres password' .` returns documentation
  only. The Nix evaluator never reads any secret byte, because every
  read happens at runtime against `/run/agenix/`.

- **TLS for free.** No `certbot`, no `acme.sh`, no DNS-challenge
  juggling, no cert renewal cron. Tailscale Serve terminates HTTPS at
  the tailnet edge using its built-in MagicDNS certificates. The
  Backstage container speaks plain HTTP on `127.0.0.1:7007` and never
  knows TLS exists.

- **No "production" vs "dev" drift.** The same image runs on whichever
  host I point at, the same agenix secrets get loaded (re-keyed to
  whatever host key is in `secrets.nix`), the same Tailscale path
  pattern lights up.

## Where it is now

Backstage is live at `https://p510.tail833f7.ts.net/backstage`. It
shows me + one System (`freundcloud-infra`) + one Component
(`nixos_config`) right now. The catalog-onboard cron fires tomorrow at
06:17 UTC and over the next ~week the other 70 repos walk themselves
in via PRs. Each PR is one merge button — and editable to add owner /
domain / dependency richness as I figure out what I actually want.

Open in the next iteration:

- TechDocs (needs an S3-compatible storage backend; MinIO container is
  the obvious match)
- Kubernetes plugin (if/when I revive the k3s microvms that have been
  dormant since I built them)
- A nightly `pg_dump` to `/var/backups` so a corrupted volume doesn't
  cost catalog history
- GitHub App instead of fine-grained PATs (narrower scopes, single
  rotation UI, cleaner audit)

The whole thing took roughly half a day spread across an evening. Half
of that was Backstage's `app-config.yaml` tuning, which is OS-agnostic
pain. The other half was the four gotchas above. The "Nix wiring" —
the module, the agenix bridge, the systemd dependencies, the
container network — was the EASY part, because the patterns already
existed elsewhere in
[nixos_config](https://github.com/olafkfreund/nixos_config) and I
copy-pasted shamelessly from
[`modules/services/skill-pool.nix`](https://github.com/olafkfreund/nixos_config/blob/main/modules/services/skill-pool.nix).

That's the real win of having spent the last year building everything
declaratively: when you decide you want a developer portal, you've
already written most of the boilerplate. The new module is mostly the
parts that are genuinely Backstage-specific.
