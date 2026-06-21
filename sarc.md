---
layout: landing
title: "SARC — multi-cloud compliance orchestration"
permalink: /sarc/
description: >-
  SARC is the orchestration and correlation layer above Kosli and ServiceNow —
  multi-cloud, multi-CI, auditor-ready. 5-axis risk scoring, one-click evidence
  for SOC 2 / ISO 27001 / DORA / PSD2 / NIST / PCI-DSS / SOX, and an MCP gateway
  for AI agents.
---

<section class="hero">
  <div class="hero-badge">SARC · regulated software delivery, auditor-ready</div>
  <h1>The orchestration layer above <span class="accent">Kosli + ServiceNow</span>.<br>Multi-cloud. Multi-CI. Auditor-ready.</h1>
  <p class="tagline">
    SARC doesn't replace your compliance investments — it's the surface that turns
    their data into the story your regulator, auditor and change board actually want.
    It unifies Kosli evidence and ServiceNow workflow into one auditable pipeline that
    runs identically on AWS, Azure, GCP and on-prem, across GitLab CI, GitHub Actions
    and Azure DevOps.
  </p>
  <div class="hero-cta">
    <a class="btn btn-primary" href="https://sarc-6f4a6f.gitlab.io/" rel="noopener">See the live walkthrough</a>
    <a class="btn btn-secondary" href="#why">Why it exists</a>
    <a class="btn btn-secondary" href="{{ '/work/#sarc' | relative_url }}">In the portfolio</a>
  </div>
</section>

<section class="section">
  <figure class="shot">
    <img src="{{ '/assets/img/work/sarc-dashboard.png' | relative_url }}"
         alt="SARC operator dashboard" loading="lazy">
    <figcaption>The operator dashboard — pipelines, change requests and compliance state in one view.</figcaption>
  </figure>
</section>

<section class="section" id="why">
  <h2>The pain SARC removes</h2>
  <p class="section-lede">Four things repeat in every regulated delivery shop. Each one
  is a place where evidence, risk or reality falls through the cracks.</p>
  <div class="card-grid">
    <div class="card">
      <span class="tag">Evidence is scattered</span>
      <h3>Nobody owns the whole story</h3>
      <p>SonarQube, Snyk, Wiz, GitGuardian, Trivy, ServiceNow, Kosli, GitLab, GitHub
      Actions, Azure DevOps — each owns a fragment of the audit story, and no one tool
      owns the whole of it.</p>
    </div>
    <div class="card">
      <span class="tag">Approvals are a bottleneck</span>
      <h3>A typo waits as long as a migration</h3>
      <p>A one-character fix and a schema migration both get the same 48-hour CAB
      review, because nothing makes the difference in risk visible.</p>
    </div>
    <div class="card">
      <span class="tag">The CMDB is always stale</span>
      <h3>Records drift from reality</h3>
      <p>What's actually running in production at month-end has drifted a long way from
      what the CMDB believes is running.</p>
    </div>
    <div class="card">
      <span class="tag">Cloud lock-in, too early</span>
      <h3>Audit stories break on migration</h3>
      <p>Compliance tooling wired to one cloud's primitives breaks the audit story the
      moment a workload moves somewhere else.</p>
    </div>
  </div>
</section>

<section class="section">
  <h2>What SARC actually delivers</h2>
  <p class="section-lede">One auditable pipeline on top of the tools you already own —
  computing the things neither Kosli nor ServiceNow can see on their own.</p>
  <div class="prose">
    <ul>
      <li>A <strong>5-axis risk clearance score</strong> per change, derived from Kosli
      attestations and written back into the ServiceNow change request — a number no
      other system in the stack computes.</li>
      <li><strong>Vulnerability SLO burndown with cost-to-fix correlation</strong> —
      remediation priced in dollars per month, not abstract severity labels.</li>
      <li><strong>One-button evidence packaging</strong> for SOC 2, ISO 27001, DORA,
      PSD2, NIST 800-53, PCI-DSS and SOX — the feature customers cite first.</li>
      <li><strong>AI agent recipes</strong> that turn findings into one-click fix
      merge requests across all three CI platforms.</li>
      <li>An <strong>MCP gateway</strong> that lets AI agents query Kosli, ServiceNow
      and portal data in plain language — without breaking compliance boundaries.</li>
      <li><strong>Service-to-incident correlation</strong> over a directed graph that
      Kosli doesn't compute and ServiceNow can't see.</li>
    </ul>
  </div>

  <div class="shot-grid">
    <figure>
      <img src="{{ '/assets/img/work/sarc-risk.png' | relative_url }}" alt="5-axis risk clearance score" loading="lazy">
      <figcaption>5-axis risk clearance per change</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/work/sarc-compliance.png' | relative_url }}" alt="Compliance dashboard with framework coverage" loading="lazy">
      <figcaption>Multi-framework coverage</figcaption>
    </figure>
    <figure>
      <img src="{{ '/assets/img/work/sarc-clusters.png' | relative_url }}" alt="Multi-cluster overview across clouds" loading="lazy">
      <figcaption>Multi-cluster, multi-cloud overview</figcaption>
    </figure>
  </div>
