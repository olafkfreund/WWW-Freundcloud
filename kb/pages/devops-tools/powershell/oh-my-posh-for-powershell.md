---
layout: doc
title: "Oh-my-Posh for PowerShell"
render_with_liquid: false
description: "Install \"oh-my-posh\" for Powershell"
---

```plaintext
Install-module posh-git
Install-module oh-my-posh
Install-module Terminal-Icons
```plaintext

To make it work in PowerShell vi need to configure the `$profile`



```plaintext
code $profile
```plaintext

Add this to Your `$profile`


```powershell
// Some codeImport-Module posh-git
 Import-Module oh-my-posh
 Import-Module PowerShellAI
 Import-Module -Name Terminal-Icons
 oh-my-posh init pwsh | Invoke-Expression

# PSReadLine
 Set-PSReadLineOption -EditMode Emacs
 Set-PSReadLineOption -BellStyle None
 Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete
 Set-PSReadLineOption -PredictionSource History
 Set-PSReadLineOption -PredictionViewStyle ListView
 Set-PSReadLineKeyHandler -Key UpArrow -Function HistorySearchBackward
 Set-PSReadLineKeyHandler -Key DownArrow -Function HistorySearchForward

```plaintext
