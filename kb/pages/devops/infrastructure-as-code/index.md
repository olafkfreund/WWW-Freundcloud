---
layout: doc
title: "Infrastructure as Code"
render_with_liquid: false
---

```ascii
The Evolution of Infrastructure:
┌───────────Day 1──────────┐  ┌───────Day 365─────────┐
│                          │  │                        │
│  terraform plan          │  │  terraform plan        │
│  terraform apply         │  │                        │
│                         │  │  🤔 419 to change      │
│  + 3 to add             │  │  📝 891 to add         │
│  ~ 1 to change          │  │  ❌ 234 to destroy     │
│  - 0 to destroy         │  │                        │
│                         │  │  Dev: "It grew         │
│  "Perfect! Ship it!"    │  │   organically..."      │
└──────────────────────────┘  └────────────────────────┘
```

> "Infrastructure as Code: Because clicking buttons in a cloud console is for people who don't like excitement in their life."
