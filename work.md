---
layout: landing
title: Work
permalink: /work/
description: Projects and platforms Olaf Krasicki-Freund has designed and built.
---

<section class="section">
  <div class="prose">
    <h1 class="mt-0">Work</h1>
    <p>A handful of the things I've built or led. Some are client programmes I can
    only describe in outline; the open-source ones you can go and read — and most
    of them you can see below.</p>

    <div class="project">
    <h2 id="sarc">SARC — multi-cloud compliance pipeline</h2>
    <p><span class="tag">Product owner &amp; lead architect</span></p>
    <p>SARC (Synechron ARC) is an orchestration layer that sits on top of Kosli and
    ServiceNow and turns regulated software delivery into something you can actually
    audit at a glance. Instead of spreadsheets and manual evidence-gathering, it
    manages every framework a regulated shop cares about — DORA, PSD2, ISO 27001,
    SOC 2, SOX, NIST 800-53, PCI-DSS — from one place. I own the architecture and
    most of the build.</p>

    <figure class="shot">
      <img src="{{ '/assets/img/work/sarc-dashboard.png' | relative_url }}"
           alt="SARC operator dashboard" loading="lazy">
      <figcaption>The operator dashboard — pipelines, change requests and compliance state in one view.</figcaption>
    </figure>

    <p>Every change request gets a <strong>5-axis risk score</strong>, so a typo fix
    and a database migration don't get treated the same way. Auditors get one-click
    evidence export; the audit log is hash-chained so the trail is tamper-evident;
    and there's a cost-vulnerability correlation view that puts a number on what a
    given remediation is actually worth.</p>

    <div class="shot-grid">
      <figure>
        <img src="{{ '/assets/img/work/sarc-risk.png' | relative_url }}" alt="5-axis risk clearance score" loading="lazy">
        <figcaption>5-axis risk clearance per change</figcaption>
      </figure>
      <figure>
        <img src="{{ '/assets/img/work/sarc-compliance.png' | relative_url }}" alt="Compliance dashboard with framework coverage" loading="lazy">
        <figcaption>Multi-framework coverage</figcaption>
      </figure>
      <figure>
        <img src="{{ '/assets/img/work/sarc-clusters.png' | relative_url }}" alt="Multi-cluster overview across clouds" loading="lazy">
        <figcaption>Multi-cluster, multi-cloud overview</figcaption>
      </figure>
    </div>

    <p>The engineering trick that makes it demo well: the same repository deploys to
    AWS (EKS), Azure (AKS), GCP (GKE), OpenShift (ROSA) or a local k3d cluster off a
    single <code>TARGET_CLOUD</code> switch that drives the Terraform, the kubectl
    auth, the Helm values and the Kosli environment naming — each cloud using its
    own native data services and identity federation rather than a
    lowest-common-denominator fudge. GitLab is the source of truth, mirrored to
    GitHub and Azure DevOps on every green pipeline; images are built in-house,
    scanned with trivy, signed with cosign and attested through Kosli. The portal
    runs to 37 screens, with real-time timeline updates over server-sent events and
    a pair of Claude MCP servers (Kosli + ServiceNow) so you can ask the compliance
    state of a commit in plain English.
    → <a href="https://sarc-6f4a6f.gitlab.io/" rel="noopener">see the SARC walkthrough</a></p>
    </div>

    <div class="project">
    <h2 id="aifactory">AIFactory — spec-driven development for AI agents</h2>
    <p><span class="tag">Creator · open source</span></p>
    <p>AIFactory turns a GitHub issue into shipping code. It runs a
    <strong>planner → coder → QA</strong> agent pipeline: a planner breaks the spec
    down, a coder implements it, a QA agent reviews, and a pull request comes out the
    other end — with a human approval gate at every step rather than a "trust me" big
    bang. Models are selectable per agent role, and a web dashboard lets you watch
    each run live and replay any step.</p>

    <figure class="shot">
      <img src="{{ '/assets/img/work/aifactory-kanban.png' | relative_url }}"
           alt="AIFactory kanban board of tasks" loading="lazy">
      <figcaption>The board — issues moving through plan, code and QA.</figcaption>
    </figure>

    <div class="shot-grid">
      <figure>
        <img src="{{ '/assets/img/work/aifactory-plan.png' | relative_url }}" alt="AIFactory task plan detail" loading="lazy">
        <figcaption>A planner's breakdown of a task</figcaption>
      </figure>
      <figure>
        <img src="{{ '/assets/img/work/aifactory-console.png' | relative_url }}" alt="AIFactory live agent console" loading="lazy">
        <figcaption>Live agent console</figcaption>
      </figure>
    </div>
    <p>→ <a href="https://olafkfreund.github.io/AIFactory/" rel="noopener">olafkfreund.github.io/AIFactory</a>
    · <a href="https://github.com/olafkfreund/AIFactory" rel="noopener">source</a></p>
    </div>

    <div class="project">
    <h2 id="tfactory">TFactory — autonomous test generation</h2>
    <p><span class="tag">Creator · open source</span></p>
    <p>TFactory is AIFactory's sister project. Where AIFactory turns a spec into code,
    TFactory turns it into <em>tests</em> — it ingests a spec (or any structured
    feature description), generates a full feature, edge-case and security suite, runs
    it sandboxed in ephemeral containers with no host access, and reports back on the
    pull request, committing the passing tests. It drops into GitHub Actions as a
    reusable workflow, with the same planner → generator → sandbox-runner → reporter
    shape as AIFactory.</p>
    <p>→ <a href="https://olafkfreund.github.io/TFactory/" rel="noopener">olafkfreund.github.io/TFactory</a>
    · <a href="https://github.com/olafkfreund/TFactory" rel="noopener">source</a></p>
    </div>

    <div class="project">
    <h2 id="bifrost">Bifrost — Azure DevOps → GitHub Actions, at portfolio scale</h2>
    <p><span class="tag">Creator · open source</span></p>
    <p>GitHub's own importer (<code>gh actions-importer</code>) gets you maybe 90% of
    the way from an Azure DevOps pipeline to a GitHub Actions workflow. Bifrost is
    the other 10% — the review workflow, the semantic validation, the portfolio-level
    coordination and the audit trail that a syntactic converter leaves to you. It's
    the tooling I wish I'd had walking into a migration with hundreds of pipelines
    instead of one.</p>
    <p>The design rule is <strong>review-first</strong>: nothing is silently rewritten.
    The importer runs a dry pass, Bifrost parses the logs into typed <em>gaps</em>, and
    each gap goes to an LLM <em>grounded</em> in the actual source, the importer's
    output and the failure — so the model fills a specific hole rather than converting
    from scratch. Risk scoring stays <strong>deterministic and explainable</strong>:
    the numbers come from factors you can read, and the LLM explains them rather than
    being trusted to invent them. Every decision is recorded as a signed, exportable
    attestation.</p>
    <p>It's built to run where regulated shops actually live: <strong>air-gap
    capable</strong> against local models (Ollama / llama.cpp) so pipeline definitions
    and secrets never leave the network, with the same provider trait swapping in
    Anthropic, Gemini or Copilot when you're allowed to reach out. A React/TypeScript
    portal — portfolio heatmap, three-pane diff, approvals — sits on a Rust/Axum
    control plane (jobs, risk model, attestations), with Docker-based ingestion behind
    a <code>SourceAdapter</code> trait: ADO first, Jenkins, GitLab and Bamboo next.
    It's early — in active planning, MIT-licensed, and building in the open.
    → <a href="https://olafkfreund.github.io/bifrost/" rel="noopener">olafkfreund.github.io/bifrost</a>
    · <a href="https://github.com/olafkfreund/bifrost" rel="noopener">source</a></p>
    </div>

    <div class="project">
    <h2 id="skillpool">skill-pool — the team layer for Claude Code</h2>
    <p><span class="tag">Creator · open source</span></p>
    <p>Anthropic solved the single-developer story for Claude Code skills: drop a file
    in <code>~/.claude/skills/</code> and you're done. The <em>team</em> story wasn't
    solved — everyone hand-rolls their own <code>.claude/</code> and the knowledge of
    which prompt actually fixes which problem stays trapped on one laptop. skill-pool
    is the team layer: a self-hosted, multi-tenant registry (Rust API, Svelte portal,
    a CLI that knows what to install for the repo you just <code>cd</code>'d into).</p>

    <figure class="shot">
      <img src="{{ '/assets/img/work/skillpool-catalog.webp' | relative_url }}"
           alt="skill-pool catalog" loading="lazy">
      <figcaption>The catalog — browse, review and install skills, agents and commands.</figcaption>
    </figure>

    <p>The part I'm proudest of is <strong>retrospective capture</strong>: when Claude
    finishes a non-trivial fix, a Stop-hook scorer flags the session, a SessionEnd
    hook queues it, and a Haiku→Sonnet daemon turns the transcript into a draft
    <code>SKILL.md</code> for human review. The team's <code>.claude/</code> grows
    from the work the team actually did, not from somebody's bookmark folder. It also
    does per-tenant SSO, semantic search over <code>bge-small</code> embeddings, and
    one-binary deploys (Nix, Compose, Helm, Terraform).
    → <a href="https://olafkfreund.github.io/skill_pool/" rel="noopener">olafkfreund.github.io/skill_pool</a>
    · <a href="https://github.com/olafkfreund/skill_pool" rel="noopener">source</a></p>
    </div>

    <div class="project">
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
    Synechron's recruitment for HSBC's Kraków technology hub.
    → <a href="https://github.com/olafkfreund/SkillAi" rel="noopener">github.com/olafkfreund/SkillAi</a></p>
    </div>

    <div class="project">
    <h2 id="nixos">nixos_config — my whole machine, declared</h2>
    <p><span class="tag">Open source</span></p>
    <p>My personal NixOS estate, and the reason "infrastructure you can't rebuild from
    a clean checkout isn't infrastructure" is a thing I actually believe. It's a
    flake-based, multi-host config built on a <strong>single parameterised host
    template</strong> with a feature-flag system (dependencies and conflicts
    validated), so each machine turns on exactly what it needs from a shared base —
    an AMD workstation with ROCm for local AI, a headless Xeon media server running
    k3s microVMs, and a hybrid-graphics laptop with Secure Boot via lanzaboote.</p>
    <p>Secrets are age-encrypted with agenix and committed safely; Home Manager is
    wired in as a flake module; theming is Stylix-driven from a single base16 palette
    that colours everything from the terminal to the desktop; and the documentation
    site is generated reproducibly from the live Nix source so it never drifts. It's
    the testbed where most of what ends up in the knowledge base gets tried first.
    → <a href="https://olafkfreund.github.io/nixos_config/" rel="noopener">olafkfreund.github.io/nixos_config</a>
    · <a href="https://github.com/olafkfreund/nixos_config" rel="noopener">source</a></p>
    </div>

    <div class="project">
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
    the standard pipeline so developers get supply-chain attestation and secret
    rotation by default. I also wrote a small set of Claude Code plugins the
    migration team uses daily to scaffold and convert pipelines.</p>
    </div>

    <div class="project">
    <h2 id="neso">Backstage developer platform — NESO</h2>
    <p><span class="tag">Lead platform engineer</span></p>
    <p>Leading a team building Spotify Backstage as the internal developer platform
    for the UK's National Energy System Operator — golden-path templates,
    self-service service scaffolding, and a single pane of glass for service
    ownership, on-call and runbooks. As much defining the DevOps operating model —
    tooling standards, environment promotion, branching, the feedback loops back to
    engineers — as building the portal.</p>
    </div>

    <div class="project">
    <h2 id="opensource">More open source &amp; Claude ecosystem</h2>
    <ul>
      <li><strong>MCP servers</strong> for Kosli and ServiceNow, shipped inside
      SARC — real-world MCP in a CI/compliance context.</li>
      <li><strong>COSMIC desktop applets in Rust</strong> — KDE Connect protocol
      integration and a screen-mirroring plugin for the COSMIC ecosystem.</li>
      <li><strong>This knowledge base</strong> — <em>DevOps Help for Cloud Platform
      Engineers</em>: multi-cloud architecture, FinOps, NixOS, AIOps and Service
      Mesh patterns. <a href="{{ '/kb/' | relative_url }}">Browse it →</a></li>
    </ul>
    </div>
  </div>
</section>
