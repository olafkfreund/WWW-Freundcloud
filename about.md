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

    <h2>What I'm doing now</h2>

    <p>Two main engagements. At <strong>Jefferies</strong>, a US investment bank,
    I'm leading the migration of six business units off Bitbucket and Bamboo onto
    GitHub Enterprise and Actions — reusable workflow templates across Maven,
    Gradle, .NET, Python and Node, self-hosted runners on AKS, and the GitHub
    Enterprise governance written as Terraform so it's reviewable instead of a
    pile of console clicks. The bit I'm proudest of is the boring bit: production
    Bamboo pipelines cut over to Actions with nobody noticing.</p>

    <p>At the <strong>National Energy System Operator</strong> I'm leading a team
    building Backstage as an internal developer platform — self-service
    scaffolding, golden-path templates, and one place to find who owns what. The
    work is as much about defining the operating model as writing the code.</p>

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

    <p><strong>AI &amp; LLM tooling.</strong>
    <a href="https://github.com/olafkfreund/ollama-skill-cv-rag" rel="noopener">ollama-skill-cv-rag</a>
    does CV and skill analysis with retrieval-augmented generation on top of
    Ollama; <a href="https://github.com/olafkfreund/SOW-generator" rel="noopener">SOW-generator</a>
    drafts statements of work for consulting engagements with an LLM; and
    <a href="https://github.com/olafkfreund/nix-ai-help" rel="noopener">nix-ai-help</a>
    is a NixOS environment for running and poking at open-source models.</p>

    <p><strong>NixOS &amp; cloud infrastructure.</strong> A cluster of experiments in
    reproducible local cloud:
    <a href="https://github.com/olaffreund/nix-local-cloud" rel="noopener">nix-local-cloud</a>,
    <a href="https://github.com/olaffreund/k8s-local-clouds" rel="noopener">k8s-local-clouds</a>,
    <a href="https://github.com/olaffreund/ks3-nixos-vms" rel="noopener">ks3-nixos-vms</a>
    (lightweight k3s on NixOS VMs), and
    <a href="https://github.com/olaffreund/nix-llm-vms" rel="noopener">nix-llm-vms</a>
    for running models on throwaway machines.</p>

    <p><strong>Developer tools.</strong>
    <a href="https://github.com/olaffreund/Commit-tracking-mcp" rel="noopener">Commit-tracking-mcp</a>
    is an MCP server for analysing git history, and
    <a href="https://github.com/olaffreund/tinky-llm-buddy" rel="noopener">tinky-llm-buddy</a>
    is a small AI dev assistant. There's also
    <a href="https://github.com/olafkfreund/SkillAi" rel="noopener">SkillAi</a> and the
    Kosli/ServiceNow MCP servers — those get the full write-up over on
    <a href="{{ '/work/' | relative_url }}">Work</a>.</p>

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
