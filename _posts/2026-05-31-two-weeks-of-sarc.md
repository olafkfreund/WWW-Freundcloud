---
layout: post
title: "Two weeks of SARC: wiring ServiceNow into three CI platforms"
date: 2026-05-31 00:57:24 +0100
permalink: /blog/two-weeks-of-sarc/
tags: [devops, cicd, platform, multicloud]
comments: true
excerpt: >-
  SARC is a reference platform for compliance-pipeline delivery — ServiceNow as
  control plane, Kosli as attestation data plane, the same flow running across
  GitLab, GitHub and Azure DevOps onto four clouds. Two weeks in, here's what
  shipped, why ServiceNow + CI/CD is harder than it should be, and how we got
  three CI platforms to agree on what "compliant" means.
---

I've been heads-down on **[SARC](https://gitlab.com/compliance-calitii/sarc)** —
"Synechron ARC" — for the past fortnight. It's a public, Apache-2.0
reference platform built to answer a question regulated-industry platform
teams keep asking me in different words: *"How do I prove my pipeline is
compliant without lying to my own audit trail?"*

This is a two-week status update. The architecture is the point; the project
name on top of it is incidental.

## What SARC is, in one paragraph

SARC wires **ServiceNow** (control plane: change requests, CMDB),
**Kosli** (attestation data plane: cryptographically pinned evidence at every
stage), and a **deployment app** (CNCF's `podtato-head`, deliberately boring
so the *pipeline* is what you look at) into a delivery flow that runs
**identically across GitLab CI, GitHub Actions and Azure DevOps**, onto
**EKS, AKS, GKE, or k3d** with a single `TARGET_CLOUD` env var. OpenShift
(ROSA HCP) is a fifth read-only target. The whole stack maps to DORA, PSD2,
SOC 2, ISO 27001, PCI-DSS, SR 11-7, NIST AI 600-1 and friends. Banks and
payments processors are the use case; the demo doesn't care which.

## The problem: pipelines that don't lie

Most "compliance CI/CD" demos quietly cheat. The pipeline runs a scanner job,
the job *exists*, and a `compliant=true` flag gets written somewhere
downstream. Whether the scanner actually *passed*, or whether it scanned the
right artefact, or whether the policy is even enforceable — those are
problems for someone else, usually at audit time, often a year too late.

SARC's job is to be the version that *doesn't* cheat. Compliance flags
derive from real scanner exit codes. Policy aliases coalesce scanner names
across services so you can't sneak past by renaming a job. Attestations are
keyed to artefact SHAs. The "honesty loop" is the part that took the longest
to harden, and the part most worth showing other teams.

## ServiceNow + CI/CD: why this is harder than it sounds

ServiceNow is the system of record for change management at most of the
banks I work with. The promise is: no production deploy without an approved
Change Request, no closed Change Request without evidence, the CR in
ServiceNow and the deploy in CI tell the same story.

The reality:

- **There is no first-class CI integration.** You roll your own. The
  Table API + REST endpoints are fine but you're authoring webhook-style
  glue, retry logic, idempotency, timeouts, and OAuth/PAT auth yourself.
- **Latency and rate limits.** A CR lookup on a busy instance can take
  several seconds; pipelines that block on it need careful budgeting.
