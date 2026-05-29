# WWW-Freundcloud — Design Spec

> Created: 2026-05-29
> Status: Approved (pending implementation)
> Author: Olaf Krasicki-Freund (with Claude)

## Summary

Build a new GitHub Pages site, `olafkfreund/WWW-Freundcloud`, that does two jobs:

1. **Presents Olaf and his work** — a humanized, first-person landing/portfolio (home,
   about, CV, work) driven by the latest CV.
2. **Hosts the full knowledge base** — all ~945 GitBook markdown pages migrated from
   `/mnt/data/Source/wiki` (origin `github.com/olafkfreund/wiki`) into Jekyll, with the
   GitBook nav and content faithfully preserved.

The site is built with **Jekyll** using a **hand-rolled theme that visually reproduces
the skill_pool showcase site** (`olafkfreund.github.io/skill_pool` — a bespoke static
`site/` of HTML/CSS/JS: dark developer aesthetic, top-nav + hero, ⌘K search, feature
cards, mono code). Dark mode is the default with an accessible light toggle.

Published as **GitHub Project Pages** at `https://olafkfreund.github.io/WWW-Freundcloud`
(`baseurl: /WWW-Freundcloud`). The existing `wiki` repo is left untouched as the GitBook
source of truth; content is *copied*, never moved.

## Goals & Success Criteria

- Live site at `https://olafkfreund.github.io/WWW-Freundcloud` building green from `main`.
- Me-first homepage + about + cv + work pages, written in a human first-person British
  voice (no LLM tells), with a downloadable CV PDF.
- All ~945 KB pages reachable through a sidebar nav derived from the GitBook `SUMMARY.md`,
  with GitBook-specific syntax converted and internal links/images intact.
- Visual parity with skill_pool's theme (palette, typography, cards, code, top-nav, ⌘K
  search), responsive on mobile, dark/light toggle.
- Repeatable conversion script so the KB can be re-synced from the wiki later.

## Non-Goals (YAGNI / v1 out of scope)

- No CMS, comments, or blog (blog can be added later).
- No two-way GitBook ↔ site sync.
- No custom domain in v1 (`freundcloud.com` is a documented later phase).
- Anthropic-tailored CV (`CV_Olaf_Krasicki-Freund_Anthropic_CI.md`) stays private — not
  published.
- KB technical prose is migrated **as-is** (not rewritten/humanized); only the me-first
  pages are authored in the human voice.

---

## Section 1 — Architecture & Repo Strategy

- **New repo**: `olafkfreund/WWW-Freundcloud`, public, created with `gh repo create`.
  Separate from `olafkfreund/wiki` (which remains the GitBook source of truth).
- **Local working copy**: the existing empty dir `/home/olafkfreund/Source/GitHub/www-freundcloud`.
- **Content source**: copied out of `/mnt/data/Source/wiki` — read-only with respect to
  that repo; no fork, no push to `wiki`.
- **Generator**: Jekyll (GitHub Pages-native, handles ~1k markdown files comfortably),
  custom local theme (no remote theme gem), `baseurl: "/WWW-Freundcloud"`.
- **Deploy**: GitHub Actions workflow (not classic branch build), because the build needs
  a custom theme plus a post-build search-index step:
  `actions/checkout` → `ruby/setup-ruby` (bundler cache) → `bundle exec jekyll build` →
  Pagefind index → `actions/upload-pages-artifact` → `actions/deploy-pages`.
  Permissions `pages: write`, `id-token: write`; `concurrency: pages-deploy`.
- `.nojekyll` is **not** needed (we *want* Jekyll to run); GitHub Pages source set to
  "GitHub Actions".

### Repo layout

```
WWW-Freundcloud/
├── _config.yml
├── Gemfile
├── .github/workflows/pages.yml
├── _layouts/        (base.html, landing.html, doc.html)
├── _includes/       (head, top-nav, sidebar, toc, search-modal, footer, callout, tabs)
├── _sass/           (theme ported from skill_pool/site CSS: tokens, layout, components)
├── assets/
│   ├── css/main.scss
│   ├── js/ (theme-toggle.js, search.js, tabs.js, nav.js)
│   ├── img/ (migrated .gitbook/assets + assets)
│   └── cv/Olaf-Krasicki-Freund-CV-2026.pdf
├── _data/toc.yml    (generated nav tree from SUMMARY.md)
├── index.md         (home — landing layout)
├── about.md
├── cv.md
├── work.md
├── kb/              (migrated knowledge base, doc layout)
│   └── ... (mirrors wiki section hierarchy)
├── scripts/convert.py  (GitBook → Jekyll converter)
├── docs/plans/      (this spec)
└── README.md
```

