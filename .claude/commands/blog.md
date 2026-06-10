---
description: Draft, stage, and publish a post to the freundcloud Jekyll blog (GitHub Pages)
argument-hint: "[--draft|--publish <slug>|--list] <title or notes>"
allowed-tools: Bash(*), Read, Write, Edit
---

Invoke the **blog** skill to handle this request, passing the arguments below
verbatim as its input. Follow the skill's workflow exactly (locate repo → parse
mode → gather → write → validate-and-publish), including its safety rules: never
overwrite an existing post/draft, build locally before pushing, and stage only
the new post file.

Arguments:

$ARGUMENTS
