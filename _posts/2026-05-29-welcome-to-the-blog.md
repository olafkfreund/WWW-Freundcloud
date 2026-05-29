---
layout: post
title: "Hello from a terminal-green corner of the internet"
date: 2026-05-29 12:00:00 +0100
permalink: /blog/hello/
tags: [meta, devops]
comments: true
excerpt: >-
  Why I finally gave the site a blog, what I plan to write about, and how the
  whole thing is held together with Jekyll and GitHub Pages.
---

I've kept notes for years — they live in [the knowledge base]({{ '/kb/' | relative_url }}),
which started life as a GitBook and now runs here as a few hundred Markdown pages.
But the KB is reference material: how to do a thing, written to be looked up. This
is the other half — the working-out-loud half. Shorter, more opinionated, and dated.

## What I'll write about

The same things I do for a living, mostly:

- **CI/CD migrations at scale** — the unglamorous reality of moving a bank off
  Bitbucket and Bamboo onto GitHub Actions without anyone noticing.
- **Platform engineering** — golden paths, Backstage, and why "we need a platform
  team" is usually "we never wrote the path down".
- **AI agents that ship** — what actually works when you wire Claude into a real
  toolchain, from MCP servers to the planner/coder/QA pipeline in
  [AIFactory]({{ '/work/#aifactory' | relative_url }}).
- **NixOS** — because I can't stop, and reproducibility is a hill I'll die on.

## How this blog works

No CMS, no database. Each post is a Markdown file in `_posts/`, Jekyll turns it
into a page, and GitHub Pages builds and deploys it on every push. To publish, I
write a file and `git push` — or, when I'm away from the laptop, I create it
straight from the GitHub web editor on my phone.

```bash
# a new post is literally just:
$ $EDITOR _posts/2026-06-01-some-thing-i-learned.md
$ git commit -am "post: some thing I learned" && git push
```

That's the whole pipeline. More soon.
