# mobile-logo-system

A skill for Codex and Claude that creates, reviews, refines and packages mobile-first logo and app icon systems for iOS and Android, from concept territories to a handoff package.

## Layout

- `SKILL.md`: canonical entrypoint and 14-step workflow. Its Progressive Disclosure section says when each reference loads; step 7 waits for the user to pick a concept.
- `.claude/skills/mobile-logo-system/SKILL.md`: thin Claude wrapper that reaches the canonical files through `${CLAUDE_SKILL_DIR}/../../../`. `agents/openai.yaml` is Codex metadata.
- `references/`: runtime references. The five craft topics come in pairs: `<topic>.md` is the short runtime checklist the skill loads, `<topic>-guide.md` is the full author guide.
- `assets/package-template/`: the handoff package that `scripts/init_logo_system_package.py` scaffolds.
- `brand/`: this project's own logo (Construction Vesica, `brand/spec.md`), used by the README.
- `scripts/`: installer, validator, contact sheet renderer, and one `smoke_test_*.py` per tool.

## Changing the skill

1. Runtime context is the scarce resource here: v2.4.0 and v2.5.0 cut it by about 75% to stop concept generation from hanging. New detail goes into a `-guide.md` or a reference behind a Progressive Disclosure line; `SKILL.md` and the runtime checklists stay lean.
2. Edit, then run every step of `.github/workflows/ci.yml` locally: `validate_skill_repo.py` and the four smoke tests. Done is all green. `smoke_test_contact_sheet_browser.py` needs Node.js (`npx`).
3. A new tool ships with its own `smoke_test_*.py` and a step in `ci.yml`.
4. Release: one version in `SKILL.md` frontmatter, the `**Current version: X.Y.Z**` line in `README.md`, and a `## [X.Y.Z]` header in `CHANGELOG.md` (`validate_skill_repo.py` checks all three), plus upgrade steps in `MIGRATION.md` when a package breaks. Semver rules are in `README.md`.

## Source of truth and copies

This repo is the source of truth. After a change, report which copies need a sync and leave the sync to the owner. Each copy is a wrapper plus a vendor copy, made by `python3 scripts/install_skill.py --claude-project <path> --force`; that command overwrites the wrapper, and both wrappers below differ from what it writes, so merge them by hand.

- `~/Documents/thera_tales/.claude/skills/mobile-logo-system/SKILL.md` and `~/Documents/thera_tales/.claude/vendor/mobile-logo-system/`.
- `~/Documents/mobile-design-skill/.claude/skills/mobile-logo-system/SKILL.md` and `~/Documents/mobile-design-skill/.claude/vendor/mobile-logo-system/`, both gitignored in that repo.
