---
layout: doc
title: "Lunarvim"
render_with_liquid: false
description: "LunarVim on Fedora"
---

Prerequisites for installing lvim on Fedora:


```bash
sudo dnf update
sudo dnf install git make pip python npm node cargo lazygit
```plaintext


Install Lvim:


```bash
LV_BRANCH='release-1.3/neovim-0.9' bash <(curl -s https://raw.githubusercontent.com/LunarVim/LunarVim/release-1.3/neovim-0.9/utils/installer/install.sh)
```plaintext


Or try it with docker/podman


```bash
docker run -w /root -it --rm alpine:edge sh -uelic 'apk add git neovim ripgrep alpine-sdk bash --update && bash <(curl -s https://raw.githubusercontent.com/lunarvim/lunarvim/master/utils/installer/install.sh) && /root/.local/bin/lvim'
podman run -w /root -it --rm alpine:edge sh -uelic 'apk add git neovim ripgrep alpine-sdk bash --update && bash <(curl -s https://raw.githubusercontent.com/lunarvim/lunarvim/master/utils/installer/install.sh) && /root/.local/bin/lvim'
```plaintext


Lunarvim for Windows:

Prerequisite for running Lunarvim on Windows

```plaintext
winget install git make pip python npm node cargo lazygit
```plaintext


```powershell
pwsh -c "`$LV_BRANCH='release-1.3/neovim-0.9'; iwr https://raw.githubusercontent.com/LunarVim/LunarVim/release-1.3/neovim-0.9/utils/installer/install.ps1 -UseBasicParsing | iex"
```plaintext
