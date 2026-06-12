---
layout: post
title: "Cleaning out my zsh: bye oh-my-zsh, bye zplug"
date: 2026-06-12 13:15:00 +0100
permalink: /blog/cleaning-out-my-zsh-bye-oh-my-zsh-bye-zplug/
tags: [nixos, devops]
comments: true
excerpt: >-
  My shell had quietly accreted two framework managers it didn't need. Ripping
  out oh-my-zsh and zplug took startup from ~660ms to ~360ms — and surfaced a
  couple of errors they'd been politely hiding.
---

My zsh startup had crept past half a second and I'd stopped noticing, the way
you stop noticing a fan that's always on. Then I actually timed it: **~660ms**
to get a prompt. On a machine that builds the whole OS from a flake, waiting
two-thirds of a second for a shell is embarrassing. So I pulled it apart.

The culprit wasn't my config. It was two layers of framework I was paying for
and not using.

## oh-my-zsh: eleven plugins, all redundant

oh-my-zsh was loading eleven plugins and a theme. Every one of them was already
covered somewhere else: the theme by [stylix](https://github.com/danth/stylix)
(gruvbox is system-wide, OMZ wasn't doing the colours), history search by
[atuin](https://atuin.sh/), the prompt by starship — which OMZ was *also*
loading as a plugin, so it ran twice. The `sudo` plugin, the git aliases, the
completion tweaks: all things Home Manager modules or my own config already do.

OMZ was pure overhead. Worse, its `precmd` hooks were quietly interfering with
my own — I had visual command-boxes that only started rendering correctly *after*
I removed it. Gone. The look didn't change one pixel, because the look was never
OMZ's job.

## zplug: 290ms to load a single plugin

The other passenger was zplug, a plugin manager loading exactly one plugin:
github-copilot's shell suggestions. ~290ms of startup to source one file.

The fix wasn't a faster manager — it was no manager. On NixOS you don't need a
runtime plugin manager at all; you have the best one already, pinned and
reproducible:

```nix
programs.zsh.plugins = [{
  name = "you-should-use";
  src = pkgs.fetchFromGitHub { /* pinned rev + hash */ };
}];
```

Load the source directly from a `fetchFromGitHub` and the whole "manager" concept
evaporates. No defer logic, no clone-on-first-run, no lockfile that isn't my
`flake.lock`.

## The errors that were hiding in the dark

Here's the part I didn't expect. zplug loaded that copilot plugin with
`defer:2` — lazily, after the prompt. Which meant the plugin's startup error —
`gh copilot extension not found` — was being swallowed every single time. The
`gh-copilot` CLI isn't installed here and isn't wanted; my AI stack is
Claude / Antigravity / Ollama, not Copilot. The moment I switched to native
loading, the error jumped out at startup on every new shell.

Good. That's the point of cleaning up: the mess you can see is the mess you can
delete. The plugin and its two keybindings are gone, and that shaved another
**60ms** (~420ms → ~360ms).

Same story with my command-boxes — the `> cmd` and `✔ Command completed` boxes
that OMZ's hooks had been suppressing. Once they actually rendered, they ate
vertical space and added confirmation noise I never asked for. Defaulted them
**off**; a `toggle_boxes` function brings them back per session if I want them.

## The one real trap: compinit

Removing OMZ briefly made things *worse* — a 3.9s regression. The completion
dump (`compinit`) was rebuilding from scratch on every shell, because `ZDOTDIR`
was empty and the freshness check was globbing a path that didn't exist. OMZ had
been masking that with its own compinit handling.

The fix is the canonical one: a stable XDG cache location and `compinit -C -d`,
which trusts the dump and rebuilds it at most once a day instead of doing the
full security audit every prompt.

```text
~660ms  → starting point (OMZ + zplug)
 ~3.9s  → mid-removal, compinit rebuilding every shell (yikes)
~420ms  → OMZ gone, compinit cached
~360ms  → copilot plugin gone, native loading
```

## What I added back

Cleaning out isn't the same as going minimal. With the frameworks gone I had
budget to spend on things I actually use, all declarative in one
`zsh-enhancements.nix`:

- **zsh-abbr** — expand-on-space abbreviations for the commands my fingers type
  on autopilot: `git`, `nix`, `just`, `claude`.
- **dirHashes** — `cd ~nixos`, `~src`, `~dl`.
- **Esc-Esc** to prepend `sudo` to the last command (replacing the OMZ plugin).
- **fzf pickers** — `fj` (just recipe), `fgb` (git branch), `fh` (ssh host).
- **`wtf`** — pipe the last failed command to Claude and ask what went wrong.

The lesson I keep relearning: a framework is a default you've stopped
questioning. atuin, starship and stylix earn their place every shell. oh-my-zsh
and zplug were just where my config used to live before I knew better. 360ms and
no errors at login — I'll take it.
