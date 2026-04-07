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
├── .claude/
│   └── skills/
│       └── mobile-logo-system/
│           └── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── color-system.md
│   ├── concept-quality.md
│   ├── context-testing.md
│   ├── evaluation.md
│   ├── example-requests.md
│   ├── example-responses.md
│   ├── geometric-craft.md
│   ├── live-research.md
│   ├── package-spec.md
│   ├── premium-craft.md
│   ├── production-resources.md
│   ├── project-audit.md
│   ├── round-types.md
│   ├── sources.md
│   ├── typography-craft.md
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

Copy any prompt below and use it as-is with the skill. Each prompt is designed to activate the full hi-end workflow including craft pass, context testing, and production packaging.

### 1. Premium App From Scratch

```text
Use $mobile-logo-system.

I am building a premium sleep and recovery app for adults aged 25-45. The product
helps users build better sleep habits through personalized routines, ambient
soundscapes, and sleep quality tracking. The tone is calm, trustworthy, and quietly
luxurious — not clinical or gamified.

Do the following:
1. Research current Apple and Android icon guidance before starting.
2. Define 3 concept territories. Each must state the construction method
   (grid type, proportion system), color rationale with assigned roles,
   silhouette logic, and why it survives at 29px and in monochrome.
3. Score all 3 directions using the full evaluation matrix including
   geometric precision, color craft, context survival, and longevity.
4. Recommend one winner. Run the craft pass on it: verify optical corrections,
   negative space, tangent continuity, and color accessibility (WCAG, CVD).
5. Show the winner on an iOS home screen among 8 real competitor icons
   and in an App Store listing mockup.
6. Propose the wordmark: justify type classification, pairing logic,
   weight matching, and lockup construction.
7. Define the Android adaptive icon split and monochrome layer.
8. List 3 concrete improvement moves for the next refinement round.
```

### 2. Redesign a Generic Existing Icon

```text
Use $mobile-logo-system.

Our current app icon feels generic — it blends into the category and users
cannot find it on their home screen. The app is a personal finance tracker.

Do the following:
1. Audit the current icon and UI language in the project. Build a style snapshot:
   what is strong, what is weak, what is the redesign tolerance
   (evolutionary / adjacent / reset).
2. Identify specifically why the current icon is generic: category cliches used,
   silhouette uniqueness failure, color conformity.
3. Propose 3 directions — one evolutionary, one adjacent, one stretch.
   For each: state the construction grid, color harmony model, metaphor,
   and how it differentiates from the top 5 competitors in the category.
4. Run a competitor row test: place each direction among 7 real fintech
   app icons. Evaluate which stands out without losing category belonging.
5. Select the winner, run the full craft pass, and output the decision
   matrix with all 11 scoring dimensions.
6. Produce the monochrome variant and validate it under Android themed
   icon tinting with warm, cool, and neutral palettes.
```

### 3. Icon System for a Productivity Tool

```text
Use $mobile-logo-system.

Design a logo system for a project management app aimed at small creative teams.
The product is fast, minimal, and opinionated — it is not trying to be Jira.
The visual language is geometric, high-contrast, and uses a monospace typeface
in the UI.

Requirements:
1. The icon must feel native among developer and design tools
   (Figma, Linear, Notion, Arc) — not among enterprise software.
2. Propose 3 concept territories. Each must use a documented construction grid
   (show the grid, not just describe it). Explain overshoot corrections
   and pixel alignment at 48px and 29px.
3. Color palette must use a maximum of 2 colors in the mark. Justify the
   harmony model. Test grayscale and CVD (protanopia, deuteranopia).
4. The wordmark must use a contrast pairing with the symbol. Justify
   type classification, specify kerning adjustments for each letter pair.
5. Run the style-agnostic silhouette test: show the winner as flat fill,
   outline only, and cut-out. All three must be recognizable.
6. Place the icon on both iOS and Android home screens. Test with circular
   and rounded-square masks on Android.
7. Answer the 5-year durability question honestly.
```

### 4. Premium Health and Wellness App

```text
Use $mobile-logo-system.

Create a hi-end logo system for a women's health app focused on hormone tracking,
cycle insights, and holistic wellness. The brand must feel medically credible
but warm — not clinical, not generic wellness.

Key constraints:
- Must avoid: generic leaf, generic heart, pink-only palette, soft blob shapes
  (these are category cliches).
- Must feel: precise yet human, premium without being cold, science-backed
  without being sterile.
- Premium positioning is mandatory: quiet luxury, not loud branding.

Workflow:
1. Research current competitors in the category. Map the cliche landscape:
   what shapes, colors, and metaphors are overused.
2. Define 4 concept territories that deliberately avoid cliches.
   Each must state: construction method, color roles (primary/secondary/accent),
   metaphor, emotional job, primary risk, and longevity assessment.
3. Score using the full matrix. Reject any direction that fails the
   style-agnostic silhouette test or would look dated in 3 years.
4. Run the craft pass on the winner: geometric grid, optical corrections,
   negative space audit (fill counterforms with color — are they deliberate?),
   tangent continuity (G1 minimum), path cleanliness.
5. Define the color system: contrast ratios, CVD simulation, gradient-to-flat
   and gradient-to-monochrome fallbacks.
6. Wordmark: choose a typeface that signals medical credibility without
   clinical coldness. Justify the pairing. Construct horizontal and
   stacked lockups with measured proportions.
7. Context test: iOS home screen (light + dark + photo wallpaper),
   App Store listing, Settings at 29pt, competitor row of 7 icons.
8. Android adaptive icon: foreground/background split, safe-zone discipline,
   monochrome layer with intentional simplification.
9. Prepare the full handoff package.
```

