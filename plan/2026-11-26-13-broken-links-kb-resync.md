---
status: approved
issue: 13
spec: spec/2026-11-26-13-broken-links-kb-resync.md
coders:
  2: agy    # large mechanical edit set across ~30 wiki pages, with an exact mapping
  3: codex  # small tricky logic: converter path resolution plus unit test
  4: coder  # four one-line blog anchor edits
reviewers:
  - codex  # independent read of both diffs against this plan
  - agy    # second read; checks that every remap target exists
---

# Plan: Fix the broken links, recover the wiki source and reconvert the KB

Approved decisions:

- The source of truth is `olafkfreund/wiki`, with the two trash commits
  recovered on top of it.
- Fixes go in the wiki, never in `kb/` by hand. A missing page is unlinked,
  never invented.
- The converter gains a `pages/` root rule and skips `docs/index.md`.
- Merge order: wiki PR first, then the website PR.
- The goal is htmlproofer 0 and converter audit 0.

Repos:

- **Wiki:** `~/Source/GitHub/wiki`, branch `fix/kb-links-and-fides`. Step 1 is
  already done there (`a2a06f0`, `5cb6c58` on top of `a51eb22`).
- **Site:** `~/Source/GitHub/www-freundcloud`, branch
  `fix/13-broken-links-kb-resync`.

## Steps

1. **Recover the commits (done by lead).** Fetch from
   `/mnt/code/.Trash-1000/files/wiki`, cherry-pick onto `origin/main`. Verified
   by a dry-run convert that matched `kb/` apart from `docs/`.

2. **Wiki page fixes.** All paths are under `~/Source/GitHub/wiki/pages/`, and
   each link target is relative to its file. "Unlink" means `[text](x)` becomes
   `text`.
   - `containers/kubernetes/README.md`, `devops/observability/README.md` and
     `devops/observability/dashboard.md`:
     `../../should-learn/kubernetes/troubleshooting/README.md` →
     `../../should-learn/kubernetes/troubleshooting/kubernetes-pod-troubleshooting-commands.md`.
     All three files are at the same depth, so the prefix is unchanged.
   - `devops/governance/README.md`: `../../../reference/tool-comparison.md` →
     `../../reference/tool-comparison.md`.
   - `public-clouds/aws/README.md`:
     - `../../../terraform/aws-scenarios.md` → `../../terraform/aws-scenarios.md`
     - `../../../need-to-know/cloud-compliance/README.md` →
       `../../need-to-know/cloud-compliance/README.md`
     - `../../../sre/senarios/aws-vm-monitoring-api.md` →
       `../../sre/senarios/aws-vm-monitoring-api.md` (keep `senarios`: the
    `scenarios/` copy is a zero-byte stub)
   - `public-clouds/README.md`: `azure/azure-landing-zone/README.md` →
     `landing_zones/azure-landing-zone/README.md`.
   - `public-clouds/azure/README.md`: `azure-landing-zone/README.md` →
     `../landing_zones/azure-landing-zone/README.md`.
   - `devops/source-control/gitlab/README.md`:
     - `../../ci-cd/README.md` → `../../ci-cd-platforms/README.md` (exists).
     - `../../containers/README.md` ("Container Registry"): unlink. The only
       candidates are an empty stub and an unrelated Kubernetes page.
     - `../git-workflows.md` → `../git-branching-strategies.md`
     - `../../iac/README.md`: unlink.
   - `terraform/README.md`:
     - `../iac/README.md`: unlink.
     - `../../group-1/bicep/README.md` → `../bicep/README.md` (exists).
   - Unlink each of these, keeping the text:
     - `public-clouds/aws/services/README.md`: ec2, lambda, ebs, rds, dynamodb,
       vpc, cloudfront.
     - `public-clouds/gcp/services/README.md`: cloud-spanner, firestore.
     - `llm/copilot/README.md`: agent-mode, infrastructure-deployment,
       editor-integration, custom-instructions, project-roles.
     - `devops/observability/tracing.md` and `metrics.md`: open-telemetry.
     - `metrics.md`: kubernetes/monitoring.
   - **http → https:**
     - `devops/agile-development/README.md:209`
     - `agile-development/README.md:60`
     - `devops/agile-development/senarios/software_service.md:941`
     - `should-learn/terraform/configuration/aws.md:89,95`
     - `should-learn/linux/configuration/cloud-init/cloud-init-examples.md:179`
       (the markdown link only, not the apt source on line 195)
     - `need-to-know/testing/end-to-end-testing/real-life-example.md:5`
     - Also any other `http://agilemanifesto.org` in the same files, for
       example the line-5 prose links.
   - `should-learn/kubernetes/ingress-controllers/traefik.md:91`: the line
     becomes `` Access at: `http://127.0.0.1:9000/dashboard/` ``.
   - `should-learn/kubernetes/tips/k8s-troubleshooting-pod-in-container-creating-status.md`:
     delete the five `<a href="#xxxx" id="#xxxx"></a>` suffixes on lines 48,
     65, 96, 106 and 116.
   - Missing section anchors:
     - `devops/ci-cd-platforms/tekton/build-and-push-an-image-with-tekton.md:27`:
       `../README.md#installation-guide-2025` →
       `README.md#installation-guide-2025`. The heading `## Installation Guide
       (2025)` is in the sibling README, so only the depth was wrong.
     - `llm/README.md:9`: unlink "AI-Assisted Testing". The target page holds
       only a heading.
   - `should-learn/kubernetes/README.md:9`: replace the `{% include %}` line with
     the 9-line body of `_snippets/kubernetes-prerequisites.md`.
   - `devops/tools-to-install/kubernetes/klone.md:3`: replace the `{% embed %}`
     with
     `[klone write-up (gist)](https://gist.github.com/vishal-sarg/93ce03ba30f57101b5d46e1e31ab6bec#file-klone-blog-md)`.
   - `showcase/README.md`, Factory section:
     - The heading becomes `### The Factory suite — PFactory · AIFactory ·
       TFactory · CFactory · RFactory`.
     - Line 46 becomes, verbatim: `84% of developers use AI coding tools; only
       29% trust the output. The Factory suite is the trust layer for that gap —
       five products around one idea: **AI can write the code, but someone still
       has to be accountable for it**. Four of them are the stages of the **PARR
       pipeline** — Prepare · Act · Reflect · Review — with a human gate at every
       seam rather than one "trust me" big bang. The fifth, RFactory, brings that
       pipeline into the team's calls.`
     - Add the bullet: `- **RFactory (the meeting room)** — an AI bot that
       joins your Meet, Zoom, Teams or Slack calls, runs the standup straight
       from the CFactory board, and turns what the team agrees into changes
       through the other four, each one waiting on a named approver.`
     - "The spine that makes four products cohere" → "The spine that makes the
       four PARR products cohere". "every product emits" → "each of them
       emits".
     - The link row adds `· [RFactory](https://github.com/olafkfreund/RFactory)`.
   - Verify with a preview into temporary paths (the converter deletes its
     `--out` tree, so never run it without these flags here):

     ```bash
     T=$(mktemp -d); python3 scripts/convert.py --wiki ~/Source/GitHub/wiki --out $T/kb --data $T/toc.yml --report $T/report.txt; grep -c "BROKEN LINK\|LEFTOVER LIQUID" $T/report.txt
     ```

     Before step 3, the only findings left are the 16 `pages/…` links and the
     fenced `./docs/runbook.md` example. Run it from the site repo.
   - Traps: don't edit fenced code blocks. Do not touch `SUMMARY.md`. Never
     stage or commit.

