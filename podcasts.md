---
layout: landing
title: Podcasts
permalink: /podcasts/
description: >-
  Audio walkthroughs of the projects — SARC, Fides, Hecate, the Agentic SDLC
  reference build and the Factory suite — generated with Google NotebookLM.
---

<section class="hero">
  <div class="hero-badge">▶ Listen · {{ site.data.podcasts | size }} episodes</div>
  <h1>The projects, out <span class="accent">loud</span>.</h1>
  <p class="tagline">
    Two hosts talking through what I've built and why, generated with Google
    NotebookLM from the projects' own documentation. If you'd rather listen on a
    commute than read a showcase page, start here — every episode has a download
    link, and each one is also embedded next to the project it covers.
  </p>
  <div class="hero-cta">
    <a class="btn btn-secondary" href="{{ '/showcase/' | relative_url }}">Read the showcase instead</a>
    <a class="btn btn-secondary" href="{{ '/work/' | relative_url }}">Client work</a>
  </div>
</section>

<section class="section">
  <div class="prose podcast-list">
    {% for ep in site.data.podcasts %}
    <figure class="podcast">
      <figcaption class="podcast-head">
        <span class="tag">▶ {{ ep.duration }}</span>
        <strong>{{ ep.title }}</strong>
      </figcaption>
      <p class="podcast-blurb">{{ ep.blurb }}</p>
      <audio controls preload="none" src="{{ '/assets/audio/podcasts/' | append: ep.file | relative_url }}">
        Your browser can't play audio inline —
        <a href="{{ '/assets/audio/podcasts/' | append: ep.file | relative_url }}">download the episode</a>.
      </audio>
      <p class="podcast-foot">
        <a href="{{ '/showcase/#' | append: ep.anchor | relative_url }}">Read about {{ ep.project }} →</a>
        · <a href="{{ '/assets/audio/podcasts/' | append: ep.file | relative_url }}" download>Download {{ ep.size }}</a>
      </p>
    </figure>
    {% endfor %}
  </div>
</section>

<section class="section">
  <div class="prose">
    <p class="text-muted">These are machine-generated from each project's own
    documentation, so treat them as a readable summary rather than my own words —
    the written pages are the authoritative version. Audio is 96 kbps mono AAC;
    the files live in the repo, so a download is a plain HTTP fetch with nothing
    tracking it.</p>
  </div>
</section>
