---
layout: doc
title: "AzAPI provider"
render_with_liquid: false
description: ">-"
---

```hcl
terraform {
  required_providers {
    azapi = {
      source  = "azure/azapi"
      version = "=0.1.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.2"
    }
  }
}

provider "azapi" {
  default_location = "eastus"
  default_tags = {
    team = "Azure deployments"
  }
}

provider "azurerm" {
  features {}
}
```plaintext



```hcl
# Provision a Lab Service Account and a Lab that are in public preview
resource "azapi_resource" "qs101-account" {
  type      = "Microsoft.LabServices/labaccounts@2018-10-15"
  name      = "qs101LabAccount"
  parent_id = azurerm_resource_group.qs101.id

  body = jsonencode({
    properties = {
      enabledRegionSelection = false
    }
  })
}

resource "azapi_resource" "qs101-lab" {
  type      = "Microsoft.LabServices/labaccounts/labs@2018-10-15"
  name      = "qs101Lab"
  parent_id = azapi_resource.qs101-account.id

  body = jsonencode({
    properties = {
      maxUsersInLab  = 10
      userAccessMode = "Restricted"
    }
  })
}
```plaintext


```bash
terraform init -upgrade
```plaintext
