---
status: draft
issue: 11
intent: intent/2026-11-26-11-about-rfactory-nixarchy-apps.md
---

# Spec: About page refresh, RFactory on the site, nixarchy apps and plugins

## Design

### RFactory as the fifth Factory product

The four PARR products keep their stage letters. RFactory sits beside them as
**the meeting room**: an AI bot that joins Meet, Zoom, Teams or Slack calls, runs
the standup straight from the CFactory board, and turns what the team agrees into
changes through the other four, each waiting on a named approver. That wording
matches what its README states. It makes no audit-trail claim for RFactory.

Every Factory description moves from four products to five:

- `index.md:49-55`. The Factory card names RFactory. A new RFactory card goes
  right after it, linking to `/showcase/#factory`.
- `showcase.md:54-60`. The at-a-glance card says "Five products" and gives
  RFactory's role next to plan, build, test and watch.
- `showcase.md:342-408` (`#factory`):
  - the tag pill adds RFactory;
  - "Four products around one idea" becomes "Five products";
  - a fifth bullet goes in for RFactory;
  - the infographic caption says it shows the four PARR stages;
  - the "spine" sentence says the four PARR products share the audit trail and
    RFactory reads the same board;
  - the link row adds RFactory.
- `work.md:72-121` (`#factory`): "five-product suite", the RFactory bullet, the
  "spine" paragraph scoped to the four PARR products, and an RFactory link.
- `cv.md:80-83`: the product list adds RFactory.
- `about.md`. The "What I'm doing now" paragraph adds RFactory. The open-source
  paragraph lists five.

### Showcase count drift

- `index.md:44-46` says "Eighteen systems" and adds AWS Dashboard and nix-skills
  to the names.
- The `showcase.md` front-matter description adds AWS Dashboard.
- The showcase heading already says eighteen, and RFactory doesn't add an entry.

### nixarchy apps and plugins

Inside `showcase.md#nixarchy`, between the "naming is deliberate" paragraph
(`:893`) and the source link (`:897`), add an "Apps and plugins" `<h3>`. Under it
go three bold-led groups, each a plain `<ul>` with one line per repo linking to
GitHub. No new CSS: `h3`, `ul` and `li` take the page's base styles, the same as the other `.project` lists.

**Selection rule** (owner: "the ones I have done"): a public repo where Olaf wrote
most of the commits, or a substantial share of them for a fork, and which isn't a
pure Nix packaging of someone else's app. A fork gets a short "built on <upstream>"
credit. That gives 22 repos:

- **Shell and menus:** nixarchy-menu (built on evindor/keystroke), nixarchy-pkg,
  nixarchy-plugin-browser (built on OmarchyFans/omarchy-fans-plugin-browser),
  nixarchy-flatsnap, nixarchy-hyprsettngs (built on
  AbdulazizAlwabel/omarchy-hyprforge), nixi-nixarchy (built on
  respira-crece-lidera/archy-omarchy), nixarchy-voice (built on
  wombatoperator/omarchy-voice).
- **Development and infrastructure:** nixarchy-devenv, nixarchy-microvm,
  nixarchy-distrobox, nixarchy-podman (built on i228808/omapodman), nixarchy-winvm
  (built on yanuarpmbd/omarchy-winvm-widget), nixarchy-ghtui, nixarchy-gltui,
  nixarchy-herdr (built on jankeesvw/omarchy-herdr), nixarchy-llm-index.
- **Everyday:** nixarchy-flux (built on bjarneo/flux), nixarchy-omapod (built on
  arikisonfire/omapod), omateams (built on Divanyx/omateams), nixarchy-meeting-mode
  (built on jburchel/omarchy-meeting-mode), nixarchy-meetingai, omagovee.

**Left out:**

- Packagings of third-party apps: nixarchy-flea, nixarchy-omabroadcast,
  nixarchy-omatheme, nixarchy-hyprflip, nixarchy-gliff-manager,
  nixarchy-googlebook-vm.
- Forks with no or minor own commits: omarchy-webcam, omarchy-bar-folder,
  omarchy-notification-center-plugin, nixarchy-pixelbuds, nixarchy-pager,
  nixarchy-lofi-focus, nixarchy-daily-plugin, nixiplug, nixarchy-bbs.
- omagmail, whose README is empty.

### About page

Commit the existing working-tree draft (HSBC name only, Factory paragraph, the
COSMIC → nixarchy line), plus the five-product wording above.

## Alternatives rejected

- **A separate `#rfactory` showcase entry.** The owner chose `/showcase/#factory`.
- **A card grid for the 22 apps.** It would be heavier than any other entry and
  isn't needed; a grouped list scans fine.
- **Listing every nixarchy-family repo.** The owner limited it to his own work.
- **Editing the Factory infographic.** It's a raster image, so the caption covers
  the gap instead.

## Risks

- Factory copy claims RFactory can't back up. Mitigation: its description uses
  README facts only (joins calls, standup from the board, changes wait for a named
  approver). It doesn't claim the audit trail or that it writes cards.
- Broken internal links or anchors. Mitigation: htmlproofer on the built site.
- Fork credits that name the wrong upstream. Mitigation: each one is taken from
  `gh api repos/olafkfreund/<repo> -q .parent.full_name`.

## Verification

- `bundle exec jekyll build` succeeds.
- `bundle exec htmlproofer _site --disable-external --ignore-empty-alt --allow-missing-href --ignore-urls "/pagefind/"`
  passes.
- `grep -rn -i "four products\|four-product\|Seventeen" index.md showcase.md work.md cv.md about.md`
  finds no stale wording. "four PARR" is fine.
- `grep -c 'github.com/olafkfreund/' showcase.md` rises by 22 plus the RFactory
  link.
- After the merge, the GitHub Pages deploy finishes and `/`, `/about/` and
  `/showcase/` show the changes.
