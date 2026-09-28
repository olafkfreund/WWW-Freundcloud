---
status: draft
issue: 9
spec: spec/2026-09-28-9-showcase-latest-projects.md
---

# Plan: Showcase the latest projects — nixarchy, Agentic SDLC, nix-skills

## Approved decisions (from the spec)

- "nix-skill" = `olafkfreund/nix-skills`.
- All edits go in `showcase.md`, and images go in `assets/img/showcase/`, copied into
  the repo rather than hotlinked. Nothing under `kb/` or `infographics/` changes.
- Use the existing markup: `figure.shot` for a lead image, `figure.shot.infographic`
  for infographics, and `div.shot-grid` with `figure`s for the rest. Every `img` gets
  `loading="lazy"` and meaningful alt text.
- **nixarchy:** stills only, no GIFs. Put `desktop.jpg` in a lead `figure.shot` before
  the two existing infographics. Add a shot-grid (menu-ask, search, devenv) after the
  "What that buys" paragraph. The existing prose stays as it is.
- **Agentic SDLC:** the repo's infographic goes in a `figure.shot.infographic` after
  the first paragraph, with its real width and height. Add a screencast link to the
  link line.
- **nix-skills:** a new `div.project` with `id="nix-skills"` right after nixarchy.
  Tags are `Creator · open source` and `Nix · agent skills`. Copy comes from the README
  (the problem, ten skills, three ways in, the demo command in `<pre><code>`). Add a
  1440×900 headless-Chromium screenshot of the docs site as webp, and `docs · source`
  links. If the capture is unusable, ship the section as text only.
- Add a nix-skills card right after the nixarchy card. Change "Seventeen/seventeen" to
  "Eighteen/eighteen" (lines 14 and 30) and add "nix-skills" to the front-matter
  description.

## Steps

1. **Fetch images**: download into `assets/img/showcase/` with
   `gh api repos/olafkfreund/<repo>/contents/<path> -H 'Accept: application/vnd.github.raw'`:
   - nixarchy `docs/img/desktop/desktop.jpg` → `nixarchy-desktop.jpg`
   - nixarchy `docs/img/desktop/menu-ask.webp` → `nixarchy-menu-ask.webp`
   - nixarchy `docs/img/desktop/search-results.jpg` → `nixarchy-search.jpg`
   - nixarchy `docs/img/plugins/devenv-bound.jpg` → `nixarchy-devenv.jpg`
   - agentic-sdlc-showcase `site/assets/img/governing-software-in-the-age-of-ai.webp`
     → `agentic-sdlc-infographic.webp`

   → verify with `magick identify` on each: a valid image with the expected byte size
   (41,539 / 42,334 / 59,108 / 91,318 / 430,180).
2. **Capture nix-skills docs**:
   `chromium --headless --hide-scrollbars --window-size=1440,900 --virtual-time-budget=5000 --screenshot=<scratch>/ns.png https://olafkfreund.github.io/nix-skills/`,
   then `magick <scratch>/ns.png -quality 82 assets/img/showcase/nix-skills-docs.webp`.
   → verify by viewing the image: a fully rendered page with no banner and no blank
   areas. If it fails, use the text-only fallback and note that here.
3. **`showcase.md` counts and metadata**: update lines 7–9, 14 and 30.
   → verify: `grep -ci eighteen showcase.md` → 2, and `grep -ci seventeen` → 0.
4. **`showcase.md` card**: add the nix-skills card after the nixarchy card.
   → verify: `grep -c 'class="card"' showcase.md` → 18.
5. **`showcase.md` Agentic SDLC**: add the infographic figure and the screencast link
   (`https://olafkfreund.github.io/agentic-sdlc-showcase/screencast/`).
   → verify the figure's width and height match the output of step 1's identify.
6. **`showcase.md` nixarchy**: add the lead figure and the shot-grid.
   → verify that all 4 new `src` paths exist on disk.
7. **`showcase.md` nix-skills section**: add it after the nixarchy `</div>`.
   → verify that `id="nix-skills"` appears exactly once.
8. **Build and check** (see Tests), then take a visual screenshot of the three
   anchors on `jekyll serve`.
9. **Commit and open a PR**: one commit for the images and `showcase.md`, then a PR
   that links the intent, spec and plan and closes #9.

## Tests

```bash
bundle exec jekyll build                      # exit 0
bundle exec htmlproofer _site --disable-external --ignore-empty-alt \
  --allow-missing-href --ignore-urls "/pagefind/"   # no new failures on showcase/
grep -c 'class="card"' showcase.md             # 18
```

Visual check: headless Chromium screenshots of `http://localhost:4000/showcase/#nixarchy`,
`#agentic-sdlc` and `#nix-skills`, with every image rendered.

## Rollback

Revert the implementation commit (`git revert <sha>`). That removes the six images
and the `showcase.md` edits, and Pages redeploys on the next push to `main`. The
intent, spec and plan stay.
