---
status: draft
issue: 9
intent: intent/2026-09-28-9-showcase-latest-projects.md
---

# Spec: Showcase the latest projects — nixarchy, Agentic SDLC, nix-skills

## Resolved open questions (defaults, change on review)

The intent was approved without answers to its three questions. This spec uses these
defaults:

1. **"nix-skill" means `olafkfreund/nix-skills`.**
2. **nix-skills gets a real screenshot** of its docs site
   (<https://olafkfreund.github.io/nix-skills/>), taken with headless Chromium.
   No new infographic. If the capture comes out unusable, the section ships as text
   plus the install snippet.
3. **nixarchy uses stills only, no GIFs.** The GIFs are 0.3–1 MB each, and the page
   already carries fourteen image-heavy sections.

## Design

All edits go in `showcase.md`, and new images go in `assets/img/showcase/`. Nothing else
changes. The markup reuses the page's existing patterns: `figure.shot` for the lead
image and `div.shot-grid` with three `figure`s for the rest (see the SARC section,
`showcase.md:174-206`).

### nixarchy (`showcase.md:820`)
Copy these four stills from `olafkfreund/nixarchy` `docs/img/` into
`assets/img/showcase/`, keeping their original format:

| Source | Target | Use |
|---|---|---|
| `desktop/desktop.jpg` | `nixarchy-desktop.jpg` | lead `figure.shot`, after the intro paragraph |
| `desktop/menu-ask.webp` | `nixarchy-menu-ask.webp` | shot-grid |
| `desktop/search-results.jpg` | `nixarchy-search.jpg` | shot-grid, next to the "Install ▸ Search, 137k rows" paragraph |
| `plugins/devenv-bound.jpg` | `nixarchy-devenv.jpg` | shot-grid |

The lead screenshot goes before the two infographics, so the page shows the actual
desktop first and the explainers after it. The shot-grid goes after the
"What that buys" paragraph. The existing prose stays as it is.

### Agentic SDLC (`showcase.md:405`)
- Copy `site/assets/img/governing-software-in-the-age-of-ai.webp` from the
  `agentic-sdlc-showcase` repo to `assets/img/showcase/agentic-sdlc-infographic.webp`.
  Show it as `figure.shot.infographic` after the first paragraph, with its real
  `width`/`height` read from the file.
- Add a **screencast** link to the existing link line:
  `→ the walkthrough · the screencast · source`.

### nix-skills (new)
- A new `div.project` section with `id="nix-skills"`, placed right after nixarchy
  because it comes from the same Nix work.
- Tags: `Creator · open source`, `Nix · agent skills`.
- Copy, taken from the README:
  - The problem: agents give Nix advice that is out of date, meant for another
    distribution, or imperative.
  - The answer: ten pinned, source-backed skills for Claude Code, Codex, OpenCode and
    Antigravity. It installs skills, not agents.
  - The ten skills in one sentence, grouped: language, NixOS operations, Home Manager,
    nix-darwin, devenv, microvm.nix, Nixpkgs, the wiki, and coding agents on NixOS.
  - The three ways in: a demo VM (`nix run github:olafkfreund/nix-skills?dir=demo`),
    a flake template for your own machine, or a Home Manager module for the skills
    only. Show a single `<pre><code>` block with the demo command.
- Screenshot: `assets/img/showcase/nix-skills-docs.webp`, captured at 1440×900
  with `chromium --headless --screenshot` and converted with `magick`.
- Links: `→ docs · source`.
- A card in the at-a-glance grid right after the nixarchy card, tagged
  `Nix · agent skills`.

### Counts and metadata
- Line 14: "Seventeen" → "Eighteen". Line 30: "seventeen" → "eighteen".
- Front-matter `description`: add "nix-skills" after "nixarchy".

## Alternatives rejected

- **Embedding the nixarchy feature GIFs.** They add several MB to one page and show
  the same things the stills and infographics already cover.
- **Generating a new NotebookLM infographic for nix-skills.** It can't be reproduced
  in this session, and a docs screenshot is real rather than illustrative.
- **Hotlinking images from GitHub raw URLs.** Every other section hosts its own
  images, and hotlinks break on a rename upstream and bypass html-proofer.
- **A separate page per project.** The showcase is one page by design.

## Risks

- The copied screenshots drift from upstream as the projects change. That's
  accepted; every other section has the same trade-off.
- The docs-site capture could catch a cookie banner or a half-loaded state. Check
  it visually before committing. The fallback is text only (see question 2).
- The page gains about 0.8 MB, most of it lazy-loaded.

## Verification

- `bundle exec jekyll build` succeeds.
- `bundle exec htmlproofer _site --disable-external --ignore-empty-alt --allow-missing-href --ignore-urls "/pagefind/"`
  reports no new failures on `/showcase/`.
- On `jekyll serve`, a screenshot of `/showcase/#nixarchy`, `#agentic-sdlc` and
  `#nix-skills` shows every image loading, and the grid shows eighteen cards
  (`grep -c 'class="card"' showcase.md` → 18).
