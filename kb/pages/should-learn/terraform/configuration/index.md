---
layout: doc
title: "Terraform Configuration"
render_with_liquid: false
description: "Terraform configuration guide for multiple cloud providers including AWS, Azure, and GCP"
---

This section covers Terraform configuration across multiple cloud providers. Terraform uses the HashiCorp Configuration Language (HCL) to declaratively describe your infrastructure.

## Provider Configuration

<div class="tabs">
<div class="tab-buttons"><button class="active">Azure</button><button class="">AWS</button><button class="">GCP</button></div>
<div class="tab-panel active" markdown="1">

```hcl

# Azure Provider configuration
provider "azurerm" {
  features {}
  subscription_id = "your-subscription-id"
  tenant_id       = "your-tenant-id"
}

# Create a resource group
resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
  
  tags = {
    environment = "dev"
  }
}

```
plaintext

For more details on Azure specific configurations, see the [Azure section](azure/index.html).
</div>
<div class="tab-panel" markdown="1">

```hcl

# AWS Provider configuration
provider "aws" {
  region = "us-west-2"
}

# Create a VPC
resource "aws_vpc" "example" {
  cidr_block = "10.0.0.0/16"
  
  tags = {
    Name = "example-vpc"
    Environment = "dev"
  }
}

```
plaintext

For more details on AWS specific configurations, see the [AWS section](aws.html).
</div>
<div class="tab-panel" markdown="1">

```hcl

# GCP Provider configuration
provider "google" {
  credentials = file("account.json")
  project     = "your-project-id"
  region      = "us-central1"
}

# Create a GCP network
resource "google_compute_network" "example" {
  name                    = "example-network"
  auto_create_subnetworks = false
}

```
plaintext

For more details on GCP specific configurations, see the [GCP section](gcp.html).
</div>
</div>

## Backend Configuration

Your Terraform state can be stored in various backends. Choose the one that best fits your workflow:

<div class="tabs">
<div class="tab-buttons"><button class="active">Azure Storage</button><button class="">S3</button><button class="">GCS</button></div>
<div class="tab-panel active" markdown="1">

```hcl

terraform {
  backend "azurerm" {
    resource_group_name  = "terraform-state-rg"
    storage_account_name = "terraformstate00123"
    container_name       = "tfstate"
    key                  = "prod.terraform.tfstate"
  }
}

```
plaintext
</div>
<div class="tab-panel" markdown="1">

```hcl

terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt = true
  }
}

```
plaintext
</div>
<div class="tab-panel" markdown="1">

```hcl

terraform {
  backend "gcs" {
    bucket = "tf-state-prod"
    prefix = "terraform/state"
  }
}

```
plaintext
</div>
</div>

## Current Terraform Version

This documentation assumes Terraform version 1.10 or higher.
