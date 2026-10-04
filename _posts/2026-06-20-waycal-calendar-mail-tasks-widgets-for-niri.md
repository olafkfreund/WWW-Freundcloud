---
layout: post
title: "waycal: Calendar, Mail and Tasks on niri, driven by one CLI"
date: 2026-06-20 12:00:00 +0100
permalink: /blog/waycal-calendar-mail-tasks-widgets-for-niri/
tags: [wayland, niri, quickshell, nix, gruvbox]
comments: true
excerpt: >-
  Why I built waycal: three Quickshell desktop widgets for calendar, mail and
  tasks on niri that own no credentials and speak no Google API, because the gog
  CLI already does.
---

I run a tiling Wayland session on [niri](https://github.com/YaLTeR/niri). It is
fast and out of my way, but the desktop-widget ecosystem I left behind in GNOME
and KDE does not follow me there. The tray applets and calendar popups either do
not run under a `wlr-layer-shell` compositor or feel grafted on. What I actually
wanted was small: a glance at what is next on my calendar, who has emailed me, and
what is still on my task list, sitting quietly on the desktop.

So I built **[waycal](https://github.com/olafkfreund/waycal)** — three independent
[Quickshell](https://quickshell.org) widgets for calendar, mail and tasks. The
full write-up and getting-started guide live on its own
**[Gruvbox-dark docs site](https://olafkfreund.github.io/waycal/)**. Here is why
it exists and the one design decision that shapes everything else.

## The usual approach, and why I skipped it

The obvious way to put your Google Calendar on the desktop is to have the widget
talk to the Google Calendar and Gmail APIs directly. That means embedding an OAuth
client in the widget, shipping client secrets, requesting scopes, and running a
token-refresh loop. For a read-only glance at data I already reach from the
terminal every day, that is a surprising amount of credential-handling surface to
bolt onto a desktop applet.

I did not want the widget to own any of that. I already have a CLI on this machine
that authenticates to Google and prints JSON: a tool called `gog` that speaks
Calendar, Gmail, Tasks and more from stored OAuth tokens. If one CLI already
covers all three services, then one widget codebase can host all three widgets on
top of one backend pattern, and the credentials stay entirely with the tool built
to hold them.

## The inspiration

Two projects pointed the way. The first is
[waylandar](https://github.com/samjoshuadud/waylandar), a Quickshell calendar
widget whose whole cleverness is its frontend-to-backend contract: a process
prints a JSON array to standard output, and QML calls `JSON.parse` on it. No
sockets, no IPC files, no shared state on disk. waycal keeps exactly that contract
and discards the rest of the Google-API machinery.

The second is the `gog` CLI itself. Because it already returns JSON for Calendar,
Gmail and Tasks, the "backend" for waycal is not an API client at all. It is a
roughly 300-line, standard-library-only Python adapter that runs `gog --json ...`,
normalizes the output into a small uniform schema, and prints it. If anything
fails it prints `{"error": "...", "needsAuth": true}` instead, so a widget can show
a hint rather than crash. The QML always receives valid JSON.

The palette is Gruvbox, the same retro-warm dark theme behind my
[Muninn portal](/blog/introducing-muninn-my-gruvbox-github-portal/). It is calm and
legible on a dark tiling desktop, and the docs site wears it too.

## How it fits together

```
niri keybind  ->  qs -c waycal ipc call <target> toggle
                          |
   systemd user service (EnvironmentFile: GOG_KEYRING_PASSWORD, GOG_ACCOUNT)
                          |  spawns, inherits env
       QML Process  ->  waycal-fetch <cmd>      (thin Python adapter, stdlib only)
                          |  spawns, inherits env
                      gog --json ...            (Google Calendar / Gmail / Tasks)
```

Each widget is its own layer-shell surface with its own IPC target, so calendar,
mail and tasks toggle separately and live wherever I place them. The calendar has
an always-on agenda card plus a full-month dashboard overlay; mail shows unread
threads with a badge count; tasks lists what is open and lets me tick a checkbox to
complete one in place, which simply runs `gog tasks done` and refreshes.

## The one constraint worth calling out

`gog` stores its OAuth refresh token in a file keyring. In an interactive terminal
it can prompt for the password to unlock it. The widgets run non-interactively, so
there is no prompt to answer, which means `gog` needs the password as
`GOG_KEYRING_PASSWORD` in its environment.

This is the single thing you have to set up, and it is exactly the kind of secret
that should not sit in a shell profile. waycal handles it the declarative way:
a Nix flake and a home-manager module install the UI, write the config, and run
Quickshell as a systemd user service whose `EnvironmentFile` is an
[agenix](https://github.com/ryantm/agenix) or
[sops-nix](https://github.com/Mic92/sops-nix) secret. Every `waycal-fetch` and
`gog` the UI spawns inherits it, and nothing lands in the Nix store.

```nix
programs.waycal = {
  enable = true;
  account = "you@example.com";
  keyringPasswordFile = config.age.secrets."waycal-gog".path;
  settings = {
    agenda_days = 7;
    mail_query  = "in:inbox is:unread";
    task_lists  = "all";
  };
};
```

## Try it

The [getting-started guide](https://olafkfreund.github.io/waycal/getting-started/)
covers the niri keybinds, the configuration, and a set of real examples:
narrowing the mail query to only what needs you, pinning two calendars, completing
a task from the overlay, and inspecting exactly what `gog` returned when a field
looks off. If you only want to see the backend work, one command is enough:

```bash
nix run github:olafkfreund/waycal#waycal-fetch -- agenda --days 7
```

The code is MIT licensed and on
[GitHub](https://github.com/olafkfreund/waycal). Next on the roadmap: desktop
reminder notifications and live Gruvbox theming through matugen, since the QML
`Theme` singleton is already the single source of every colour.
