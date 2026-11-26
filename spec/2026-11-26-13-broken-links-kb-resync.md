---
status: approved
issue: 13
intent: intent/2026-11-26-13-broken-links-kb-resync.md
---

# Spec: Fix the broken links, recover the wiki source and reconvert the KB

## Design

### Recover the wiki source

The two unpushed commits are fetched from the trash copy, read-only, into a fresh
clone at `~/Source/GitHub/wiki`, then cherry-picked onto `origin/main` on branch
`fix/kb-links-and-fides`:

- `a2a06f0` showcase: refresh SARC screenshots, Kosli → Fides, add the other 11
  projects
- `5cb6c58` governance: add a full Fides section alongside Kosli

A dry-run convert of that branch matches today's `kb/` byte for byte, with one
exception: a new `docs/index.md`, a Backstage TechDocs stub that wiki #3 added.

### Fix the wiki at the source (same branch)

- **Wrong-depth and moved links:** point each at the real page (mapping table in
  the plan).
- **Links to pages that were never written:** keep the link text, drop the link.
  That covers the AWS services ec2/lambda/ebs/rds/dynamodb/vpc/cloudfront, the
  GCP services cloud-spanner/firestore, the copilot subpages, `open-telemetry`,
  `kubernetes/monitoring`, `iac/README`, the GitLab "Container Registry" link and
  "AI-Assisted Testing". `git-workflows` goes to `git-branching-strategies.md`.
- **`http://` → `https://`** for agilemanifesto.org, the two docs.aws.amazon.com
  links, chef.io, sigs.k8s.io and forentrepreneurs.com. The traefik
  `127.0.0.1:9000` example is a local address, so it becomes inline code, not a
  link.
- **The five `<a href="#xxxx" id="#xxxx"></a>` GitBook tags** in
  `k8s-troubleshooting-pod-in-container-creating-status.md` are removed.
- **Missing section anchors:** the Tekton link goes to the sibling
  `README.md#installation-guide-2025`, where that heading exists.
- **Leftover GitBook tags:**
  - Inline `_snippets/kubernetes-prerequisites.md` into
    `should-learn/kubernetes/README.md`.
  - Replace the klone `{% embed %}` with a plain link to the gist.
- **Showcase:** `pages/showcase/README.md` Factory section moves to five
  products, with RFactory and the same wording as the site's `showcase.md`. The
  audit-trail sentence covers only the four PARR products.

### Converter (`scripts/convert.py`)

- Resolve a link that starts with `pages/` as wiki-root-relative, but only as a
  fallback when the file-relative path doesn't resolve. These are GitBook's self
  and cross links, 16 audit findings. A few lines in `rewrite_links`, plus unit tests. `rewrite_links` also skips
  fenced code blocks, so example links aren't rewritten or audited.
- Add `docs/index.md` to `EXCLUDE_RELPATHS`. It's a TechDocs stub, not KB
  content.

### Website

- 3 posts: `/work/#aifactory` → `/work/#factory`.
- 1 post: `/work/#backstage` → `/work/#neso`.
- Regenerate `kb/`, `_data/toc.yml` and `docs/plans/link-audit.txt` with
  `python3 scripts/convert.py --wiki ~/Source/GitHub/wiki`.

### Publish order

1. Wiki PR merged first, so the site is generated from merged source.
2. Website PR merged second.

## Alternatives rejected

- **Hand-editing `kb/`:** it's overwritten on the next conversion.
- **Making the converter unlink every missing target:** it hides real source
  rot, and the owner chose to fix the source.
- **Restoring the trash copy:** a clean clone plus a fetch is reproducible and
  leaves the trash untouched.

## Risks

- **Reconvert drops or changes content.** Mitigation: diff the regenerated `kb/`
  against today's and check that every change traces to a fix.
- **A remapped link points at the wrong page.** Mitigation: every target in the
  mapping table exists, and htmlproofer confirms it.
- **The `pages/` root rule changes links that resolved before.** Mitigation: the
  root fallback runs only when the file-relative path doesn't resolve, so no
  link that resolves today changes. The unit test plus a diff
  check confirm this.

## Verification

- `python3 -m unittest discover -s scripts` passes.
- The converter audit report has 0 `BROKEN LINK` and 0 `LEFTOVER LIQUID`
  findings.
- `jekyll build` succeeds, and htmlproofer reports 0 failures.
- `diff -rq` of the old and new `kb/` lists only the files the fixes touch.
