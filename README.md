# Mobile Logo System Skill

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
- Production package scaffolding via [`scripts/init_logo_system_package.py`](scripts/init_logo_system_package.py)
- Repository validation via [`scripts/validate_skill_repo.py`](scripts/validate_skill_repo.py)

## Repository Structure

```text
mobile-logo-system/
├── SKILL.md
├── README.md
├── .claude/
│   └── skills/
│       └── mobile-logo-system/
│           └── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── concept-quality.md
│   ├── evaluation.md
│   ├── example-requests.md
│   ├── example-responses.md
│   ├── live-research.md
│   ├── package-spec.md
│   ├── production-resources.md
│   ├── project-audit.md
│   ├── round-types.md
│   ├── sources.md
│   └── workflow.md
├── assets/
│   └── package-template/
│       ├── reviews/
│       └── selected/
└── scripts/
    ├── install_skill.py
    ├── init_logo_system_package.py
    └── validate_skill_repo.py
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
$CODEX_HOME/skills/mobile-logo-system
```

Example:

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R /path/to/mobile-logo-system "$CODEX_HOME/skills/mobile-logo-system"
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

## Validation

Validate the repository structure and relative links with:

```bash
python3 scripts/validate_skill_repo.py
```

Show installer help with:

```bash
python3 scripts/install_skill.py --help
```

## Suggested Usage Pattern

For best results, use the skill like this:

1. ask it to inspect the current project first
2. let it verify live platform/store guidance when the task depends on freshness
3. ask for a first concept round with explicit evaluation
4. ask it to recommend the strongest direction and 2-3 concrete improvement moves
5. once a direction is chosen, scaffold or fill the handoff package

## Canonical Files

- Main skill: [`SKILL.md`](SKILL.md)
- Codex metadata: [`agents/openai.yaml`](agents/openai.yaml)
- Claude wrapper: [`.claude/skills/mobile-logo-system/SKILL.md`](.claude/skills/mobile-logo-system/SKILL.md)
- Research and workflow references: [`references/`](references)
- Package templates: [`assets/package-template/`](assets/package-template)
- Utility scripts: [`scripts/`](scripts)
