param(
    [string]$SourceRoot = "C:\Users\tiany\.codex\skills",
    [string]$DestinationRoot = (Join-Path $PSScriptRoot "..\skills"),
    [switch]$IncludeSystem
)

$ErrorActionPreference = "Stop"

$resolvedDestination = [System.IO.Path]::GetFullPath($DestinationRoot)
New-Item -ItemType Directory -Force -Path $resolvedDestination | Out-Null

$skillDirs = Get-ChildItem -Path $SourceRoot -Directory
if (-not $IncludeSystem) {
    $skillDirs = $skillDirs | Where-Object { $_.Name -ne ".system" }
}

foreach ($skillDir in $skillDirs) {
    $targetPath = Join-Path $resolvedDestination $skillDir.Name
    if (Test-Path -LiteralPath $targetPath) {
        Remove-Item -LiteralPath $targetPath -Recurse -Force
    }
    Copy-Item -LiteralPath $skillDir.FullName -Destination $targetPath -Recurse -Force
    Write-Host ("Imported {0}" -f $skillDir.Name)
}

Write-Host ""
Write-Host ("Imported {0} skill(s) into {1}" -f $skillDirs.Count, $resolvedDestination)
