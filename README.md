# tianyamoon/skills

This repository is the source of truth for my custom Codex skills.

## What lives here

- `skills/`: custom skill packages that I actively maintain
- `scripts/import-local-skills.ps1`: sync custom skills from `C:\Users\tiany\.codex\skills` into this repo
- `scripts/publish-to-codex.ps1`: publish skills from this repo back to `C:\Users\tiany\.codex\skills`

## Current scope

By default, this repo tracks skills from `C:\Users\tiany\.codex\skills` and skips `.system`.

Current imported skills:

- `industry-cycle-methodology`
- `industry-logic-scorer`
- `industry-trend-stock-picker`
- `raw-taxonomy-router`
- `source-to-thesis-extractor`
- `stock-wiki`
- `technical-stock-picker`
- `wiki-link-repair`
- `zmt-gzh-zy`

Chinese alias convention:

- See `SKILL_ALIASES.md` for the recommended Chinese names.
- These aliases are a human-facing routing convention, not the native skill `name`.
- The stable explicit form is still `$english-skill-slug`.

## Recommended workflow

1. Create or refine a skill locally.
2. Run `powershell -ExecutionPolicy Bypass -File .\scripts\import-local-skills.ps1`.
3. Review `git status --short`.
4. Commit and push to GitHub.
5. When moving to another machine, clone this repo and run `powershell -ExecutionPolicy Bypass -File .\scripts\publish-to-codex.ps1`.

## Notes

- SSH access to `git@github.com:tianyamoon/skills.git` still needs a usable public key on this machine.
- If you later want this repo to also track custom skills stored under `C:\Users\tiany\.agents\skills`, we can add a second source path and an explicit allowlist.
