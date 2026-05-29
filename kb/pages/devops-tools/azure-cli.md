---
layout: doc
title: "Azure-cli"
render_with_liquid: false
description: "Azure-CLI on Fedora"
---

```bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
```plaintext


```bash
sudo dnf install -y https://packages.microsoft.com/config/rhel/9.0/packages-microsoft-prod.rpm
```plaintext



```bash
sudo dnf install -y https://packages.microsoft.com/config/rhel/8/packages-microsoft-prod.rpm
```plaintext


```bash
sudo dnf install azure-cli
```plaintext

When installed use: `az login --use-device-code`
