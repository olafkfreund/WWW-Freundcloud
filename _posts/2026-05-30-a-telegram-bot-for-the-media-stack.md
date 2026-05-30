---
layout: post
title: "A Telegram bot for the media stack"
date: 2026-05-30 14:25:52 +0100
permalink: /blog/a-telegram-bot-for-the-media-stack/
tags: [nixos, ai, agents, platform]
comments: true
excerpt: >-
  Bolted a Telegram bot onto the home media stack today — menu commands plus
  local-Ollama natural language plus inline-action notifications. Here's what
  shipped, why I didn't reach for Claude on the cloud end, and where NixOS
  made it easy.
---

The home media stack has lived behind web UIs for years. Plex on the TV,
Overseerr for requests on a browser, and Sonarr/Radarr only when something's
broken enough to need a forensic check. The natural-language MCP layer I
added to the *arr suite makes Claude on my workstation a great front-end —
but it's a workstation-only front-end. My partner doesn't open Claude. I
don't want to open Claude when I'm slumped on the couch wondering whether
the new Foundation episode landed.

So today's project: a Telegram bot for the home stack. Branch up this
morning, shipped this afternoon, one hotfix in (more on that below).

## What it does

Three surfaces in one service:

- **Slash commands.** `/search Foundation` returns hits from Sonarr and
  Radarr with inline `[➕ Add (all seasons)]` buttons. `/queue` shows
  what's downloading right now. `/status` pings the *arr stack and
  reports who's healthy.
- **Natural language.** Anything that isn't a slash command falls through
  to **Ollama** — the same `qwen2.5:7b` that already runs on my media
  server doing audiobook metadata parsing. Tool-calling format, seven
  curated functions, one fewer hop than going through the MCP servers.
  *"what's downloading right now and is the new Stephen King audiobook
  out yet"* works as one message.
- **Notifications.** Sonarr/Radarr/Overseerr POST their built-in webhooks
  to the bot on port 8090. The bot filters to a small "wins only" set —
  episode imported, request approved, audiobook landed — and pushes the
  message to Telegram with action buttons. Per spec, no failure-noise;
  the people in the house should not be trained to mute the bot.

## Why local LLM

I designed it twice. First pass had Claude on the cloud end. Second pass
— after my partner gave it five seconds of side-eye — moved to Ollama on
the media server. Reasons that mattered:

1. **No data leaves the LAN.** "what audiobooks did Olaf download" is
   exactly the sort of thing I'd rather not stream to a third party even
   if their privacy policy is fine.
2. **Zero recurring cost.** The 7B model already runs on this machine.
   Free incremental load.
3. **It just works.** Tool-calling at 7B on a 3070 Ti is fast enough —
   1–3 seconds per turn once the model is warm.

The trade-off is honest: a 7B model gets confused on long tool chains,
and you'll occasionally read replies that paraphrase the data in a
slightly weird way. Acceptable.

## How NixOS makes this fun

The service definition mirrors my other *arr-stack daemons exactly. One
module file, ~150 lines:

```nix
features.media-bot = {
  enable = true;
};
```

Behind that line: a `DynamicUser` systemd unit with the full hardening
menu (`ProtectSystem=strict`, restricted syscall filter, capped memory
at 512M), an agenix-encrypted env file containing the Telegram bot token
plus duplicated *arr API keys, an agenix-encrypted YAML whitelist of
authorised Telegram user IDs, and a tailscale-only firewall opening for
the webhook receiver. Adding a family member later is
`agenix -e secrets/media-bot-users.age` then `systemctl reload`. SIGHUP
rereads the whitelist; no restart.

The hotfix was the only place I tripped: agenix writes secrets as
root-owned `0400`, which a `DynamicUser` process can't read. The fix —
five lines — was `LoadCredential` in the systemd unit, the same pattern
my Plex MCP module already uses. Caught it on first deploy, hot-patched
it in another PR, redeployed, done. The whole "code is data, modules
compose, declare your intent" thing is real.

## What didn't ship

Things I deliberately cut to make this Phase 1:

- **WhatsApp** — Telegram-only. WhatsApp's bot story is a Meta Business
  form, Twilio per-message charges, or an unofficial bridge that gets
  your number banned. The design has a clean place to slot it later;
  today is not later.
- **Deep links to specific episodes in Plex** — webhook payloads don't
  carry Plex rating keys; I'd have to do a search-by-title lookup after
  every import.
- **`/recent`** — the *arr REST APIs don't have a clean "imported in the
  last 24h" query. The notification fabric covers it anyway.
- **Approval workflows** — everyone in the house has equal permissions
  in v1. If "teen wants to add a season of something I'd rather they
  didn't" becomes a real problem, that's when I'll wire Overseerr's
  approval flow into the bot.

## What's next

This bot is one sub-project of a longer brainstorm about the whole media
stack. Queued: a hardening sweep (one `0400` plaintext password I want
to move to agenix), Bazarr for subtitles, Kometa for collections and
posters, and a Maintainerr-style cleanup pass once the library passes
the size where it matters. Probably in that order.

For now the bot is running on the media host, polling Telegram,
listening for webhooks. The household just got a new toy. Let's see if
it gets used.
