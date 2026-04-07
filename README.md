# Mobile Logo System Skill

**Current version: 2.0.0** | [Changelog](CHANGELOG.md) | [Migration guide](MIGRATION.md)

A reusable AI skill for Codex and Claude that helps create, review, refine, and package mobile-first logo systems.

It is built for real app branding work, not generic logo prompting. The skill is designed to:

- inspect the current project before proposing new directions
- stay current with platform and store guidance
- generate stronger mobile logo and app icon concepts
- critique concepts and suggest focused improvements
- package chosen directions into reusable handoff artifacts

The skill is optimized for:

- brand mark + wordmark systems
- iOS app icons
- Android adaptive icons
- Android monochrome/themed icons
- premium or craft-sensitive app branding
- production-ready export and review packages

## What It Does

This skill behaves like a compact brand director for mobile products.

It does not just generate options. It is designed to:

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
- Geometric precision: construction grids, optical corrections, pixel alignment, tangent continuity
- Color system: harmony models, accessibility (WCAG, CVD), gradient rules, monochrome mapping
- Typography craft: type classification, symbol-type pairing, optical kerning, lockup construction
- Context testing: mandatory home screen, store listing, notification, and competitor proximity validation
- Premium craft: negative space mastery, material language, craftsmanship signals, longevity assessment
- Motion consideration for premium brands (launch, loading, micro-interactions)
- Production package scaffolding via [`scripts/init_logo_system_package.py`](scripts/init_logo_system_package.py)
- Repository validation via [`scripts/validate_skill_repo.py`](scripts/validate_skill_repo.py)

## Repository Structure

```text
mobile-logo-system/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── MIGRATION.md
├── .claude/
│   └── skills/
│       └── mobile-logo-system/
│           └── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── color-system.md          # color harmonies, accessibility, gradient rules
│   ├── concept-quality.md       # stronger concept generation and critique
│   ├── context-testing.md       # mandatory mockup contexts, competitor proximity
│   ├── evaluation.md            # scoring matrix (11 dimensions), rejection triggers
│   ├── example-requests.md      # realistic request patterns
│   ├── example-responses.md     # gold-standard answer shape
│   ├── geometric-craft.md       # construction grids, optical corrections, pixel alignment
│   ├── live-research.md         # up-to-date official and research watchlists
│   ├── package-spec.md          # final deliverables spec
│   ├── premium-craft.md         # negative space, material language, longevity
│   ├── production-resources.md  # scaffolding and handoff file guidance
│   ├── project-audit.md         # project-first alignment and redesign tolerance
│   ├── prompt-library.md        # 8 ready-to-use prompts for common scenarios
│   ├── round-types.md           # when to run flat/material/monochrome rounds
│   ├── sources.md               # source map and authority order
│   ├── typography-craft.md      # type pairing, kerning, lockup construction
│   └── workflow.md              # full 11-phase production workflow
├── assets/
│   └── package-template/
│       ├── reviews/             # project-style-snapshot, concept-scorecard, reduction-checks
│       └── selected/            # rationale, wordmark, iOS/Android/monochrome notes, export checklist
└── scripts/
    ├── install_skill.py         # install into Codex and/or Claude projects
    ├── init_logo_system_package.py  # scaffold handoff package from templates
    ├── validate_skill_repo.py   # validate repo structure and relative links
    └── smoke_test_installer.py  # installer smoke tests
```

## Quick Install From Terminal

If you want to install directly from this repository via terminal, use:

```bash
python3 scripts/install_skill.py --codex
```

To install into a Claude project:

```bash
python3 scripts/install_skill.py --claude-project /path/to/your/project
```

To install into both at once:

```bash
python3 scripts/install_skill.py --codex --claude-project /path/to/your/project
```

Useful options:

```bash
python3 scripts/install_skill.py --codex --codex-mode copy
python3 scripts/install_skill.py --claude-project /path/to/your/project --claude-mode link
python3 scripts/install_skill.py --codex --claude-project /path/to/your/project --force
```

Fresh clone example:

```bash
git clone <REPO_URL>
cd mobile-logo-system
python3 scripts/install_skill.py --codex --claude-project /path/to/your/project
```

Defaults:

- Codex install path: `${CODEX_HOME:-$HOME/.codex}/skills/mobile-logo-system`
- Codex install mode: `link`
- Claude install mode: `copy`
- Claude wrapper path: `/path/to/project/.claude/skills/mobile-logo-system/SKILL.md`
- Claude vendor path: `/path/to/project/.claude/vendor/mobile-logo-system`

## Install In Codex

### Option 1: Copy into your local Codex skills directory

Copy this repository to:

```text
${CODEX_HOME:-$HOME/.codex}/skills/mobile-logo-system
```

