---
layout: post
title: "Making the CFactory cockpit live (and honest)"
date: 2026-06-10 16:47:04 +0100
permalink: /blog/making-the-cfactory-cockpit-live-and-honest/
tags: [agents, platform, devops]
comments: true
excerpt: >-
  A day on CFactory — the cockpit over my planner/coder/tester agent pipeline.
  Killed a production 500, stopped the dashboard lying about what's running, and
  made it update itself with notifications instead of asking me to hit refresh.
---

CFactory is the cockpit over my agent pipeline — the single pane that watches
[AIFactory]({{ '/work/#aifactory' | relative_url }}) and its planner/tester
siblings churn through GitHub issues (plan → code → test, correlated by issue
number). It's the thing I leave open on a second monitor. Which means when it
lies, or freezes, or 500s, I notice. Today I spent fixing all three. Three PRs,
all live now at [cfactory.freundcloud.org.uk](https://cfactory.freundcloud.org.uk).

## The 500 that only showed up under load

First the embarrassing one. The board started throwing `HTTP 500` intermittently.
The logs were blunt:

```
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) database is locked
  File ".../app.py", line 281, in list_workitems
```

A *read* — `GET /api/workitems` — was failing because it collided with the poll
loop's write. Here's the thing I'd forgotten: production quietly fell back to
SQLite. No `DATABASE_URL` was set, so the data layer took its dev default. And
SQLite's default journal locks the **whole database** on write, so any read that
lands during a write doesn't queue — it errors immediately.

The fix is the standard SQLite-under-concurrency move: WAL mode (readers run
alongside a single writer) and a busy timeout (wait for a lock instead of raising):

```python
@event.listens_for(engine, "connect")
def _set_sqlite_pragmas(dbapi_conn, _record):
    cur = dbapi_conn.cursor()
    cur.execute("PRAGMA journal_mode=WAL")
    cur.execute("PRAGMA busy_timeout=30000")
    cur.execute("PRAGMA synchronous=NORMAL")
    cur.close()
```

Writing the regression test then flushed out a *second* 500 hiding behind the
first: `upsert_from_event` did check-then-insert, so two writers racing on the
same issue number hit `UNIQUE constraint failed`. One retry on `IntegrityError`
— by then the row exists and the second pass just updates — and a concurrency
test that hammers it with readers and writers at once now stays green. The real
long-term fix is to give prod an actual Postgres URL, but the PRAGMAs make SQLite
solid enough for the load it's under.

## The counts that lied

Next: the dashboard said **15 running tasks** when exactly one was running.

The badges were counting lifetime totals. Each work item got bucketed by the
*furthest* stage it had ever reached, so finished and idle items inflated the
numbers forever — a completed pipeline still looked busy. Worse, the view was
titled "Running tasks" but defaulted to showing everything active, so 16 items
awaiting review read as "16 running".

I pulled the live data and ran the classifier over it to be sure I wasn't
guessing: **1 running, 13 in review, 2 queued, 12 done**. So I made the count
mean what it says — an item is counted once, at the furthest stage that's still
*live* (running, in review, or queued); done and idle drop off. And I renamed
the view to **Active tasks**, because that's what it is. A dashboard you can't
trust is worse than no dashboard.

## No more hitting refresh

The complaint that kicked it off: *"I don't want to keep refreshing to see
what's new."* Fair. There was already a WebSocket pushing snapshots every few
seconds — but the client opened it exactly once and, on any drop, gave up
forever. Close the laptop, come back, and the socket was dead; the feed sat
frozen on stale data until a manual reload.

So the feed now reconnects with capped backoff and sends a keepalive ping every
25s, and the backend pushes the current snapshot **on connect** rather than
making a fresh tab wait for the next poll. The "● live" pill flips back on its
own. There's also a small version-watcher that notices when a new bundle has
deployed and reloads the tab, so I stop shipping fixes that nobody sees because
their browser cached the old `index.html`.

## And tell me when something happens

The last piece: I shouldn't have to *look* at the cockpit to know something
changed. It now fires a notification — a native OS one when the tab's in the
background, plus an in-app toast — on four transitions: a new task starts, one
finishes, one fails, or one moves into review.

The only interesting part is not being annoying about it. The state of every
task is diffed against what was last seen, so notifications fire only on genuine
transitions, and the first page load seeds the baseline silently — open the
cockpit and you don't get 40 toasts for tasks that were already there.

## The theme

None of this is clever. It's the unglamorous maintenance that decides whether a
tool earns its place on the monitor: don't 500, don't lie, don't make me poke
you, and tell me when it matters. The cockpit does all four now. Back to
watching the agents ship.
