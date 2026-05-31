---
layout: post
title: "One-button meetings: record, transcribe, summarize, done"
date: 2026-05-31 18:06:45 +0100
permalink: /blog/one-button-meetings/
tags: [nixos, ai, agents]
comments: true
excerpt: >-
  Press a key, have your meeting, press the key again. Five minutes later a
  markdown brief lands on disk with TL;DR, action items, decisions, and the
  full diarized transcript — all produced on my own hardware. Notes on the
  pipeline, the topology, and the small decisions that made it pleasant.
---

I'm in a lot of meetings. Note-taking is friction, I keep losing action
items, and the SaaS tools that promise to fix this either send my
conversations to someone else's cloud or stitch together a half-dozen
browser tabs to do it. So today I shipped a thing that does it the way
I actually want it: one keybind, local hardware, files on disk.

Press `Super+Shift+M`. Have your meeting. Press `Super+Shift+M` again.
Roughly five minutes later, a desktop notification pops up: *Meeting
brief ready*. Open `~/meetings/2026-05-31-1430.md` and there's a TL;DR,
your action items (separated from everyone else's), key decisions, open
questions, timestamped mentions of flagged keywords like *blocker* or
*deadline*, a topic timeline, participants with talk-time estimates, and
the full diarized transcript at the bottom. All produced by a pipeline
that ran entirely on my own machines.

## The pipeline, in four chunks

```
record  ──▶  transcribe         ──▶  summarize          ──▶  render
ffmpeg       whisperX large-v3       ollama mistral          bash + jq
+ pulse      + pyannote diarize      format=json             checkboxes
```

**Record.** `ffmpeg` with two PulseAudio inputs — the mic and the
*monitor* of the default sink (i.e. whatever the speakers are playing,
which on a video call is everyone else). Mix them with `amix`, encode to
16 kHz mono Opus at 24 kbps. That's ~1 MB per minute, so a three-hour
board meeting weighs ~180 MB — small enough to live in memory
comfortably for downstream tools.

```bash
ffmpeg -nostdin \
  -f pulse -i "$default_source" \
  -f pulse -i "${default_sink}.monitor" \
  -filter_complex "[0:a][1:a]amix=inputs=2:duration=longest:normalize=0" \
  -ac 1 -ar 16000 -c:a libopus -b:a 24k -application voip \
  "$audio_file"
```

I started thinking I'd need to build a PipeWire combined source via
`pw-loopback`, which is a real rabbit hole. The two-pulse-inputs-with-amix
pattern is dramatically simpler and works on any GNOME desktop that
already runs `pipewire-pulse` (i.e. all of them). `SIGINT`-on-stop with
a five-second poll flushes the Opus trailer cleanly; the keybind shell
exiting doesn't kill ffmpeg because `setsid + nohup` detach it.

**Transcribe.** `whisperX` running on CPU with `int8` quantisation. On a
16-core Threadripper that's roughly 10× realtime for the `large-v3`
model, so a 60-minute meeting transcribes in about 6 minutes.
Diarization via `pyannote/speaker-diarization-3.1` labels segments with
`SPEAKER_00`, `SPEAKER_01`, and so on.

I expected to spend an evening packaging whisperX. Instead `pkgs.whisperx`
(3.8.5 — yes, *really* in nixpkgs) pulls the entire
`pyannote/torchaudio/faster-whisper/lightning` Python stack from the
binary cache. No source builds, no shimming, no virtualenv. The only
friction is the HuggingFace token dance for the pyannote weights, more
on that below.

**Summarize.** Ollama, also local, running `mistral-small3.1`. Called
via `/api/chat` with `format: "json"` and a strict schema embedded in
the user prompt:

```text
Return a JSON object with EXACTLY these fields:
{ "user_speaker_label": "SPEAKER_XX or null if unclear",
  "tldr": "2-3 sentence summary",
  "your_action_items":  [ {"task":"...","deadline":"...","context":"..."} ],
  "other_action_items": [ {"assignee":"...","task":"...","deadline":"..."} ],
  "key_decisions":  ["..."], "open_questions": ["..."],
  "flagged_moments":[ {"timestamp":"MM:SS","speaker":"...","keyword":"...","context":"..."} ],
  "topic_timeline": [ {"start":"MM:SS","end":"MM:SS","topic":"..."} ],
  "participants":   [ {"label":"SPEAKER_XX","likely_identity":"...","talk_time_pct":0} ] }
```

The surprise was how clean the output is at `temperature=0.2` on the
first try. Mistral-small just *follows the schema*. The cleverer bit:
the prompt also tells the model *"one of these speakers IS the user —
identify which one from context"* and it figures it out from who others
address by name, who hosts, who answers specific questions. It works
well enough that I haven't bothered with voice fingerprinting.

**Render.** A bash script with `jq` queries pulls the JSON apart and
emits the markdown brief. Action items become `- [ ]` checkboxes, which
means they're directly actionable in any markdown reader (Obsidian, vim,
GitHub) without retyping. That's the smallest UX decision with the
biggest day-to-day payoff.

