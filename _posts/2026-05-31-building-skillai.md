---
layout: post
title: "Building SkillAi: CV keyword-match is a lie"
date: 2026-05-31 01:17:57 +0100
permalink: /blog/building-skillai/
tags: [ai, agents, platform]
comments: true
excerpt: >-
  Someone asked me to help with hiring, so naturally I built a platform instead.
  Here's why today's recruiting is mostly theatre, what SkillAi does about it,
  and the architecture choices I'm proudest of — including the MCP server that
  lets you orchestrate the whole thing without ever opening the app.
---

A few months back somebody asked me to "give them a hand with hiring."
What that means in practice is: read 200 CVs, work out who's worth a
30-minute call, and try not to reject anyone for the wrong reasons.

I did about ten of them properly and gave up. Not because the work was
hard — because the *tools* were terrible. So I did the thing I always do
when a workflow annoys me enough: I built one. It's called
**[SkillAi](https://github.com/olafkfreund/SkillAi)** and it's GPLv3 on
GitHub.

## What's actually broken with recruiting

Three things, depending on which side of the table you're sitting on:

1. **CV keyword-matching is a lie.** Every ATS I've ever used does some
   version of "if the CV contains 'Kubernetes' it's a match for the
   Kubernetes role." That's not evaluation, that's `grep`. Plenty of
   people who can ship Kubernetes never wrote it on their CV; plenty
   who *did* write it have never deployed anything to production.
2. **The big ATSs cost a fortune and own your data.** Greenhouse, Lever,
   Workday — pick your tens of thousands per year, plus a cheerful
   "your candidate data lives in our cloud now." For an agency or a
   consulting bench, neither of those is fine.
3. **Recruiters can't read code, and engineers can't read 200 CVs.**
   The bit that matters — "could this person actually do this job?" —
   falls in the gap between the two roles and rarely gets a serious
   answer.

I wanted a tool that closed that gap, didn't cost me five figures a
year, and let me keep candidate data on infrastructure I control.

## What SkillAi is

Self-hosted, multi-tenant recruiting portal. Next.js 16, PostgreSQL
with `pgvector`, Postgres row-level-security for tenant isolation
(every table has a `tenant_id`, RLS policies on all of them, cross-tenant
reads are architecturally impossible), Claude + Gemini for the AI layer,
Drizzle ORM, Auth.js, Tailwind. Runs `docker compose up -d` on a laptop;
deploys to AWS via Terraform (EKS + RDS + EFS + ECR + KMS) for about
£150/month if you size it sensibly.

It is deliberately **not** an ATS. ATSs solve workflow and compliance
plumbing. SkillAi solves the one thing they don't: *give me a
ten-second, explainable answer to "who are the best candidates for
this role, and why?"*

Two months in, the codebase is at 344 commits with real test coverage,
GDPR Article 17 erasure, an audit trail, EU/UK compliance fields, and
production-grade AWS hardening (control-plane logging, RDS deletion
protection, EFS prevent-destroy, secrets-as-K8s-Secrets, the
boring-but-important stuff).

## How it actually scores

Two pipelines, deliberately different shapes.

**Per-candidate scoring.** Claude `claude-sonnet-4-6` is called with
forced tool-use — `tool_choice: { type: 'any' }` against a
`submit_candidate_score` JSON schema — so the response is *always* a
structured object validated by Zod. There is no "parse the AI's text
response" code path anywhere in this codebase. Four dimensions, each
0–100 with reasoning: technical, experience, cultural fit,
communication.

The interesting parts of the prompt are what you don't get from a naive
implementation:

- **Customer framework bands.** If you're hiring into HSBC GCB5, the
  scoring prompt is told "TARGET BAND: GCB5" and the band description.
  The AI calibrates against the *target* seniority, not generic
  "years of experience." This single change made the rankings stop
  feeling random.
- **Soft budget signal.** Day rate vs candidate ask is mentioned to the
  AI as context, but it's explicitly told *not* to lower the four
  dimension scores on budget grounds. "Cheap" is not a synonym for
  "good." A senior who's £100 over budget shouldn't suddenly become a
  worse engineer.
- **HR skill packs.** Vendored talent-acquisition / people-analytics /
  EU-UK content gets appended as `HR_POLICY:` and the `skill_used`
  flag is logged so I can A/B compare with the pack off.

**Auto-match.** When a role is created, `pgvector` cosine-similarity
top-30 over Gemini embeddings → hard filters (availability, prior
rejection by that customer, ≤125% of budget) → top 3 survivors go
through Claude scoring tagged `auto_match_scoring` so spend hits a
separate $50/tenant/day cap. Hybrid retrieve-then-rerank, basically.

## The MCP server is the actual product story

Most recruiting tools try to *be* everything — calendar, email, drive,
notes, contracts. SkillAi explicitly doesn't. Instead it exposes a
48-tool **MCP server** at `/api/mcp` covering every action (scoring,
search, shortlist, interviews, approvals, GDPR exports, admin). Then
you point Claude Desktop at it, and the LLM composes workflows across
whichever MCP servers you already have — Gmail, Calendar, Drive,
GitHub, your CRM, whatever.

```
"Draft a polite rejection email to candidates who scored below 60
 on Role X, attach the role description, and BCC the hiring manager."
```

That single sentence orchestrates SkillAi + Gmail + the role's PDF
exporter. The LLM owns the workflow; SkillAi just owns its data.

Write tools require `confirmed: true` so "approve all candidates"
can't fire by accident. Tokens are argon2-hashed `skl_<env>_<24-base62>`,
scoped per tenant, sliding-window rate-limited. Read/write/admin
scopes are gated separately.

I'd been doing recruiter work in Claude Desktop *anyway* — pasting
CVs, drafting emails, comparing candidates. The MCP server just made
that the explicit shape of the product rather than the workaround.

## What landed in the last 30 days

A whirlwind:

- **Auto-match end-to-end** (May 21) — pgvector prefilter, Claude
  rerank, role-detail UI panel, wired into role creation.
- **AWS production hardening** — Terraform VPC/EKS/RDS/EFS/ECR/IAM,
  then a security sweep over the whole stack (encrypted state, EKS
  envelope encryption, locked API CIDRs, secrets via K8s Secret not
  env, the lot).
- **EU/UK compliance + GDPR** — right-to-work fields, share code,
  sponsorship state, processing consent, Article 17 erasure with PII
  redaction from `ai_usage`, audience-gated PDF compliance section.
- **HR skill packs system** — per-tenant toggle, injected into
  scoring + interview prep + transcript analysis, `skill_used`
  audit metadata.
- **Astro Starlight docs site** at `docs-site/`, auto-generated
  OpenAPI + MCP catalogue + DB schema reference. Skill-pool terminal
  theme because I couldn't help myself.

## Where it goes next

More MCP. The unfair advantage of the LLM-orchestrates pattern is that
every feature I add to SkillAi becomes one new verb the user can call
from any context. I'd rather ship five new MCP tools this month than
five new dashboard pages.

The whole thing is GPLv3 on
[GitHub](https://github.com/olafkfreund/SkillAi). If you want to run
the same hiring loop on your own infrastructure — `docker compose up`
or full AWS — go ahead, fork it, send me bugs.
