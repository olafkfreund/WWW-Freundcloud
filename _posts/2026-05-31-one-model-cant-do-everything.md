---
layout: post
title: "One model can't do everything"
date: 2026-05-31 15:40:00 +0100
permalink: /blog/one-model-cant-do-everything/
tags: [ai, agents, platform, multicloud]
comments: true
excerpt: >-
  Why no single LLM is the right tool for every phase of a job, how
  AIFactory routes plan/code/QA across different models and providers —
  Claude, local Ollama, Bedrock, Gemini — and how that turns into auditable
  internal workflows that save time, money, and a lot of debugging headaches.
---

Procurement wants one vendor, one model, one bill. I understand the urge —
it's the same urge that makes people buy a single adjustable wrench and call
it a toolbox. It works right up until you need to actually torque something.

A frontier reasoning model is overkill for renaming a variable. A cheap local
model that's perfectly fine at boilerplate will happily hallucinate your auth
flow with total confidence. Picking one model for everything means you're
either overpaying for the easy 80% or under-resourcing the hard 20%. Usually
both.

## A job isn't one task

The thing people miss is that shipping a change isn't a single prompt. It has
phases, and each phase has a different cost/quality shape:

- **Spec + plan** — wants a strong reasoner. This is where getting it wrong is
  expensive, because everything downstream inherits the mistake.
- **Coding** — most of it is boilerplate the cheap models handle fine. Route
  the bulk there; save the expensive brain for the gnarly bits.
- **QA** — wants a *skeptical second opinion*, and ideally a **different model
  than wrote the code**. A model reviewing its own output is an echo chamber
  with extra steps.

So the interesting unit of choice isn't "which model" — it's "which model, for
*which phase*."

## What I actually do

This is the whole reason [AIFactory]({{ '/work/#aifactory' | relative_url }})
does per-phase model selection instead of a global setting. The pipeline —
planner → coder → QA — stays the same; only the routing changes:

```text
plan:  claude-opus               # the expensive brain, where it pays off
code:  ollama:qwen2.5-coder:14b  # local, free, fast, fine for the 80%
qa:    claude-sonnet             # a different lens than the coder used
```

Three lines. No rewiring, no separate tools, no "AI platform" committee. Plan
with Opus, let a local qwen do the typing, have Sonnet play bad cop on the
result.

## Why this matters more in an enterprise, not less

The "one model" fantasy falls apart fastest exactly where the stakes are
highest:

- **Data residency.** Some repos can't leave the perimeter. Route those
  through a local Ollama or a Bedrock/Vertex model in your *own* cloud account;
  route the low-sensitivity stuff to a frontier API. Same workflow, different
  endpoint per task.
- **Cost.** Sending every keystroke to a frontier model is how you turn up to
  the quarterly review explaining a five-figure inference bill. Push the bulk
  to cheap or local, reserve the premium model for the 20% that needs it.
  Delegating the coder phase to a local model or a provider agent cuts spend
  roughly 10× on those tasks.
- **Audit.** Every phase logs which model ran, on which spec, with which
  prompt, reviewed by whom. When someone in risk asks "what wrote this line and
  who checked it," that's a query, not a shrug.

> The model that's cheapest to run and the model that's safest to trust are
> rarely the same model. Pretending otherwise is a budget line or an incident,
> your choice.

## The debugging win nobody mentions

Here's the one that saves the most hours in practice. When a build gets stuck —
the coder keeps producing the same broken patch, QA keeps bouncing it — the
variable is usually *the model*, not your prompt. With per-phase routing you
swap the coder from a local 14B up to Sonnet, re-run that one phase, and move
on. No rewriting, no starting over.

A second model is a second pair of eyes that doesn't share the first one's
blind spots. I've watched a task ping-pong for twenty minutes under one model
and clear in a single pass under another. That's not magic — it's just that
different training mixes fail differently.

## Turning it into a workflow

A model picker is a toy. The point is to make it a *tool your process calls*,
not a chat box your engineers babysit. AIFactory exposes an MCP control plane,
a `/handover` skill for Claude Code, and delegation to GitHub Copilot or GitLab
Duo — so you can wire it into the flow you already have:

> issue triaged → spec + plan on Claude → coding delegated to Copilot on a
> normal repo, or to local Ollama on a sensitive one → QA on Sonnet →
> merge-ready branch, with the whole chain audit-logged.

Internal teams build their own flows on top of that without me being in the
loop. Spec-driven, reviewable, and self-hostable — which is the only version of
"AI in the pipeline" a regulated shop will actually sign off on. The docs walk
through it at [aifactory.freundcloud.com](https://aifactory.freundcloud.com).

## The headache it actually removes

The headache was never "AI writes bad code sometimes." It's "I committed to one
model and one vendor, and now half my job is fighting that decision." Choice
per job — per *phase* — makes the decision reversible. Wrong model? Change one
line and re-run. Vendor outage? Reroute. New cheaper model drops? Try it on the
boilerplate first, keep the expensive one where it earns its keep.

One wrench is not a toolbox. One model is not a strategy.
