---
status: draft
issue: 11
author: olafkfreund
---

# Intent: About page refresh, RFactory on the start page, nixarchy apps and plugins

## Problem

The site lags what Olaf is doing now:

- **About page (`about.md`).** It doesn't mention the current HSBC engagement.
  The Factory suite gets one line in the open-source section, not a place under
  "What I'm doing now". "Away from the keyboard" still describes NixOS + COSMIC
  Rust applets, though that hobby has since become nixarchy.
- **Start page (`index.md`, "Selected work").** RFactory isn't there.
  `olafkfreund/RFactory` (public) is a meeting-agent web app: an AI bot joins
  Meet, Zoom, Teams or Slack calls to run standups from the CFactory board and to
  make approved changes through the Factory services. It appears nowhere on the
  site. The Factory card still lists four products.
- **Showcase (`showcase.md#nixarchy`).** The entry covers the nixarchy core but
  none of the apps and plugins built around it. About 35 public repos under
  `olafkfreund` are in that family (`nixarchy-*`, `oma*`, `omarchy-*`, `nixi*`):
  the menu, devenv/microvm/distrobox/podman widgets, Flux phone link, omaPOD,
  omateams, meeting mode, voice, the Hyprland settings studio, llm-index, Nixi
  and others.

## Proposed outcome

- `/about/` mentions HSBC (no detail beyond the name), gives the Factory suite a
  paragraph under "What I'm doing now", and says in "Away from the keyboard" that
  the NixOS tinkering became nixarchy. Already drafted in the working tree on this
  branch.
- `/` has an RFactory card in "Selected work", and the Factory card mentions
  RFactory as the fifth product.
- `/showcase/#nixarchy` lists the nixarchy apps and plugins: one line each,
  linking to the repo, grouped so the list scans.

## Affected users and systems

- Files: `about.md`, `index.md`, `showcase.md`. Possibly `cv.md`, `work.md` and
  the about-page open-source paragraph if they also name the four Factory products.
- Visitors to <www.freundcloud.com> (GitHub Pages; deploys from `main`).
- No hosts, services or secrets.

## Constraints

- HSBC: the name only. No team, programme, role or dates.
- Link only to public repos. Private ones (`factory-lab-*`, `factory-runners`,
  `rfactory-fixture`) stay off the site.
- Keep the site's existing card and `.project` markup and CSS. No new styles
  unless the list genuinely needs one.
- CI runs htmlproofer on the built site, so internal links and anchors must
  resolve.

## Open questions

1. **RFactory card target.** No `#rfactory` section exists. Should the card link
   straight to the GitHub repo, or should this task also add a short RFactory
   section to `showcase.md` (and update the "Seventeen systems" count)?
2. **Which apps and plugins.** Your own plugins and apps only, or also the Nix
   packagings of third-party projects (`nixarchy-flea`, `nixarchy-omabroadcast`,
   `nixarchy-gliff-manager`, `nixarchy-hyprflip`, `nixarchy-googlebook-vm`)? And
   what about the non-desktop ones (`nixarchy-bbs`, `mcp-nixarchy`, `nixarchy-pkg`)?
3. **Factory wording elsewhere.** Should `cv.md`, `work.md` and the about page's
   open-source paragraph also move from four products to five, or stay as they are?
