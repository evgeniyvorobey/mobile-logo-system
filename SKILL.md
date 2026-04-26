---
name: mobile-logo-system
version: 2.6.0
description: Use when creating or refining a mobile-first logo system that includes a brand mark, wordmark, iOS app icon, Android adaptive icon, monochrome/themed icon, and shipping-ready asset package. Best for research-backed app branding work that must inspect the current project or brand first, stay current with platform and logo/icon guidance, and generate strong concepts, critique, and refinement.
---

# Mobile Logo System

A compact brand director + mobile icon production workflow. Not a generic logo-prompt skill.

## When To Use

Use when the user wants: a new mobile logo or app icon, refinement of an existing mark, logo concepts for an app/startup/product, flat/material/monochrome iterations, an adaptive icon package, a wordmark paired with a symbol, evaluation of directions, or a production-ready export.

Do not use for: general illustration without mobile-icon constraints, brand strategy with no logo deliverable, one-off decorative graphics.

## Output Contract

Every response must include: `Mode:`, `Platform scope:`, `Assumptions:`, `Known facts:` vs `Recommendations:`, accessibility/legibility considerations, `Next actions:`.

When the task is design production, create or update artifacts. When a handoff package is needed, read [references/production-resources.md](references/production-resources.md) and scaffold with `python3 scripts/init_logo_system_package.py`.

## Workflow

Full workflow details: [references/workflow.md](references/workflow.md)

### 1. Classify the request

Choose one mode: concept generation, concept review, concept refinement, asset packaging, export/readiness audit.

#### Quality tier

**Standard** (default) — 7-dimension evaluation, reduction/monochrome checks, basic platform validation.

**Hi-end** — full craft pipeline: geometric construction, color audit, typography craft, premium craft, context testing, longevity, motion. 11-dimension matrix.

Hi-end triggers: user requests premium/craft-level quality, premium/luxury brand, large user base, store optimization priority, specific craft step references.

State the chosen tier in the first response. Can upgrade mid-workflow.

### 2. Audit the current project

Read [references/project-audit.md](references/project-audit.md). Inspect local files, screenshots, UI, icons, brand assets before proposing directions. Extract: product personality, visual language, logo equity, redesign tolerance. If recognizable visual language exists, first concept family must stay compatible.

### 3. Build context

Extract: product category, audience, emotional territory, competitive landscape, premium intent, primary surfaces, deliverable scope (symbol-only / wordmark-only / full system). Preserve user's existing direction unless they ask for a reset.

### 4. Separate the deliverables

Never collapse into one blob: brand mark, wordmark, iOS icon, Android adaptive, Android monochrome, store presentation. Same concept can drive all, but each surface has different constraints.

### 5. Follow source priority

Read [references/live-research.md](references/live-research.md) and [references/sources.md](references/sources.md). Order: (1) project audit, (2) platform docs, (3) HCI research, (4) premium research if relevant, (5) market scan, (6) inspiration galleries last. Platform constraints win over project style. Project truth wins over inspiration.

### 6. Generate concept territories

When the brief asks for more variety, more creativity, a less generic mark, or a reset, read [references/creative-divergence.md](references/creative-divergence.md) first. Run a short 8-12 seed divergence pass, then shortlist.

Define 3-5 territories before variants. Each: core metaphor, emotional job, brand fit, mobile fit, primary risk, silhouette logic, 60px/29px survival, evolutionary/adjacent/reset stance. Cover meaning, silhouette topology, construction method, and platform priority — not only visual style. Keep short if user wants immediate visuals, but do not skip.

### 7. Present concepts and wait for user selection

**Mandatory gate. Do not self-select a winner.**

**7a.** Produce **up to 5** marks (SVG or Pencil frame — schematic-level geometry sufficient). Each: one-line name, territory, brief rationale, primary risk. Read [references/concept-quality.md](references/concept-quality.md). Cover: one project-aligned, one distinctive, one stretch (if brief allows). No wordmarks, lockups, full color systems, or production files.

**7b.** State strongest direction (one sentence). **Ask user to choose.** Do not proceed until they respond.

### 8. Produce rounds

After user selects: (1) iterative refinement, (2) craft pass, (3) flat round if useful, (4) material/premium if useful, (5) monochrome if useful, (6) motion if warranted, (7) package. See [references/round-types.md](references/round-types.md).

### 9. Craft pass (hi-end only)

> Standard tier skips to step 10. **Load craft files only at this step.**