## Distributed by default

Two hosts run this: my laptop (where most meetings happen) and my
workstation (where the heavy compute lives). They share one `meet` CLI
but a single module option picks behaviour:

```nix
# razer (laptop)
features.meetingTranscribe = {
  enable = true;
  processHost = "p620";   # rsync .opus up, ssh meet-process, rsync .md back
};

# p620 (workstation)
features.meetingTranscribe = {
  enable = true;
  processHost = "local";  # whisperX + ollama right here
  installProcessor = true;
};
```

Razer records, then `rsync`s the audio to p620 over Tailscale, SSHes
there to run `meet-process`, and `rsync`s the resulting markdown back.
The laptop never touches whisperX. Same `Super+Shift+M` keybind, same
notification, same output path — the module just decides at runtime
where the work happens.

## The NixOS-y bits worth flagging

The whole thing is a single feature module
(`modules/services/meeting-transcribe.nix`, ~730 lines) enabled per-host
with `features.meetingTranscribe.{enable, processHost, ollamaModel,
userName, userEmail, flagKeywords, …}`. Both scripts are
`pkgs.writeShellApplication` derivations, which means `shellcheck` runs
as part of the Nix build and refuses to install garbage. That caught
four real bugs during this build, including a dead `let` binding, an
unused variable, and a `sed` invocation where bash parameter expansion
would do.

The HuggingFace token is an `agenix` secret. If it's missing — which it
will be the first time you deploy — diarization gracefully degrades to a
plain transcript without speaker labels. **No assertion blocks the
deploy.** Add the secret later, redeploy, and diarization lights up.
This is the right shape for one-secret-the-user-has-to-go-fetch
features: don't make first-deploy hostage to a setup step that has
nothing to do with the rest of the system.

The GNOME keybind is declarative via `dconf` in a single
`keybindings.nix` file. Per [the voice-input
post]({{ '/blog/voice-into-the-prompt/' | relative_url }}), GNOME's
custom-keybindings list is the kind of dconf key where two modules
writing to it silently drops entries — so we treat one file as the
single source of truth, and adding `Super+Shift+M` is a five-line block.

## Caveats

A few rough edges I've left to fix later:

- **HuggingFace token dance.** You need a free HF account, *plus* you
  must accept the EULA on two pyannote models
  (`speaker-diarization-3.1` and `segmentation-3.0`), *plus* generate a
  read token, before diarization works. The script tells you, but it's
  still annoying for a first-time setup.
- **CPU whisperX isn't free.** ~10× realtime on a 16-core CPU means a
  one-hour meeting takes ~6 minutes to process. Fine for "press button,
  get notes a few minutes later", not for real-time captioning. ROCm
  wheels for CTranslate2 aren't in nixpkgs yet; when they land I'll
  switch.
- **Speaker-identity heuristic misfires in 1-on-1s.** When both speakers
  say "I think we should…" in similar tones, the LLM occasionally swaps
  the labels. For 5+ people it's reliable; for two-person calls I
  sometimes have to manually flip the assignees.

## What's next

Two things on my list:

- **Rolling inbox.** Pipe the day's action items into a single
  `~/meetings/inbox.md` so I have one weekly-triage file instead of N
  per-meeting briefs.
- **Auto-issue creation.** When a meeting is clearly about a specific
  repo, optionally `gh issue create` for each "your action item" with a
  link back to the brief. Opt-in via a flag (`meet stop --issues=nixos`)
  rather than always-on, because I don't want every chat with my
  partner about laundry showing up as GitHub issues.

For now: hotkey, talk, brief in five minutes. Same boring-on-purpose
shape as the [voice-input
post]({{ '/blog/voice-into-the-prompt/' | relative_url }}), just on a
different time scale. The PR is
[olafkfreund/nixos_config#699](https://github.com/olafkfreund/nixos_config/pull/699)
for anyone who wants to read the module.
