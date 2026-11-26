---
layout: post
title: "nixarchy: teaching the pipeline to look after itself"
date: 2026-11-26 14:54:49 +0100
permalink: /blog/nixarchy-teaching-the-pipeline-to-look-after-itself/
tags: [nixos, agents, cicd]
comments: true
excerpt: >-
  GitHub ran every scheduled job nine hours late, my own agents kept running
  the account out of API calls, and every release still needed me at the
  keyboard. A week of making nixarchy's maintenance loop run without me.
---

[nixarchy]({{ '/blog/nixarchy-omarchy-on-nixos/' | relative_url }}) has a lot
of automation. A nightly job boots VMs and installs the desktop from scratch.
A daily job bumps every pinned app. Another moves the flake inputs. A review
job reads all of it at 06:00 and edits one GitHub issue with what needs doing.
On paper, the project maintains itself.

In practice I spent this week starting workflows by hand, launching four
freshly bumped apps so their PR could merge, moving two commit pins the review
had flagged, and deploying edge to my desktop and laptop. Every step was
automated except the part where something decides to take it. So that became
the work: an epic called *self-running maintenance*, seven pieces, and the
rule that I should be reading outcomes, not driving each step.

## GitHub's scheduler is "best effort"

On 25 November none of the scheduled workflows ran at their time. The nightly
due at 03:00 arrived at 12:01. The review due at 06:00 arrived at 16:18, and
then failed on a GitHub API error. Nothing noticed, because the review is the
job that reports a workflow that hasn't run, and the review was late too.

The fix is a watchdog that doesn't live on GitHub. A timer on my desktop, every
five minutes, asks for each scheduled job whether its slot has had a run.
If not, and nothing is queued, it dispatches one. When GitHub's own late copy
turns up hours afterwards, it cancels that, so the job doesn't run twice.

That last rule sounds simple and isn't. The weekly workflow has three jobs
on three schedules, and with delays of nine hours a run's creation time can't
tell you which job it is. So the watchdog never cancels a weekly run. The edge
workflow cancels whatever was running when a new run arrives. So the watchdog
only cancels a late run while its own run is still alive, or the day ends with
no edge run at all. Codex found that one in review. I'd have shipped it.

My favourite bug of the week came out of the first live dry run:

```text
jq: Argument list too long
```

A dev shell exports `$out`. Bash keeps the export attribute on a `local out`,
so a 250 KB API reply went into the environment of every child process, and
Linux refuses any single string over 128 KiB. The fixture tests passed because
their replies were small. There's now a fixture with a reply over 128 KiB, and
the trap is written into the repo's agent notes for whoever hits it next.

## My agents were eating the API budget

The account ran out of its 5,000 GitHub requests an hour on three days running.
I measured instead of guessing: 69 requests one minute, 145 the next. I ruled
out the laptop, the k3d cluster and the hosted CI. What was left was short
`gh` calls from agent sessions on the desktop. `gh run watch` polls every three
seconds by default, a few requests a tick, so a single watcher costs about 40
a minute.

A paragraph telling agents to be polite wouldn't survive the next busy
afternoon, so it's a hook. My Claude Code guard now refuses `gh run watch` and
`gh pr checks --watch` without an `--interval` of 30 seconds or more. Its test
fails with the rule switched off, which in this repo is the bar for calling
something a check.

## Two bugs from a stranger's fresh install

Someone installed nixarchy and got two errors at login: `module 'hypr.monitors'
not found`, then `Command not found: "herdr"`. Both had one cause. Their account
had never had the per-user Home Manager step, and only that step wrote the
Hyprland files and installed herdr.

Every VM test here logs in as a user called `omarchy`, whose setup has always
run. The suite was green the whole time, because it never varied the one thing
that broke. Now a missing Hyprland file falls back to the shipped default, and
herdr ships system-wide. Each fix has a check that fails without it.

## Who does what

Most of this week's code was written by Codex, not by me or Claude.

The split that settled in:

- **Claude** leads: writes the intent, spec and plan, runs every check
  locally, reviews the diffs, commits, and never lets a finding go.
- **Codex** does a read-only design pass from the actual files, with line
  references. Then it implements in its own herdr tab, and reviews the result
  again.
- **Me:** I approve the shape and merge anything that changes CI.

Every check has to be shown failing before it's trusted, which caught more
than once a check that couldn't fail.

It isn't magic. I pinned two edge rows to a dated version string. Edge stamps
the run's date into its version, so the rows went stale the next morning and
held edge back for an afternoon. Codex once read a PR number out of the wrong
line, and an "@codex review" landed on a pull request merged months ago. The
difference from a year ago is that these get found in an hour, by the process,
and written down.

## What's actually on

Honest status, because "done" is a strong word:

- **The watchdog script** is merged. Its p620 timer goes live with the next deploy.
- **The default milestone for new issues** is live. **The API guard** is
  merged, and takes effect on each machine at its next switch.
- **A Claude fixer for red bump PRs** replaces Copilot. It's three jobs, so the
  token never shares a job with PR code. It's queued to merge, along with
  **stale-pin proposals** and the **herdr fix**.
- **The launch test** that would let bump PRs merge themselves is being built.
  Auto-merge ships off until I've seen it run.
- **Hosts following edge** is built and switched off. Codex flagged missing
  safety gates. Reading the script, I found the laptop's path ignored its
  "don't switch" flag entirely. So for now the pin bump is automatic and the
  switch is still mine.

That last one is the right answer for a machine I'm sitting at. The rest of
the loop can get on with things without me.
