---
status: draft
issue: 11
spec: spec/2026-11-26-11-about-rfactory-nixarchy-apps.md
coders:
  1: coder  # copy edits with exact text given; the default implementer
  2: coder  # same agent, warm cache
  3: coder  # same agent, warm cache
  4: coder  # same agent, warm cache
reviewers:
  - codex  # independent read of the diff against this plan
  - agy    # second independent read; checks the copy and links
---

# Plan: About page refresh, RFactory on the site, nixarchy apps and plugins

Approved decisions, carried over from the spec:

- **RFactory** is the fifth Factory product, "the meeting room". Every page says
  five. Its card links to `/showcase/#factory`, and the showcase count stays at
  eighteen.
- **Start page count:** "Eighteen systems", and the names add AWS Dashboard and
  nix-skills. The `showcase.md` front-matter description adds AWS Dashboard.
- **nixarchy:** 22 repos in three groups under an "Apps and plugins" `<h3>` in
  `showcase.md#nixarchy`. Forks get a "built on" credit. No new CSS.
- **HSBC:** the name only.
- **RFactory wording:** README facts only, with no audit-trail claim for it.

The RFactory line, used wherever a bullet is needed:

> **RFactory (the meeting room)**: an AI bot that joins your Meet, Zoom, Teams
> or Slack calls, runs the standup straight from the CFactory board, and turns
> what the team agrees into changes through the other four, each one waiting on
> a named approver.

The repo is `https://github.com/olafkfreund/RFactory`.

## Steps

1. **`index.md`**
   - At lines 44-46, the showcase card text becomes: "Eighteen systems in one
     place — SARC, Fides, Hecate, the Factory suite, the Agentic SDLC reference
     build, Bifrost, Janus, Myrmex Hive, ravn-agents, DORA Dashboard, SkillAi,
     Odin, Muninn, Huginn, lxconnect, AWS Dashboard, nixarchy and nix-skills."
   - At lines 52-54, the Factory card text becomes: "A governed pipeline for AI
     software delivery — PFactory plans it, AIFactory builds it, TFactory tests
     it, CFactory watches it, and RFactory brings it into your team calls. PARR,
     with a human gate at every seam and model-agnostic via MCP."
   - Right after that card's `</a>` (line 55), insert a card with:
     - `href="{{ '/showcase/#factory' | relative_url }}"`
     - tag "Open source · AI agents"
     - `<h3>RFactory</h3>`
     - text: "The Factory suite's meeting room. An AI bot joins your Meet, Zoom,
       Teams or Slack call, runs the standup straight from the CFactory board,
       and turns what the team agrees into changes, each waiting on a named
       approver."
   - Verify with `grep -n "RFactory\|Eighteen" index.md`.
   - Traps: keep the `<a class="card">` / `<span class="tag">` markup exactly as
     the neighbouring cards have it.

2. **`showcase.md`**
   - Front matter, lines 5-9: insert "AWS Dashboard, " before "nixarchy and
     nix-skills".
   - At-a-glance card, line 57: "Four products, one idea" → "Five products, one
     idea". Adjust the rest of that sentence if it lists the products.
   - `#factory`, line 343: the tag pill becomes "PFactory · AIFactory · TFactory
     · CFactory · RFactory".
   - Line 348: "Four products around one idea" → "Five products around one idea".
   - Infographic `<figcaption>`, around line 356: append " The four PARR stages
     are shown; RFactory sits in the meeting room beside them."
   - After the CFactory `<li>` (ends line 382), add `<li>` with the RFactory line
     above.
   - Line 399: "The spine that makes four products cohere" → "The spine that
     makes the four PARR products cohere". Change "every product emits the same
     audit trail" to "each of them emits the same audit trail". After that
     sentence, add: "RFactory reads the same board, so what a team agrees on a
     call lands as a card like any other."
   - Link row, lines 404-408: after the CFactory link, add
     `· <a href="https://github.com/olafkfreund/RFactory" rel="noopener">RFactory</a>`.
   - Verify with
     `grep -n "Five products\|RFactory\|AWS Dashboard, nixarchy" showcase.md`.
   - Traps: don't touch `{% include %}` lines or the image paths.

