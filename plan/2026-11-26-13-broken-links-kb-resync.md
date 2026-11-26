---
status: draft
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
     Recompute the depth from each file.
   - `devops/governance/README.md`: `../../../reference/tool-comparison.md` →
     `../../reference/tool-comparison.md`.
   - `public-clouds/aws/README.md`:
     - `../../../terraform/aws-scenarios.md` → `../../terraform/aws-scenarios.md`
     - `../../../need-to-know/cloud-compliance/README.md` →
       `../../need-to-know/cloud-compliance/README.md`
     - `../../../sre/senarios/aws-vm-monitoring-api.md` →
       `../../sre/scenarios/aws-vm-monitoring-api.md`
   - `public-clouds/README.md`: `azure/azure-landing-zone/README.md` →
     `landing_zones/azure-landing-zone/README.md`.
   - `public-clouds/azure/README.md`: `azure-landing-zone/README.md` →
     `../landing_zones/azure-landing-zone/README.md`.
   - `devops/source-control/gitlab/README.md`:
     - `../../ci-cd/README.md` → `../../ci-cd-platforms/README.md` if that file
       exists; otherwise unlink.
     - `../../containers/README.md` → `../../../containers/kubernetes.md`
     - `../git-workflows.md` → `../git-branching-strategies.md`
     - `../../iac/README.md`: unlink.
   - `terraform/README.md`:
     - `../iac/README.md`: unlink.
     - `../../group-1/bicep/README.md` → `../bicep/README.md` if it exists;
       otherwise `../bicep/bicep-with-github-actions.md`.
   - Unlink each of these, keeping the text:
     - `public-clouds/aws/services/README.md`: ec2, lambda, ebs, rds, dynamodb,
       vpc, cloudfront.
     - `public-clouds/gcp/services/README.md`: cloud-spanner, firestore.
     - `llm/copilot/README.md`: agent-mode, infrastructure-deployment,
       editor-integration, custom-instructions, project-roles.
     - `devops/observability/tracing.md` and `metrics.md`: open-telemetry.
     - `metrics.md`: kubernetes/monitoring.
     - `devops/documentation/examples/real-world-examples.md`:
       `./docs/runbook.md`.
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
       drop `#installation-guide-2025`.
     - `llm/README.md:9`: drop `#ai-assisted-testing`.
   - `should-learn/kubernetes/README.md:9`: replace the `{% include %}` line with
     the 8-line body of `_snippets/kubernetes-prerequisites.md`.
   - `devops/tools-to-install/kubernetes/klone.md:3`: replace the `{% embed %}`
     with
     `[klone write-up (gist)](https://gist.github.com/vishal-sarg/93ce03ba30f57101b5d46e1e31ab6bec#file-klone-blog-md)`.
   - `showcase/README.md`, Factory section:
     - The heading becomes `### The Factory suite — PFactory · AIFactory ·
       TFactory · CFactory · RFactory`.
     - "four products around one idea" → "five products around one idea".
       Then: "Four of them are the stages of the **PARR pipeline**" …, and add
       "The fifth, RFactory, brings that pipeline into the team's calls."
     - Add the bullet: `- **RFactory (the meeting room)** — an AI bot that
       joins your Meet, Zoom, Teams or Slack calls, runs the standup straight
       from the CFactory board, and turns what the team agrees into changes
       through the other four, each one waiting on a named approver.`
     - "The spine that makes four products cohere" → "The spine that makes the
       four PARR products cohere". "every product emits" → "each of them
       emits".
     - The link row adds `· [RFactory](https://github.com/olafkfreund/RFactory)`.
   - Verify by running step 5's dry-run convert. The report should show only
     the `pages/…` self-link findings, which step 3 fixes.
   - Traps: don't edit fenced code blocks. Do not touch `SUMMARY.md`. Never
     stage or commit.

3. **Converter (`scripts/convert.py`) and its test.**
   - In `rewrite_links`, replace the `target = …` line with:

     ```python
     base = "" if raw.startswith("pages/") else src_dir  # GitBook root-relative links
     target = os.path.normpath(os.path.join(base, raw)).replace(os.sep, "/")
     ```

   - Add `"docs/index.md"` to `EXCLUDE_RELPATHS`, with a comment: Backstage
     TechDocs stub.
   - Add a test to `scripts/test_convert.py`. Call `rewrite_links` with
     `src_rel="pages/a/b.md"`, `out_rel="pages/a/b.md"`,
     `known={"pages/c/d.md"}` and the body `[x](pages/c/d.md)`. Assert the
     output is `[x](../c/d.html)`. Also assert that the relative `[y](../c/d.md)`
     still resolves the same way.
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

5. **Lead: dry run, regenerate, check.**
   - Run:

     ```bash
     python3 scripts/convert.py --wiki ~/Source/GitHub/wiki
     ```

     The audit should show 0 BROKEN LINK and 0 LEFTOVER LIQUID.
   - `git diff --stat kb` should list only files the fixes touch, with no
     deleted Fides pages.
   - `jekyll build` passes, and htmlproofer reports 0 failures.

6. **Lead: reviews, commits, PRs, merge.**
   - Codex and agy review both diffs, plus a fresh Opus review.
   - Wiki: commit as `fix(kb): repair dead links, http, anchors; RFactory in
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
