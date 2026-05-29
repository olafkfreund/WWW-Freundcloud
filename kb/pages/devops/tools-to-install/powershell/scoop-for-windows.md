---
layout: doc
title: "Scoop for Windows"
render_with_liquid: false
---

Install scoop with PowerShell:


```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time
irm get.scoop.sh | iex
```plaintext


Example use:

```powershell
scoop bucket add nerd-fonts 
```plaintext