Example:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R /path/to/mobile-logo-system "${CODEX_HOME:-$HOME/.codex}/skills/mobile-logo-system"
```

Or use the installer:

```bash
python3 scripts/install_skill.py --codex
```

After that, Codex can use the canonical skill entrypoint:

- [`SKILL.md`](SKILL.md)

And the Codex UI metadata:

- [`agents/openai.yaml`](agents/openai.yaml)

### Option 2: Keep it as a repo and point Codex at it

If you already manage skills as repositories, keep this repo where you want it and load:

- `SKILL.md` as the main skill entrypoint
- `agents/openai.yaml` as the Codex UI metadata

For a standalone copied install instead of a symlink:

```bash
python3 scripts/install_skill.py --codex --codex-mode copy
```

### Typical Codex Invocation

```text
Use $mobile-logo-system.

Study the current app, propose 3 stronger mobile-first icon directions, keep them consistent with the existing UI language, and tell me which one should move forward.
```

## Install In Claude

### Option 1: Project-local Claude skill

This repository includes a Claude-compatible wrapper at:

- [`.claude/skills/mobile-logo-system/SKILL.md`](.claude/skills/mobile-logo-system/SKILL.md)

When this repository is opened as a Claude project, you can invoke it directly with:

```text
/mobile-logo-system
```

Or with a task inline:

```text
/mobile-logo-system review the current app icon and propose a stronger Android adaptive + monochrome path
```

### Option 2: Manual Claude skill install

Install into an existing Claude project with:

```bash
python3 scripts/install_skill.py --claude-project /path/to/your/project
```

This creates:

- a Claude wrapper at `.claude/skills/mobile-logo-system/SKILL.md`
- a vendor copy of the repo at `.claude/vendor/mobile-logo-system`

If you prefer a symlinked vendor install instead of a copied one:

```bash
python3 scripts/install_skill.py --claude-project /path/to/your/project --claude-mode link
```

If you rerun the install over an existing setup, use:

```bash
python3 scripts/install_skill.py --claude-project /path/to/your/project --force
```

## Production Package Scaffolding

When the user wants a real handoff package, scaffold one with:

```bash
python3 scripts/init_logo_system_package.py /path/to/logo-system --project-name "Project Name"
```

Useful options:

```bash
python3 scripts/init_logo_system_package.py /path/to/logo-system \
  --project-name "Project Name" \
  --owner "Brand Team" \
  --date "2026-04-07"
```

This creates a reusable package with:

- review files
- rationale files
- iOS notes
- Android adaptive notes
- monochrome notes
- export checklist

## Versioning

This skill uses [semantic versioning](https://semver.org/):
- **major** — breaking changes to templates, evaluation matrix, or workflow phases
- **minor** — new reference files or capabilities without breaking existing packages
- **patch** — typos, wording, link fixes

Show the current version:

```bash
python3 scripts/install_skill.py --version
```

When upgrading with `--force`, the installer shows the version transition and warns about major upgrades.

Scaffolded handoff packages include the skill version in `export-checklist.md` so each package remembers which version created it.

See [`CHANGELOG.md`](CHANGELOG.md) for what changed in each version.
See [`MIGRATION.md`](MIGRATION.md) for step-by-step upgrade instructions.

## Validation

Validate the repository structure and relative links with:

```bash
python3 scripts/validate_skill_repo.py
```

Run installer smoke tests with:

```bash
python3 scripts/smoke_test_installer.py
```

Show installer help with:

```bash
python3 scripts/install_skill.py --help
```

## Ready-To-Use Prompts

8 detailed prompts covering the most common scenarios: premium app from scratch, redesign of a generic icon, productivity tool, health/wellness, children's app, production audit, Android-first, and brand refresh with equity preservation.

Each prompt activates the full hi-end workflow: craft pass, context testing, geometric construction, color accessibility, and production packaging.

See the full prompt library: [`references/prompt-library.md`](references/prompt-library.md)

Prompts work in both platforms:
- Codex: `Use $mobile-logo-system.` followed by the prompt text
- Claude: `/mobile-logo-system` followed by the prompt text

The skill is bilingual — prompts can be written in any language.

## Suggested Usage Pattern

For best results, use the skill like this:

1. ask it to inspect the current project first
2. let it verify live platform/store guidance when the task depends on freshness
3. ask for a first concept round with explicit evaluation
4. ask it to recommend the strongest direction and 2-3 concrete improvement moves
5. run the craft pass (geometric construction, color, typography, premium, context testing)
6. refine based on craft pass findings
7. validate in real context (home screen, store listing, competitor row)
8. once a direction is validated, scaffold or fill the handoff package

## Canonical Files

- Main skill: [`SKILL.md`](SKILL.md)
- Codex metadata: [`agents/openai.yaml`](agents/openai.yaml)
- Claude wrapper: [`.claude/skills/mobile-logo-system/SKILL.md`](.claude/skills/mobile-logo-system/SKILL.md)
- Research and workflow references: [`references/`](references)
- Package templates: [`assets/package-template/`](assets/package-template)
- Utility scripts: [`scripts/`](scripts)
- Changelog: [`CHANGELOG.md`](CHANGELOG.md)
- Migration guide: [`MIGRATION.md`](MIGRATION.md)