- **Bidirectional truth.** The pipeline needs to *read* ServiceNow
  ("is the CR approved?") *and* write back to it ("we deployed
  SHA `abc123` to prod at 14:02"). Both halves have to survive partial
  failure without the CMDB and the cluster ending up in different
  realities.
- **Schema drift.** Every enterprise instance has its own custom
  fields, lifecycle states, and approval workflows. Your "approved"
  is not their "approved".

The pattern that worked: a small **MCP server** in the repo wraps
ServiceNow's API with a typed tool surface — `get_change_request`,
`assert_cr_approved`, `report_deployment` — and the pipelines call it via
ArgoCD PreSync / PostSync hooks. The MCP server handles auth, retries,
schema-mapping, and idempotency in one place. Pipelines stay declarative;
the messy bit is contained. Same approach works for Kosli: one MCP
server, six tools, every CI platform calls it the same way.

The unexpected win: because the same MCP servers are also reachable from
AI agents, it turns out you can ask Claude "show me all CRs blocking
this morning's deploys" and get an actual answer, not a hallucinated one.

## Three CI platforms, one pipeline

Most banks I work with run **at least two** of GitLab, GitHub and Azure
DevOps simultaneously, usually because of an acquisition, a re-platform
half-finished, or a strict line between regulated and non-regulated
estates. SARC has to demonstrate the same compliance posture on all
three. That ruled out "build it on the one I like best".

What worked:

- **GitLab is canonical.** All real work happens in `gitlab.com`. The
  `gitlab-compliance-templates/` directory is the source of truth for
  the compliance framework includes.
- **GitHub and ADO are force-mirrored replicas.** Pushes to GitLab
  trigger a mirror job that `--force-with-lease`-pushes the same refs
  to the GitHub and ADO repos. Mirror failures are `allow_failure: true`
  — a broken mirror doesn't break a real deploy.
- **Shared step templates.** A `detect-changes` stage, tool-version
  constants, and a buildx + registry-cache pattern live as templates
  consumed identically on all three platforms. The platform-specific
  YAML around them is thin.
- **OIDC to every cloud.** No static cloud credentials anywhere. Each
  CI platform federates to AWS / Azure / GCP via OIDC, scoped per
  environment. ADO + GitHub + GitLab all support it; the wiring is
  different in each but the resulting trust chain is the same.

The honest answer on what's *not* solved: cosmetic divergence. ADO's
Environment approvals don't map 1:1 to GitLab's manual jobs don't map 1:1
to GitHub's deployment environments. We exposed all three behind the
same MCP server so the portal can normalise — but in the raw CI YAML,
the approval gate is platform-shaped.

## What shipped in the last two weeks

A few themes, picked from ~340 commits:

- **MCP-Client Gateway** — the portal can now *propose* GitHub
  `issue_write` actions through an in-cluster `github-mcp-server`
  sidecar, then route them through an admin-approval UI before
  execution. AI agents propose, humans approve in a typed UI, gateway
  executes with full audit and idempotency. This is the most fun thing
  to demo.
- **Kosli honesty loop.** `KOSLI_COMPLIANT` now derives from real
  scanner exit codes, not job presence. `policy:aliases` coalesces
  scanner names across portal + podtato so policies stay enforceable
  when services rename their scanners.
- **Azure DevOps parity push.** Extracted shared `detect-changes`,
  added `Cache@2` for Helm/Terraform/binaries, bound `gitops_bump`
  and `dast_postsync_qa` to ADO Environments, consolidated DIY
  scanners into MSDO.
- **Self-hosted AWS-EC2 GitLab runner pool.** Multi-AZ fallback, nightly
  docker prune, larger default sizing because the portal kept OOMing on
  t3.medium during build. Buildx registry-cache layers cut average CI
  time by about a third.
- **Security sweep.** SSRF + deserialisation hardening across the
  portal's HTTP clients, Next.js 16.2.6 bump, capabilities tightened
  across charts and Dockerfiles, 24 SAST MEDIUMs triaged and 11
  critical findings closed.

## What's next

More closed-loop AI — the proposed/approved/executed pattern from the
MCP-Client Gateway, repeated across more tool surfaces. ServiceNow
write paths beyond CR-state-update (CMDB CI relationship pruning, mostly).
And cleaning up the still-platform-shaped approval gates by hiding them
behind a single portal control rather than three different CI UIs.

If you work somewhere with ServiceNow on one side, three CI platforms in
the middle, and an external auditor on the other side: the codebase is
public. Steal the patterns that help.
