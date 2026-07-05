param(
    [string]$SourceRoot = (Join-Path $PSScriptRoot "..\skills"),
    [string]$DestinationRoot = "C:\Users\tiany\.codex\skills"
)

$ErrorActionPreference = "Stop"

$resolvedSource = [System.IO.Path]::GetFullPath($SourceRoot)
New-Item -ItemType Directory -Force -Path $DestinationRoot | Out-Null

$skillDirs = Get-ChildItem -Path $resolvedSource -Directory

foreach ($skillDir in $skillDirs) {
    $targetPath = Join-Path $DestinationRoot $skillDir.Name
    if (Test-Path -LiteralPath $targetPath) {
        Remove-Item -LiteralPath $targetPath -Recurse -Force
    }
    Copy-Item -LiteralPath $skillDir.FullName -Destination $targetPath -Recurse -Force
    Write-Host ("Published {0}" -f $skillDir.Name)
}

Write-Host ""
Write-Host ("Published {0} skill(s) into {1}" -f $skillDirs.Count, $DestinationRoot)