3. **Converter (`scripts/convert.py`) and its test.**
   - In `rewrite_links`, resolve relative to the file first, then fall back to
     the wiki root only for a `pages/…` link that didn't resolve:

     ```python
     target = os.path.normpath(os.path.join(src_dir, raw)).replace(os.sep, "/")
     if target not in known and raw.startswith("pages/"):
         target = os.path.normpath(raw).replace(os.sep, "/")  # GitBook root-relative
     ```

   - `rewrite_links` must not touch fenced code blocks (```` ``` ```` or `~~~`).
     Split the body on fence lines, rewrite only the parts outside fences, and
     rejoin. A link inside an example is example text: it's neither rewritten
     nor audited.
   - Add `"docs/index.md"` to `EXCLUDE_RELPATHS`, with a comment: Backstage
     TechDocs stub.
   - Add a test to `scripts/test_convert.py`. Call `rewrite_links` with
     `src_rel="pages/a/b.md"`, `out_rel="pages/a/b.md"`,
     `known={"pages/c/d.md"}` and the body `[x](pages/c/d.md)`. Assert the
     output is `[x](../c/d.html)`. Add these assertions:
     - When both `pages/a/pages/c/d.md` and `pages/c/d.md` are in `known`, the
       link resolves to the relative one, `pages/a/pages/c/d.md`.
     - A link inside a fenced block comes back unchanged and adds no audit line.
   - Verify with `python3 -m unittest discover -s scripts`.

4. **Blog anchors.**
   - `_posts/2026-05-29-welcome-to-the-blog.md:28`,
     `_posts/2026-05-31-one-model-cant-do-everything.md:43` and
     `_posts/2026-06-10-making-the-cfactory-cockpit-live-and-honest.md:15`:
     `/work/#aifactory` → `/work/#factory`.
   - `_posts/2026-06-05-backstage-freundcloud-portal.md:15`:
     `/work/#backstage` → `/work/#neso`.
   - Verify with `grep -rn "work/#aifactory\|work/#backstage" _posts`, which
     should return nothing.

5. **Lead: preview, regenerate, check.**
   - Preview into temporary paths, as in step 2. The audit must print 0, and
     `diff -rq kb $T/kb` must list only files the fixes touch, apart from
     `kb/index.md`, which the converter preserves.
   - Check that `$T/kb/pages/devops/governance/fides` has the same 7 files as
     `kb/`.
   - Regenerate the live outputs only after the wiki PR merges and `wiki` is
     on `main` at the merge commit. Record that commit's SHA in the site commit
     body.

     ```bash
     python3 scripts/convert.py --wiki ~/Source/GitHub/wiki
     ```

   - Build and check:

     ```bash
     bundle exec jekyll build
     LD_LIBRARY_PATH=$(nix build --no-link --print-out-paths nixpkgs#curl.out)/lib bundle exec htmlproofer _site --disable-external --ignore-empty-alt --allow-missing-href --ignore-urls "/pagefind/"
     ```

     Expected result: `HTML-Proofer finished successfully`.

6. **Lead: reviews, commits, PRs, merge.**
   - Codex and agy review both diffs, plus a fresh Opus review.
   - Wiki: commit (step 2 edits only) as `fix(kb): repair dead links, http, anchors; RFactory in
     showcase`, push the branch with the recovered commits, open a PR, merge.
   - Site: commit, push, PR linking all three artifacts, merge after the wiki.
   - Watch the Pages deploy, then spot-check two fixed KB pages live.

## Tests

- `python3 -m unittest discover -s scripts` passes.
- `grep -c "BROKEN LINK\|LEFTOVER LIQUID" docs/plans/link-audit.txt` prints `0`.
- htmlproofer prints "HTML-Proofer finished successfully".
- `ls kb/pages/devops/governance/fides` still lists 7 pages.

## Rollback

- Site: revert the merge commit on `main`.
- Wiki: revert its merge commit. The recovered commits stay in history either
  way.
