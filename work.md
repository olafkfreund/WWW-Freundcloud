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
    and a database migration don't get treated the same way — low-risk changes clear
    themselves and only the ones that matter land on a human's desk, which is what
    actually shrinks the CAB queue. Auditors get one-click evidence export and
    time-boxed, magic-link sessions into the <em>same</em> dashboard the change board
    and the regulators use — no more assembling an "audit binder" by hand. The audit
    log is hash-chained so the trail is tamper-evident, and a cost-vulnerability
    correlation view puts a number on what a remediation is actually worth ("fix this,
    save $X/month") by joining Snyk, Wiz and Trivy findings to spend.</p>

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
    → <a href="{{ '/sarc/' | relative_url }}">the full SARC showcase</a>
    · <a href="https://sarc-6f4a6f.gitlab.io/" rel="noopener">the live walkthrough</a></p>
    </div>

    <div class="project">
    <h2 id="factory">The Factory suite — a governed pipeline for AI software delivery</h2>
    <p><span class="tag">Creator · open source</span></p>
    <p>What started as AIFactory grew into a four-product suite around one idea: AI can
    write the code, but someone still has to be accountable for it. 84% of developers
    use AI coding tools; only 29% trust the output. The Factory suite is the trust and
    governance layer for that gap, built around the <strong>PARR pipeline</strong> —
    <strong>Prepare · Act · Reflect · Review</strong> — with a human gate at every seam
    rather than one "trust me" big bang.</p>
    <ul>
      <li><strong>PFactory (Prepare)</strong> — plans work grounded in live cloud and
      Backstage context, runs architecture, security, feasibility and best-practice
      gates <em>with citations</em>, and only emits governed GitHub epics and issues
      once a human has signed the plan.</li>
      <li><strong>AIFactory (Act)</strong> — turns those specs into code and QA in
      isolated git worktrees, model-agnostic across Claude, Gemini, OpenAI and local
      Ollama, and can delegate sub-tasks to other coding agents.</li>
      <li><strong>TFactory (Reflect)</strong> — autonomously generates and runs tests
      in ephemeral sandboxes, grades each run on five signals (coverage delta,
      stability, mutation testing, lint and semantic relevance) and reports back on the
      pull request.</li>
      <li><strong>CFactory (Review)</strong> — the control-tower cockpit: one pane of
      glass with a live, animated dependency graph across plan → code → test, an
      advise-and-confirm copilot, and per-task and per-worker cost and token tracking.</li>
    </ul>

    <figure class="shot">
      <img src="{{ '/assets/img/work/aifactory-kanban.png' | relative_url }}"
           alt="AIFactory kanban board of tasks" loading="lazy">
      <figcaption>AIFactory — issues moving through plan, code and QA.</figcaption>
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

    <p>The spine that makes it cohere is deliberately boring plumbing: a shared
    correlation key, a normalized completion-event schema and a canonical port map, so
    every product emits the same audit trail — HMAC-anchored logs and completion
    records of exactly the kind the EU AI Act is about to ask for. It's model-agnostic
    through MCP, and you can watch the whole thing run live.
    → <a href="https://olafkfreund.github.io/AIFactory/" rel="noopener">AIFactory</a>
    · <a href="https://olafkfreund.github.io/TFactory/" rel="noopener">TFactory</a>
    · <a href="https://github.com/olafkfreund/Factory" rel="noopener">the meta-repo</a></p>
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
    <h2 id="ravn">ravn-agents — self-healing for Linux fleets that never decides on its own</h2>
    <p><span class="tag">Creator · open source · MIT</span></p>
    <p>Ravn detects and fixes problems across Linux infrastructure — standalone hosts,
    Kubernetes, air-gapped networks — without phoning home to anyone's cloud. The whole
    design is a reaction to "AIOps" that asks you to trust a black box: detection is
    <strong>deterministic</strong> ("rules you can read, not a statistical model you
    have to trust"), remediation runs from pre-authored, risk-tiered templates that
    need human or signed-policy approval, and every command is <strong>Ed25519-signed,
    verified and logged</strong> to an append-only Postgres trail. The local model only
    ever <em>explains</em> — it suggests next steps in plain language; it never decides
    what's wrong or what runs.</p>
    <p>Three layers: edge agents (<code>ravnd</code>) detect and execute approved fixes,
    a control plane (<code>ravn-server</code>) handles ingestion and policy, and a web
    portal owns inventory, approvals and audit. Default-deny throughout — circuit
    breakers, fleet kill switches, risk tiers — and because inference runs locally on
    CPU it works fully offline. Rust backend, React front end, shipped as static
    binaries, NixOS modules, OCI images and Kubernetes manifests.
    → <a href="https://github.com/olafkfreund/ravn-agents" rel="noopener">source</a></p>
    </div>

    <div class="project">
    <h2 id="lxconnect">lxconnect — your Android phone as an MCP tool surface</h2>
    <p><span class="tag">Creator · open source</span></p>
    <p>lxconnect bridges Android (Waydroid or a real device) to the Linux desktop, and
    the interesting half is the <strong>MCP server it runs on the phone</strong>. The
    Android app stands up a Ktor MCP server on port 8080 and hooks into
    <code>NotificationListenerService</code> and <code>PackageManager</code> — so an LLM
    or agent on your laptop can treat the phone as a set of tools: read notifications,
    open native deep links (<code>mailto:</code>, <code>spotify:</code>), launch and
    control apps, read system status, even drive the camera, all over a standard MCP
    transport.</p>
    <p>That turns "my phone" into something an agent can actually reach — triage
    notifications onto the desktop, hand a 2FA push to the right app, let a Claude
    session check or act on the device without you picking it up. A Python daemon reads
    a Server-Sent-Events stream from the phone and surfaces it through
    <code>libnotify</code>; a GTK4/PyGObject app gives you a native UI to test and
    control it. The whole thing is a declarative Nix flake — <code>nix run
    github:olafkfreund/lxconnect#gui</code> and you're live.
    → <a href="https://github.com/olafkfreund/lxconnect" rel="noopener">source</a></p>
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
    score and note on infrastructure the team controls. A typical open role pulls
    50–200 applications; the incumbents (Greenhouse, Workday) nail the workflow, charge
    tens of thousands a year, store your candidates on someone else's servers, and
    still leave the actual hard part — ranking people fairly — to a keyword match.
    SkillAi answers one question in seconds instead: who are the best candidates, and
    why.</p>
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
    <h2 id="rolehunter">rolehunter — the candidate's side of the same table</h2>
    <p><span class="tag">Creator · open source · GPL v3</span></p>
    <p>If SkillAi is the recruiter's side, rolehunter is the candidate's. It's a
    self-hosted, single-user job-hunt copilot: paste a job (or pull one from JSearch /
    LinkedIn), score it 0–100 against your master CV <em>with reasoning</em>, then
    auto-tailor an ATS-friendly CV and a one-click cover-letter PDF for that specific
    role. Applications and interviews live in a searchable table or Kanban board, with
    LLM-generated behavioural flashcards and a rejection taxonomy so patterns surface
    after a couple of entries.</p>
    <p>The part I like best is <strong>skill-gap aggregation</strong>: it clusters the
    gap strings from every match into canonical skills and pulls curated learning
    resources from whitelisted docs — so the job hunt quietly turns into a study plan.
    Next.js 15 / React 19 / TypeScript on Postgres 16 + pgvector, Drizzle for queries
    and Playwright for the PDFs, running as two localhost-bound Docker containers on
    randomised ports. Single-user by design — your CV never leaves your box.
    → <a href="https://github.com/olafkfreund/rolehunter" rel="noopener">source</a></p>
    </div>

    <div class="project">
    <h2 id="gog">gog &amp; gogmail — Google Workspace without leaving the terminal</h2>
    <p><span class="tag">Creator · open source</span></p>
    <p>gog is a CLI that authenticates to Google Workspace; gogmail is the
    keyboard-driven TUI on top of it. Between them they put Gmail, Calendar, Drive,
    Docs, Sheets, Slides, Tasks, Contacts, Chat and Meet (plus Zoom) into a single
    Textual interface — read and write mail, RSVP to events, edit Sheets cells inline,
    spin up meetings, all without a browser tab. A context-aware Gemini side panel can
    actually <em>act</em> — fetch data, draft replies, star mail, change tasks from a
    plain-language request — with optional voice in and spoken replies.</p>
    <p>It's also the layer under a couple of my other experiments:
    <strong>waycal</strong>, my Wayland/niri calendar, mail and task widgets, is just
    Quickshell QML driven by the same <code>gog</code> CLI. Python 3.10+, packaged for
    Nix, <code>.deb</code>, <code>.rpm</code> and zipapp.
    → <a href="https://github.com/olafkfreund/gogmail" rel="noopener">gogmail</a></p>
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
    <h2 id="opensource">More open source &amp; the Linux desktop</h2>
    <ul>
      <li><strong><a href="https://olafkfreund.github.io/gnome-quick-web-apps/" rel="noopener">gnome-quick-web-apps</a></strong>
      — a GTK4/libadwaita manager that turns any site into a native GNOME app: paste a
      URL and it pulls the name, icon and theme from the web manifest, then runs each
      app CEF-isolated with its own profile and true URL-scope confinement.</li>
      <li><strong>COSMIC &amp; the Linux desktop in Rust</strong> — a native
      <a href="https://github.com/olafkfreund/cosmic-ext-connect-desktop-app" rel="noopener">KDE-Connect app for COSMIC</a>,
      an <a href="https://github.com/olafkfreund/cosmic-ext-rdp-server" rel="noopener">RDP server</a>,
      notification and RSS applets, and
      <a href="https://github.com/olafkfreund/r-hyprconfig" rel="noopener">r-hyprconfig</a>,
      a real-time Hyprland config TUI.</li>
      <li><strong><a href="https://github.com/olafkfreund/nixos-template" rel="noopener">nixos-template</a></strong>
      — a batteries-included starting point for a NixOS journey, and the most-used
      thing I've published.</li>
      <li><strong><a href="https://muninn.freundcloud.com" rel="noopener">Muninn</a></strong>
      — a zero-backend, Gruvbox GitHub portal and WebMCP playground for local browser
      agents.</li>
      <li><strong>MCP servers</strong> for Kosli and ServiceNow, shipped inside SARC —
      real-world MCP in a CI/compliance context.</li>
      <li><strong>This knowledge base</strong> — <em>DevOps Help for Cloud Platform
      Engineers</em>: multi-cloud architecture, FinOps, NixOS, AIOps and Service
      Mesh patterns. <a href="{{ '/kb/' | relative_url }}">Browse it →</a></li>
    </ul>
    </div>
  </div>
</section>
