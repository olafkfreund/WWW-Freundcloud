# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Jekyll site published to GitHub Pages on a custom domain (`www.freundcloud.com`,
set via `CNAME`, so `baseurl` is `""` and the site is served from root). It has
two distinct halves with different rules:

- **Me-first pages** — hand-written portfolio: `index.md`, `about.md`, `work.md`,
  `cv.md`, `blog.md`. These opt into pretty URLs via per-page `permalink` front matter.
- **Knowledge base** (`kb/`) — ~700 pages **generated** from a GitBook wiki by
  `scripts/convert.py`. Do not hand-edit files under `kb/` (they are overwritten
  on the next conversion) — the one exception is `kb/index.md`, which is preserved.

## Commands

```bash
bundle install
bundle exec jekyll serve            # dev server at http://localhost:4000/

# Full production build incl. search index (Pagefind only works on a built site):
bundle exec jekyll build
npx -y pagefind@latest --site _site

# Link/image integrity (same check CI runs):
bundle exec htmlproofer _site --disable-external --ignore-empty-alt --allow-missing-href --ignore-urls "/pagefind/"
```

Re-sync the KB from the GitBook wiki (regenerates `kb/`, `_data/toc.yml`,
`kb/img/`, and `docs/plans/link-audit.txt`):

```bash
python3 scripts/convert.py --wiki /mnt/data/Source/wiki
python3 -m unittest discover -s scripts   # converter unit tests (test_convert.py)
```

There is no other test suite — `test_convert.py` is the only test target.

## Architecture & conventions you can't see at a glance

- **Layout defaults are path-scoped** (`_config.yml`): everything under `kb/` gets
  `layout: doc` (sidebar nav from `_data/toc.yml`); everything else defaults to
  `layout: landing`. Posts use `layout: post`. All layouts wrap `base.html`.
- **KB pages set `render_with_liquid: false`.** Migrated docs contain literal
  `{{ }}` / `{% %}` (Helm, Go templates, shell) that must NOT be parsed by Liquid.
  Keep this in mind before adding Liquid anywhere in KB content.
- **The converter is link-aware.** It mirrors the wiki tree 1:1 under `kb/`, keeps
  relative links, and rewrites `.md` → `.html` (KB permalinks preserve path with
  `.html`). `README.md` → `index.md`. Images go to `kb/img/` with per-file relative
  paths. It is idempotent. See the docstring in `scripts/convert.py` for the full
  link-preservation strategy before changing conversion logic.
- **Search** is Pagefind, indexed at build time — it returns nothing on a plain
  `jekyll serve`; you must build + run pagefind against `_site`.
- **Theme** is hand-rolled in `_sass/theme.scss` (dark by default, light via a
  toggle persisted in `localStorage`). No CSS framework.
- **Posts** live in `_posts/` as `YYYY-MM-DD-slug.md` with front matter:
  `layout: post`, `title`, `date`, `permalink: /blog/<slug>/`, `tags`,
  `comments: true` (giscus), `excerpt`. Drafts go in `_drafts/`. Post images live
  under `assets/img/posts/` and are referenced via
  `{{ '/assets/img/posts/x.png' | relative_url }}`. Prefer the `/blog` skill to
  draft/stage/publish posts.
- **Feeds/SEO**: `jekyll-feed` is scoped to `posts` only (KB pages are excluded
  from the RSS feed); `jekyll-seo-tag` and `jekyll-sitemap` are active.
- **Analytics** (GoatCounter) is off until `analytics.goatcounter.code` is set in
  `_config.yml`.
- **Backstage**: `catalog-info.yaml` registers this as a Component; `mkdocs.yml`
  drives TechDocs (`docs/`). These are infra metadata, not the published site.

## Deploy

`.github/workflows/pages.yml` runs on push to `main`: Jekyll build
(`JEKYLL_ENV=production`) → Pagefind index → html-proofer (non-blocking) →
deploy via GitHub Pages Actions. Pages source must be set to **GitHub Actions**.