### 5. Children's Educational App

```text
Use $mobile-logo-system.

Design a logo and icon system for a children's reading app (ages 4-8).
Parents choose the app, children use it. The icon must appeal to both:
trustworthy and smart for parents, fun and inviting for kids.

Constraints:
- Must survive without relying on a character or mascot (the icon must work
  as geometry, not illustration).
- Maximum 3 colors. Must pass CVD simulation — children with color vision
  deficiency must still recognize the icon.
- Must work at 29px — children's app icons are often shown in parental
  control lists at small sizes.

Steps:
1. Audit the category: what do top children's education apps look like?
   Where is the white space for differentiation?
2. Define 3 territories. For each: metaphor, construction grid,
   color roles with accessibility rationale, reduction rule at 29px.
3. Score and select. The winner must pass: small-size test, monochrome test,
   CVD test, and the "would a parent trust this?" test.
4. Run the craft pass. Pay special attention to corner radius progression
   (children's apps often use generous radii — make this intentional, not random).
5. Wordmark: choose a typeface that is friendly but not babyish.
   Parents should not feel embarrassed to have this on their phone.
6. Context test: place among real children's app icons on a home screen.
   Also test in the App Store "Kids" category listing.
7. Android monochrome: verify the shape reads clearly under Material You tinting.
8. Prepare the handoff package with all platform variants.
```

### 6. Quick Audit and Production Fix

```text
Use $mobile-logo-system.

Audit the current logo system in this project and tell me if it is actually
ready to ship. Do not redesign anything — just evaluate what exists.

Check:
1. Reduction: test at 1024px, 180px, 120px, 60px, 48px, 29px.
   Log what survives, what collapses, what is optional.
2. Geometric craft: is the mark built on a grid? Are optical corrections
   applied? Are there tangent breaks or unnecessary anchor points?
3. Color: are contrast ratios sufficient? Does grayscale conversion
   preserve hierarchy? Does the palette survive CVD simulation?
4. Monochrome: does the Android monochrome layer exist?
   Is it a deliberate design or an auto-derived grayscale?
5. Context: place the icon on an iOS and Android home screen among
   real competitors. Does it stand out? Does it belong?
6. Longevity: run the style-agnostic silhouette test (flat, outline, cut-out).
   Is the identity structural or effect-dependent?
7. Wordmark: is the pairing justified? Is kerning correct at logo scale?
8. Package completeness: list every deliverable as pass / revise / missing.

Output a prioritized punch list ordered by shipping risk.
Do not suggest a redesign unless something is fundamentally broken.
```

### 7. Android-First With Monochrome Focus

```text
Use $mobile-logo-system.

We are shipping an Android-first utility app (file manager / system tool category).
The icon must be optimized for Android adaptive icons and Material You theming.
iOS is secondary but must work.

Priority order:
1. The monochrome / themed icon layer is the primary deliverable, not an afterthought.
   Design it first: a single-color silhouette that carries the full identity.
2. Build the full-color version from the monochrome foundation, not the other way around.
3. Foreground/background split: the foreground must survive all mask shapes
   (circle, squircle, rounded square, teardrop). Test parallax shift (+/- 4dp).
4. Construction: use a grid that maps cleanly to 48dp (mdpi) and 108dp canvas.
   Show the safe zone (72dp). Apply optical corrections.
5. Color: maximum 2 colors on the foreground layer. The background must be a single
   flat color that works with all system mask shapes.
6. Test the monochrome icon under 5 different Material You palettes
   (warm red, cool blue, neutral gray, earth green, vibrant purple).
7. Context: Android launcher with circular mask, launcher with squircle mask,
   themed icon row, notification bar silhouette.
8. iOS adaptation: adjust the composition for the squircle mask. Verify at 29pt.
9. Wordmark: only if needed. The app name in the launcher is usually sufficient
   for utility apps.
```

### 8. Brand Refresh With Equity Preservation

```text
Use $mobile-logo-system.

Our app has 2M+ active users. The current icon is recognizable but looks dated —
it was designed 4 years ago and relies on gradients and glow effects that feel
like a previous design era.

Critical constraint: users must still find their app on the home screen after
the update. The silhouette must remain recognizable. The refresh is evolutionary,
not a reset.

Steps:
1. Audit the current mark. Document: what is the recognizable silhouette?
   What elements are carrying the identity (shape, color, internal structure)?
   What elements are purely stylistic (gradients, shadows, effects)?
2. Separate structural identity from stylistic treatment:
   render the current icon as a flat single-color fill. This is the equity
   that must survive.
3. Propose 3 evolutionary refinements. Each must:
   - preserve the core silhouette within a recognizability threshold
   - remove dated stylistic elements
   - improve geometric construction (rationalize freehand curves onto a grid)
   - improve small-size survival (remove detail that clogs at 29px)
   - modernize without chasing the current trend
4. Score using the full matrix. Add a specific "recognizability preservation"
   criterion: would an existing user find this icon after the update?
5. Run the craft pass on the winner: grid construction, optical corrections,
   negative space, color accessibility, path cleanliness.
6. Context test: show old and new icons side by side on a home screen.
   The transition should feel like the same brand evolved, not a different app.
7. Define the monochrome path. If the old icon never had one, explain
   what simplification was required.
8. Prepare the handoff package with before/after comparison notes.
```

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
