---
layout: landing
title: About
permalink: /about/
description: Olaf Krasicki-Freund — DevOps and platform engineering leader, 30 years in.
---

<section class="section">
  <div class="container prose">
    <h1 class="mt-0">About me</h1>

    <img class="about-portrait"
         src="{{ '/assets/img/about/olaf.jpg' | relative_url }}"
         alt="Olaf Krasicki-Freund"
         width="180" height="180">

    <p>I've been doing this for thirty years, which means I started before "DevOps"
    was a word and watched the whole thing arrive — bare metal, then virtual
    machines, then the cloud, then the realisation that none of it matters if
    developers can't ship. These days I work the platform side of that problem:
    the tooling, pipelines and golden paths that let a few hundred engineers move
    without standing on each other.</p>

    <p>I'm London-based, originally Norwegian, with Polish heritage that the
    surname gives away. I contract through Calitii, now part of Synechron, which
    puts me on regulated-sector programmes — banks and public-sector bodies where
    "move fast and break things" is not on the table and the audit trail has to be
    real.</p>

    <h2>What I've been doing here</h2>

    <p>Two main engagements. At <strong>Jefferies</strong>, a US investment bank,
    I led the migration of six business units off Bitbucket and Bamboo onto
    GitHub Enterprise and Actions — reusable workflow templates across Maven,
    Gradle, .NET, Python and Node, self-hosted runners on AKS, and the GitHub
    Enterprise governance written as Terraform so it was reviewable instead of a
    pile of console clicks. The bit I'm proudest of is the boring bit: production
    Bamboo pipelines cut over to Actions with nobody noticing.</p>

    <p>At the <strong>National Energy System Operator</strong> I led a team
    building Backstage as an internal developer platform — self-service
    scaffolding, golden-path templates, and one place to find who owns what. The
    work was as much about defining the operating model as writing the code.</p>

    <h2>How I work</h2>

    <p>I'm happiest when I can do the whole arc — architect the thing, write the
    Terraform, then stand in front of the CTO and explain why. I don't think those
    are separate jobs. The architecture decisions that survive contact with
    production are usually made by people who've also had to operate it at 3am.</p>

    <p>A couple of things I believe, after enough scar tissue to mean them:
    security controls developers route around are worse than no controls, because
    they cost you the same and buy you nothing. Infrastructure you can't rebuild
    from a clean checkout isn't infrastructure, it's a liability with a hostname.
    And most "we need a platform team" problems are really "we never wrote down
    the golden path" problems.</p>

    <h2>War stories</h2>

    <p>At Live-Tech Games I scaled a platform to a million concurrent users on AKS
    — a redesign into microservices and some fairly aggressive autoscaling, under
    a launch deadline that did not move. At Ofgem I moved legacy regulatory
    applications onto a microservices architecture and wrote the DevSecOps
    blueprints the organisation standardised on. At R3 I ran a multinational
    DevSecOps team on their distributed-ledger products and put real SRE practice
    in place — SLOs, error budgets, the lot.</p>

    <h2>Open source &amp; side projects</h2>

    <p>A lot of how I learn a tool is by building something real with it and
    putting it on GitHub. Most of these started as "I wonder if…" on a weekend
    and turned into things I actually use.</p>

    <p><strong>Delivery &amp; governance.</strong>
    <a href="https://github.com/olafkfreund/fides" rel="noopener">Fides</a> is a
    tamper-evident evidence ledger for the SDLC;
    <a href="https://github.com/olafkfreund/Hecate" rel="noopener">Hecate</a> is the
    cross-environment promotion layer FluxCD never had; and the
    <a href="https://github.com/olafkfreund/agentic-sdlc-showcase" rel="noopener">Agentic SDLC</a>
    reference build is the operating model for agent-written software as a repository
    that runs, with gates proven to refuse rather than merely to pass. The
    <a href="{{ '/showcase/#factory' | relative_url }}">Factory suite</a> — PFactory,
    AIFactory, TFactory, CFactory — is the pipeline that uses them.</p>

    <p><strong>AI &amp; LLM tooling.</strong> Mostly MCP, in one form or another:
    <a href="https://github.com/olafkfreund/janus" rel="noopener">Janus</a>, an MCP
    gateway built to survive a security review;
    <a href="https://github.com/olafkfreund/myrmex-hive" rel="noopener">Myrmex Hive</a>,
    agent orchestration with zero inbound ports;
    <a href="https://github.com/olafkfreund/lxconnect" rel="noopener">lxconnect</a>,
    which runs an MCP server on an Android phone; and the WebMCP portals —
    <a href="https://github.com/olafkfreund/Muninn" rel="noopener">Muninn</a> for GitHub,
    <a href="https://github.com/olafkfreund/Huginn" rel="noopener">Huginn</a> for GitLab,
    and an <a href="https://github.com/olafkfreund/AWS_dashboard" rel="noopener">AWS dashboard</a>
    that hands your own account to the agent in the browser tab. Earlier on there was
    <a href="https://github.com/olafkfreund/ollama-skill-cv-rag" rel="noopener">ollama-skill-cv-rag</a>
    for RAG over CVs and skills, and
    <a href="https://github.com/olafkfreund/SOW-generator" rel="noopener">SOW-generator</a>
    for drafting statements of work.</p>

    <p><strong>NixOS &amp; cloud infrastructure.</strong>
    <a href="https://github.com/olafkfreund/nixarchy" rel="noopener">nixarchy</a> vendors
    the whole Omarchy desktop onto NixOS instead of reimplementing it;
    <a href="https://github.com/olafkfreund/cloud-nixos" rel="noopener">cloud-nixos</a>
    builds and deploys hardened NixOS server images across AWS, GCP, Azure and European
    clouds with sops-nix and OpenTofu; and
    <a href="https://github.com/olafkfreund/nixos-k3d-lab" rel="noopener">nixos-k3d-lab</a>
    turns a multi-node Kubernetes dev cluster into a NixOS service with no registry in
    sight. <a href="https://github.com/olafkfreund/nixos-template" rel="noopener">nixos-template</a>
    is the batteries-included starting point, and
    <a href="https://github.com/olafkfreund/nixos_config" rel="noopener">nixos_config</a>
    is my whole estate declared in Nix.</p>

    <p><strong>Developer tools.</strong>
    <a href="https://github.com/olafkfreund/skill_pool" rel="noopener">skill-pool</a> is
    the team layer for Claude Code's <code>.claude/</code> directory;
    <a href="https://github.com/olafkfreund/herdr" rel="noopener">herdr</a> is a terminal
    multiplexer for coding agents;
    <a href="https://github.com/olafkfreund/dionysus" rel="noopener">dionysus</a> presents
    Markdown from a terminal or a browser and ships its own MCP server; and
    <a href="https://github.com/olafkfreund/gogmail" rel="noopener">gogmail</a> puts Google
    Workspace in a TUI. <a href="https://github.com/olafkfreund/SkillAi" rel="noopener">SkillAi</a>
    and the rest get the full write-up over on
    <a href="{{ '/showcase/' | relative_url }}">the showcase</a>.</p>

    <h2>Away from the keyboard</h2>

    <p>I tinker with NixOS and the COSMIC desktop more than is strictly
    reasonable, and I've written a few Rust applets for it. I was a governor at the
    Norwegian School in London for four years. I speak English, Norwegian and
    Polish. And I'll happily lose an afternoon to a music festival lineup.</p>

    <blockquote>They say cloud makes you feel younger. I've been 25 for about
    twenty-five cloud years now.</blockquote>

    <p>If any of this is your kind of problem, I'm easy to find —
    <a href="{{ site.linkedin_url }}" rel="noopener">LinkedIn</a>,
    <a href="https://github.com/{{ site.github_username }}" rel="noopener">GitHub</a>,
    or <a href="mailto:{{ site.email }}">{{ site.email }}</a>.</p>
  </div>
</section>
