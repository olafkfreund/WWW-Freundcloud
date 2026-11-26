---
status: approved
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

- **RFactory** is the fifth Factory product, "the meeting room". Every page lists
  five. The four PARR products keep their stage roles. RFactory's copy uses README
  facts only: it joins calls, runs the standup from the CFactory board, and
  changes wait for a named approver. It makes no audit-trail claim and doesn't
  say it writes cards. Its card links to `/showcase/#factory`, and the showcase
  count stays at eighteen.
- **Start page count:** "Eighteen systems". The names add AWS Dashboard (after
  Huginn, before lxconnect) and nix-skills. The `showcase.md` front-matter
  description adds AWS Dashboard in the same position.
- **nixarchy:** 22 repos in three groups under an "Apps and plugins" `<h3>` in
  `showcase.md#nixarchy`. Forks Olaf extended get a "built on" credit (owner
  decision). No new CSS.
- **HSBC:** the name only. The about-page draft is already in the working tree.

This is the RFactory `<li>`, written as HTML. These pages are raw HTML, so
Markdown is not parsed inside them:

```html
<li><strong>RFactory (the meeting room)</strong> — an AI bot that joins your Meet,
Zoom, Teams or Slack calls, runs the standup straight from the CFactory board, and
turns what the team agrees into changes through the other four, each one waiting
on a named approver.</li>
```

The repo name `nixarchy-hyprsettngs` is spelled that way on GitHub. It isn't a typo.

## Steps

1. **`index.md`**
   - Lines 44-46, replace the paragraph text up to `<strong>` with: "Eighteen
     systems in one place — SARC, Fides, Hecate, the Factory suite, the Agentic
     SDLC reference build, Bifrost, Janus, Myrmex Hive, ravn-agents, DORA
     Dashboard, SkillAi, Odin, Muninn, Huginn, AWS Dashboard, lxconnect, nixarchy
     and nix-skills."
   - Lines 52-54, the Factory card `<p>` becomes: "Five products, one governed
     pipeline for AI software delivery — PFactory plans it, AIFactory builds it,
     TFactory tests it, CFactory watches it, and RFactory brings it into your team
     calls. PARR, with a human gate at every seam and model-agnostic via MCP."
   - Right after that card's closing `</a>` (line 55), insert:

     ```html
         <a class="card" href="{{ '/showcase/#factory' | relative_url }}">
           <span class="tag">Open source · AI agents</span>
           <h3>RFactory</h3>
           <p>The Factory suite's meeting room. An AI bot joins your Meet, Zoom,
           Teams or Slack call, runs the standup straight from the CFactory board,
           and turns what the team agrees into changes, each waiting on a named
           approver.</p>
         </a>
     ```

   - Verify with `grep -n "RFactory\|Eighteen\|Five products" index.md`, which
     should show 3 or more lines.
   - Traps: match the indentation of the neighbouring cards.

2. **`showcase.md`, Factory**
   - Front matter, lines 5-9: "Muninn, Huginn, lxconnect, nixarchy and
     nix-skills." → "Muninn, Huginn, AWS Dashboard, lxconnect, nixarchy and
     nix-skills."
   - At-a-glance card, lines 57-59, the `<p>` text becomes: "Five products, one
     idea: AI can write the code, but someone is still accountable. Plan, build,
     test, watch — and talk it through on a call — with a human gate at every
     seam."
   - `#factory`, line 343: the second tag becomes "PFactory · AIFactory ·
     TFactory · CFactory · RFactory".
   - Lines 347-351, the paragraph becomes: "84% of developers use AI coding tools;
     only 29% trust the output. The Factory suite is the trust layer for that gap.
     Five products around one idea — AI can write the code, but someone still has
     to be accountable for it. Four of them are the stages of the
     `<strong>`PARR pipeline`</strong>`: `<strong>`Prepare · Act · Reflect ·
     Review`</strong>`, with a human gate at every seam rather than one "trust me"
     big bang. The fifth, RFactory, brings that pipeline into the team's calls."
     Keep the existing `<strong>` tags.
   - The `<figcaption>` on line 357 becomes: "Idea in, shipped software out —
     through sixteen guards, with the PARR loop (prepare, act, reflect, review)
     turning underneath. The picture shows the four PARR stages; RFactory joins
     them in the meeting room."
   - After line 381 (the CFactory `</li>`), before `</ul>` on line 382, insert
     the RFactory `<li>` above.
   - Line 399: "The spine that makes four products cohere" → "The spine that
     makes the four PARR products cohere". "so every product emits the same
     audit trail" → "so each of them emits the same audit trail". Add nothing
     about RFactory there.
   - Link row, lines 404-408: after the CFactory link line, add
     `· <a href="https://github.com/olafkfreund/RFactory" rel="noopener">RFactory</a>`.
   - Verify with
     `grep -c "RFactory" showcase.md`, which should be 5 or more, and
     `grep -n "Four products\|every product emits" showcase.md`, which should
     return nothing.
   - Traps: don't touch `{% include %}` lines, image paths or `alt` text.

