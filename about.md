---
layout: landing
title: About
description: Olaf Krasicki-Freund — DevOps and platform engineering leader, 30 years in.
---

<section class="section">
  <div class="container prose">
    <h1 class="mt-0">About me</h1>

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
