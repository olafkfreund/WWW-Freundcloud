---
layout: landing
title: null
description: >-
  Olaf Krasicki-Freund — DevOps and Platform Engineering leader. GitHub
  Enterprise migration, internal developer platforms, multi-cloud, and a
  large cloud-engineering knowledge base.
---

<section class="hero">
  <div class="hero-badge">▲ DevOps · Platform Engineering · 30 years in</div>
  <h1>I build the <span class="accent">platforms</span><br>other engineers build on.</h1>
  <p class="tagline">
    I'm Olaf — a DevOps and platform engineering leader. Right now I'm moving a
    tier-1 investment bank off Bitbucket and Bamboo onto GitHub Enterprise, and
    standing up a Backstage developer platform for the UK's energy system operator.
  </p>
  <div class="hero-cta">
    <a class="btn btn-primary" href="{{ '/work/' | relative_url }}">See what I've built</a>
    <a class="btn btn-secondary" href="{{ '/cv/' | relative_url }}">Read the CV</a>
    <a class="btn btn-secondary" href="{{ '/kb/' | relative_url }}">Knowledge base</a>
  </div>
</section>

<section class="section">
  <h2>Selected work</h2>
  <p class="section-lede">A few things I've designed, written, and shipped.</p>
  <div class="card-grid">
    <a class="card" href="{{ '/work/#sarc' | relative_url }}">
      <span class="tag">Multi-cloud · Compliance</span>
      <h3>SARC</h3>
      <p>A compliance pipeline that ships the same code to AWS, Azure, GCP and a
      laptop k3d cluster from one switch — wiring ServiceNow, Kosli and three CI
      platforms into one auditable flow.</p>
    </a>
    <a class="card" href="{{ '/work/#aifactory' | relative_url }}">
      <span class="tag">Open source · AI agents</span>
      <h3>AIFactory &amp; TFactory</h3>
      <p>Spec-driven development for AI agents: a planner → coder → QA pipeline that
      turns a GitHub issue into a pull request — and a sister project that
      autogenerates and runs the tests.</p>
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
      <p>Leading six business units at a US investment bank off Bitbucket + Bamboo
      onto GitHub Actions — reusable workflow templates, self-hosted runners on
      AKS, and governance as Terraform instead of clicks.</p>
    </a>
    <a class="card" href="{{ '/work/#nixos' | relative_url }}">
      <span class="tag">Open source · NixOS</span>
      <h3>nixos_config</h3>
      <p>My whole machine estate declared in Nix — multi-host flakes with a
      feature-flag system, Agenix secrets, Home Manager and a custom CLI.</p>
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
  <h2>What I'm into</h2>
  <p class="section-lede">
    Internal developer platforms and golden paths · multi-cloud Kubernetes ·
    Terraform and Nix for things that rebuild the same way every time ·
    DevSecOps that developers don't route around · LLM tooling and MCP servers ·
    and a Linux desktop held together with NixOS and a bit of Rust.
  </p>
</section>