3. **`showcase.md#nixarchy`**
   - After the "The naming is deliberate" `<p>` (ends line 896 before step 2;
     find it by text) and before the `<p>→ <a href="https://github.com/olafkfreund/nixarchy"`
     line, insert:

     ```html
     <h3>Apps and plugins</h3>
     <p>nixarchy is the base. Most of what I use day to day is built on top of it as
     Omarchy plugins and small apps. Where one started as somebody else's Omarchy
     plugin, the credit says so.</p>
     ```

   - Then three groups, each a `<p><strong>Group.</strong></p>` followed by a
     `<ul>`. Each `<li>` is
     `<a href="https://github.com/olafkfreund/NAME" rel="noopener">NAME</a> — DESC`.
     For a fork, append
     `(built on <a href="https://github.com/UP" rel="noopener">UP</a>)` before
     the closing full stop.
   - **Shell and menus.**
     - nixarchy-menu: native quick menu for nixarchy. UP evindor/keystroke.
     - nixarchy-pkg: search nixpkgs, turn apps and services on, set NixOS
       options and apply, from the shell, on the keyboard.
     - nixarchy-plugin-browser: browse the Omarchy plugin marketplace and check
       each plugin can run on NixOS. UP
       OmarchyFans/omarchy-fans-plugin-browser.
     - nixarchy-flatsnap: install Flatpak and Snap apps from the menu, kept
       declarative.
     - nixarchy-hyprsettngs: a live-preview Hyprland studio for gaps, borders,
       palette colours, blur, animations with a curve editor, app rules and
       profiles. UP AbdulazizAlwabel/omarchy-hyprforge.
     - nixi-nixarchy: Nixi, a guided tour, offline manual search and an AI
       tutor grounded in your own machine. UP respira-crece-lidera/archy-omarchy.
     - nixarchy-voice: operate the desktop by talking to it, with a local
       policy gate approving every action. UP wombatoperator/omarchy-voice.
   - **Development and infrastructure.**
     - nixarchy-devenv: a bar widget and menu for devenv environments: create
       from templates, enter, edit, update, delete.
     - nixarchy-microvm: the same for NixOS MicroVMs.
     - nixarchy-distrobox: the same for Distrobox boxes.
     - nixarchy-podman: a Podman container manager in the bar. UP
       i228808/omapodman.
     - nixarchy-winvm: Windows VM control from the menu. UP
       yanuarpmbd/omarchy-winvm-widget.
     - nixarchy-ghtui: a keyboard-driven GitHub Actions panel.
     - nixarchy-gltui: the same for GitLab pipelines.
     - nixarchy-herdr: herdr sessions and the agents in them, across tailnet
       hosts, on a keybind. UP jankeesvw/omarchy-herdr.
     - nixarchy-llm-index: a local, self-updating file and code index for LLM
       agents, over MCP.
   - **Everyday.**
     - nixarchy-flux: connect the desktop to your phone: files, clipboard,
       notifications, media and camera. UP bjarneo/flux.
     - nixarchy-omapod: a podcast app with a bar widget. UP arikisonfire/omapod.
     - omateams: Microsoft Teams in an Omarchy-themed window with an unread
       badge. UP Divanyx/omateams.
     - nixarchy-meeting-mode: join a call and the desktop goes quiet by itself.
       UP jburchel/omarchy-meeting-mode.
     - nixarchy-meetingai: an ambient real-time meeting copilot.
     - omagovee: Govee light control with local MCP automation.
   - Verify that each of the 22 names appears exactly once as a link:

     ```bash
     for n in nixarchy-menu nixarchy-pkg nixarchy-plugin-browser nixarchy-flatsnap nixarchy-hyprsettngs nixi-nixarchy nixarchy-voice nixarchy-devenv nixarchy-microvm nixarchy-distrobox nixarchy-podman nixarchy-winvm nixarchy-ghtui nixarchy-gltui nixarchy-herdr nixarchy-llm-index nixarchy-flux nixarchy-omapod omateams nixarchy-meeting-mode nixarchy-meetingai omagovee; do echo "$n $(grep -c "olafkfreund/$n\"" showcase.md)"; done
     ```

     Every count should be 1.
   - Traps: keep it inside the nixarchy `<div class="project">`, before its
     closing `</div>`. Escape `&` as `&amp;`.