</section>

<section class="section">
  <h2>What it means in the boardroom</h2>
  <p class="section-lede">The same platform answers three very different executives.</p>
  <div class="card-grid">
    <div class="card">
      <span class="tag">For the CFO</span>
      <h3>Audit cost, quantified</h3>
      <p>Audit prep drops from weeks of compilation to one click. Cost–vulnerability
      correlation puts remediation ROI in dollars. One platform replaces 4–6 manual
      processes previously held together by spreadsheets.</p>
    </div>
    <div class="card">
      <span class="tag">For the CIO / CTO</span>
      <h3>Real parity, no capture</h3>
      <p>Cloud parity is real — the same Terraform shape on AWS, Azure, GCP and
      on-prem. CI parity is real — the same gates on GitLab CI, GitHub Actions and
      Azure DevOps. You own the open architecture end to end, deployed in your cloud.</p>
    </div>
    <div class="card">
      <span class="tag">For the CCO / Head of GRC</span>
      <h3>Evidence on demand</h3>
      <p>Auditors get their own time-boxed, magic-link session, read-only to the audit
      and compliance routes. Evidence is reproducible per deployment, not compiled per
      quarter. AI governance for the EU AI Act, NIST AI RMF and ISO 42001 is built in,
      not bolted on.</p>
    </div>
  </div>
</section>

<section class="section">
  <h2>By the numbers</h2>
  <div class="card-grid">
    <div class="card"><h3>7 frameworks</h3><p>SOC 2, ISO 27001, DORA, PSD2, NIST 800-53, PCI-DSS, SOX — one-click evidence each.</p></div>
    <div class="card"><h3>3 CI platforms</h3><p>GitLab CI (source of truth), GitHub Actions (full parity), Azure DevOps.</p></div>
    <div class="card"><h3>5 deploy targets</h3><p>AWS EKS, Azure AKS, GCP GKE, OpenShift and a local k3d cluster from one switch.</p></div>
    <div class="card"><h3>37 portal screens</h3><p>Operator, change requests, vulnerabilities, control mapping, evidence, audit log and more.</p></div>
    <div class="card"><h3>Tamper-evident</h3><p>A hash-chained audit log, so the trail can't be quietly rewritten.</p></div>
    <div class="card"><h3>MCP-native</h3><p>Ask the compliance state of a commit in plain English, via the MCP gateway.</p></div>
  </div>
</section>

<section class="section">
  <h2>What SARC is <em>not</em></h2>
  <p class="section-lede">The scope guards matter as much as the features — SARC is a
  thin, honest orchestration layer, not a land-grab.</p>
  <div class="prose">
    <ul>
      <li>Not a SaaS competing with ServiceNow — the workflow control plane stays in ServiceNow.</li>
      <li>Not a SaaS competing with Kosli — the evidence data plane stays in Kosli.</li>
      <li>Not a CI platform. Not a cloud. Not a CMDB replacement. Not an authentication system.</li>
    </ul>
  </div>
</section>

<section class="section">
  <h2>How you adopt it</h2>
  <p class="section-lede">SARC is a reference architecture and demo platform — you don't
  subscribe to it, you adopt it.</p>
  <div class="prose">
    <p>A typical engagement is a 4–8 week MVP install. After that, the customer owns
    and operates it: no SaaS bill, no per-seat fee, no vendor capture — the open
    architecture is deployed in your cloud and audited by you.</p>
    <p>
    → <a href="https://sarc-6f4a6f.gitlab.io/" rel="noopener">Walk through the live portal</a>
    · <a href="{{ '/work/#sarc' | relative_url }}">See SARC in the portfolio</a>
    </p>
  </div>
</section>
