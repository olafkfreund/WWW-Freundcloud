---
status: approved
issue: 9
author: olafkfreund
---

# Intent: Showcase the latest projects — nixarchy, Agentic SDLC, nix-skills

## Problem

`/showcase/` (`showcase.md`) is behind the GitHub account:

- **nix-skills** (`olafkfreund/nix-skills`, updated 2026-09-26) is not on the site
  at all. It ships ten source-backed Nix/NixOS agent skills with a docs site, a demo VM
  and a Home Manager module.
- **nixarchy** (94 stars, the most active repo) has a section with two infographics
  but no real screenshots, although its repo has a full set under `docs/img/`
  (desktop, menus, search, feature GIFs).
- **Agentic SDLC** (`agentic-sdlc-showcase`) has a section with only a podcast embed.
  No image, even though the repo publishes an infographic
  (`site/assets/img/governing-software-in-the-age-of-ai.webp`) and a screencast page.

The page's hero says "Seventeen systems", and that count and the at-a-glance grid
would need to change too.

## Proposed outcome

On `/showcase/`:

- A new **nix-skills** section, with an at-a-glance card, a description taken from its
  README (what it is, the ten skills, three ways to start) and links to docs and source.
- The **nixarchy** section shows real screenshots from the repo alongside the existing
  infographics.
- The **Agentic SDLC** section shows the repo's infographic and links to the screencast.
- The hero count, the grid and the front-matter description all match the new set.

## Affected users and systems

- `showcase.md`, with new images under `assets/img/showcase/`.
- Site visitors. Deploys to www.freundcloud.com through `.github/workflows/pages.yml`.

## Constraints

- Nothing under `kb/` is edited. Don't touch the untracked `infographics/` folder:
  it only holds sources for images already on the site (the Fides, Bifrost and Janus
  ones, among others).
- Keep image weight reasonable. The repo GIFs are 0.3–1 MB each, so use a few stills
  (jpg/webp) rather than every GIF.
- Follow the existing section pattern: `figure.shot`, the `shot-grid`, lazy loading
  and meaningful alt text.
- html-proofer must stay clean.

## Open questions

1. You wrote "nix-skill". The repo is **nix-skills**. Is that the right one?
   (`nixi-nixarchy` and `nixarchy-voice` are also recent, if you meant those as well.)
2. nix-skills has **no screenshots**. Is text plus a code snippet OK? Or should I
   capture a screenshot of its docs site
   (olafkfreund.github.io/nix-skills), or generate an infographic?
3. For nixarchy, should I use stills only (desktop, menu-ask, search-results), or
   also one or two feature GIFs (e.g. `themes.gif`, `voice.gif`)?
