---
layout: post
title: "Cloudflare Tunnel, not Tailscale, behind Starlink CGNAT"
date: 2026-06-07 03:14:07 +0100
permalink: /blog/cloudflare-tunnel-not-tailscale-behind-starlink-cgnat/
tags: [nixos, platform, kubernetes, networking]
comments: true
excerpt: >-
  Three Tailscale-shaped approaches that didn't survive contact with reality,
  and the Cloudflare Tunnel architecture that finally did. A story about CGNAT,
  sidecar fragility, and what "right answer for most cases" actually means.
---

The homelab sits behind Starlink. Starlink does CGNAT. There is no public
IPv4, no port forward on my router that goes anywhere useful, and no
amount of fighting with my ISP that fixes it. Anything reaching my
services from "the internet" has to come through a service that owns a
public IP and tunnels traffic to me — the homelab speaks only outbound.

That single constraint disqualifies whole families of ingress designs
before I write a line of config. It does not disqualify anything that
opens a persistent outbound connection to a relay or an edge. Modern
options that fit that shape: Tailscale Funnel, Cloudflare Tunnel,
self-hosted `frp` on a cheap VPS, and the now-paid `ngrok` family. I
spent a weekend talking myself out of three of them.

## The first instinct was Tailscale

I was already running Tailscale across the host fleet for SSH, kubectl,
and the laptop. Adding a public-internet face to it felt like one config
line away. The case made itself: I was paying nothing, the daemon was
already there, and the [k8s operator
docs](https://tailscale.com/kb/1236/kubernetes-operator) make per-service
hostnames look trivial.

Three things eventually pushed me off that path.

First, the hostnames stay under `*.ts.net`. Funnel terminates TLS at
their edge with a Tailscale-issued cert; there's no path to *my* domain
in the URL bar without paying for something equivalent to Cloudflare for
SaaS on the Tailscale side. The browser-facing surface of a homelab is a
small detail, but it's not nothing — when my partner clicks a bookmark
I'd rather not have a `.ts.net` suffix in her face. Petty? Sure. Real?
Also yes.

Second, the **free tier of Tailscale Funnel caps at 3 services per
tailnet**. Three. I run roughly twenty. There is a path to lift that
cap, and it's not free, and the upgrade isn't aimed at homelab use cases.

Third — and this is where the weekend went — I tried the **sidecar
pattern** as a workaround. It's the obvious "let each Pod join the
tailnet on its own" approach: one `tailscale` container per Deployment,
auth key in a Secret, hostname env var, Tailscale Serve config in a
ConfigMap. It works with a plain auth key, no OAuth client juggling, and
the per-service `*.ts.net` hostname comes out the other end. So I built
it.

## The sidecar story

The sidecar pattern bit me three times in three days.

**Pod restarts rotated the tailnet identity.** Every time `argocd-server`
recreated its pod, `tailscaled` inside the sidecar registered with a
fresh node key (because `TS_STATE_DIR=/tmp/...` was ephemeral) and
Tailscale assigned a new device. Tailscale doesn't recycle the canonical
hostname when a new node key shows up; it appends a suffix. I watched
`argocd` become `argocd-1`, then `argocd-2`, then `argocd-3`. DNS for the
canonical name kept pointing at the original device, which was now
forever offline. My bookmarks were broken every time the cluster needed
a rolling restart.

**The PVC fix had a sharper edge.** I gave `TS_STATE_DIR` a
`PersistentVolumeClaim` backed by `local-path-provisioner`, expecting
that pinning the node key across restarts would stop the rename
treadmill. It did. Then I went into the Tailscale admin and deleted the
stale `argocd-1` / `argocd-2` / `argocd-3` device entries to clean up.
On the next pod start, `tailscaled` read the cached node key from the
PVC and tried to reconnect with a key the control plane had just
revoked. The result: a wedged daemon that retried forever, emitting

```
PollNetMap: initial fetch failed 404: node not found
```

once every fifteen seconds. No auto-recovery. The fix was a manual
state wipe inside the container, which meant
`kubectl exec rm -rf /var/lib/tailscale/*` followed by a pod delete.
Doable. Memorable. The kind of recovery that hides in a runbook nobody
will read at 11pm.

**Per-pod boilerplate didn't compose.** Every Deployment that wanted
exposure needed the sidecar container, the env-from-Secret for the auth
key, a separate ConfigMap holding the Tailscale Serve config, and
volume wiring for both. I tried to make that a copy-paste recipe and it
was always *almost* clean. I shipped it for five services and the
maintenance load wasn't terrible, but it wasn't free either. Multiply by
twenty.

The third one is the one I could have lived with. The first two are the
ones that made me stop.

## The pivot to Cloudflare Tunnel

I knew Cloudflare Tunnel existed. I'd been avoiding it because I didn't
want a CDN in front of my homelab. The constraint shrugged at that
preference.

Cloudflare Tunnel runs a small daemon (`cloudflared`) that opens
persistent outbound QUIC connections to Cloudflare's edge. When a public
request lands at `<name>.<home-domain>`, Cloudflare terminates TLS with a
real Let's Encrypt cert for my domain and forwards the request bytes
through one of the open connections to my daemon, which proxies it to a
local URL. There are no inbound ports, no public IP, no port forward,
and no sidecars.

It solves all three things the sidecar pattern couldn't:

- **My domain in the URL bar.** I added a domain as a free-tier
  Cloudflare zone, pointed its registrar nameservers at Cloudflare, and
  every public hostname I expose is under my apex with a real cert.
- **No service cap.** The free plan doesn't gate on tunnel hostname
  count. The twenty hostnames I now route would have needed a paid
  Tailscale plan; here they're a config-file line each.
- **No per-pod state to corrupt.** One daemon per scope — host-side or
  in-cluster — handles all the hostnames it knows about. There is no
  cached node key to revoke. There is no admin console where I can
  accidentally orphan an identity. The whole class of failure I spent a
  weekend on doesn't exist in this design.

I accept the trade-offs honestly. **Cloudflare can see plaintext at the
edge** for anything tunneled through it; for genuinely sensitive admin
paths I keep the tailnet available and don't expose them publicly at
all. **They could change the free-tier policy** and kick me off, which
would take down the public face of the homelab; the mitigation is that
every public service is *also* on the tailnet, so the failure mode is
"public goes down, admins keep working" rather than total outage.
**Authoritative DNS for one of my domains now lives with Cloudflare**;
the registrar still bills me, but Cloudflare answers queries. That's
reversible by switching the NS records back, and the actual records I
maintain stay in version control via the tunnel CLI.

## The architecture that landed

Two `cloudflared` connectors, each scoped to where the services
actually live.

The **host-side connector** is a NixOS systemd service running on the
homelab host. Its ingress map is declared inline in the host config:

```nix
features.cloudflared = {
  enable = true;
  tunnelId = "<tunnel-id>";
  ingress = {
    "<name1>.<home-domain>" = "http://localhost:<port>";
    "<name2>.<home-domain>" = "http://localhost:<port>";
    # ...
  };
};
```

It exposes services that already run on the host — the developer portal,
the media stack, anything bound to `localhost`.

The **in-cluster connector** is a Kubernetes `Deployment` inside the k3d
cluster, with its config in a `ConfigMap` shipped from the GitOps repo:

```yaml
ingress:
  - hostname: <name>.<home-domain>
    service: http://<svc>.<ns>.svc.cluster.local:<port>
```

It exposes services that live in the cluster — Factory components, the
GitOps controller itself, the identity provider.

Adding a new hostname is a one-line change to whichever connector owns
the target, plus one `cloudflared tunnel route dns` invocation to create
the matching CNAME at Cloudflare. End-to-end propagation is a couple of
minutes. The two connectors are independent — changing the cluster's
routing never touches the host's, and vice versa.

The full design is in
[the public-ingress TechDoc](https://nixos.freundcloud.com/architecture/public-ingress/),
with the host-side ops runbook in [the cloudflared
docs](https://nixos.freundcloud.com/applications/cloudflared-tunnel/).

## What this taught me

"It's the right answer for most cases" doesn't mean it's the right
answer for *your* case. Tailscale is brilliant at what Tailscale is
built for — a private mesh of trusted devices, kubectl from the couch,
SSH without thinking about jump hosts. It is not built to be a
public-internet ingress, and the parts you'd need to make it one (Funnel
limits, sidecar fragility, the `.ts.net` cert chain) aren't there
because that's not the product.

**The fragility class matters more than the boilerplate.** I would have
shipped sidecar copy-paste forever; I couldn't ship "the canonical
hostname silently moved to a `-3` suffix and DNS still points at the
dead `-2`". The two failure modes look similar from a distance — both
mean adding a service is more work than it should be — but only one of
them is the kind that wakes you up at 11pm.

**CGNAT-bound homelab? Cloudflare Tunnel is the default.** Even if you
don't think you want a CDN in front of you. The architecture is clean,
the daemon is small, the failure modes are legible, and the trade-offs
are honest. Everything else I tried turned into a series of workarounds
I had to remember.

The sidecars are gone. The `argocd-server` Pod is `1/1` again. There
hasn't been a `404 node not found` in the logs all week. That's the
shape of the thing working.