4. **`work.md`, `cv.md`, `about.md`**
   - `work.md`:
     - Line 74: "a four-product suite" → "a five-product suite".
     - After line 94 (the CFactory `</li>`), before `</ul>` on line 95, insert
       the RFactory `<li>` above.
     - Lines 114-116: "The spine that makes it cohere" → "The spine that makes
       the four PARR products cohere". "so every product emits" → "so each of
       them emits".
     - Link row, around lines 119-121: before the meta-repo link, add
       `· <a href="https://github.com/olafkfreund/RFactory" rel="noopener">RFactory</a>`.
   - `cv.md:82-83`: "and the Factory suite — PFactory, AIFactory, TFactory and
     CFactory — a governed pipeline" → "and the five-product Factory suite —
     PFactory, AIFactory, TFactory, CFactory and RFactory — a governed pipeline".
   - `about.md`:
     - The "What I'm doing now" Factory paragraph: "CFactory is the cockpit over
       all three." → "CFactory is the cockpit over the first three, and RFactory
       brings it into your team calls: an AI bot that runs the standup from the
       board and turns what's agreed into approved changes."
     - The open-source paragraph, around line 109: "The Factory suite — PFactory,
       AIFactory, TFactory, CFactory — is the pipeline that uses them." → "The
       five-product Factory suite — PFactory, AIFactory, TFactory, CFactory and
       RFactory — is the pipeline that uses them." Match the existing link markup
       around "Factory suite".
   - Verify with `grep -n RFactory work.md cv.md about.md`, which should show 2,
     1 and 2 or more lines, and with `grep -n "every product emits" work.md`,
     which should return nothing.
   - Traps: `about.md` already carries the HSBC and nixarchy edits uncommitted.
     Keep them.

5. **Lead: build and check.** Run:

   ```bash
   bundle exec jekyll build
   bundle exec htmlproofer _site --disable-external --ignore-empty-alt --allow-missing-href --ignore-urls "/pagefind/"
   ```

   Then run the commands in Tests.
6. **Lead: review, commit, PR, merge, publish.**
   - Opus review plus the Codex and agy reviews, each given the plan path and
     the `git diff`.
   - Commit `feat(site): RFactory, five-product Factory, nixarchy apps and HSBC (#11)`.
   - Push, open a PR linking all three artifacts, and merge.
   - Watch the Pages deploy, then fetch `/`, `/about/` and `/showcase/` from
     <www.freundcloud.com> and grep each for "RFactory".

## Tests

- The Jekyll build exits 0, and htmlproofer reports zero failures.
- This returns nothing:

  ```bash
  grep -rn -i "four products\|four-product\|Seventeen\|every product emits\|over all three" index.md showcase.md work.md cv.md about.md
  ```

- The 22-name loop in step 3 prints 1 for every name.
- Every linked repo is public:

  ```bash
  gh api repos/olafkfreund/<repo> -q .private
  ```

  should print `false` for RFactory and each of the 22.

## Rollback

Revert the merge commit on `main`. Pages redeploys the previous site.
