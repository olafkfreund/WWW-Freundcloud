---
name: blog
description: >-
  Draft, stage, and publish a post to the freundcloud Jekyll blog (this repo,
  deployed to www.freundcloud.com via GitHub Pages). Triggers on "/blog",
  "write a blog post", "draft a post", "publish a post", "promote a draft", or
  any request to add/list posts for this site.
allowed-tools: Bash(*), Read, Write, Edit
---

# Blog publishing

You write and publish posts for **<www.freundcloud.com>**, a Jekyll site
deployed to GitHub Pages from `olafkfreund/WWW-Freundcloud`. Posts are Markdown
files in `_posts/`; pushing to `main` triggers `.github/workflows/pages.yml`,
which builds the site (Jekyll → Pagefind → html-proofer) and deploys it. Drafts
live in `_drafts/` and are never built or deployed until promoted.

## Step 0 — Locate and verify the repo

Run from a working copy of this repo. Find the root with
`git rev-parse --show-toplevel`. If the cwd isn't inside `WWW-Freundcloud`, try
`~/Source/GitHub/www-freundcloud`. If neither exists, stop and ask — do not
clone or guess. Confirm `_config.yml`, `_posts/`, and `_layouts/post.html` all
exist; if not, stop and say so. All paths below are relative to the root.

## Step 1 — Parse the mode

The argument string selects the mode:

- `--list` → **List drafts.** Print each file in `_drafts/` (filename + title).
  Do nothing else.
- `--publish <slug>` → **Promote a draft** at `_drafts/<slug>.md`. Go to Step 4.
- `--draft <rest>` → **Draft only.** Write to `_drafts/`, no date, no push.
  Do Step 2, then Step 3 (draft variant). Stop after writing.
- plain text → **Publish-ready.** Treat the text as title/topic/notes.
  Do Step 2 → Step 3 → Step 4.

## Step 2 — Gather what you need

Derive **title**, **angle**, 2–4 lowercase **tags** (from the site's themes:
devops, platform, cicd, nixos, ai, agents, multicloud, kubernetes, meta, …),
and a one-to-two sentence **excerpt**.

Only ask about fields you genuinely can't infer. Rich notes → infer everything
and proceed. A bare title → ask for angle + tags in one batch, then continue.

**Slug:** lowercase the title, replace non-alphanumerics with single hyphens,
trim leading/trailing hyphens.

## Step 3 — Write the post

**Match the house voice.** Read `_posts/2026-05-29-welcome-to-the-blog.md`
first and mirror it: first-person, opinionated, working-out-loud, dry wit,
concrete over abstract, short paragraphs, `##` section headings, fenced code
blocks with a language where useful. Internal links use Jekyll's `relative_url`
filter, e.g. `[the KB]({{ '/kb/' | relative_url }})`. No marketing fluff, no
"in today's fast-paced world" openers. Aim 400–900 words unless the notes
clearly want more or less.

**Images** (if any): place under `assets/img/posts/` and reference with
`![alt]({{ '/assets/img/posts/<file>.png' | relative_url }})`.

**Front matter** — every field is required and read by the templates:

```yaml
---
layout: post
title: "<title>"
date: <YYYY-MM-DD HH:MM:SS +0100>
permalink: /blog/<slug>/
tags: [<tag>, <tag>]
comments: true
excerpt: >-
  <one-to-two sentence summary; shown on the blog index and in RSS>
---
```

- **Publish-ready:** set `date` from real local time
  (`date "+%Y-%m-%d %H:%M:%S +0100"`) and write to
  `_posts/<YYYY-MM-DD>-<slug>.md` (prefix from `date +%F`).
- **--draft:** write to `_drafts/<slug>.md` and omit the `date:` line entirely
  (Jekyll assigns it at publish time). Report the path and remind me I can ship
  it later with `/blog --publish <slug>`. Do not continue to Step 4.

**Safety:** if the target file already exists, stop and warn — never overwrite
an existing post or draft. Show me the proposed file (front matter + body) and
wait for go-ahead before publishing.

## Step 4 — Publish (publish-ready and --publish only)

1. If promoting a draft: read `_drafts/<slug>.md`, add a `date:` line with the
   current local time, write it to `_posts/<YYYY-MM-DD>-<slug>.md`, and
   `git rm` the draft.
2. **Validate locally first:** `JEKYLL_ENV=production bundle exec jekyll build`.
   If the build fails, stop, show the error, and do **not** push — this catches
   YAML/Liquid breakage that would fail the deploy.
3. Stage **only** the new post (and the removed draft, if any) — never
   `git add -A`. Confirm with `git status` that nothing unexpected is staged.
4. Commit: `git commit -m "post: <title>"`.
5. Push: `git push origin main`. Never force-push.
6. Report: the live URL `https://www.freundcloud.com/blog/<slug>/`, the commit
   hash, and that the Pages Action takes ~1–2 min to build and deploy.

## Notes

- Comments use giscus, enabled per-post via `comments: true`; live comments need
  the one-time giscus repo/category IDs in `_includes/giscus.html` (placeholders
  today). Mention once if relevant; filling them is outside this skill's job.
- Never edit already-published posts and never touch files other than the single
  new post (+ the promoted draft) unless I explicitly ask.
