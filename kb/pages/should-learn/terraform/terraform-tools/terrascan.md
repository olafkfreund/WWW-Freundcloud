---
layout: doc
title: "Terrascan"
render_with_liquid: false
description: ">-"
---

Install Linux:


```bash
curl -L "$(curl -s https://api.github.com/repos/tenable/terrascan/releases/latest | grep -o -E "https://.+?_Darwin_x86_64.tar.gz")" > terrascan.tar.gz
tar -xf terrascan.tar.gz terrascan && rm terrascan.tar.gz
install terrascan /usr/local/bin && rm terrascan
$ alias terrascan="`pwd`/terrascan
terrascan
```plaintext


Windows Install:

```plaintext
tar -zxf terrascan_<version number>_Windows_x86_64.tar.gz
```plaintext

Docker use:

```bash
$ docker run --rm tenable/terrascan version
```plaintext

Use terrascan with docker from command line:


```bash
alias terrascan="docker run --rm -it -v "$(pwd):/iac" -w /iac tenable/terrascan"
```plaintext
