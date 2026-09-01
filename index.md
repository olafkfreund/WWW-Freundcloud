---
layout: landing
title: null
description: >-
  Olaf Krasicki-Freund — DevOps and Platform Engineering leader. Self-hosted
  compliance for regulated delivery, GitHub Enterprise migration, internal
  developer platforms, multi-cloud, and a large cloud-engineering knowledge base.
---

<section class="hero">
  <div class="hero-badge">▲ DevOps · Platform Engineering · 30 years in</div>
  <h1>I build the <span class="accent">platforms</span><br>other engineers build on.</h1>
  <p class="tagline">
    I'm Olaf — a DevOps and platform engineering leader. Right now I'm product owner
    and lead architect on <a href="{{ '/showcase/#sarc' | relative_url }}">SARC</a>:
    self-hosted, tamper-evident compliance for regulated delivery — one install,
    every framework, and nobody else holding your audit trail. Before that I moved a
    tier-1 investment bank onto GitHub Enterprise and stood up a Backstage developer
    platform for the UK's energy system operator.
  </p>
  <div class="hero-cta">
    <a class="btn btn-primary" href="{{ '/showcase/#sarc' | relative_url }}">See what I'm building</a>
    <a class="btn btn-secondary" href="{{ '/work/' | relative_url }}">Client work</a>
    <a class="btn btn-secondary" href="{{ '/cv/' | relative_url }}">Read the CV</a>
    <a class="btn btn-secondary" href="{{ '/kb/' | relative_url }}">Knowledge base</a>
  </div>
</section>