---

## Section 2 — Theme (matching skill_pool)

- **Port skill_pool/site CSS** into `_sass/`: colour tokens (dark base, accent), type
  scale, spacing, card styles, code-block styling, top-nav, footer. The skill_pool
  showcase is plain HTML/CSS/JS, so its stylesheet is liftable; tokens become SCSS vars.
- **Dark default + light toggle**: CSS custom properties under `[data-theme]`; a small
  `theme-toggle.js` persists choice in `localStorage` and respects
  `prefers-color-scheme` on first visit.
- **Two layouts**:
  - `landing` — top-nav + hero + card grid (me-first pages).
  - `doc` — top-nav + left sidebar nav (from `_data/toc.yml`) + right in-page TOC
    (auto from headings) + prev/next.
- **Search**: **Pagefind** static index built post-`jekyll build`; ⌘K modal mirroring
  skill_pool. Scales to ~1k pages with no server.
- **Icons**: Lucide (inline SVG includes), matching skill_pool.
- **Responsive**: sidebar collapses to a drawer on mobile; nav becomes a hamburger.
- **Accessibility**: keyboard-navigable nav + search, visible focus states, sufficient
  contrast in both themes (verify with axe).

---

## Section 3 — Personal Presentation (humanized "me" pages)

Driven by `CV_Olaf_Krasicki-Freund_2026.md` (latest general CV, 27 Apr 2026), with deeper
project detail pulled from the comprehensive version where useful.

- **`index.md` (home, landing layout)**: hero (name; one-line positioning — *DevOps &
  Platform Engineering leader, 30 years, currently leading a tier-1 bank's GitHub
  Enterprise migration*); CTAs → CV / Knowledge Base / GitHub; a short first-person
  intro; **featured work cards** (SARC, SkillAi, Jefferies GHE migration, NESO Backstage
  IDP); a brief "what I'm into" strip.
- **`about.md`**: long-form first-person career story — the arc, how he works, concrete
  war-stories (1M concurrent users on AKS at Live-Tech; zero-downtime Bamboo→Actions
  cutover at Jefferies), languages, governor role, interests.
- **`cv.md`**: structured CV rendered from the concise 2026 version + a **"Download PDF"**
  button linking `assets/cv/Olaf-Krasicki-Freund-CV-2026.pdf` — explicitly copied **and
  renamed** from the source `CV Olaf Krasicki-Freund 2026.pdf` (spaces → hyphens). The CV
  folder copy step must **exclude** the private `CV_Olaf_Krasicki-Freund_Anthropic_CI.md`.
- **`work.md`** (portfolio): deeper write-ups — SARC (multi-cloud compliance pipeline),
  SkillAi (open-source AI recruiting), COSMIC Rust applets, Kosli/ServiceNow MCP servers,
  the GitBook KB itself — each with links.

### Humanization rules (binding for me-first pages)

- First person ("I led…", "I tend to…"), **UK spelling**.
- Concrete specifics over buzzwords; prefer a named outcome to an adjective.
- Vary sentence and paragraph length; avoid uniform triplet bullet lists.
- **Strip LLM tells**: no "leverage", "in today's fast-paced landscape", "robust
  solutions", "passionate about", boastful symmetric bullets, or emoji-joke padding.
- Keep the tone warm and direct, lightly conversational — **professional, minimal humour**
  (per sign-off: dad-jokes stripped; see Open Items if you want a couple back).
- Written by hand into the pages, not generated-and-pasted in bulk.

---

## Section 4 — Content Migration Pipeline

A repeatable Python converter `scripts/convert.py` transforms the GitBook tree
(`/mnt/data/Source/wiki`) into Jekyll under `kb/`. KB prose is preserved **as-is**.

1. **Front matter**: drop GitBook `description:`/`cover:` YAML; emit Jekyll front matter
   (`title` from first H1 or SUMMARY label, `layout: doc`, `nav_order`/`parent` from the
   SUMMARY hierarchy).
2. **GitBook blocks** (63 files contain `{% … %}`):
   - `{% hint style="info|warning|danger|success" %}` → `callout` include.
   - `{% tabs %}/{% tab %}` → `tabs` include (JS-driven).
   - `{% code %}` / `{% endcode %}` → standard fenced code block.
   - `{% content-ref %}`, `{% embed %}`, `{% file %}` → plain markdown link.
