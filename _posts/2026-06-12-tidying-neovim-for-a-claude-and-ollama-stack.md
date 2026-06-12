---
layout: post
title: "Tidying Neovim for a Claude-and-Ollama stack"
date: 2026-06-12 13:16:00 +0100
permalink: /blog/tidying-neovim-for-a-claude-and-ollama-stack/
tags: [nixos, ai]
comments: true
excerpt: >-
  I pulled Codeium and Mason out of my Neovim, wired in local Ollama completion,
  and fixed a read-only-store bug that had been quietly failing every Lazy sync.
  Notes on making nvim behave on NixOS.
---

Right after [putting my zsh on a diet]({{ '/blog/cleaning-out-my-zsh-bye-oh-my-zsh-bye-zplug/' | relative_url }})
I turned the same eye on Neovim. Same disease, different editor: things I'd
enabled once, stopped using, and never removed — plus a NixOS-specific bug that
had been failing silently for weeks.

My AI stack is deliberately narrow: **Claude** (via Claude Code) for the heavy
agentic work, **Antigravity** (`agy`) as a second opinion, and **Ollama** for
anything that should never leave the machine. There is no Copilot here and no
Codeium. But my nvim config didn't know that yet.

## Dropping Codeium

Codeium was an `ai.codeium` LazyVim extra I'd added in a more promiscuous phase.
It wanted an account and a network round-trip for completions I now get locally.
Out it went.

The interesting bit is *how* it went. LazyVim normally manages extras through its
`:LazyExtras` UI — which is imperative state that lives outside my flake. That's
exactly the kind of thing I don't want on NixOS. So `lazyvim.json` is now
declarative, checked into the repo, with no codeium entry. The flake is the
source of truth for which extras exist, not a TUI I clicked through six months
ago and forgot.

## Mason doesn't work here, so turn it off

Mason is the LazyVim default for installing LSP servers and formatters. It
downloads prebuilt binaries — which **do not run on NixOS**, because they're
linked against an FHS layout that doesn't exist. People burn hours on this.

The right answer is to stop fighting it. LSPs and formatters come from Nix, on
`PATH`:

```nix
home.packages = with pkgs; [
  rust-analyzer pyright ruff
  nixd gopls nodePackages.prettier
];
```

And Mason gets a ten-line `mason.lua` that disables it and its auto-install
hooks. I verified `rust-analyzer`, `pyright` and `ruff` still attach to buffers
with Mason fully off — they do, because they were always coming from Nix anyway.
Mason was a second, broken package manager bolted onto the one that actually
works.

## Adding the local layer back

With the dead weight gone, I wired in the Ollama coding stack I actually wanted:

- **minuet-ai.nvim** — inline fill-in-the-middle completion against Ollama's
  `qwen2.5-coder:7b`, surfaced as a [blink.cmp](https://github.com/Saghen/blink.cmp)
  source with a score offset so it ranks sensibly against LSP completions.
  Throttled, and `OLLAMA_ENDPOINT` overrides the host so my laptop can borrow the
  workstation's GPU. Copilot, but local.
- **codecompanion.nvim** — chat, inline and agentic edits against the bigger
  `qwen2.5-coder:14b`, under `<leader>o`. Claude keeps `<leader>a`, Ollama gets
  `<leader>o`, and `<leader>ag` drops `agy` into a terminal split. Three AIs,
  three leaders, no overlap.
- **oil.nvim** — an editable file explorer that Claude Code can hook for
  `@`-mentions.

Everything points at the same models the rest of the machine uses. Nothing new
to install, nothing to authenticate.

## The bug that was failing every sync

This is the one that actually annoyed me. Every `:Lazy sync` showed blink.cmp as
**`Failed (1)`** and I'd been ignoring it. The error, once I read it:

```text
E152: Cannot open .../doc/tags for writing
```

lazy.nvim runs `:helptags doc/` after every sync to rebuild help tags. But
blink.cmp was installed via Home Manager's `home.file`, which symlinks it into
the **read-only Nix store**. You can't write `doc/tags` into a read-only
directory, so helptags failed, every time.

`home.file` stays read-only even with `recursive = true` — that's by design. The
fix is to copy the plugin into a writable directory on activation instead of
symlinking it, and make the copy idempotent with a source stamp so it only
re-copies when the store path actually changes:

```nix
# copy-on-activation: writable dir, re-copied only when the
# blink.cmp store path changes (stamped to avoid churn)
home.activation.blinkCmp = lib.hm.dag.entryAfter ["writeBoundary"] ''
  # ... compare stored stamp, rsync from $src if different ...
'';
```

After that, `doc/tags` is writable, `Lazy sync` finishes clean, and the editor
stops lying to me about its own health.

## The pattern

Both cleanups — zsh and nvim — were the same shape. Remove the tools that
duplicate what Nix already does (Mason, zplug, oh-my-zsh's plugins). Remove the
integrations for services I don't use (Codeium, Copilot). Make the config
declarative so it can't drift behind a UI. And read the errors you've been
trained to scroll past — they're usually pointing at the exact thing you should
delete.

Verified on p620 and razer: plugins install and load, the FIM endpoint returns
completions, LSPs attach with Mason off, and there's not a single Codeium or
Copilot warning left at startup. Quiet is the goal.