3. **`showcase.md#nixarchy`**
   - Between the "The naming is deliberate" paragraph (ends line 896) and the
     `→ source` paragraph, insert:

     ```html
     <h3>Apps and plugins</h3>
     <p>nixarchy is the base; most of what I use day to day is built on top of it as
     Omarchy plugins and small apps. Where one started as somebody else's Omarchy
     plugin, the credit says so.</p>
     ```

   - Then three groups, each a `<p><strong>Group.</strong></p>` followed by a
     `<ul>`. Each `<li>` is
     `<a href="https://github.com/olafkfreund/NAME" rel="noopener">NAME</a> — DESC`,
     with `(built on <a href="https://github.com/UP" rel="noopener">UP</a>)` for
     forks.
   - **Shell and menus.**
     - nixarchy-menu: native quick menu for nixarchy (built on
       evindor/keystroke).
     - nixarchy-pkg: search nixpkgs, turn apps and services on, set NixOS
       options and apply, from the shell, on the keyboard.
     - nixarchy-plugin-browser: browse the Omarchy plugin marketplace and check
       each plugin can run on NixOS (built on
       OmarchyFans/omarchy-fans-plugin-browser).
     - nixarchy-flatsnap: install Flatpak and Snap apps from the menu, kept
       declarative.
     - nixarchy-hyprsettngs: a Hyprland studio with live preview: gaps,
       borders, palette colours, blur, animations with a curve editor, app rules
       and profiles (built on AbdulazizAlwabel/omarchy-hyprforge).
     - nixi-nixarchy: Nixi, a guided tour, offline manual search and an AI
       tutor grounded in your own machine (built on
       respira-crece-lidera/archy-omarchy).
     - nixarchy-voice: operate the desktop by talking to it, with a local
       policy gate approving every action (built on
       wombatoperator/omarchy-voice).
   - **Development and infrastructure.**
     - nixarchy-devenv: a bar widget and menu for devenv environments: create
       from templates, enter, edit, update, delete.
     - nixarchy-microvm: the same for NixOS MicroVMs.
     - nixarchy-distrobox: the same for Distrobox boxes.
     - nixarchy-podman: a Podman container manager in the bar (built on
       i228808/omapodman).
     - nixarchy-winvm: Windows VM control from the menu (built on
       yanuarpmbd/omarchy-winvm-widget).
     - nixarchy-ghtui: a keyboard-driven GitHub Actions panel.
     - nixarchy-gltui: the same for GitLab pipelines.
     - nixarchy-herdr: herdr sessions and the agents in them across tailnet
       hosts, on a keybind (built on jankeesvw/omarchy-herdr).
     - nixarchy-llm-index: a local, self-updating file and code index for LLM
       agents, over MCP.
   - **Everyday.**
     - nixarchy-flux: connect the desktop to your phone: files, clipboard,
       notifications, media and camera (built on bjarneo/flux).
     - nixarchy-omapod: a podcast app with a bar widget (built on
       arikisonfire/omapod).
     - omateams: Microsoft Teams in an Omarchy-themed window with an unread
       badge (built on Divanyx/omateams).
     - nixarchy-meeting-mode: join a call and the desktop goes quiet by itself
       (built on jburchel/omarchy-meeting-mode).
     - nixarchy-meetingai: an ambient real-time meeting copilot.
     - omagovee: Govee light control with local MCP automation.
   - Verify with `grep -c 'github.com/olafkfreund/nixarchy-\|olafkfreund/oma\|olafkfreund/nixi-' showcase.md`.
   - Traps: keep it inside `<div class="project">`, before its closing
     `</div>`. Escape `&` as `&amp;`.

4. **`work.md`, `cv.md`, `about.md`**
   - `work.md`:
     - Line 74: "a four-product suite" → "a five-product suite".
     - After the CFactory `<li>` (ends around line 95), add the RFactory `<li>`.
       Its text is the RFactory line, starting `<strong>RFactory (the meeting
       room)</strong>`.
   - `cv.md:82-83`: "PFactory, AIFactory, TFactory and CFactory" → "PFactory,
     AIFactory, TFactory, CFactory and RFactory".
   - `about.md`:
     - The "What I'm doing now" Factory paragraph: after "CFactory is the
       cockpit over all three.", add "RFactory brings it into your team calls:
       an AI bot that runs the standup from the board and turns what's agreed
       into approved changes." Change "all three" to "the other three".
     - The open-source paragraph, around line 109: "PFactory, AIFactory,
       TFactory, CFactory" → "PFactory, AIFactory, TFactory, CFactory and
       RFactory".
   - Verify with `grep -n RFactory work.md cv.md about.md`.
   - Traps: `about.md` already carries the HSBC and nixarchy edits uncommitted.
     Keep them.

5. **Lead: build and check.** Run:

   ```bash
   bundle exec jekyll build
   bundle exec htmlproofer _site --disable-external --ignore-empty-alt --allow-missing-href --ignore-urls "/pagefind/"
   ```

   Then run the stale-wording grep from Tests.
6. **Lead: review, commit, PR, merge, publish.**
   - Opus review plus the Codex and agy reviews, each given the plan path and
     the `git diff`.
   - Commit `feat(site): RFactory, five-product Factory, nixarchy apps and HSBC (#11)`.
   - Push, open a PR linking all three artifacts, merge, and watch the Pages
     deploy.

## Tests

- The Jekyll build exits 0, and htmlproofer reports zero failures.
- `grep -rn -i "four products\|four-product\|Seventeen" index.md showcase.md work.md cv.md about.md`
  returns nothing.
- Every listed repo is public: `gh api repos/olafkfreund/<repo> -q .private`
  returns `false`.

## Rollback

Revert the merge commit on `main`. Pages redeploys the previous site.
