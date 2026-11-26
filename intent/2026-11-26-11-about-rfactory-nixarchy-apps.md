---
status: approved
issue: 11
author: olafkfreund
---

# Intent: About page refresh, RFactory on the site, nixarchy apps and plugins

## Problem

The site lags what Olaf is doing now. Each point describes `main`.

- **About page (`about.md`).** It doesn't mention the current HSBC engagement.
  The Factory suite gets one line in the open-source section, not a place under
  "What I'm doing now". "Away from the keyboard" still describes NixOS + COSMIC
  Rust applets, though that hobby has since become nixarchy.
- **RFactory is nowhere on the site.** `olafkfreund/RFactory` (public) is a
  meeting-agent web app: an AI bot joins Meet, Zoom, Teams or Slack calls, runs
  standups from the CFactory board, and makes approved changes through the
  Factory services. Every page that describes the Factory suite says four
  products and maps them one-to-one onto PARR (Prepare · Act · Reflect · Review):
  - `index.md:49` (the card, which links to `/work/#factory`)
  - `showcase.md:54` (the at-a-glance card)
  - `showcase.md:342-408` (`#factory`: tag pill, "Four products", the four
    bullets, "the spine that makes four products cohere", links, and an
    infographic that shows four)
  - `work.md:72-95` (`#factory`)
  - `cv.md:80`
  - `about.md`, in the open-source paragraph and in the new "What I'm doing now"
    paragraph
- **The showcase count is already wrong.** `showcase.md` has 18 entries and says
  "eighteen". The start page card (`index.md:44`) says "Seventeen" and names 16;
  it leaves out AWS Dashboard and nix-skills. The `showcase.md` front-matter
  description leaves out AWS Dashboard.
- **Showcase `#nixarchy`.** The entry covers the nixarchy core but none of the
  apps and plugins built around it. About 35 public repos under `olafkfreund` are
  in that family (`nixarchy-*`, `oma*`, `omarchy-*`, `nixi*`): the menu,
  devenv/microvm/distrobox/podman widgets, Flux phone link, omaPOD, omateams,
  meeting mode, voice, the Hyprland settings studio, llm-index, Nixi and others.

## Proposed outcome

- `/about/` mentions HSBC (no detail beyond the name), gives the Factory suite a
  paragraph under "What I'm doing now", and says in "Away from the keyboard" that
  the NixOS tinkering became nixarchy. These edits are already drafted,
  uncommitted, in this branch's working tree. They'll be committed with the
  implementation.
- `/` has an RFactory card in "Selected work", next to the Factory card.
- Every Factory description on the site treats RFactory the same way, and all of
  them agree with one another.
- The showcase counts agree everywhere: start page card, showcase heading and
  front matter.
- `/showcase/#nixarchy` lists the nixarchy apps and plugins: one line each,
  linking to the repo, grouped so the list scans.

## Affected users and systems

- Files: `about.md`, `index.md`, `showcase.md`, `work.md`, `cv.md`.
- Visitors to <www.freundcloud.com> (GitHub Pages; deploys from `main`).
- No hosts, services or secrets.

## Constraints

- HSBC: the new engagement copy names HSBC only, with no team, programme, role or
  dates. The existing SkillAi lines ("in production for HSBC Kraków hiring") stay
  as they are.
- Link only to public repos. Private ones (`factory-lab-*`, `factory-runners`,
  `rfactory-fixture`) stay off the site.
- Keep the site's existing card and `.project` markup and CSS. No new styles
  unless the list genuinely needs one.
- The Factory infographic image can't be edited here. If RFactory joins the suite,
  the caption or the text around it must make clear the image shows the four
  PARR stages.
- CI runs htmlproofer on the built site, so internal links and anchors must
  resolve.

## Open questions

1. **How RFactory is framed.** Is it a fifth Factory product, so every page says
   "five" and it gets a role beside the PARR stages, for example "the meeting
   layer over PARR"? Or is it a companion app built on the suite, with the "four
   products" copy staying and RFactory mentioned as built on top of it?
2. **Where the RFactory card links.** Options:
   - (a) `/showcase/#factory`, with an RFactory part added to that section.
   - (b) A new `#rfactory` showcase entry. The total becomes nineteen, and the
     entry gets an at-a-glance card.
   - (c) The GitHub repo. Every other "Selected work" card links internally.
3. **Which nixarchy apps and plugins, and how many.** Your own plugins and apps
   only, or also the Nix packagings of third-party projects (`nixarchy-flea`,
   `nixarchy-omabroadcast`, `nixarchy-gliff-manager`, `nixarchy-hyprflip`,
   `nixarchy-googlebook-vm`)? What about the non-desktop ones (`nixarchy-bbs`,
   `mcp-nixarchy`, `nixarchy-pkg`)? And every eligible repo, or a curated set? A
   full list of 25–35 lines makes `#nixarchy` far longer than any other entry.

## Decisions (owner, 2026-11-26)

1. RFactory is the fifth Factory product, so every page says five.
2. The RFactory card links to `/showcase/#factory`, which gets an RFactory part.
   The showcase count stays at eighteen.
3. List only Olaf's own nixarchy apps and plugins ("the ones I have done"): no
   packagings of third-party projects. Clarified by the owner on 2026-11-26: forks
   he ported and substantially extended are included, each with an upstream
   credit. Forks with no or minor own commits stay off.

The owner's approval covers this intent and the spec and plan that follow
("Approved make the changes and publish", confirmed as "cover all").
