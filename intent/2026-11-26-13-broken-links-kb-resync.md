---
status: approved
issue: 13
author: olafkfreund
---

# Intent: Fix the broken links, recover the wiki source and reconvert the KB

## Problem

- htmlproofer reports 62 failures on the built site. `origin/main` has the same
  62, so none are new:
  - 4 are blog posts linking to `/work/#aifactory` and `/work/#backstage`,
    anchors that no longer exist.
  - The other 58 are in the KB (`kb/`), which `scripts/convert.py` generates
    from `olafkfreund/wiki`:
    - about 46 links to wiki pages that don't exist, or that use the wrong
      relative depth;
    - 10 `http://` links;
    - 5 GitBook anchor tags whose id contains `#`;
    - 2 links to section anchors that don't exist.
- The wiki source behind today's `kb/` is in the trash
  (`/mnt/code/.Trash-1000/files/wiki`, deleted 2026-11-10). Two commits there
  were never pushed: the Fides governance section and the showcase refresh. So
  `olafkfreund/wiki` on GitHub is behind the live KB, and a reconvert from it
  would delete the Fides pages.
- The KB showcase page (`kb/pages/showcase/index.md`) still describes the Factory
  suite as four products. CLAUDE.md says not to hand-edit `kb/`.
- The converter also reports two leftover GitBook tags, an `include` and an
  `embed`, that render as literal text.

## Proposed outcome

- The two recovered commits are on `olafkfreund/wiki` `main`, so the source of
  truth matches the site again.
- The wiki is fixed at the source. Each dead link goes to the right existing page
  or, where no such page exists, becomes plain text. The `http` links become
  `https`, the broken anchors are fixed, the showcase says five Factory products,
  and the leftover GitBook tags are resolved.
- `kb/` is regenerated from the fixed wiki, and the 4 blog anchors are corrected.
- htmlproofer on the built site reports **0** failures, and the converter's audit
  report has no broken links.

## Affected users and systems

- Repos: `olafkfreund/WWW-Freundcloud` (blog posts, `scripts/convert.py` and its
  test, regenerated `kb/`, `_data/toc.yml`, `docs/plans/link-audit.txt`), and
  `olafkfreund/wiki` (page fixes plus the two recovered commits).
- Visitors to <www.freundcloud.com/kb/> and the blog.
- No hosts or services.

## Constraints

- The regenerated `kb/` must not lose content: compared with today's `kb/`, the
  only differences are the intended fixes.
- Never invent a page that doesn't exist. Point to a real page, or unlink.
- The trash copy is read-only: fetch from it, don't restore or edit it.
- `kb/index.md` is preserved by the converter, so leave it alone.

## Open questions

None. The owner chose "blog + wiki, reconvert" and gave one approval for all three
gates ("fix what is needed fixing", confirmed as "cover all").
