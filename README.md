# Mobile Logo System Skill

**Current version: 2.2.0** | [Changelog](CHANGELOG.md) | [Migration guide](MIGRATION.md)

A reusable AI skill for Codex and Claude that helps create, review, refine, and package mobile-first logo systems.

It is built for real app branding work, not generic logo prompting. The skill behaves like a compact brand director for mobile products.

## Contents

- [What It Does](#what-it-does)
- [Key Capabilities](#key-capabilities)
- [Quality Tiers](#quality-tiers)
- [Installation](#installation)
- [Production Package](#production-package)
- [Repository Structure](#repository-structure)
- [Versioning](#versioning)
- [Validation](#validation)
- [Ready-To-Use Prompts](#ready-to-use-prompts)
- [Suggested Usage Pattern](#suggested-usage-pattern)
- [Compatibility](#compatibility)
- [Canonical Files](#canonical-files)

## What It Does

1. inspect the current product and visual language first
2. verify current platform and store constraints when freshness matters
3. generate concept territories with real silhouette logic
4. evaluate options for reduction, monochrome survival, and platform fit
5. propose the next improvement moves or ask only high-leverage questions
6. scaffold a real handoff package when the project needs files

## Key Capabilities

- Project-first audit using local assets, screenshots, design boards, and current UI patterns
- Live research workflow for Apple, Android, App Store, and Google Play guidance
- Stronger concept quality rules so first rounds are differentiated instead of decorative noise
- Review/refinement loops that identify the best option, its weakest point, and 2-3 concrete upgrade moves
- Hi-end craft pass: geometric construction, color system, typography craft, premium craft, context validation
- Production package scaffolding via [`scripts/init_logo_system_package.py`](scripts/init_logo_system_package.py)
- Repository validation via [`scripts/validate_skill_repo.py`](scripts/validate_skill_repo.py)

## Quality Tiers

The skill supports two quality tiers:

- **Standard** — solid, production-aware work. Concept territories, 7-dimension evaluation, reduction and monochrome checks, basic platform validation. Default for most requests.
- **Hi-end** — full craft pipeline. Adds geometric construction, color system audit, typography craft, premium craft, comprehensive context testing, longevity assessment, and motion consideration. Activated when the work demands it.

See the tier selection triggers in [`SKILL.md`](SKILL.md) step 1.

## Installation

### Codex

Quick install (symlink, recommended):

```bash
python3 scripts/install_skill.py --codex
```

Copy instead of symlink:

```bash
python3 scripts/install_skill.py --codex --codex-mode copy
```

Override Codex home:

```bash
python3 scripts/install_skill.py --codex --codex-home /path/to/codex
```

Default install path: `${CODEX_HOME:-$HOME/.codex}/skills/mobile-logo-system`

**Invocation:**

```text
Use $mobile-logo-system.

Study the current app, propose 3 stronger mobile-first icon directions, keep them consistent with the existing UI language, and tell me which one should move forward.
```

### Claude

Quick install into a Claude project:

```bash
python3 scripts/install_skill.py --claude-project /path/to/your/project
```

Symlink instead of copy:

```bash
python3 scripts/install_skill.py --claude-project /path/to/your/project --claude-mode link
```

This creates:
- a Claude wrapper at `.claude/skills/mobile-logo-system/SKILL.md`
- a vendor copy of the repo at `.claude/vendor/mobile-logo-system`

**Invocation:**

```text
/mobile-logo-system review the current app icon and propose a stronger Android adaptive + monochrome path
```

### Both at once

```bash
python3 scripts/install_skill.py --codex --claude-project /path/to/your/project
```

### Upgrading

Rerun with `--force` to overwrite an existing install:

```bash
python3 scripts/install_skill.py --codex --force
```

The installer shows the version transition and warns about major upgrades.

### Using this repo directly

If you opened this repository as a Claude project, the skill is already available via `/mobile-logo-system`. No installation needed.

For Codex, load `SKILL.md` as the main skill entrypoint and `agents/openai.yaml` as metadata.

## Production Package

Scaffold a handoff package:

```bash
python3 scripts/init_logo_system_package.py /path/to/logo-system --project-name "Project Name"
```

Options:

```bash
python3 scripts/init_logo_system_package.py /path/to/logo-system \
  --project-name "Project Name" \
  --owner "Brand Team" \
  --date "2026-04-07"
```

This creates review files, rationale files, iOS/Android notes, monochrome notes, and an export checklist.

## Repository Structure

```text
mobile-logo-system/
├── SKILL.md                           # canonical skill entrypoint
├── README.md
├── CHANGELOG.md
├── MIGRATION.md
├── LICENSE
├── .github/
│   └── workflows/
│       └── ci.yml                     # repo validation + installer smoke tests
├── .claude/
│   └── skills/
│       └── mobile-logo-system/
│           └── SKILL.md               # Claude wrapper
├── agents/
│   └── openai.yaml                    # Codex UI metadata
├── references/
│   ├── color-system.md                # color harmonies, accessibility, gradient rules
│   ├── concept-quality.md             # stronger concept generation and critique
│   ├── context-testing.md             # mandatory mockup contexts, competitor proximity
│   ├── evaluation.md                  # scoring matrix, rejection triggers
│   ├── example-requests.md            # realistic request patterns
│   ├── example-responses.md           # gold-standard answer shape
│   ├── geometric-craft.md             # construction grids, optical corrections, pixel alignment
│   ├── live-research.md               # up-to-date official and research watchlists
│   ├── package-spec.md                # final deliverables spec
│   ├── premium-craft.md               # negative space, material language, longevity
│   ├── production-resources.md        # scaffolding and handoff file guidance
│   ├── project-audit.md               # project-first alignment and redesign tolerance
│   ├── prompt-library.md              # 8 ready-to-use prompts for common scenarios
│   ├── round-types.md                 # when to run flat/material/monochrome rounds
│   ├── sources.md                     # source map and authority order
│   ├── typography-craft.md            # type pairing, kerning, lockup construction
│   └── workflow.md                    # full 11-phase production workflow
├── assets/
│   └── package-template/
│       ├── reviews/                   # project-style-snapshot, concept-scorecard, reduction-checks
│       └── selected/                  # rationale, wordmark, iOS/Android/monochrome notes, export checklist
└── scripts/
    ├── install_skill.py               # install into Codex and/or Claude projects
    ├── init_logo_system_package.py    # scaffold handoff package from templates
    ├── validate_skill_repo.py         # validate repo structure and relative links
    └── smoke_test_installer.py        # installer smoke tests
```

## Versioning

This skill uses [semantic versioning](https://semver.org/):
- **major** — breaking changes to templates, evaluation matrix, or workflow phases
- **minor** — new reference files or capabilities without breaking existing packages
- **patch** — typos, wording, link fixes

Show the current version:

```bash
python3 scripts/install_skill.py --version
```

See [`CHANGELOG.md`](CHANGELOG.md) for what changed in each version.
See [`MIGRATION.md`](MIGRATION.md) for step-by-step upgrade instructions.

## Validation

```bash
python3 scripts/validate_skill_repo.py        # structure, links, version consistency
python3 scripts/smoke_test_installer.py        # installer smoke tests
python3 scripts/install_skill.py --help        # installer options
```

## Ready-To-Use Prompts

8 detailed prompts covering common scenarios: premium app from scratch, redesign of a generic icon, productivity tool, health/wellness, children's app, production audit, Android-first, and brand refresh with equity preservation.

Each prompt activates the appropriate workflow depth. Prompts work in both platforms and can be written in any language.

See the full prompt library: [`references/prompt-library.md`](references/prompt-library.md)

## Suggested Usage Pattern

1. ask it to inspect the current project first
2. let it verify live platform/store guidance when the task depends on freshness
3. ask for a first concept round with explicit evaluation
4. ask it to recommend the strongest direction and 2-3 concrete improvement moves
5. if hi-end: run the craft pass (geometric construction, color, typography, premium, context testing)
6. refine based on evaluation or craft pass findings
7. validate in real context (home screen, store listing, competitor row)
8. once a direction is validated, scaffold or fill the handoff package

## Compatibility

- **Python**: 3.9+
- **Platforms**: Codex (OpenAI), Claude (Anthropic)
- **OS**: macOS, Linux. Windows works but the default symlink install mode (`--codex-mode link`) may require Developer Mode or elevated permissions — use `--codex-mode copy` on Windows to avoid this.
- **CI**: tested on Ubuntu with Python 3.9 and 3.12
- **License**: [MIT](LICENSE)

## Canonical Files

- Main skill: [`SKILL.md`](SKILL.md)
- Codex metadata: [`agents/openai.yaml`](agents/openai.yaml)
- Claude wrapper: [`.claude/skills/mobile-logo-system/SKILL.md`](.claude/skills/mobile-logo-system/SKILL.md)
- Research and workflow references: [`references/`](references)
- Package templates: [`assets/package-template/`](assets/package-template)
- Utility scripts: [`scripts/`](scripts)
- Changelog: [`CHANGELOG.md`](CHANGELOG.md)
- Migration guide: [`MIGRATION.md`](MIGRATION.md)
- License: [`LICENSE`](LICENSE)
