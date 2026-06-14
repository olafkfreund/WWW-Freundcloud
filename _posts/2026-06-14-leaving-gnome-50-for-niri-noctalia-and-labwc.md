---
layout: post
title: "Leaving GNOME 50 for niri, Noctalia, and labwc"
date: 2026-06-14 13:15:05 +0100
permalink: /blog/leaving-gnome-50-for-niri-noctalia-and-labwc/
tags: [nixos, devops]
comments: true
excerpt: >-
  GNOME 50 spent a few weeks falling apart on my machines, so I rebuilt the
  desktop around niri, Noctalia, and labwc — and ended up doing far more with
  far less effort.
---

I didn't go looking for a new desktop. GNOME went looking for the door.

GNOME 50 (gnome-shell 50.1, riding nixos-unstable) has been quietly falling
apart on my fleet for weeks. Visual glitches that survive a redraw. Sessions
that hang on the way out. The shell deciding, mid-workday, that it would rather
not. None of it was catastrophic on its own — it was the steady tax of *babysitting
the thing that's supposed to get out of my way*. When the layer that's meant to
be invisible starts demanding attention, that's the signal.

So I rebuilt it. The whole desktop now runs on three small, sharp tools instead
of one large fragile one.

## The new stack

- **[niri](https://github.com/YaLTeR/niri)** — a scrollable-tiling Wayland
  compositor, and the primary workflow. Windows live on an infinite horizontal
  strip of columns instead of being crammed onto one screen.
- **labwc** — a tiny floating wlroots compositor as the fallback session, for the
  rare moments I want plain stacking windows.
- **[Noctalia](https://github.com/noctalia-dev/noctalia)** — a Quickshell-based
  shell: bar, launcher, control-center, notifications. The bits GNOME bundles,
  unbundled.
- **greetd + the Noctalia greeter** — GDM is gone. The login screen is now a
  greetd session that matches the rest of the desktop, listing niri, labwc, and
  (yes, still) GNOME as choices.

The honest caveat first: swapping the *greeter* doesn't fix GNOME's glitches —
that's a session problem, not a login problem. The greeter swap is about not
shipping a whole second display manager I no longer use. The glitch fix is
simply *not running GNOME as my session.*

## Doing more with less effort

This is the part I didn't expect. I assumed a tiling compositor would be a
trade: more control, more fiddling. niri is the opposite. Scrollable tiling means
I stop *managing* windows entirely — no dragging, no snapping, no hunting for the
half-tiled thing that drifted off-screen. New windows open full-width; I scroll
columns with `Mod+H/L` or `Mod+scroll`; I never think about geometry again.

Then the small wins stack up. A few that earn their keep daily:

```text
Mod+S            screenshot — interactive region/window/output picker
Mod+Shift+R      screen recording — hardware-encoded, toggle on/off
Mod+Ctrl+Shift+F windowed "fake" fullscreen — for Google Slides etc.
Mod+O            overview — zoomed-out view of every column
```

Screenshots and recordings are wired straight into the compositor (the recorder
is hardware-encoded `wl-screenrec`), which matters because I capture a *lot* when
I'm working through a problem. "Fake" fullscreen tells an app it went fullscreen
while leaving it a normal window — presentations stop hijacking the monitor. None
of this needed an extension, a tweak tool, or a settings daemon. It's a few lines
of config.

## It's all declarative

Because this is [NixOS]({{ '/kb/' | relative_url }}), the entire desktop is
code. niri's keybinds, the Noctalia shell, the greeter, even monitor brightness
over DDC/CI (`ddcutil`) — all in the flake, all reproducible across the P620
workstation and the Razer laptop from the same modules.

Theming is the satisfying bit. Everything pulls from one Stylix base16 palette
(gruvbox-dark), so the colour flows outward: niri's window borders, the Noctalia
bar, terminals, GTK and Qt apps — one source of truth, no per-app theme files
fighting each other. I generate Noctalia's palette straight from the Stylix
colours, so when the scheme changes, the shell changes with it.

```nix
# the entire "make windows look right" diff, conceptually
programs.niri.settings.layout = {
  default-column-width.proportion = 1.0;   # full-width, not niri's half
  border = {
    enable = true;
    width = 2;
    active.color = "#${colors.base0B}";    # same green everywhere
  };
};
```

Electron apps, the usual Wayland sore spot, just work — `NIXOS_OZONE_WL=1` was
already in the shared environment, so Slack, VS Code, and friends render natively
with no blurry XWayland fallback.

## Was it worth it?

The whole switch landed in [one PR](https://github.com/olafkfreund/nixos_config/pull/906)
this weekend. A few days in, the desktop has stopped being a thing I notice — which
is the highest compliment I can pay it. GNOME 50 may well stabilise; unstable is
unstable, and that's the deal I signed up for. But I'm not going back. niri turned
window management from a chore into something that happens *for* me, and a glitchy
shell turned out to be exactly the push I needed to find that out.

Less desktop. More work done. That's the trade I'll take every time.
