---
layout: post
title: "Voice into the prompt: Groq, ydotool, and seven PRs"
date: 2026-05-31 16:00:20 +0100
permalink: /blog/voice-into-the-prompt/
tags: [nixos, ai, agents]
comments: true
excerpt: >-
  I wanted to talk to Claude Code instead of typing. Took seven PRs, two
  dead protocols, and one stale dconf key — but pressing a hotkey and
  watching the transcript appear in the focused terminal is genuinely
  worth it. Notes on what I tried, what failed, and why Groq + ydotool
  won.
---

I've been using Claude Code, Codex, and Antigravity CLI more than my
own fingers care to admit, and most of what I send them is short:
"fix the failing test in `auth.py`", "what does this regex actually
match", "bump warp-terminal and PR it." Stuff I'd happily *say* if there
were a key to push. So today I built that.

The endpoint is simple: hold `Super+Shift+Space`, talk, release, the
transcript appears in whatever terminal is focused. Works with any CLI
because the typing is app-agnostic. Path to get there was anything but
simple.

## Three architectures, one won

I started with three shapes on the table.

**A — voice to keystrokes.** Hotkey → record → transcribe → type into
the focused window. Works with literally any app because there's no
integration; it's just keyboard input.

**B — voice to a tmux pane.** Same record + transcribe, but `tmux
send-keys` into a *specific* persistent pane running `claude
--continue`. Doesn't need the terminal focused. "Jarvis for coding."

**C — voice to print mode + TTS reply.** Record, transcribe, call
`claude --print "..."`, capture the response, speak it via Piper.
Hands-free but you give up interactive file edits and tool use, which
is most of what makes these CLIs valuable.

I picked **A**. B was tempting, but voice as a parallel input channel
to an *interactive* CLI session keeps the agents in the mode they're
actually good at. C trades away too much.

## Whisper, in three flavors

Voice → text needs a Whisper backend. Three options, ranked by what I
actually ended up wanting:

- **Local `whisper-server` on p620 via `whisper-cpp`.** Free, private,
  works offline. nixpkgs ships it CPU-only (no hipBLAS build flags),
  so on base.en it's ~1.5–3 s per phrase. Fine, not snappy.
- **OpenAI Whisper API** (`whisper-1`). ~500–800 ms, $0.006/min. Same
  model nixpkgs ships, just hosted.
- **Groq Whisper-Large-v3.** ~200–400 ms, **$0.000111/min**. Same
  Whisper Large model OpenAI hosts, but on Groq's LPU silicon. 60×
  cheaper than OpenAI, 3–4× faster.

Groq's the obvious pick. I left the local backend wired as a fallback
for offline use — flipping back is one line in `profile.nix`.

## What didn't work

Here's where the time went.

**`wtype` does not work on GNOME Wayland.** Mutter has, on principle,
declined to implement the `virtual_keyboard_v1` Wayland protocol that
`wtype` (and `xdotool`'s Wayland cousins) need. You get a polite
*"Compositor does not support the virtual keyboard protocol"* and your
text goes nowhere. The fix is `ydotool`, which writes via `/dev/uinput`
at the kernel level and doesn't care what compositor you're running.
Different tradeoffs — needs a system daemon (`ydotoold`) and user
group access to the socket — but it actually works.

**A typo in my existing `keybindings.nix` had been quietly broken for
months.** The custom-keybindings list was being written to
`/org/.../media-keys/custom-keybindings/custom-keybinding-list`
(singular + `-list`, under the subdirectory) when GNOME reads
`custom-keybindings` (plural, at the parent path). Every prior
"reload to apply" silently dropped the list. I only noticed because
my new dconf write to the *correct* path competed with the broken
one and home-manager's list-merge made things weirder. Fixed by
rewriting the path. The lesson: dconf typos don't fail, they just
don't take effect.

**`programs.ydotool.enable = true` does *not* add your user to the
`ydotool` group.** I assumed it would. It doesn't — the option just
runs the daemon and exposes the binary. You have to add
`"ydotool"` to `users.users.<you>.extraGroups` yourself, *and* log
out and back in for the new group to land in your live session.

**Home-manager's dconf activation doesn't fire reliably during a
NixOS-module-mode rebuild.** The activation script ran, but `dconf
load` didn't get called against my live session. Manually `dconf
write`-ing the keybind worked and persists across reboots, so I shipped
that as a workaround. Real fix is a separate yak.

Seven PRs in total: feature, three bug fixes, a TasksMax bump for
whisper-server (`pthread_create EAGAIN` when I capped threads too
tight), an "actually use Groq" wire-up, and the user-group fix.

## The current shape

```
hotkey (Super+Shift+Space)
   │
   ▼
voice-input  ← writeShellApplication (sox VAD + curl + ydotool)
   │
   ▼  ~16 kHz mono WAV, ~1–10s
api.groq.com/openai/v1/audio/transcriptions
   │
   ▼  text, ~250 ms round trip
ydotool type --delay 5 -- "$TEXT"
   │
   ▼
whatever window is focused
```

API key in agenix (`api-groq.age`, recipients = `allUsers ++ allHosts`,
script reads `/run/agenix/api-groq` at runtime — never embedded in the
store). VAD auto-stops the recording on 2 s of silence, hard cap 30 s.
Notifications report `🎙️ Listening` → `🎙️ Typed: <transcript>`.

## What this opens up

A few things I'm already using it for:

- **Dictating to Claude Code while looking at the screen, not at the
  keyboard.** Faster than typing for anything multi-sentence.
- **Quick prompts to Codex / Antigravity** without switching context to
  type — same hotkey, whichever terminal happens to be focused.
- **Shell commands** when you know what you want but don't want to
  type the full sentence: "git log since yesterday with stat" lands in
  the prompt and you hit enter.
- **Search queries, browser URLs, anything keyboard.** The script
  doesn't know what app it's typing into.

The next thing I want is push-to-talk *with* release detection (right
now VAD is fine but feels a beat slow). After that, maybe a per-prefix
router so saying "codex: …" sends to a Codex pane instead of the
focused window — but I might end up back at Shape B for that, and I'm
not sure it's worth the bookkeeping.

For now: hotkey, talk, transcript. Boring shape, the right kind of
boring.
