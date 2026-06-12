---
layout: post
title: "Letting VS Code into CFactory — the right way, not the easy way"
date: 2026-06-12 14:13:36 +0100
permalink: /blog/letting-vscode-into-cfactory-the-right-way/
tags: [agents, platform, devops]
comments: true
excerpt: >-
  My editor extension couldn't connect to the hosted CFactory cockpit. The fix
  looked like a one-liner and turned into a proper investigation: reading the
  extension's own code, untangling an SSO proxy, building a universal token gate,
  and a staged rollout that never once locked me out of my own dashboard.
---

[CFactory]({{ '/blog/making-the-cfactory-cockpit-live-and-honest/' | relative_url }})
is the cockpit over my agent pipeline — the pane that watches the planner, coder
and tester churn through GitHub issues. I also have a VS Code extension,
`factory-vscode`, that brings that same view into the editor. There was just one
problem: against the *hosted* cockpit at
[cfactory.freundcloud.org.uk](https://cfactory.freundcloud.org.uk), the extension
wouldn't connect. It kept asking for a token, and no token I gave it worked.

This is the story of fixing that — and why the obvious fix was the wrong one. It's
a small feature with a long tail of "wait, that won't work for everyone," and I
think the way it unfolded is a decent showcase of doing the work properly instead
of shipping the first thing that compiles.

## The obvious fix that wasn't

I'd already built the hand-off the extension expected: a `/connect/vscode` endpoint
that mints a token and redirects it back to the editor, plus a `/settings/token`
copy page. Done, shipped, deployed. Except the editor still wouldn't connect.

So I did the thing I should have done first: I **read the extension's actual code**
instead of trusting the contract in the issue. Two findings landed immediately.

First, the UriHandler rejects an empty token:

```ts
const token = params.get("token") ?? "";
if (!token) {
  vscode.window.showErrorMessage("Factory: the auth callback did not include a token.");
  return;
}
```

And my hosted cockpit runs its key store **open** — so `/connect/vscode` was handing
back an empty token, and the extension was right to refuse it. The hand-off couldn't
work until there was a real token to hand.

Second, and bigger: the cockpit sits behind an **oauth2-proxy** (Keycloak SSO). That
gate is built for a human in a browser. The extension talks to the API from inside
the editor with `Authorization: Bearer <token>` — and oauth2-proxy doesn't care about
your bearer; it wants a browser login, so it bounces every API call to a login page.
A pasted token sent to the cockpit URL never even reaches CFactory.

So the real problem wasn't "mint a token." It was "how does a programmatic client
authenticate to a thing that's wrapped in interactive SSO?"

## The fork — and the question that reframed it

There were two honest paths:

- **Keycloak OIDC.** The extension already had a first-class OIDC login built in.
  Reuse the SSO: the editor logs in, gets a Keycloak token, and oauth2-proxy is
  taught to accept that token instead of forcing the browser dance.
- **A CFactory API key.** Give CFactory its own token gate, independent of any proxy,
  and hand the editor a key.

OIDC was elegant and reused infrastructure I already had, so I started there. Then I
asked myself the question that reframed the whole thing:

> *What if someone runs CFactory without Keycloak? This has to work in every scenario.*

That killed OIDC-as-the-answer on the spot. OIDC only exists where Keycloak does. The
mechanism that works **everywhere** — local, self-hosted, behind any proxy — is
CFactory's own API key. OIDC isn't the foundation; it's a convenience layer you add
*on top* where SSO happens to exist. So I built the universal thing first.

## Building the gate properly

The temptation was to slap auth on `/api` and move on. But a blunt gate breaks real
traffic, so I mapped what actually had to keep flowing and built a single middleware
that enforces a scoped key only where it should:

```python
# Enforce on /api/* and /connect/* — but leave the machinery that must stay open alone.
_EXEMPT_PREFIXES = ("/api/events",)   # the idempotent inbound webhook from the factories
# also exempt: /health (k8s probes), /mcp (its own secret)
```

Read endpoints need a `read` key; write endpoints additionally need `write`; the
WebSocket feed authenticates the same way; and **open mode stays a no-op** so local
dev and the current production posture don't change until someone opts in. Then the
piece that makes it all hold together: the cockpit's own nginx injects the key for
browser users, who are *already* past the SSO gate — so turning on enforcement
doesn't break the human-facing dashboard.

I wrote the tests for the exemptions and the scope split before wiring it to anything
real. Thirteen of them. The whole suite — 220 — stayed green.

## The rollout that refused to lock me out

Here's where dedication looks like paranoia. Enforcing a key store while the cockpit
isn't yet injecting that key would 401 my own dashboard. So I refused to do it in one
move. I staged it:

1. **Inject, but stay open.** Ship the nginx key-injection while the key store is still
   open. Injecting a key nothing checks is a harmless no-op — but now the cockpit is
   *ready*. Verified the dashboard was untouched.
2. **Then enforce.** Turn the key store on. The cockpit keeps working because it's
   already injecting; the editor path now demands a key.

Two commits, a verification between them, and at no point was there a window where I
could have locked myself out of the thing I use to watch everything else.

I also found the simplification that saved a pile of work: I didn't need a new public
hostname for the editor. CFactory already exposes `cfactory-mcp.freundcloud.org.uk`
straight to the backend, bypassing the SSO proxy, for its read-only MCP server. The
editor could just use that — and the key-store middleware already leaves `/mcp` alone,
so the two coexist. No new DNS, no new certificate.

## The gotcha that made it click

With everything deployed, one thing still mattered enough to write in bold in every
doc I touched: **use the API URL, not the cockpit URL.**

- `cfactory.freundcloud.org.uk` → SSO gate → rejects a pasted token (302 to login).
- `cfactory-mcp.freundcloud.org.uk` → straight to the backend → your token is the gate.

I proved it live, which is the only proof I trust:

```
# editor host, no key
$ curl -s -o /dev/null -w '%{http_code}\n' https://cfactory-mcp.freundcloud.org.uk/api/workitems
401
# editor host, with the key
$ curl -s -o /dev/null -w '%{http_code}\n' -H "Authorization: Bearer $KEY" .../api/workitems
200
# cockpit host, still SSO-gated for browsers
$ curl -s -o /dev/null -w '%{http_code}\n' https://cfactory.freundcloud.org.uk/api/workitems
302
```

Three numbers — 401, 200, 302 — that say the whole design holds: the editor is gated
by its key, the browser is gated by SSO, and neither breaks the other.

## The result

You open `/settings/token`, copy the token, point the extension at the API URL, paste,
and you're in. No copy-paste dance with the wrong URL, no SSO detour, no expiry. And
because the universal path is the API key, it works the same whether you run CFactory
behind Keycloak, behind some other proxy, or on your laptop with no auth at all.

The OIDC layer is still there too, for anyone who wants the editor to log in via SSO
with auto-refreshing tokens — it just isn't load-bearing anymore. Every deployment has
a path that works.

It would have been faster to poke a hole in the proxy and call it done. It would also
have quietly exposed an API to the internet, broken for everyone not using my exact
SSO, and lied to the next person who read the docs. The right way took a few more
hours: read the real code, ask "does this work for everyone," build the universal
mechanism, stage it so nothing breaks, and verify it live. That's the version I want
running on the second monitor.

*Docs, for the curious: the [editor connection guide](https://github.com/olafkfreund/CFactory/blob/main/docs/guides/token-gated-api.md)
covers every scenario, and the extension README now spells out the cockpit-vs-API-URL
gotcha so nobody else loses an afternoon to it.*
