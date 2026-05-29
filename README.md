# WWW-Freundcloud

Personal site and cloud-engineering knowledge base for Olaf Krasicki-Freund,
published with Jekyll to GitHub Pages at
<https://olafkfreund.github.io/WWW-Freundcloud>.

Two halves:

- **Me-first pages** — `index.md`, `about.md`, `work.md`, `cv.md`: a humanized
  first-person portfolio with a downloadable CV.
- **Knowledge base** — `kb/`: ~700 pages migrated from a GitBook wiki, with a
  sidebar nav (`_data/toc.yml`), GitBook syntax converted, and Pagefind search.

## Local development

```bash
bundle install
bundle exec jekyll serve            # http://localhost:4000/WWW-Freundcloud/
```

Search (Pagefind) only works against a production build:

```bash
bundle exec jekyll build
npx -y pagefind@latest --site _site
bundle exec jekyll serve --skip-initial-build   # then browse _site, or re-serve
```

## Re-syncing the knowledge base from GitBook

The KB is generated from the GitBook wiki. To re-import after the wiki changes:

```bash
python3 scripts/convert.py --wiki /mnt/data/Source/wiki
python3 -m unittest discover -s scripts   # converter unit tests
```

This regenerates `kb/` (preserving the hand-written `kb/index.md`),
`_data/toc.yml`, `kb/img/`, and writes `docs/plans/link-audit.txt`.

## Theme

A hand-rolled theme in `_sass/theme.scss` ported from the skill_pool showcase
site — dark by default, light via the toggle (persisted in `localStorage`).

## Deploy

`.github/workflows/pages.yml` builds with Jekyll, indexes with Pagefind, checks
internal links with html-proofer, and deploys via GitHub Pages Actions. Set the
Pages source to **GitHub Actions** in repo settings.