Read and run checklists: [geometric-craft.md](references/geometric-craft.md), [color-system.md](references/color-system.md), [typography-craft.md](references/typography-craft.md), [premium-craft.md](references/premium-craft.md), [context-testing.md](references/context-testing.md).

Output: corrections made, remaining risks, updated mark.

### 10. Evaluate

Read [references/evaluation.md](references/evaluation.md). Must survive: small-size reduction, monochrome, dark/light backgrounds, shape memory, category cliché comparison. Reject if: needs effects to work, collapses at 60px/29px, generic, wrong emotional tone, can't become Android adaptive icon.

### 11. Validate in context

> Full protocol: hi-end. Standard: verify 60px/29px, one home screen (light+dark), monochrome survival.

Read [references/context-testing.md](references/context-testing.md). Test: iOS/Android home screens, store listings, Settings/29pt, notification bar, splash screen, competitor row (5-7 icons).

### 12. Improve or question

Identify strongest direction, its weakest point, 2-3 improvement moves. Ask only high-leverage questions. Proceed with labeled assumptions when answers unavailable.

### 13. Motion (optional, hi-end recommended)

Launch transition, loading states, micro-interactions. Outer silhouette stable — animation inside. Mark must work without motion.

### 14. Package

Read [references/package-spec.md](references/package-spec.md). Include: rationale, mark + wordmark notes, iOS/Android/monochrome guidance, export checklist, unresolved risks.

## Tooling

- **Pencil/.pen**: new rounds in separate frames, verify with screenshots
- **Figma**: when user provides Figma URL or expects design system alignment
- **Image generation**: mood/exploration only, not final masters
- **Production package**: [references/production-resources.md](references/production-resources.md), scaffold with `init_logo_system_package.py`
- **Web research**: when platform guidance may have changed, premium claims need grounding, store behavior matters
- **Local files**: always search project first for logos, design boards, icons, UI screenshots, color tokens, typography

## Bilingual Policy

Reply in user's language. Keep source titles in original language. Prefer English labels with localized explanatory copy for reusable artifacts.

## Progressive Disclosure

Load only when needed:
- [references/sources.md](references/sources.md) — source map
- [references/live-research.md](references/live-research.md) — research watchlists
- [references/project-audit.md](references/project-audit.md) — project alignment
- [references/workflow.md](references/workflow.md) — full workflow
- [references/production-resources.md](references/production-resources.md) — handoff files
- [references/creative-divergence.md](references/creative-divergence.md) — broad idea range
- [references/concept-quality.md](references/concept-quality.md) — concept critique
- [references/evaluation.md](references/evaluation.md) — scoring
- [references/package-spec.md](references/package-spec.md) — deliverables
- [references/round-types.md](references/round-types.md) — specialized rounds
- [references/geometric-craft.md](references/geometric-craft.md) — step 9 only
- [references/color-system.md](references/color-system.md) — step 9 only
- [references/typography-craft.md](references/typography-craft.md) — step 9 only
- [references/context-testing.md](references/context-testing.md) — step 9 only
- [references/premium-craft.md](references/premium-craft.md) — step 9 only

## Hard Constraints

Do not:
- invent official platform rules or current store behavior without checking live sources
- claim shipping readiness without reduction checks and context testing
- choose a winner based on aesthetics alone
- treat wordmark and app icon as interchangeable
- rely on raster tracing as the final identity method
- skip Android monochrome/themed icon considerations
- skip export planning when a real package is requested
- fake diversity by changing only color, effects, or minor styling
- overproduce variants without narrowing the decision space
- self-select a winning concept — present options and wait for user's choice
- generate wordmarks, lockups, production files before user confirms direction in step 7b
- load craft files (geometric, color, typography, premium, context) before step 9
- ignore existing design system without saying so explicitly
- ask broad questions when a labeled assumption suffices
- present geometry without construction method
- present colors without roles and monochrome fallbacks
- skip craft pass on hi-end work
- use effects to rescue a weak silhouette
- treat negative space as leftover
- present wordmark without type classification and pairing logic
- declare premium without passing silhouette test

## Success Criteria

### Both tiers
Brand-correct, mobile-correct, project-aligned, research-backed, reduction-safe (60px/29px), platform-aware, explainable, package-ready.

### Hi-end (additional)
Geometrically constructed, color-rationalized, context-validated, typography-crafted, premium-verified.

### Failure signals
Fails at 60px or Android monochrome → failed. Disappears on real home screen → failed. Depends on effects for identity → failed. Freehand geometry → not hi-end.
