---
layout: doc
title: "TFLint"
render_with_liquid: false
description: ">-"
---

* Find possible errors (like invalid instance types) for Major Cloud providers (AWS/Azure/GCP).
* Warn about deprecated syntax, unused declarations.
* Enforce best practices, naming conventions.

Linux:


```bash
curl -s https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh | bash
```plaintext


Windows:

```plaintext
choco install tflint
```plaintext

Docker/Podman

```bash
docker run --rm -v $(pwd):/data -t ghcr.io/terraform-linters/tflintas
```plaintext

You can install the plugin by adding a config to `.tflint.hcl` and running `tflint --init`:

```hcl
plugin "azurerm" {
    enabled = true
    version = "0.24.0"
    source  = "github.com/terraform-linters/tflint-ruleset-azurerm"
}
```plaintext
