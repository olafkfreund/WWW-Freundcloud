---
layout: post
title: "Of Claude and chores"
date: 2026-05-31 00:04:07 +0100
permalink: /blog/of-claude-and-chores/
tags: [nixos, ai, agents, meta]
comments: true
excerpt: >-
  How I keep claude-code and claude-desktop fresh on NixOS today (custom
  derivations + hourly GitHub Actions watchers + an /update-claude-code skill),
  and how I'm going to close the loop with a scheduled agent. Includes three
  dad jokes about updates and chores I refuse to apologise for.
---

Two things in life are certain: death, and the next `claude-code` release
dropping the moment I sit down to deploy yesterday's. There's a third — the
nixpkgs update for it landing about two weeks later — but that one's optional
if you're willing to do a bit of homework.

So I did the homework. This post is what's wired up, what isn't yet, and some
appalling jokes I refuse to apologise for.

## The problem

`pkgs.claude-code` from nixpkgs lags upstream because it depends on a
maintainer running `update.sh` against the unstable channel. When Anthropic
ships a new CLI on a Tuesday, nixpkgs catches up the *following* Tuesday at
best, sometimes later. Claude Desktop has the same shape — it rides on
[aaddrick/claude-desktop-debian](https://github.com/aaddrick/claude-desktop-debian)'s
build script, which itself rides on the upstream Electron app's release
cadence.

Net result: I'm always a week behind unless I do something about it.

> My package manager said the update could wait. I told it that's just a
> `chore`-able offense.

## What I shipped

Two custom derivations under `pkgs/` in the NixOS repo:

- `claude-code-native` — sources straight from Anthropic's GCS binary channel.
  Immune to the npm-side refactors that broke nixpkgs's build last quarter.
- `claude-desktop-linux` — pinned by commit SHA to the aaddrick fork, with an
  overlay that patches a `sed` pattern upstream uses to copy node-pty native
  binaries into a writable `.unpacked/` directory. (Yes, that was a fun
  evening.)

Both ship a tiny `versions.json` next to the derivation holding the version
string and the per-arch SRI hashes. Bumping is "change three lines, run
`nix build`, commit." Calling that "ergonomic" is generous, but it beats
two weeks of waiting.

```nix
# pkgs/claude-code-native/versions.json (the only file that needs editing)
{
  "version": "2.1.158",
  "sources": {
    "x86_64-linux":  { "hash": "sha256-AAAA…" },
    "aarch64-linux": { "hash": "sha256-BBBB…" }
  }
}
```

## What watches the watchers

Two GitHub Actions workflows live in `.github/workflows/`:

- `claude-code-watch.yml`
- `claude-desktop-watch.yml`

Both run on an hourly cron. They probe upstream — the GCS binary channel for
claude-code, the aaddrick fork's tags for claude-desktop — compare against
what I have pinned in this repo, and if there's drift, they `gh issue create`
with a dedupe key. So when v2.1.159 lands, I get exactly *one* issue
labelled `claude-code-update`, not nine.

Then I run the `/update-claude-code` Claude Code skill, which:

1. Prefetches the new SRI hashes from npm/GitHub.
2. Edits `versions.json` (or `flake.nix` for claude-desktop).
3. Builds + smoke-tests the binary on the current host.
4. Tests the full system closure on all three of my hosts.
5. Opens a PR with the changelog inline.
6. Tells me where the rollback knob is (it's `nixos-rebuild switch
   --rollback`, but you'd be amazed how often that slips your mind at 23:47
   on a Friday).

> Why did the chore commit feel undervalued? It kept getting squashed.

## What's next

The honest answer is "close the loop and stop touching the keyboard." Two
candidates on the table:

**Option A — `/schedule` to a remote agent.** Claude Code has a `/schedule`
command that runs a remote agent on a cron schedule. I'd schedule
`/update-claude-code` to fire either when a watcher issue opens, or hourly
polling the same endpoints, let it do the prefetch-build-test work in the
cloud, and have it open the PR itself. Total work for me: clicking *merge*
on a green PR. Or yelling "no" at one that's red, then merging the next.

**Option B — beef up the GHA workflow.** Same outcome, different runner.
The workflow that opens the issue today could open a PR directly, run
`nix build` in CI, and post results. Cheaper (no Anthropic credit burn,
no remote-agent quota), but harder to debug when something goes sideways
at 03:00, which it will, because that's the only time it ever goes sideways.

I'll probably do (A) first, because the cron-driven remote agent is *also*
the right shape for half a dozen other update chores in this repo —
`warp-terminal`, `copilot-cli`, `antigravity`, `claude-desktop`, the
flake-inputs lock, and so on. One pattern, many beneficiaries. The chore
agent giveth, and the chore agent giveth more.

> I asked the bot to handle my updates. It said "I'm not the maintenance
> type, but I do enjoy a fresh `git fetch`."

## Why bother

Because manual maintenance is the silent killer of side projects. Every
minute spent yak-shaving a version bump is a minute not spent on the actual
thing the tool exists to enable. The whole point of a declarative system
like NixOS is that the *config* is the artefact — but if I'm the one doing
the diff every week, the artefact lives in my head, which means it dies
with me.

So: cron, agents, watchers. Updates as automated chores. The dad jokes are
free.
