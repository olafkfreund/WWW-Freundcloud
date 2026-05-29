---
layout: landing
title: Work
permalink: /work/
description: Projects and platforms Olaf Krasicki-Freund has designed and built.
---

<section class="section">
  <div class="container prose">
    <h1 class="mt-0">Work</h1>
    <p>A handful of the things I've built or led. Some are client programmes I can
    only describe in outline; the open-source ones you can go and read.</p>

    <h2 id="sarc">SARC — multi-cloud compliance pipeline</h2>
    <p><span class="tag">Product owner &amp; lead architect</span></p>
    <p>SARC is Synechron's demo platform for regulated CI/CD — the thing you put in
    front of a prospect who needs to see ServiceNow, Kosli and their CI talking to
    each other before they'll believe it. I own the architecture and most of the
    build.</p>
    <p>The trick that makes it worth showing: the same repository deploys to AWS,
    Azure, GCP or a local k3d cluster off a single <code>TARGET_CLOUD</code>
    switch, which drives the Terraform, the kubectl auth, the Helm values and the
    Kosli environment naming. Each cloud uses its own native data services and
    identity federation — IRSA, Workload Identity, WIF — rather than a
    lowest-common-denominator fudge.</p>
    <p>GitLab is the source of truth, mirrored automatically to GitHub and Azure
    DevOps on every green pipeline, with 17 dispatchable GitHub Actions workflows
    for the GitHub-native customers. Every image is built in-house, scanned with
    trivy, signed with cosign and attested through Kosli — twelve Kosli
    environments (four clouds × dev/qa/prod) feeding one compliance flow. Promotion
    runs dev → qa → prod, gated by a Kosli risk score, then a ServiceNow change
    request, then a GitOps tag bump through ArgoCD. There's also a pair of Claude
    MCP servers for Kosli and ServiceNow, so you can ask the compliance state of a
    commit in plain English during a demo.</p>

    <h2 id="skillai">SkillAi — open-source AI recruiting</h2>
    <p><span class="tag">Author &amp; lead architect · GPL v3</span></p>
    <p>SkillAi is a self-hosted recruiting platform built on Claude and Gemini that
    ranks, compares and archives candidates against a role — and keeps every CV,
    score and note on infrastructure the team controls. I built it because the
    incumbents solve the workflow problem and leave the actual hard part, ranking
    people fairly, to a keyword match.</p>
    <p>It parses CVs in every format people actually send (PDF, DOCX, ODT, TXT,
    RTF), scores candidates across four dimensions — technical skills, experience,
    cultural fit, communication — and uses vector-embedding search so an old
    candidate can be re-evaluated against a new role. It generates interview packs
    with rubrics and follow-up questions, does multi-tenant RBAC, and talks to
    Google and Microsoft calendars. It's in production as the backbone of
    Synechron's hiring for HSBC's Kraków technology hub.
    → <a href="https://github.com/olafkfreund/SkillAi" rel="noopener">github.com/olafkfreund/SkillAi</a></p>

    <h2 id="jefferies">GitHub Enterprise migration — Jefferies</h2>
    <p><span class="tag">Lead DevOps &amp; migration architect</span></p>
    <p>Leading the move of six business units at a tier-1 US investment bank off
    Bitbucket Cloud and Bamboo onto GitHub Enterprise Cloud and Actions, for the
    CTO office. I designed the Phase 1 reference architecture — reusable workflow
    templates spanning Maven, Gradle, .NET, Python, Node and multi-stage Docker,
    with NFS-backed caching and JFrog Artifactory over OIDC — and the self-hosted
    runner estate on AKS via Actions Runner Controller.</p>
    <p>The governance is Terraform: org and team structure, repo lifecycle, branch
    protection, GHAS configuration, signed-commit enforcement — idempotent and
    reviewable, not ClickOps. Snyk, SonarQube and HashiCorp Vault are baked into
    the standard pipeline so supply-chain attestation and secret rotation are the
    default rather than an afterthought. I also wrote a small set of Claude Code
    plugins the migration team uses daily to scaffold and convert pipelines.</p>

    <h2 id="neso">Backstage developer platform — NESO</h2>
    <p><span class="tag">Lead platform engineer</span></p>
    <p>Leading a team building Spotify Backstage as the internal developer platform
    for the UK's National Energy System Operator — golden-path templates,
    self-service scaffolding, and a single pane of glass for service ownership,
    on-call and runbooks. As much defining the DevOps operating model — tooling
    standards, environment promotion, branching, the feedback loops back to
    engineers — as building the portal.</p>

    <h2 id="opensource">Open source &amp; Claude ecosystem</h2>
    <ul>
      <li><strong>MCP servers</strong> for Kosli and ServiceNow, shipped inside
      SARC — real-world MCP in a CI/compliance context.</li>
      <li><strong>COSMIC desktop applets in Rust</strong> — KDE Connect protocol
      integration and a screen-mirroring plugin for the COSMIC ecosystem.</li>
      <li><strong>This knowledge base</strong> — <em>DevOps Help for Cloud Platform
      Engineers</em>: multi-cloud architecture, FinOps, NixOS, AIOps and service
      mesh patterns. <a href="{{ '/kb/' | relative_url }}">Browse it →</a></li>
    </ul>
  </div>
</section>