3. **Figures/images**: `<figure><img src="../.gitbook/assets/X">…</figure>` → markdown
   image with path rewritten to `/assets/img/X` (baseurl-aware).
4. **Folder READMEs**: per-folder `README.md` → `index.md` so directories resolve. If a
   folder has both a `README.md` and a same-named sibling page, the converter logs the
   collision and keeps the `README.md` as `index.md` (sibling unchanged).
5. **Navigation**: parse the 502-line `SUMMARY.md` into `_data/toc.yml`, preserving the
   emoji-prefixed section groups and nesting; the sidebar renders from this data file.
6. **Link audit**: emit a report of SUMMARY entries that point at non-existent or
   duplicate paths (e.g. `infrastructure-as-code-iac/…` stubs vs the real `pages/…`
   targets). Decision per finding: fix the link, point at the canonical page, or drop the
   entry — the site must ship with **zero internal 404s**.
7. **Assets**: copy `.gitbook/assets/` and `assets/` → `assets/img/`; **exclude**
   `_book/`, `_snippets/` build artefacts, `.npm-global`, and other non-content dirs.
   The converter logs **actual runtime counts** (pages, block files, assets) rather than
   trusting the hardcoded figures below — the wiki may change before re-sync.
8. **Idempotent**: re-running the script regenerates `kb/` + `_data/toc.yml` cleanly so
   the KB can be re-synced from the wiki in future.

---

## Section 5 — Testing & Verification

- **Converter unit tests**: fixtures for each transform — a hint file, a tabs file, a
  figure file, a folder README, a SUMMARY fragment — assert expected Jekyll output.
- **CI gates**:
  - `bundle exec jekyll build` must succeed (no Liquid/YAML errors).
  - **html-proofer** over `_site`: internal links + images resolve (external links
    non-blocking / allow-listed).
  - Pagefind index builds without error.
- **Manual checks**:
  - Visual diff of `landing` and `doc` layouts against skill_pool (palette, type, cards,
    code, nav, search).
  - Spot-check ≥10 converted KB pages including every GitBook-block type.
  - Mobile (drawer nav) + light/dark toggle + ⌘K search.
  - axe accessibility pass on home + one doc page.

---

## Section 6 — Migration & Rollout Order

1. **Scaffold**: Jekyll + ported theme + CI workflow, no content → green build, blank
   dark site renders locally and in Actions.
2. **Me-first pages**: author home/about/cv/work in the human voice; add CV PDF → review.
3. **KB conversion**: run `convert.py` on the full wiki; resolve link-audit findings →
   zero internal 404s.
4. **Search + nav**: wire Pagefind + sidebar from `_data/toc.yml` → full review.
5. **Publish**: `gh repo create olafkfreund/WWW-Freundcloud --public`, push `main`, enable
   Pages (source: GitHub Actions), verify the live URL builds and renders.
6. **Later (separate phase)**: custom domain `freundcloud.com` (CNAME + DNS), optional
   analytics, optional blog.

---

## Open Items (RESOLVED 2026-05-29)

- **Humour**: ✅ Keep a couple of dry asides on personal pages (tasteful, not padding).
- **Analytics**: ✅ Wire privacy-friendly **GoatCounter** in v1 (no cookies, no PII).
- **Git identity**: ✅ Commit with the default global identity (`olaf.loken@gmail.com`),
  plus the required `Co-Authored-By` trailer per global Agent OS standards.

## Key Facts (reference)

- Wiki: ~732 content `.md` excluding `_book/` build artefacts (695 in `pages/` — exact),
  ~84 MB, GitBook flavour, origin `git@github.com:olafkfreund/wiki.git`; ~66 files use
  `{% %}` blocks; `SUMMARY.md` is ~501 lines. (The "~945" figure counts build artefacts
  the converter excludes; treat runtime counts as authoritative.)
- Theme source: `olafkfreund/skill_pool` → published from a static `site/` dir via
  `.github/workflows/pages.yml` (NOT the SvelteKit app, NOT Jekyll). CSS is portable.
- CV: `CV_Olaf_Krasicki-Freund_2026.md` (canonical) + `CV Olaf Krasicki-Freund 2026.pdf`
  for download, in `/home/olafkfreund/Documents/Caliti/Privat/CV`.
- Environment: `gh` authed as `olafkfreund` (full scopes), Ruby 3.4.9, Node 24, Bundler
  2.6.9; Jekyll to be installed via Bundler.
- Publish target: `https://olafkfreund.github.io/WWW-Freundcloud`.
