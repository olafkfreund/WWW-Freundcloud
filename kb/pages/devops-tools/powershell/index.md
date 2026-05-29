---
layout: doc
title: "PowerShell"
render_with_liquid: false
description: "PowerShell on Fedora Linux"
---

```bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo
sudo dnf makecache
sudo dnf install powershell
pwsh
```plaintext


Running PowerShell from a container:


```bash
podman run \
 -it \
 --privileged \
 --rm \
 --name powershell \
 --env-host \
 --net=host --pid=host --ipc=host \
 --volume $HOME:$HOME \
 --volume /:/var/host \
 mcr.microsoft.com/powershell \
 /usr/bin/pwsh -WorkingDirectory $(pwd)as
```plaintext
