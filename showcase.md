---
layout: landing
title: Showcase
permalink: /showcase/
description: >-
  A showcase of the platforms Olaf Krasicki-Freund has designed and built —
  SARC, Fides, Hecate, the Factory suite, the Agentic SDLC reference build,
  Bifrost, Janus, Myrmex Hive, ravn-agents, DORA Dashboard, SkillAi, Odin,
  Muninn, Huginn, lxconnect and nixarchy.
---

<section class="hero">
  <div class="hero-badge">Showcase · platforms, not prototypes</div>
  <h1>Seventeen systems, one <span class="accent">throughline</span>.</h1>
  <p class="tagline">
    Everything below is self-hosted, auditable and built for environments where
    "just trust the vendor" isn't an answer — regulated banks, air-gapped networks,
    homelabs. Most of it is open source and running. Each one started because I hit
    the problem myself and the tool I wanted didn't exist.
  </p>
  <div class="hero-cta">
    <a class="btn btn-primary" href="#sarc">Start with SARC</a>
    <a class="btn btn-secondary" href="{{ '/work/' | relative_url }}">Client work &amp; roles</a>
    <a class="btn btn-secondary" href="https://github.com/olafkfreund" rel="noopener">GitHub</a>
  </div>
</section>

<section class="section">
  <h2>All seventeen, at a glance</h2>
  <p class="section-lede">One line each — click through to the full write-up and screenshots.</p>
  <div class="card-grid">
    <a class="card" href="#sarc">
      <span class="tag">Compliance · multi-cloud</span>
      <h3>SARC</h3>
      <p>Turns "are we compliant?" into a question the system answers with live
      evidence. Risk-scored change gates, one-click audit evidence for eight
      frameworks, identical on any cloud.</p>
    </a>
    <a class="card" href="#fides">
      <span class="tag">Evidence ledger · Go</span>
      <h3>Fides</h3>
      <p>A tamper-evident record of every state change in the SDLC. Provenance
      from commit to running runtime, four-eyes approval, WORM retention — the
      ledger inside SARC, and standalone.</p>
    </a>
    <a class="card" href="#hecate">
      <span class="tag">GitOps promotion · Go</span>
      <h3>Hecate</h3>
      <p>Flux knows how to make a cluster match git. It has no opinion about what
      should be in git next. Hecate is that missing layer — promotion as four
      resources, with evidence and tracing built in.</p>
    </a>
    <a class="card" href="#factory">
      <span class="tag">Governed AI delivery</span>
      <h3>The Factory suite</h3>
      <p>Four products, one idea: AI can write the code, but someone is still
      accountable. Plan, build, test and watch — with a human gate at every
      seam.</p>
    </a>
    <a class="card" href="#agentic-sdlc">
      <span class="tag">Reference build · playbook</span>
      <h3>Agentic SDLC</h3>
      <p>The operating model for agent-written software, as a repository that runs.
      Seven stages, gates proven to <em>refuse</em>, and a vendor swap you can
      execute in four directions.</p>
    </a>
    <a class="card" href="#bifrost">
      <span class="tag">Migration · Rust</span>
      <h3>Bifrost</h3>
      <p>The last 10% of an Azure DevOps → GitHub Actions migration that the
      importer leaves to you. Review-first, explainable risk, signed
      attestations, air-gap capable.</p>
    </a>
    <a class="card" href="#janus">
      <span class="tag">MCP gateway · Go</span>
      <h3>Janus</h3>
      <p>Any REST API as MCP tools — built to survive the security review.
      Fail-closed secrets, SSRF egress guard, tool-hash pinning, DLP redaction
      before the LLM ever sees the data.</p>
    </a>
    <a class="card" href="#myrmex">
      <span class="tag">Orchestration · Go</span>
      <h3>Myrmex Hive</h3>
      <p>Fleet management with <em>zero</em> inbound ports — agents dial out over
      SSH, and there's no shell to inject into because commands never touch
      one.</p>
    </a>
    <a class="card" href="#ravn">
      <span class="tag">Self-healing · Rust</span>
      <h3>ravn-agents</h3>
      <p>Detects and fixes Linux fleet problems without phoning home.
      Deterministic rules, Ed25519-signed remediation, and a local model that
      explains but never decides.</p>
    </a>
    <a class="card" href="#dora">
      <span class="tag">Delivery metrics · Next.js</span>
      <h3>DORA Dashboard</h3>
      <p>DORA-4 plus the metrics teams actually argue about, unified from GitHub
      and Jira behind your own SSO. No third-party data egress, ever.</p>
    </a>
    <a class="card" href="#skillai">
      <span class="tag">AI recruiting · in production</span>
      <h3>SkillAi</h3>
      <p>Answers "who are the best candidates, and why?" in seconds instead of a
      keyword match. Running as the backbone of hiring for HSBC's Kraków hub.</p>
    </a>
    <a class="card" href="#odin">
      <span class="tag">Homelab · React + FastAPI</span>
      <h3>Odin</h3>
      <p>A control room for a NixOS fleet — host vitals, service health, k3d and
      ArgoCD state, GPU and LLM cost analytics, all in one Nix-declared
      dashboard.</p>
    </a>
    <a class="card" href="#muninn">
      <span class="tag">WebMCP · zero backend</span>
      <h3>Muninn</h3>
      <p>A Gruvbox GitHub portal that AI agents can drive from inside your
      browser tab — a real app that doubles as a WebMCP playground.</p>
    </a>
    <a class="card" href="#huginn">
      <span class="tag">WebMCP · GitLab</span>
      <h3>Huginn</h3>
      <p>Muninn's other raven — the same zero-backend Gruvbox portal aimed at
      GitLab, with pipelines, MRs, vulnerabilities and a local Ollama terminal.</p>
    </a>
    <a class="card" href="#awsdash">
      <span class="tag">WebMCP · AWS</span>
      <h3>AWS Dashboard</h3>
      <p>Running instances and console logins from your own AWS profile, published
      to the browser's agent as tools — credentials never leave the machine.</p>
    </a>
    <a class="card" href="#lxconnect">
      <span class="tag">Android · MCP · Nix</span>
      <h3>lxconnect</h3>
      <p>Runs an MCP server <em>on your phone</em>, so an agent on your laptop can
      read notifications, open deep links and drive apps as ordinary tools.</p>
    </a>
    <a class="card" href="#nixarchy">
      <span class="tag">NixOS · desktop</span>
      <h3>nixarchy</h3>
      <p>A whole Arch-native desktop — 429 commands of it — vendored onto NixOS
      with its menus rewired to Nix. Tracking upstream is a source bump, not a
      re-port.</p>
    </a>
  </div>
