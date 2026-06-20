---
layout: post
title: "Factories, bridges, and a fleet that heals itself"
date: 2026-06-20 11:48:51 +0100
permalink: /blog/factories-bridges-and-self-healing/
tags: [ai, agents, devops, platform]
comments: true
excerpt: >-
  A roundup of what I've been building lately — a four-product governed pipeline
  for AI software delivery, a review-first Azure DevOps → GitHub Actions migrator,
  self-healing for Linux fleets, and an Android phone you can hand to an agent.
---

I've shipped a lot of small things lately and a few large ones, and the thread
running through all of them is the same: I trust AI to *do* the work and I trust
it not at all to be *accountable* for the work. Everything below is an attempt to
put a human gate, a signature, or an audit trail exactly where the agent would
otherwise just say "trust me." Here's the tour. The full writeups live on the
[work page]({{ '/work/' | relative_url }}); this is the why.

## AIFactory grew up into a suite

What used to be one project — AIFactory, turning a GitHub issue into a pull
request — is now a four-product suite built around a pipeline I call **PARR**:
**Prepare · Act · Reflect · Review**.

- **PFactory** *prepares*: it plans work grounded in live cloud and Backstage
  context, runs architecture, security and feasibility gates with citations, and
  only emits GitHub epics once a human has signed the plan.
- **AIFactory** *acts*: specs become code and QA in isolated git worktrees,
  model-agnostic across Claude, Gemini, OpenAI and local Ollama.
- **TFactory** *reflects*: it generates and runs tests in ephemeral sandboxes and
  grades each run on five signals — coverage delta, stability, mutation testing,
  lint and semantic relevance.
- **CFactory** *reviews*: a control-tower cockpit with a live dependency graph
  across plan → code → test, an advise-and-confirm copilot, and per-task cost and
  token tracking.

The number that made me build it: 84% of developers use AI coding tools, but only
29% trust the output. The Factory suite is the governance layer for that gap. The
glue is deliberately boring — a shared correlation key, a normalized
completion-event schema, HMAC-anchored logs — which is precisely the audit trail
the EU AI Act is about to ask everyone for. [More on the Factory
suite →]({{ '/work/#factory' | relative_url }})

## Bifrost: the other 10% of a migration

GitHub's own importer gets an Azure DevOps pipeline maybe 90% of the way to a
GitHub Actions workflow. **[Bifrost]({{ '/work/#bifrost' | relative_url }})** is
the other 10% — the review, the validation, the portfolio-scale coordination and
the audit trail it leaves to you. Nothing is silently rewritten: the importer
does a dry run, Bifrost parses the gaps, and each gap goes to an LLM *grounded* in
the actual source and the failure, so the model fills a specific hole instead of
converting from scratch. Risk scoring stays deterministic and explainable; the
model explains, it doesn't decide. It's air-gap capable on local models, because
the shops that have hundreds of pipelines to migrate are exactly the ones whose
pipeline definitions can't leave the network. Rust and React, MIT, building in the
open.

## ravn-agents: self-healing that never decides on its own

If you've ever been sold "AIOps," you've been asked to trust a black box with
root. **[ravn-agents]({{ '/work/#ravn' | relative_url }})** is my answer to that.
Detection is *deterministic* — rules you can read, not a statistical model you
have to believe. Remediation runs from pre-authored, risk-tiered templates that
need human or signed-policy approval, and every command is Ed25519-signed,
verified and logged to an append-only trail. The local model only ever
*explains*. It runs on standalone hosts, Kubernetes and fully air-gapped
networks, because inference is local and on CPU. Rust, React, MIT.

## lxconnect: handing your phone to an agent

This one's smaller and stranger and I like it a lot.
**[lxconnect]({{ '/work/#lxconnect' | relative_url }})** bridges Android to the
Linux desktop, and the good half is the **MCP server it runs on the phone**. The
Android app stands up a Ktor MCP server and hooks into Android's notification and
package APIs, so an agent on my laptop can treat the phone as a set of tools: read
notifications, open native deep links, launch apps, read system status, drive the
camera. "My phone" becomes something a Claude session can actually reach. It's a
Nix flake — `nix run github:olafkfreund/lxconnect#gui` and you're live.

## The two sides of the hiring table

I ended up building both ends of recruiting, a year apart and from opposite
chairs. **[SkillAi]({{ '/work/#skillai' | relative_url }})** is the recruiter's
side: a self-hosted ranker that answers "who are the best candidates, and why" in
seconds, instead of paying Workday tens of thousands a year to store your people
on someone else's servers and still rank them by keyword. It's in production
hiring for HSBC's Kraków hub. **[rolehunter]({{ '/work/#rolehunter' | relative_url }})**
is the candidate's side: score a job against your CV, auto-tailor an ATS-friendly
CV and cover letter, track applications, and — my favourite touch — cluster the
skill-gaps from every rejection into a study plan. Both self-hosted, both GPL,
both keeping the sensitive data on your own box.

## And a pile of desktop Rust

Quieter, but it's where I unwind: **[gog and gogmail]({{ '/work/#gog' | relative_url }})**
put all of Google Workspace into a terminal TUI with a Gemini side-panel that can
actually act; **gnome-quick-web-apps** turns any website into a native GNOME app;
and there's a steady drip of COSMIC applets, an RDP server, and a real-time
Hyprland config TUI. The [work page]({{ '/work/' | relative_url }}) has the lot.

The common shape, again: let the model do the work, never let it be the last word.
That's the whole philosophy, and lately it's been a productive one.
