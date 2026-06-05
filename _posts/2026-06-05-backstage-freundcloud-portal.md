---
layout: post
title: "Backstage portal: how the freundcloud home lab now sees itself"
date: 2026-06-05 23:13:16 +0100
permalink: /2026/06/backstage-freundcloud-portal/
tags: [platform, nixos, devops]
comments: true
excerpt: >-
  Four phases in one evening: a Gruvbox theme, wiring eight dormant GitHub
  plugins, GitLab parity, and real-time webhooks through a Tailscale Funnel.
  What worked, what fought back, and how the home lab portal finally became
  fun to look at
---

The home lab has had a [Backstage]({{ '/work/#backstage' | relative_url }})
portal for a while. It signed in, the catalog populated, GitHub OAuth worked.
But it also looked exactly like Spotify's scaffolded default and most of the
plugins were dormant — installed in `package.json`, never wired up. This
session was about closing that gap. Four phases. Fifteen image bumps. One
working webhook bridge.

## Phase A — make it look like the rest of the world I live in

Gruvbox Dark + Gruvbox Light, registered with two `ThemeBlueprint.make()`
extensions, both built from `createUnifiedTheme()` with the full
Backstage-extended palette (navigation, status, banner, bursts — the lot).
Then a new cloud-and-sine-wave SVG logo in `LogoIcon.tsx` /
`LogoFull.tsx`, using `fill: currentColor` so it reads cleanly on either
theme without a per-theme variant. JetBrains Mono at the theme level so
the whole UI looks like the terminal next to it.

The one surprise: when I wrote my `homePageOverride`, I forgot to pass
`title: 'Home'` and `icon: <HomeIcon />` through to `originalFactory`.
Backstage's new declarative-frontend sidebar derives the Home nav item
from the page extension itself — no `NavItemBlueprint` exists for it —
so the moment those props go missing, the Home link silently vanishes
from the menu. Fix is two lines. Lesson is: in the new system,
everything is an extension, and overriding a page means inheriting all
of its required props.

## Phase B — wiring dormant plugins, then unwiring three of them

Eight GitHub plugins were sitting in `package.json` doing nothing. Half
just worked: `@roadiehq/backstage-plugin-github-insights` and
`@backstage-community/plugin-github-deployments` ship `/alpha` bundles,
so `@backstage/plugin-catalog/alpha` auto-discovers them in
`node_modules` and attaches their content as entity tabs and overview
cards. Free.

The other three were the legacy ones. `@backstage/plugin-github-actions`,
`@roadiehq/.../github-pull-requests`, `@roadiehq/.../security-insights`.
They use `createRoutableExtension` with an internal `rootRouteRef` —
and in the declarative frontend, the new router doesn't know where to
mount that ref unless you wire `app.routes.bindings` explicitly. Both
`compatWrapper` and `convertLegacyPlugin` from
`@backstage/core-compat-api` failed to do it for me. After three
iterations I just uninstalled them.

A few hours later I learned `@backstage-community` has shipped
modernised replacements: `plugin-github-actions`, `-issues`,
`-pull-requests-board`, plus `-tech-insights`. All have proper alpha
bundles. All worked first try. The GitHub Actions entity tab now shows
the very CI runs that deployed the plugin.

## Phase C — GitLab parity, sitting idle on purpose

`@backstage/plugin-catalog-backend-module-gitlab` for discovery,
`@backstage/plugin-scaffolder-backend-module-gitlab` for 12 new
`gitlab:*` scaffolder actions, and
`@immobiliarelabs/backstage-plugin-gitlab/alpha` on the frontend. The
catalog provider runs hourly. There are currently zero GitLab projects
in the personal account, so it discovers nothing — but the day a
`catalog-info.yaml` lands on a GitLab project, it'll show up with full
Pipelines, MRs, Releases, Code Owners, Coverage, and README tabs.

The immobiliare plugin needed a config nudge: it attaches nine
Overview cards to **every** entity without checking for the
`gitlab.com/project-slug` annotation. Each card fires a GitLab API
call with whatever slug it can find — including the GitHub one — and
renders "wrong project_slug or project_id" nine times per page. I
disabled them all in `app-config.production.yaml` until there's GitLab
data worth showing.

## Phase D — real-time freshness via a Tailscale Funnel

This is the one I'm proud of. The widgets used to refresh every five
minutes. The catalog discovery ran hourly. I wanted the home page to
update on a push the instant GitHub knew about it.

`@backstage/plugin-events-backend-module-github` exposes
`POST /api/events/http/github`, HMAC-validates incoming webhooks
against `GITHUB_WEBHOOK_SECRET`, and publishes onto a `github` topic
on the in-process events bus. The secret is a 64-char hex string from
`openssl rand -hex 32`, agenix-encrypted and decrypted at activation
on the p510 host:

```bash
openssl rand -hex 32 | agenix -e secrets/backstage-github-webhook-secret.age
```

The bridge from events bus to UI is a small custom backend module —
about 30 lines — that subscribes to the `github` topic and re-broadcasts
on the `github:activity` signals channel:

```ts
export const signalsGithubBridge = createBackendModule({
  pluginId: 'signals',
  moduleId: 'github-bridge',
  register(reg) {
    reg.registerInit({
      deps: { events: eventsServiceRef, signals: signalsServiceRef, logger: coreServices.logger },
      async init({ events, signals, logger }) {
        await events.subscribe({
          id: 'github-activity-bridge',
          topics: ['github'],
          async onEvent(params) {
            const eventName = params.metadata?.['x-github-event'] ?? 'unknown';
            const repo = (params.eventPayload as any)?.repository?.full_name ?? 'unknown';
            logger.info(`signals/github-bridge: rebroadcasting ${eventName} from ${repo}`);
            await signals.publish({
              recipients: { type: 'broadcast' },
              channel: 'github:activity',
              message: { event: eventName, repo, timestamp: new Date().toISOString() },
            });
          },
        });
      },
    });
  },
});
```

The Recent Activity widget on the home page now calls
`useSignal('github:activity')` and re-fetches on every push. The
5-minute `setInterval` poll is still there as a fallback for clients
that lose the WebSocket — but most of the time, the widget updates in
under a second.

### Tailscale Funnel was the interesting bit

GitHub needs a public HTTPS URL to deliver to. The Backstage portal is
behind Tailscale Serve on the host's tailnet hostname and is tailnet-only.
So is everything else on port 443: Plex, Sonarr, Radarr, Lidarr, NZBGet,
Tautulli, Prowlarr, Overseerr, the lot. Tailscale Funnel is per-port, not
per-path — funnel 443 and you expose every one of those services publicly.
That's a terrible idea.

Funnel does support 443, 8443, and 10000. Nothing was on 8443.

```nix
${pkgs.tailscale}/bin/tailscale funnel --bg --https=8443 \
  --set-path=/api/events/http/github \
  http://localhost:7007/api/events/http/github
```

The target URL needs the path repeated — `--set-path` strips the matched
prefix when forwarding, so a bare `http://localhost:7007` target would
send `:8443/api/events/http/github` to `localhost:7007/`, which is the
React app root. POSTs to `/` give 404; GETs return the index page. I
spent twenty minutes on that one.

With the public URL alive, registering on all 69 non-archived
`olafkfreund` repos took about thirty seconds:

```bash
SECRET=$(agenix -d secrets/backstage-github-webhook-secret.age)
URL="https://<your-funnel-host>:8443/api/events/http/github"
gh repo list olafkfreund --limit 200 --json name --jq '.[].name' | while read REPO; do
  gh api -X POST "/repos/olafkfreund/$REPO/hooks" \
    -F "events[]=push" -F "events[]=pull_request" \
    -F "events[]=issues" -F "events[]=release" \
    -F "config[url]=$URL" -F "config[content_type]=json" \
    -F "config[secret]=$SECRET" --silent
done
```

68 created, 1 already existed from the smoke test, 0 failures. Every
push, pull request, issue, and release on any of my repos now hits the
events backend within ~100ms, the bridge logs `rebroadcasting <event>
from <repo>`, and the home widget refreshes without a manual reload.

## The entity pages got noticeably better too

After all four phases I went back and enriched the `catalog-info.yaml`
on both repos — proper titles, multi-line descriptions, eight tags
each, real links, the full set of Backstage annotations
(`techdocs-ref`, `source-location`, `view-url`, `edit-url`,
`project-readme-path`). The result is that the entity pages stopped
looking like raw `kubectl get` output and started looking like
documentation.

## The deploy loop

Every backstage repo PR triggers a CI build that pushes
`ghcr.io/olafkfreund/backstage@sha256:...`. Every digest change is a PR
on `olafkfreund/nixos_config` bumping `modules/services/backstage.nix`.
Every nixos PR I admin-merged triggered `just p510` and rolled the
podman container forward. Fifteen images this session:

```
adefc77 → c707f8d → 9082e12 → 4f79f5d → 349d3c10
→ cc024bb3 → 3458fc58 → 149315cd → 14ce8351 → 05cd3f92
→ e22ae753 → 58af6263 → d4107d8f → 3921d610 → 028ca273
```

The cadence forced confidence. Nothing could be half-merged. Every
commit had to land cleanly because the deploy was always one click
away.

## What's still on the list

Three things I deliberately kicked down the road:

- **Issue [#18](https://github.com/olafkfreund/backstage/issues/18)** —
  proper `convertLegacyRouteRef` + `app.routes.bindings` for the legacy
  routable plugins. The community successors covered the user-visible
  scope, so this is mostly a "do it right one day" hygiene item.
- **A `python-service-gitlab` template variant** — 30 minutes of work,
  zero value until I actually have a GitLab project to scaffold into.
- **Kubernetes plugin** — the k3s microvms on p510 are dormant. The
  moment they come back online, this gets a one-evening pass.

Everything else is shipped, deployed, documented in the portal's own
TechDocs, and looking — finally — like the rest of the freundcloud
universe.