</section>

<section class="section">
  <div class="prose">

  <div class="project">
  <h2 id="sarc">SARC — compliance automation for regulated delivery</h2>
  <p><span class="tag">Product owner &amp; lead architect</span> <span class="tag">Self-hosted</span></p>
  <p><strong>SARC turns "are we compliant?" from a question your team answers with
  spreadsheets and screenshots into a question the system answers with live
  evidence — automatically, every time you ship.</strong></p>
  <p>Regulated software delivery breaks in three predictable places. Audit prep
  becomes a fire drill, because the evidence is scattered across five to ten tools
  and nobody owns the whole story. The change board becomes a bottleneck, because a
  one-character fix and a schema migration both sit in the same 48-hour queue. And
  the compliance story itself gets locked to one cloud, so it breaks the moment a
  workload moves. SARC is the orchestration layer that fixes all three.</p>

  <figure class="shot">
    <img src="{{ '/assets/img/work/sarc-dashboard.png' | relative_url }}"
         alt="SARC portal dashboard showing compliance, DORA metrics, vulnerabilities and environment state" loading="lazy">
    <figcaption>The dashboard — compliance posture, DORA metrics, vulnerabilities, SBOM coverage and every environment, live.</figcaption>
  </figure>

  <p>Every change gets a <strong>5-axis risk clearance score</strong> — artifact,
  scope, attestation, temporal and code — derived from live attestations and
  written straight back onto the ServiceNow change request, each axis showing the
  controls it maps to (NIST 800-30, PCI-DSS 4.0, ISO 27005, DORA). Low-risk
  changes clear themselves; only the ones that matter land on a human's desk.
  That single number is what actually shrinks the CAB queue — and no other system
  in the stack computes it.</p>
  <p>Auditors don't get a binder. They get a time-boxed, magic-link session,
  read-only, into the <em>same</em> dashboard the change board uses, with one-click
  evidence export for <strong>SOC 2, ISO 27001, DORA, PSD2, NIST 800-53, PCI-DSS,
  SOX and HIPAA</strong>. A cost–vulnerability correlation view prices remediation
  in dollars per month rather than abstract severity labels.</p>

  <div class="shot-grid">
    <figure>
      <img src="{{ '/assets/img/work/sarc-risk.png' | relative_url }}" alt="SARC deployment clearance with the five risk axes broken down" loading="lazy">
      <figcaption>Deployment clearance, axis by axis</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/work/sarc-compliance.png' | relative_url }}" alt="SARC compliance status per framework" loading="lazy">
      <figcaption>Per-framework control posture</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/work/sarc-clusters.png' | relative_url }}" alt="SARC live Kubernetes cluster topology" loading="lazy">
      <figcaption>Live cluster topology, any cloud</figcaption>
    </figure>
  </div>

  <p>The engineering trick that makes it demo well: the same repository deploys to
  AWS (EKS), Azure (AKS), GCP (GKE), OpenShift or a local k3d cluster off a single
  <code>TARGET_CLOUD</code> switch that drives the Terraform, the kubectl auth, the
  Helm values and the environment naming — each cloud using its own native data
  services and identity federation rather than a lowest-common-denominator fudge.
  GitLab CI is the source of truth, with full parity on GitHub Actions and Azure
  DevOps. Images are built in-house, scanned with Trivy and signed with cosign.
  Evidence is recorded by <a href="#fides">Fides</a>, shipped inside SARC — so there
  is <strong>zero SaaS egress</strong>: nothing about your delivery pipeline leaves
  your infrastructure. An in-cluster AI assistant answers questions about compliance
  state without needing a cloud API key.</p>
  <p>Portal, by the numbers: <strong>37 screens</strong>, real-time timeline updates
  over server-sent events, MCP servers so you can ask the compliance state of a
  commit in plain English, and role-shaped dashboards for directors, engineers,
  auditors and finance. It's not SaaS — you don't subscribe to SARC, you adopt it.
  A typical engagement is a <strong>4–8 week MVP install</strong>, after which the
  customer owns and operates it. No per-seat fee, no vendor capture.</p>
  <p>→ <a href="https://sarc-6f4a6f.gitlab.io/" rel="noopener">Walk through the live portal</a>
  · <a href="https://sarc-6f4a6f.gitlab.io/docs/intro/" rel="noopener">Read the docs</a></p>
  </div>

  <div class="project">
  <h2 id="fides">Fides — a tamper-evident evidence ledger for the SDLC</h2>
  <p><span class="tag">Creator · open source</span> <span class="tag">Go</span></p>
  <p>Named after the Roman goddess of trust and oaths, Fides records and evaluates
  <em>every</em> state change in the software delivery lifecycle as it happens, and
  turns the result into an audit-ready single source of truth. It's the evidence
  layer inside SARC, and it stands alone.</p>

  <figure class="shot">
    <img src="{{ '/assets/img/showcase/fides-overview.jpg' | relative_url }}"
         alt="Fides Assurance Console showing compliance posture, controls coverage and live checks" loading="lazy">
    <figcaption>The Assurance Console — live compliance and provenance posture across every tracked artifact.</figcaption>
  </figure>

  <p>The core is <strong>supply-chain provenance</strong>: artifacts are traced by
  cryptographic SHA-256 digest from git commit to running runtime, with cosign
  signatures, SLSA in-toto attestations and SBOMs verified along the way. Drift and
  shadow-change detection continuously compares what's <em>running</em> to what was
  <em>approved</em>, so unauthorised deployments surface instead of hiding until the
  next audit.</p>

  <div class="shot-grid">
    <figure>
      <img src="{{ '/assets/img/showcase/fides-controls.jpg' | relative_url }}" alt="Fides controls and coverage across compliance frameworks" loading="lazy">
      <figcaption>Controls &amp; coverage</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/showcase/fides-attestations.jpg' | relative_url }}" alt="Fides attestation evidence chain" loading="lazy">
      <figcaption>Attestation evidence</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/showcase/fides-artifacts.jpg' | relative_url }}" alt="Fides artifacts and SBOM view" loading="lazy">
      <figcaption>Artifacts &amp; SBOM</figcaption>
    </figure>
  </div>

  <p>The bits that matter to an auditor are first-class rather than bolted on.
  Control catalogs for <strong>SOC 2, ISO 27001, NIST 800-53, PCI-DSS, DORA, PSD2
  and SOX</strong> import with one command and report per framework.
  <strong>Segregation of duties</strong> distinguishes human sign-off from machine
  automation — four-eyes needs two distinct humans, and the change gate will not
  recommend approval without a human review. <strong>FDA 21 CFR Part 11</strong>
  electronic records and ECDSA signature validation are supported. Evidence can sit
  behind <strong>S3 Object Lock (WORM)</strong> retention, and Postgres row-level
  security enforces tenant isolation at the database layer, not just in the app.</p>
  <p>The change gate itself emits an evidence-backed approve/hold verdict with a
  0–100 risk score, and writes it onto the matching ServiceNow change request.
  <em>Fides advises; ServiceNow decides.</em> An LLM audit gateway runs against
  Ollama, llama.cpp or Gemini, so natural-language compliance checks work
  air-gapped. Go API, PostgreSQL, pluggable vaults (HashiCorp, AWS, GCP, Azure),
  an MCP server, and a CLI that covers record → verify → gate.</p>
  <p>→ <a href="https://github.com/olafkfreund/fides" rel="noopener">github.com/olafkfreund/fides</a></p>
  </div>

  <div class="project">
  <h2 id="hecate">Hecate — the promotion layer Flux never had</h2>
  <p><span class="tag">Creator · open source · Apache 2.0</span> <span class="tag">Go · pre-alpha</span></p>
  <p>Flux makes a cluster match what is in git. It has no opinion about <strong>what
  should be in git next</strong> — so cross-environment promotion gets hand-rolled in
  CI, once per organisation, and quietly becomes the least-reviewed code in the
  delivery path. Argo has Rollouts for within an environment and is well served
  across them; Flux has Flagger for within, and nothing for across. Hecate fills
  that slot.</p>

  <p>The whole API is four resources. A <strong>Beacon</strong> watches registries,
  charts and repos — or reuses Flux Operator's own <code>ResourceSetInputProvider</code>
  rather than inventing a second opinion about what "newest" means — and emits a
  <strong>Bundle</strong>: an immutable, content-addressed set of artifact versions,
  the unit that moves. A <strong>Gate</strong> is an environment plus the threshold a
  Bundle must cross to enter it. A <strong>Passage</strong> is one attempt to move one
  Bundle through one Gate, as declarative steps — clone, set image, commit, push,
  reconcile, and wait for the cluster to actually reach the revision rather than
  assuming it did.</p>

  <p>The details are the regulated-delivery ones. Gates take <code>after: [staging]</code>
  so production can only admit what already cleared staging, and
  <code>requireApproval</code> where a human belongs. CI can tell a Beacon to look now
  instead of waiting for its interval, authenticated by its own OIDC workload token
  reviewed by Kubernetes — no shared secret, no HMAC, and an identity that can poke a
  Beacon still cannot read your Gates. Compliance evidence and OpenTelemetry tracing
  are emitted by the promotion itself, not reconstructed afterwards. Go 1.26,
  Apache 2.0, at <strong>v0.8.2</strong> and honest about being pre-alpha.</p>
  <p>→ <a href="https://olafkfreund.github.io/Hecate/" rel="noopener">hecate docs</a>
  · <a href="https://github.com/olafkfreund/Hecate" rel="noopener">source</a></p>
  </div>

  <div class="project">
  <h2 id="factory">The Factory suite — a governed pipeline for AI software delivery</h2>
  <p><span class="tag">Creator · open source</span> <span class="tag">PFactory · AIFactory · TFactory · CFactory</span></p>
  <p>84% of developers use AI coding tools; only 29% trust the output. The Factory
  suite is the trust layer for that gap. Four products around one idea — AI can
  write the code, but someone still has to be accountable for it — built on the
  <strong>PARR pipeline</strong>: <strong>Prepare · Act · Reflect · Review</strong>,
  with a human gate at every seam rather than one "trust me" big bang.</p>

  <figure class="shot">
    <img src="{{ '/assets/img/showcase/factory-cockpit.png' | relative_url }}"
         alt="CFactory mission control showing work items, events, spend and a live event feed" loading="lazy">
    <figcaption>CFactory mission control — the plan → code → test strip, anomalies, live agents and spend, in one pane.</figcaption>
  </figure>

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
    stability, mutation testing, lint and semantic relevance) and reports back on
    the pull request.</li>
    <li><strong>CFactory (Review)</strong> — the control-tower cockpit: a live,
    animated dependency graph across plan → code → test, an advise-and-confirm
    copilot, and per-task and per-worker cost and token tracking.</li>
  </ul>

  <div class="shot-grid">
    <figure>
      <img src="{{ '/assets/img/showcase/factory-plan.png' | relative_url }}" alt="PFactory planning portal showing acceptance criteria and gate results" loading="lazy">
      <figcaption>PFactory — acceptance criteria, gates passed</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/showcase/factory-build.png' | relative_url }}" alt="AIFactory human review gate with merge, create PR and request changes" loading="lazy">
      <figcaption>AIFactory — the human review gate</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/showcase/factory-test.png' | relative_url }}" alt="TFactory visual inspection reports with pass and attention verdicts" loading="lazy">
      <figcaption>TFactory — graded verdicts per run</figcaption>
    </figure>
  </div>

  <p>The spine that makes four products cohere is deliberately boring plumbing: a
  shared correlation key, a normalized completion-event schema and a canonical port
  map, so every product emits the same audit trail — HMAC-anchored logs and
  completion records of exactly the kind the EU AI Act is about to ask for. It's
  model-agnostic through MCP, and you can watch the whole thing run live.</p>
  <p>→ <a href="https://olafkfreund.github.io/AIFactory/" rel="noopener">AIFactory</a>
  · <a href="https://olafkfreund.github.io/TFactory/" rel="noopener">TFactory</a>
  · <a href="https://github.com/olafkfreund/PFactory" rel="noopener">PFactory</a>
  · <a href="https://github.com/olafkfreund/CFactory" rel="noopener">CFactory</a>
  · <a href="https://github.com/olafkfreund/Factory" rel="noopener">the meta-repo</a></p>
  </div>

  <div class="project">
  <h2 id="agentic-sdlc">Agentic SDLC — the playbook, as a repository that runs</h2>
  <p><span class="tag">Author · open source</span> <span class="tag">Reference implementation</span></p>
  <p>Every organisation writing an "AI in the SDLC" policy right now is writing a PDF.
  This is the same argument as a working build: seven stages, five planes, a portable
  artifact chain and an autonomy matrix — expressed as code that runs, gates that
  refuse, and evidence produced as a by-product rather than reconstructed for an
  auditor later.</p>

  <p>Two things make it more than a demo. First, <code>make negative</code>: twelve
  deliberate violations — a float on a monetary field, a personal field in an error
  message, an unaudited <code>POST</code>, an edit to a frozen path, a change claiming
  more autonomy than it earned — each one refused by code, with the control id and the
  reason. <em>A gate verified only by passing is indistinguishable from a gate that
  cannot fail.</em> Second, no model sits in the gate. Models diagnose, propose, draft
  and review; the decision to allow or block is arithmetic over version-controlled
  policy YAML — the same tables governance signed off.</p>

  <p>The Substitution Test is the part that survives procurement. GitHub Copilot is the
  agent runtime here, deliberately: the playbook's claim is that the operating model
  must outlive a change of vendor, so the honest way to make it is to use a specific
  vendor and keep every asset in an open format. Copilot is invoked in exactly one step
  per stage; <code>make swap</code> switches vendor four ways and re-scores under each.
  The context, skills, policy, gates and evidence do not move — 12/12 portable, 12/12
  gates proven to refuse, 24/24 evals. And because a chain of commits <em>is</em> the
  audit trail, <code>query_evidence.py --control SEC-API-01</code> answers "which
  production changes touched this control, which were agent-authored, at what autonomy
  tier, and who approved each" in seconds rather than a week.</p>
  <p>→ <a href="https://olafkfreund.github.io/agentic-sdlc-showcase/" rel="noopener">the walkthrough</a>
  · <a href="https://github.com/olafkfreund/agentic-sdlc-showcase" rel="noopener">source</a></p>
  </div>

  <div class="project">
  <h2 id="bifrost">Bifrost — Azure DevOps → GitHub Actions, at portfolio scale</h2>
  <p><span class="tag">Creator · open source · MIT</span> <span class="tag">Rust + React</span></p>
  <p>GitHub's own importer gets you maybe 90% of the way from an Azure DevOps
  pipeline to a GitHub Actions workflow. Bifrost is the other 10% — the review
  workflow, the semantic validation, the portfolio-level coordination and the audit
  trail a syntactic converter leaves to you. It's the tooling I wish I'd had walking
  into a migration with hundreds of pipelines instead of one.</p>

  <figure class="shot">
    <img src="{{ '/assets/img/showcase/bifrost-heatmap.png' | relative_url }}"
         alt="Bifrost portfolio heatmap of pipeline migration readiness" loading="lazy">
    <figcaption>The portfolio heatmap — hundreds of pipelines, ranked by risk and readiness.</figcaption>
  </figure>

  <p>The design rule is <strong>review-first</strong>: nothing is silently rewritten.
  The importer runs a dry pass, Bifrost parses the logs into typed <em>gaps</em>, and
  each gap goes to an LLM <em>grounded</em> in the actual source, the importer's
  output and the failure — so the model fills a specific hole rather than converting
  from scratch. Risk scoring stays <strong>deterministic and explainable</strong>:
  the numbers come from factors you can read, and the LLM explains them rather than
  being trusted to invent them. Every decision is a signed, exportable attestation.</p>

  <div class="shot-grid">
    <figure>
      <img src="{{ '/assets/img/showcase/bifrost-assessment.png' | relative_url }}" alt="Bifrost per-pipeline migration assessment" loading="lazy">
      <figcaption>Per-pipeline assessment</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/showcase/bifrost-coverage.png' | relative_url }}" alt="Bifrost coverage matrix of migrated pipeline features" loading="lazy">
      <figcaption>Coverage matrix</figcaption>
    </figure>
  </div>

  <p>It's built to run where regulated shops actually live: <strong>air-gap
  capable</strong> against local models (Ollama / llama.cpp) so pipeline definitions
  and secrets never leave the network, with the same provider trait swapping in
  Anthropic, Gemini or Copilot when you're allowed to reach out. A React/TypeScript
  portal sits on a Rust/Axum control plane, with Docker-based ingestion behind a
  <code>SourceAdapter</code> trait: ADO first, Jenkins, GitLab and Bamboo next.</p>
  <p>→ <a href="https://olafkfreund.github.io/bifrost/" rel="noopener">olafkfreund.github.io/bifrost</a>
  · <a href="https://github.com/olafkfreund/bifrost" rel="noopener">source</a></p>
  </div>

  <div class="project">
  <h2 id="janus">Janus — an MCP gateway for air-gapped enterprises</h2>
  <p><span class="tag">Creator · open source</span> <span class="tag">Go</span></p>
  <p>Every enterprise wants to give its LLMs access to internal APIs. Almost none of
  them can, because the security review kills it. Janus is the gateway that survives
  that review: it turns any REST/HTTP API into MCP tools dynamically — declare the
  endpoint, map the request body to a JSON Schema template, and the gateway
  generates the MCP tool definition for you.</p>

  <figure class="shot">
    <img src="{{ '/assets/img/showcase/janus-tools.png' | relative_url }}"
         alt="Janus MCP tools registry in the gateway portal" loading="lazy">
    <figcaption>REST endpoints, translated into MCP tools — no bespoke server per API.</figcaption>
  </figure>

  <p>The security posture is the product. It's <strong>fail-closed by
  construction</strong>: secrets under 32 bytes and the process refuses to start,
  so there is no usable default. An <strong>SSRF egress guard</strong> blocks
  private, loopback and link-local addresses at dial time, including DNS rebinds.
  <strong>Tool-definition hash pinning</strong> defends against rug-pulls — every
  tool carries a SHA-256 hash and a version, and in strict mode a call is blocked
  the moment a definition changes after approval. Opt-in <strong>DLP
  redaction</strong> masks emails, Luhn-validated card numbers, JWTs, AWS keys and
  IBANs in tool arguments and downstream responses <em>before they reach the
  LLM</em>, and logs the class and count without ever logging the value.</p>

  <div class="shot-grid">
    <figure>
      <img src="{{ '/assets/img/showcase/janus-dashboard.png' | relative_url }}" alt="Janus gateway dashboard with downstream API health" loading="lazy">
      <figcaption>Gateway health &amp; downstream status</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/showcase/janus-audit.png' | relative_url }}" alt="Janus audit log of tool calls" loading="lazy">
      <figcaption>Audit log of every tool call</figcaption>
    </figure>
  </div>

  <p>It's also current with where the protocol is going: stateless Streamable HTTP
  transport that scales across replicas (matching the MCP 2026-07-28 direction),
  legacy HTTP+SSE for older clients, W3C Trace Context propagated into OpenTelemetry
  spans, and an opt-in <strong>OAuth 2.1 resource server</strong> with RFC 9728
  metadata and audience-bound tokens — so enterprise-managed authorization works on
  the same path. RBAC maps straight from IdP group claims, fail-closed: a user in no
  mapped group gets no tools. Point it at an OpenAPI 3.x spec and it imports the
  whole surface in one shot.</p>
  <p>→ <a href="https://janus.freundcloud.com/" rel="noopener">janus.freundcloud.com</a>
  · <a href="https://github.com/olafkfreund/janus" rel="noopener">source</a></p>
  </div>

  <div class="project">
  <h2 id="myrmex">Myrmex Hive — agent orchestration with zero inbound ports</h2>
  <p><span class="tag">Creator · open source</span> <span class="tag">Go</span></p>
  <p>The usual way to manage a fleet of edge machines is to open a port on each of
  them. Myrmex Hive inverts it. The agent on each target node opens an
  <strong>outbound</strong> SSH tunnel to a central gateway, and JSON-RPC rides that
  channel — so your edge servers expose <em>nothing</em>, and the entire class of
  attack that starts with a public scanner finding your management port simply
  doesn't apply.</p>
  <p>Two more decisions do most of the security work. The agent executes binaries
  directly via OS process forks rather than through a shell, which structurally
  eliminates shell-injection — there is no shell to inject into — and every argument
  is validated against operator-defined regular expressions in config. Tunnels use
  Go's native <code>crypto/ssh</code> with Ed25519 signature validation and
  ChaCha20-Poly1305 / AES-GCM ciphers. Gateway access is bearer-token authorised, and
  the orchestrator can front a local Ollama model so the reasoning stays on your
  hardware too.</p>
  <p>It ships the way infrastructure software should: a Nix flake with NixOS modules
  for declarative agent/gateway roles, a Homebrew cask for macOS, deb and rpm
  packages, container images, an <code>install.sh</code> that generates keys and boots
  the systemd unit, and a PowerShell installer for Windows Server. MCP over stdio or
  SSE, with a CLI and portal on top.</p>
  <p>→ <a href="https://myrmex-hive.freundcloud.com" rel="noopener">myrmex-hive.freundcloud.com</a>
  · <a href="https://github.com/olafkfreund/myrmex-hive" rel="noopener">source</a></p>
  </div>

  <div class="project">
  <h2 id="ravn">ravn-agents — self-healing for Linux fleets that never decides on its own</h2>
  <p><span class="tag">Creator · open source · MIT</span> <span class="tag">Rust</span></p>
  <p>Ravn detects and fixes problems across Linux infrastructure — standalone hosts,
  Kubernetes, air-gapped networks — without phoning home to anyone's cloud. The whole
  design is a reaction to "AIOps" that asks you to trust a black box.</p>

  <figure class="shot">
    <img src="{{ '/assets/img/showcase/ravn-topology.png' | relative_url }}"
         alt="ravn-agents fleet topology view" loading="lazy">
    <figcaption>Fleet topology — hosts, clusters and the state of each.</figcaption>
  </figure>

  <p>Detection is <strong>deterministic</strong>: rules you can read, not a
  statistical model you have to trust. Remediation runs from pre-authored,
  risk-tiered templates that need human or signed-policy approval. Every command is
  <strong>Ed25519-signed, verified and logged</strong> to an append-only Postgres
  trail. The local model only ever <em>explains</em> — it suggests next steps in
  plain language; it never decides what's wrong or what runs. That line is the
  entire point.</p>

  <div class="shot-grid">
    <figure>
      <img src="{{ '/assets/img/showcase/ravn-events.png' | relative_url }}" alt="ravn-agents events overview" loading="lazy">
      <figcaption>Events, with plain-language explanations</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/showcase/ravn-remediations.png' | relative_url }}" alt="ravn-agents remediation approval queue" loading="lazy">
      <figcaption>Remediations, pending approval</figcaption>
    </figure>
  </div>

  <p>Three layers: edge agents (<code>ravnd</code>) detect and execute approved
  fixes, a control plane (<code>ravn-server</code>) handles ingestion and policy, and
  a web portal owns inventory, approvals and audit. Default-deny throughout —
  circuit breakers, fleet kill switches, risk tiers — and because inference runs
  locally on CPU it works fully offline. Rust backend, React front end, shipped as
  static binaries, NixOS modules, OCI images and Kubernetes manifests.</p>
  <p>→ <a href="https://github.com/olafkfreund/ravn-agents" rel="noopener">source</a></p>
  </div>

  <div class="project">
  <h2 id="dora">DORA Dashboard — delivery intelligence that can't leave the building</h2>
  <p><span class="tag">Creator · open source</span> <span class="tag">Next.js + Postgres</span></p>
  <p>Regulated enterprises — finance, insurance, healthcare, public sector — cannot
  put delivery data into a multi-tenant SaaS analytics tool, so they compile it by
  hand across GitHub and Jira every quarter. This is the defensible self-hosted
  alternative: one portal, behind Entra ID SSO and GitHub OAuth, with
  <strong>no third-party data egress</strong>.</p>

  <figure class="shot">
    <img src="{{ '/assets/img/showcase/dora-detail.png' | relative_url }}"
         alt="DORA Dashboard metric detail view" loading="lazy">
    <figcaption>Drill into any metric — the trend, the target, and the work behind it.</figcaption>
  </figure>

  <p>It covers the <strong>DORA-4</strong> canon — deployment frequency, lead time
  for changes, change failure rate, MTTR — plus the extended delivery and quality
  set that teams actually argue about in retros: cycle time, work item age, blocked
  time, delivery predictability, average velocity, test automation coverage, defect
  escape rate and defect root cause. Every number traces back to the GitHub or Jira
  record it came from.</p>

  <div class="shot-grid">
    <figure>
      <img src="{{ '/assets/img/showcase/dora-overview.png' | relative_url }}" alt="DORA Dashboard overview of delivery metrics" loading="lazy">
      <figcaption>Delivery performance overview</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/showcase/dora-charts.png' | relative_url }}" alt="DORA Dashboard charts view" loading="lazy">
      <figcaption>The same data, as trends</figcaption>
    </figure>
  </div>

  <p>Next.js 16 on TypeScript, PostgreSQL 16 + Prisma, Auth.js with Entra ID OIDC and
  RBAC, Octokit and the Jira REST API for ingestion. Ships as a hardened Docker image
  with compose for small installs and a Helm chart for Kubernetes — air-gap friendly,
  with self-hosted fonts and assets and no runtime CDN dependency. Early days and
  building in the open.</p>
  <p>→ <a href="https://github.com/olafkfreund/dora-dashboard" rel="noopener">source</a></p>
  </div>

  <div class="project">
  <h2 id="skillai">SkillAi — open-source AI recruiting, in production</h2>
  <p><span class="tag">Author &amp; lead architect · GPL v3</span> <span class="tag">Live</span></p>
  <p>A typical open role pulls 50–200 applications. The incumbents nail the workflow,
  charge tens of thousands a year, store your candidates on someone else's servers,
  and still leave the hard part — ranking people fairly — to a keyword match. SkillAi
  answers one question in seconds instead: <strong>who are the best candidates, and
  why?</strong></p>

  <figure class="shot">
    <img src="{{ '/assets/img/showcase/skillai-dashboard.png' | relative_url }}"
         alt="SkillAi recruiting dashboard" loading="lazy">
    <figcaption>The dashboard — roles, pipelines and candidate scoring at a glance.</figcaption>
  </figure>

  <p>It parses CVs in every format people actually send (PDF, DOCX, ODT, TXT, RTF),
  scores candidates across four dimensions — technical skills, experience, cultural
  fit, communication — and uses vector-embedding search so an old candidate can be
  re-evaluated against a new role instead of being lost. It generates interview packs
  with rubrics and follow-up questions, does multi-tenant RBAC, and talks to Google
  and Microsoft calendars. Every CV, score and note stays on infrastructure the team
  controls.</p>

  <div class="shot-grid">
    <figure>
      <img src="{{ '/assets/img/showcase/skillai-role.png' | relative_url }}" alt="SkillAi role detail with ranked candidates" loading="lazy">
      <figcaption>A role, with candidates ranked and reasoned</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/showcase/skillai-interview.png' | relative_url }}" alt="SkillAi generated interview pack" loading="lazy">
      <figcaption>Generated interview pack</figcaption>
    </figure>
  </div>

  <p>It's not a demo: SkillAi runs in production as the backbone of Synechron's
  recruitment for HSBC's Kraków technology hub. Built on Claude and Gemini,
  TypeScript, self-hosted, GPL v3.</p>
  <p>→ <a href="https://github.com/olafkfreund/SkillAi" rel="noopener">github.com/olafkfreund/SkillAi</a></p>
  </div>

  <div class="project">
  <h2 id="odin">Odin — a control room for the homelab</h2>
  <p><span class="tag">Creator · private</span> <span class="tag">React + FastAPI + Nix</span></p>
  <p>Odin is the single pane of glass over my own NixOS fleet — three machines, a
  k3d cluster, a media pipeline and a pile of local models. Live CPU, memory,
  storage, core temperature, battery and uptime per host; real-time port health for
  Plex, Sonarr, Radarr, Bazarr, NZBGet, n8n, Backstage, LiteLLM, Ollama and ArgoCD;
  a live map of namespaced Kubernetes resources and ArgoCD sync state; GPU VRAM and
  active Ollama models alongside token and cost analytics for Claude and Gemini; and
  the media ingestion queues with mount capacity.</p>
  <p>A React + Vite frontend on a FastAPI aggregator backend, wrapped in a
  declarative Nix <code>devenv</code> shell so the whole thing comes up with
  <code>direnv allow</code> and <code>just dev</code>. The design language —
  "Prism Dark", glassmorphic panels, neon accents per hardware pool — is hand-rolled
  vanilla CSS, and the real-time cost charts are pure SVG rather than a charting
  library. It's the place where "infrastructure you can't rebuild from a clean
  checkout isn't infrastructure" gets tested against my own estate. Private repo.</p>
  </div>

  <div class="project">
  <h2 id="muninn">Muninn — a GitHub portal that browser-native agents can drive</h2>
  <p><span class="tag">Creator · open source</span> <span class="tag">WebMCP playground</span></p>
  <p>Named after one of Odin's ravens, Muninn travels the GitHub API and brings back
  memory: repositories, Actions runs, pull requests, issues, security alerts and
  stars, in one responsive Gruvbox-themed portal with zero backend.</p>

  <figure class="shot">
    <img src="{{ '/assets/img/showcase/muninn-1.png' | relative_url }}"
         alt="Muninn GitHub dashboard overview in Gruvbox dark theme" loading="lazy">
    <figcaption>Overview — workflows, PRs, issues and security alerts across every repo.</figcaption>
  </figure>

  <p>The reason it exists is the last feature: Muninn implements the experimental
  browser-native <strong>WebMCP</strong> draft, registering client-side capabilities
  — <code>list_loaded_repos</code>, <code>list_pull_requests</code>,
  <code>list_issues</code>, <code>trigger_action_workflow</code> — as tools an AI
  agent running <em>in your browser tab</em> can call. It's a real, useful app that
  doubles as a place to find out what WebMCP is actually good for.</p>

  <div class="shot-grid">
    <figure>
      <img src="{{ '/assets/img/showcase/muninn-3.png' | relative_url }}" alt="Muninn pull requests panel" loading="lazy">
      <figcaption>Pull requests, reviewers and CI status</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/showcase/muninn-5.png' | relative_url }}" alt="Muninn security alerts view" loading="lazy">
      <figcaption>Dependabot &amp; code-scanning alerts</figcaption>
    </figure>
  </div>

  <p>Beyond that: universal client-side search across repos, PRs, issues and runs;
  a real-time notification engine combining Web Notifications with in-app toasts and
  startup deduplication; Dependabot and code-scanning alerts unified; routine
  automations like draft-PR labelling and stale-issue cleanup; and a local Ollama
  chat terminal wired straight into the dashboard. Jekyll and vanilla JavaScript,
  developed in a <code>devenv</code> shell.</p>
  <p>→ <a href="https://muninn.freundcloud.com" rel="noopener">muninn.freundcloud.com</a>
  · <a href="https://github.com/olafkfreund/Muninn" rel="noopener">source</a></p>
  </div>

  <div class="project">
  <h2 id="huginn">Huginn — the other raven, pointed at GitLab</h2>
  <p><span class="tag">Creator · open source</span> <span class="tag">Zero backend · WebMCP</span></p>
  <p>Muninn and Huginn are Odin's two ravens, and they do the same job here for the two
  forges. Huginn is the GitLab half — GitLab.com or self-hosted — in the same
  Gruvbox light/dark treatment, with the same zero-backend architecture: the personal
  access token lives in the browser and never reaches a server, because there isn't
  one.</p>
  <p>It runs pipelines and cancels them, reviews and merges MRs, triages and labels
  issues, surfaces project vulnerabilities and star analytics, and does unified
  client-side search across all of it. A notification engine combines desktop Web
  Notifications with in-app toasts for new issues, MR events, finished CI runs and new
  vulnerability alerts, with deduplication so a page load doesn't spam you. A local
  <strong>Ollama</strong> terminal sits in the dashboard for drafting and code
  analysis, and an optional background daemon watches edits, runs validation and
  triages project status.</p>
  <p>Like Muninn it registers browser-native <strong>WebMCP</strong> tools —
  <code>list_loaded_projects</code>, <code>list_merge_requests</code>,
  <code>list_issues</code>, <code>trigger_pipeline_run</code> — so an agent in the tab
  can query and act without your token ever leaving the browser context. Jekyll and
  vanilla JavaScript, reproducible via <code>devenv</code>.</p>
  <p>→ <a href="https://github.com/olafkfreund/Huginn" rel="noopener">source</a></p>
  </div>

  <div class="project">
  <h2 id="awsdash">AWS Dashboard — your own AWS account, as browser-agent tools</h2>
  <p><span class="tag">Creator · open source</span> <span class="tag">WebMCP</span></p>
  <p>The smallest of these, and the clearest illustration of why WebMCP is interesting.
  A browser page cannot read <code>~/.aws/credentials</code>, and it shouldn't — so a
  thin Node proxy holds the AWS SDK and the local profile, serves the static page, and
  the page publishes what it fetched to the browser's agent through
  <code>navigator.modelContext.registerTool</code>.</p>
  <p>What it surfaces is deliberately the two things you actually check first: every
  running EC2 instance, and who successfully logged into the console in the last 24
  hours, from CloudTrail. The IAM permissions it needs are exactly
  <code>ec2:DescribeInstances</code> and <code>cloudtrail:LookupEvents</code> — nothing
  else. An agent in the tab can then answer "what's running and who's been in?" as
  tool calls, while the credentials stay on the machine. Tailwind, glassmorphic dark
  mode, one file of backend.</p>
  <p>→ <a href="https://github.com/olafkfreund/AWS_dashboard" rel="noopener">source</a></p>
  </div>

  <div class="project">
  <h2 id="lxconnect">lxconnect — your Android phone as an MCP tool surface</h2>
  <p><span class="tag">Creator · open source</span> <span class="tag">Kotlin + Nix</span></p>
  <p>lxconnect bridges Android — Waydroid or a real device — to the Linux desktop,
  and the interesting half is the <strong>MCP server it runs on the phone</strong>.
  The Android app stands up a Ktor MCP server on port 8080 and hooks into
  <code>NotificationListenerService</code> and <code>PackageManager</code>, so an
  agent on your laptop can treat the phone as a set of tools: read notifications,
  open native deep links (<code>mailto:</code>, <code>spotify:</code>), launch and
  control apps, read system status, even drive the camera — all over a standard MCP
  transport.</p>
  <p>That turns "my phone" into something an agent can actually reach: triage
  notifications onto the desktop, hand a 2FA push to the right app, let a Claude
  session check or act on the device without you picking it up. A Python daemon reads
  a server-sent-events stream from the phone and surfaces it through
  <code>libnotify</code>; a GTK4/PyGObject app gives you a native UI to test and
  control it. The whole thing is a declarative Nix flake — <code>nix run
  github:olafkfreund/lxconnect#gui</code> and you're live.</p>
  <p>→ <a href="https://github.com/olafkfreund/lxconnect" rel="noopener">source</a></p>
  </div>

  <div class="project">
  <h2 id="nixarchy">nixarchy — a whole desktop, vendored onto NixOS</h2>
  <p><span class="tag">Creator · open source</span> <span class="tag">Nix · v4.0.1</span></p>
  <p><a href="https://omarchy.org" rel="noopener">Omarchy</a> 4.x is not a dotfiles
  repo, it's an application: <strong>429 shell commands</strong>, a QuickShell desktop
  shell, 22 themes and Hyprland driven through its Lua API. The usual Nix answer to
  something like that is to reimplement it, which produces a port that diverges from
  upstream the day after it lands. nixarchy packages the upstream tree <em>as a
  derivation</em> and replaces only the parts that assume Arch — so tracking a new
  release is a source bump, not a re-port.</p>
  <p>What that buys: the Install menu writes to your Nix config instead of running
  pacman, with 56 curated applications selectable that way and every other nixpkgs
  package and NixOS option one <code>Install ▸ Search</code> away — a single picker
  over 137k rows. Plugins and themes still install from a git URL at runtime the way
  upstream intends. Every command that assumed <code>/usr</code> either points at what
  NixOS actually uses or says plainly why it cannot. There's a bootable ISO that takes
  seven questions and leaves you with a machine that is a flake you own, offline.</p>
  <p>The naming is deliberate: upstream's 431 commands keep upstream's name, because a
  bug in <code>omarchy theme set</code> is a bug to report there, and renaming it would
  say otherwise. <code>nixarchy</code> owns what this port adds and <code>exec</code>s
  through for everything else.</p>
  <p>→ <a href="https://github.com/olafkfreund/nixarchy" rel="noopener">source</a></p>
  </div>

  </div>
</section>

<section class="section">
  <h2>Want one of these in your estate?</h2>
  <p class="section-lede">
    Most of this is open source and self-hosted by design — clone it and go. SARC
    and Fides are adopted rather than subscribed to, typically as a 4–8 week MVP
    install after which you own and operate it.
    <a href="{{ '/about/' | relative_url }}">Get in touch</a>, or see the
    <a href="{{ '/work/' | relative_url }}">client work and roles</a> behind them.
  </p>
</section>
