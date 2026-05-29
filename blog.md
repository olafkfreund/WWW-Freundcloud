---
layout: landing
title: Blog
permalink: /blog/
description: Notes on DevOps, platform engineering, multi-cloud, AI agents and NixOS.
---

<section class="section">
  <div class="prose">
    <h1 class="mt-0">Blog</h1>
    <p>Notes from the work — platform engineering, CI/CD migrations, multi-cloud,
    AI agents, and whatever NixOS rabbit hole I'm down this week.</p>

    {% if site.posts.size > 0 %}
    <ul class="post-list">
      {% for post in site.posts %}
      <li class="post-list-item">
        <a class="post-list-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <time class="post-list-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%-d %b %Y" }}</time>
        {% if post.excerpt %}<p class="post-list-excerpt">{{ post.excerpt | strip_html | truncatewords: 32 }}</p>{% endif %}
      </li>
      {% endfor %}
    </ul>
    {% else %}
    <p class="text-muted">$ ls _posts/ — nothing here yet. First post coming soon.</p>
    {% endif %}
  </div>
</section>
