---
layout: post
title: "I taught my CLI to publish this blog"
permalink: /blog/teaching-claude-to-blog/
tags: [meta, ai, agents, devops]
comments: true
excerpt: >-
  A /blog slash command that drafts a post in my voice, stages it in
  _drafts/, validates the Jekyll build, and pushes to main. The whole
  publishing pipeline is now one line from any terminal.
---

The last post explained how this blog works: a Markdown file in `_posts/`,
Jekyll, GitHub Pages, `git push`. That's a good pipeline right up until the
moment you have an idea on a Tuesday night and the friction of *opening the
repo, remembering the front-matter shape, getting the date format right* is
just enough to make you not bother. The posts that don't get written are
never the ones that were hard to write. They're the ones that were slightly
annoying to start.

So I removed the annoying part.

## One command

There's now a `/blog` slash command wired into my CLI. I type the topic —
or paste a few rough bullets — and it does the boring half:

```bash
/blog notes on why I moved CI off Bamboo
```

It derives a slug, fills in the five front-matter fields the templates
actually read (`title`, `date`, `permalink`, `tags`, `excerpt`), writes the
prose in something close to my own voice, and — only after a local
`jekyll build` passes — commits and pushes the single new file to `main`.
GitHub Actions takes it from there.

## The parts that matter

Two design choices did most of the work:

- **A drafts folder.** `--draft` writes to `_drafts/` with no date, so a
  half-formed idea can sit there until it's ready. `--publish <slug>` stamps
  it with today's date and moves it into `_posts/`. Jekyll ignores `_drafts/`
  in a production build, so nothing leaks before I mean it to.
- **A build gate before the push.** The thing I never want is a broken YAML
  block taking down the deploy. The command runs `bundle exec jekyll build`
  locally first; if it fails, nothing gets pushed. The CI htmlproofer and
  Pagefind steps are the second net, not the first.

## Why declare it in Nix

The command isn't a script I keep in one repo — it lives in my home-manager
config as a `home.file` entry, which means the same `/blog` shows up on every
machine I rebuild: the desktop, the server, the laptop. No syncing, no
"which version is current". The config *is* the source of truth, and the
slash command is just one more thing the flake installs.

That's the whole trick, really. The blog was already as simple as a blog can
be. The command didn't make publishing simpler — it made *starting* free.