<section class="section">
  <h2>Selected work</h2>
  <p class="section-lede">A few things I've designed, written, and shipped.</p>
  <div class="card-grid">
    <a class="card" href="{{ '/showcase/#sarc' | relative_url }}">
      <span class="tag">Multi-cloud · Compliance</span>
      <h3>SARC</h3>
      <p>A compliance pipeline that ships the same code to AWS, Azure, GCP and a
      laptop k3d cluster from one switch — wiring ServiceNow, the Fides evidence
      ledger and three CI platforms into one auditable flow.
      <strong>See the full showcase →</strong></p>
    </a>
    <a class="card" href="{{ '/showcase/' | relative_url }}">
      <span class="tag">Everything, with screenshots</span>
      <h3>Project showcase</h3>
      <p>Seventeen systems in one place — SARC, Fides, Hecate, the Factory suite,
      the Agentic SDLC reference build, Bifrost, Janus, Myrmex Hive, ravn-agents,
      DORA Dashboard, SkillAi, Odin, Muninn, Huginn, lxconnect and nixarchy.
      <strong>Browse the showcase →</strong></p>
    </a>
    <a class="card" href="{{ '/work/#factory' | relative_url }}">
      <span class="tag">Open source · AI agents</span>
      <h3>The Factory suite</h3>
      <p>A governed pipeline for AI software delivery — PFactory plans it, AIFactory
      builds it, TFactory tests it, CFactory watches it. PARR, with a human gate at
      every seam and model-agnostic via MCP.</p>
    </a>
    <a class="card" href="{{ '/showcase/#hecate' | relative_url }}">
      <span class="tag">Open source · GitOps</span>
      <h3>Hecate</h3>
      <p>The promotion layer FluxCD never had. Four resources — Beacon, Bundle, Gate,
      Passage — move an immutable set of artifact versions across environments, with
      approvals, compliance evidence and OpenTelemetry tracing built in. Go.</p>
    </a>
    <a class="card" href="{{ '/showcase/#agentic-sdlc' | relative_url }}">
      <span class="tag">Open source · Governance</span>
      <h3>Agentic SDLC</h3>
      <p>The operating model for agent-written software as a repository that runs —
      seven stages, no model in the gate, and twelve deliberate violations proving
      each gate refuses rather than merely passes.</p>
    </a>
    <a class="card" href="{{ '/work/#bifrost' | relative_url }}">
      <span class="tag">Open source · Migration</span>
      <h3>Bifrost</h3>
      <p>Azure DevOps → GitHub Actions migration at portfolio scale. Wraps GitHub's
      importer with a review-first workflow, explainable risk scoring and signed
      attestations — air-gap capable on local models. Rust + React.</p>
    </a>
    <a class="card" href="{{ '/work/#ravn' | relative_url }}">
      <span class="tag">Open source · Rust</span>
      <h3>ravn-agents</h3>
      <p>Self-healing for Linux fleets that never decides on its own — deterministic
      detection, Ed25519-signed remediation, AI that only explains. Runs on hosts,
      Kubernetes and air-gapped networks.</p>
    </a>
    <a class="card" href="{{ '/work/#skillpool' | relative_url }}">
      <span class="tag">Open source · Claude Code</span>
      <h3>skill-pool</h3>
      <p>The team layer for Claude Code's <code>.claude/</code> — a self-hosted
      registry (Rust + Svelte) with retrospective capture that turns the work the
      team actually did into reviewable skills.</p>
    </a>
    <a class="card" href="{{ '/work/#skillai' | relative_url }}">
      <span class="tag">Open source · AI</span>
      <h3>SkillAi</h3>
      <p>A self-hosted recruiting platform built on Claude and Gemini. Parses CVs,
      scores candidates four ways, and keeps every byte on infrastructure the
      team owns. In production hiring for HSBC's Kraków hub.</p>
    </a>
    <a class="card" href="{{ '/work/#jefferies' | relative_url }}">
      <span class="tag">CI/CD · Migration</span>
      <h3>GitHub Enterprise migration</h3>
      <p>Led six business units at a US investment bank off Bitbucket + Bamboo onto
      GitHub Actions — reusable workflow templates, self-hosted runners on AKS, and
      governance as Terraform instead of clicks. Delivered.</p>
    </a>
    <a class="card" href="{{ '/work/#nixos' | relative_url }}">
      <span class="tag">Open source · NixOS</span>
      <h3>nixos_config</h3>
      <p>My whole machine estate declared in Nix — multi-host flakes with a
      feature-flag system, Agenix secrets, Home Manager and a custom CLI. Plus
      <a href="{{ '/showcase/#nixarchy' | relative_url }}">nixarchy</a>, which vendors
      the whole Omarchy desktop onto NixOS with its menus rewired to Nix.</p>
    </a>
    <a class="card" href="{{ '/work/#lxconnect' | relative_url }}">
      <span class="tag">Open source · Linux desktop</span>
      <h3>Desktop &amp; terminal tooling</h3>
      <p>An Android phone as an MCP tool surface (lxconnect), Google Workspace in a TUI
      (gog/gogmail), websites as native GNOME apps, and a pile of COSMIC and Hyprland
      Rust.</p>
    </a>
    <a class="card" href="{{ '/kb/' | relative_url }}">
      <span class="tag">Writing</span>
      <h3>Knowledge base</h3>
      <p>Years of notes on cloud architecture, Kubernetes, IaC, DevSecOps and
      NixOS — the reference I wish I'd had starting out. Hundreds of pages,
      searchable.</p>
    </a>
  </div>
</section>

<section class="section">
  <h2>Latest writing</h2>
  <p class="section-lede">Working out loud — the newest from the <a href="{{ '/blog/' | relative_url }}">blog</a>.</p>
  <ul class="post-list">
    {% for post in site.posts limit:3 %}
    <li class="post-list-item">
      <a class="post-list-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <time class="post-list-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%-d %b %Y" }}</time>
      {% if post.excerpt %}<p class="post-list-excerpt">{{ post.excerpt | strip_html | truncatewords: 28 }}</p>{% endif %}
    </li>
    {% endfor %}
  </ul>
</section>

<section class="section">
  <h2>What I'm into</h2>
  <p class="section-lede">
    Internal developer platforms and golden paths · multi-cloud Kubernetes ·
    Terraform and Nix for things that rebuild the same way every time ·
    DevSecOps that developers don't route around · LLM tooling and MCP servers ·
    and a Linux desktop held together with NixOS and a bit of Rust.
  </p>
</section>
