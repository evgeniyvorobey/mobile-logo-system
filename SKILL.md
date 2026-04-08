---
name: mobile-logo-system
version: 2.4.1
description: Use when creating or refining a mobile-first logo system that includes a brand mark, wordmark, iOS app icon, Android adaptive icon, monochrome/themed icon, and shipping-ready asset package. Best for research-backed app branding work that must inspect the current project or brand first, stay current with platform and logo/icon guidance, and generate strong concepts, critique, and refinement.
---

# Mobile Logo System

Use this skill for mobile-first brand identity work where the output must survive real product constraints, not just look good on a white canvas.

This skill is optimized for:
- logo + wordmark systems
- iOS app icons
- Android adaptive icons
- monochrome/themed icon variants
- premium or brand-heavy mobile products
- bilingual design rationale and handoff

This is not a generic logo-prompt skill.
It should behave like a compact brand director + mobile icon production workflow.

## When To Use

Use this skill when the user wants any of the following:
- a new mobile logo or app icon
- refinement of an existing mobile mark
- logo concepts for an app, startup, or product brand
- flat/material/monochrome iterations
- an adaptive icon package for Android
- a wordmark paired with a mobile brand symbol
- evaluation of which logo direction should move forward
- a production-ready export and QA checklist

Do not use this skill for:
- general illustration or mascot design without mobile-icon constraints
- brand strategy with no logo/icon deliverable
- one-off decorative graphics that will not live as app icons or identity assets

## Output Contract

Every response produced with this skill must:
- start with `Mode:`
- include `Platform scope:`
- include `Assumptions:`
- distinguish `Known facts:` from `Recommendations:`
- include accessibility or legibility considerations by default
- end with `Next actions:`

When the task is design production, the skill should create or update artifacts, not just discuss them.

When a reusable handoff package is needed:
- read [references/production-resources.md](references/production-resources.md)
- prefer the bundled package templates over ad hoc file naming
- scaffold files when useful instead of leaving the package implied

## Workflow

### 1. Classify the request

Choose exactly one primary mode:
- concept generation
- concept review
- concept refinement
- asset packaging
- export/readiness audit

#### Quality tier

Determine the quality tier for this task:

**Standard** — solid, production-aware work. Covers concept territories, 7-dimension evaluation (Distinctive, Small size, Brand fit, Premium, Monochrome, Platform, Wordmark), reduction and monochrome checks, basic platform validation. Suitable for most requests.

**Hi-end** — full craft pipeline. Adds geometric construction pass, color system audit, typography craft, premium craft, comprehensive context testing, longevity assessment, and motion consideration. Uses the full 11-dimension evaluation matrix.

Default to **standard** unless any of these triggers are present:
- the user explicitly requests hi-end, premium, production-ready, or craft-level quality
- the brand is positioned as premium, luxury, or craft-sensitive
- the product has a large established user base
- store optimization or competitive differentiation is a stated priority
- the user references specific craft steps (geometric grid, color accessibility, typography craft)

The tier can be upgraded mid-workflow if the work evolves. State the chosen tier in the first response.

### 2. Audit the current project before ideation

Read [references/project-audit.md](references/project-audit.md) first whenever local files, screenshots, UI, icons, brand assets, or prior explorations are available.

Always inspect the project before proposing a new visual direction.

Extract or infer:
- current product personality
- visual language already in use
- existing logo/icon equity
- whether the redesign should be evolutionary, adjacent, or a reset
- what must stay recognizable
- what is currently weak or inconsistent

Default rule:
- if the project already has a recognizable visual language, the first concept family must stay compatible with it
- only propose a stylistic reset as an explicit alternative lane

### 3. Build context before drawing

Extract or infer:
- product category
- target audience
- emotional territory
- competitive landscape
- premium or non-premium intent
- where the mark will appear most often
- whether the deliverable is symbol-only, wordmark-only, or full system

If a user already has a direction, preserve its intent unless they ask for a reset.

### 4. Treat the deliverables as separate surfaces

Never collapse these into one blob:
- brand mark
- wordmark
- iOS app icon
- Android adaptive icon
- Android monochrome/themed icon
- store presentation render

The same concept can drive all of them, but each surface has different constraints.

### 5. Follow the source priority

Read [references/live-research.md](references/live-research.md) and [references/sources.md](references/sources.md) early.

Use this discovery order:
1. internal brand/product context and current project audit
2. official platform and store documentation
3. perception and HCI research
4. premium/luxury perception research when relevant
5. market scan and competitor patterns
6. inspiration galleries only after the above

Never let Dribbble/Behance/Pinterest become the source of truth.

Conflict rule:
- if current project style and platform shipping constraints disagree, platform constraints win
- if inspiration and project truth disagree, project truth wins

### 6. Generate concept territories first

Before sketching variants, define 3-5 concept territories.

Each territory must state:
- core metaphor
- emotional job
- why it fits the brand
- why it fits mobile icon constraints
- primary risk
- silhouette logic
- why it should still work at `60px` and `29px`
- whether it is evolutionary, adjacent, or reset relative to the current project

If the user asks for immediate visuals, keep the territory step short but do not skip it.

### 7. Present concepts and wait for user selection

This is a **mandatory gate**. Do not self-select a winner.

#### 7a. Generate visual concepts

Produce **up to 5** logo or app icon concepts — one per territory (or two for a strong territory).

For each concept show:
- the mark as an **SVG or Pencil frame** — keep it simple, schematic-level geometry is sufficient
- a one-line name
- which territory it belongs to
- a brief rationale (2-3 sentences)
- the primary risk

Read [references/concept-quality.md](references/concept-quality.md) when generating concepts.

The concept set should cover purposeful range:
- one project-aligned or evolutionary direction
- one direction that improves distinctiveness without breaking fit
- one stretch direction only if the brief or brand tolerance allows it

Avoid random variation in gradients only, corner radius only, minor internal decoration, or trivial color swaps presented as new concepts.

Do not generate wordmarks, lockups, color systems, full packages, or production files at this stage.

#### 7b. Stop and ask the user

After presenting the concepts:
1. State which direction you consider strongest and why (one sentence).
2. **Ask the user to choose** a direction or request changes.
3. **Do not proceed** to refinement, craft pass, or packaging until the user responds.

If the user asks for modifications to a concept, iterate on that concept and re-present before moving on.

### 8. Produce rounds intentionally

After the user selects a direction, the production order is:
1. iterative refinement of the chosen concept
2. craft pass (geometric, color, typography, premium, context)
3. only if useful: flat round
4. only if useful: material/premium round
5. only if useful: monochrome round
6. motion consideration (optional, recommended for premium)
7. package and export checklist

Do not force flat/material/monochrome rounds unless:
- the user asks for them
- the platform package requires them
- the current concept depends on surface effects to survive

### 9. Run a craft pass before finalizing

> **Hi-end tier only.** Standard tier skips this step — move directly to evaluation.
>
> **Load craft files only at this step** — do not read geometric-craft.md, color-system.md, typography-craft.md, premium-craft.md, or context-testing.md before the user has confirmed a direction in step 7b.

After the user has selected a direction and refinement is underway, run a dedicated craft pass.

Read [references/geometric-craft.md](references/geometric-craft.md), [references/color-system.md](references/color-system.md), [references/typography-craft.md](references/typography-craft.md), and [references/premium-craft.md](references/premium-craft.md).

The craft pass covers:
- geometric construction: verify or establish a grid, apply optical corrections, clean paths
- color craft: assign roles, check contrast ratios, test grayscale and CVD, define fallbacks
- typography craft: justify pairing, match weights, kern at logo scale, construct lockups
- premium craft: audit negative space, check fill ratio, verify light direction, run silhouette test
- context validation: place on real home screens, test at store listing scale, run competitor row

Output a list of corrections made and remaining craft risks.

The craft pass is what separates competent work from hi-end work.

### 10. Evaluate aggressively

Read [references/evaluation.md](references/evaluation.md) before selecting a direction.

A strong direction must survive:
- small-size reduction
- monochrome conversion
- dark and light backgrounds
- shape memory after brief exposure
- comparison with category clichés

Reject concepts that:
- need glow or gradients to work
- collapse at 60px or 29px
- look generic in category
- signal the wrong emotional tone
- cannot plausibly become an Android adaptive icon

### 11. Validate in real context

> **Full protocol is hi-end tier.** Standard tier: verify at 60px and 29px, test on one home screen (light and dark), confirm monochrome survival. Skip competitor row and full store listing mockups.

Read [references/context-testing.md](references/context-testing.md) before declaring any direction production-ready.

Every mark that advances past concept selection must be tested in:
- iOS and Android home screens (light and dark wallpapers, among real competitor icons)
- App Store and Google Play listing scale
- Settings / 29pt scale
- notification bar (if applicable)
- splash screen

Run a direct competitor row comparison: place the icon among 5-7 direct competitors.

A mark that looks great in isolation but fails on a home screen needs revision.

### 12. Improve or question before the next round

After presenting any concept set or review:
- identify the strongest direction
- identify the weakest point in that direction
- propose 2-3 concrete improvement moves
- ask only the smallest number of high-leverage questions needed for the next round

Questions are warranted when the answer could materially change the direction, such as:
- redesign tolerance: evolution vs reset
- whether an existing symbol must be preserved
- premium positioning is mandatory vs optional
- the icon must optimize for a specific store, market, or audience
- legal/trademark constraints are already known

If those answers are unavailable, proceed with labeled assumptions rather than blocking.

### 13. Consider motion (optional, hi-end recommended)

When the brand can benefit from animation, consider how the mark could animate:
- app launch transition (icon to splash screen)
- loading states (pulsing, rotating, morphing)
- micro-interactions within the product UI

Motion-ready principles:
- the mark should have a clear element hierarchy that can be animated sequentially
- the outer silhouette should be stable — animation should happen inside the silhouette
- the mark must work fully without animation — motion is an enhancement, never a requirement

Document which element could animate first, what kind of motion fits the brand, and any constraints.

Skip this step only when the user explicitly wants static-only output or the project does not warrant it.

### 14. Package for shipping

Read [references/package-spec.md](references/package-spec.md) before final handoff.

The final package must include:
- chosen concept rationale
- mark + wordmark usage notes
- iOS icon guidance
- Android foreground/background/monochrome guidance
- flat master if applicable
- export checklist
- unresolved risks

## Tooling Guidance

### Pencil / `.pen`

Use Pencil when the work should be created or reviewed inside an existing `.pen` design file.

Preferred behavior:
- keep prior design frames untouched unless explicitly asked to edit them
- create new concept rounds in separate frames
- verify each important round with screenshots
- export final review boards when useful

### Figma

Use Figma when the user provides a Figma URL, node, or expects alignment to an existing design system or brand workspace.

### Image generation

Use image generation only for broad exploration or mood support.
Do not treat generated raster outputs as final logo masters.
Final logo decisions must be validated as simplified vector-like forms.

### Production package resources

Use [references/production-resources.md](references/production-resources.md) when the user wants files, handoff, or a real package.

If the project does not already contain a handoff structure, scaffold one with:

`python3 scripts/init_logo_system_package.py /target/path/logo-system --project-name "Project Name"`

Then fill or update only the files that are warranted by the current task.

### Web research

Use browsing whenever:
- platform guidance might have changed
- the user asks for research
- direct citations or links help the handoff
- premium/perception claims need grounding
- store behavior or icon testing guidance matters
- the skill needs updated logo/icon guidance rather than stale memory

### Local files

Always search the local project first for:
- current logo explorations
- design boards
- app icon assets
- existing wordmarks
- product constraints

Also inspect when available:
- UI screenshots
- app store screenshots
- color tokens or brand variables
- typography choices
- existing motion or illustration style

If the product already has a clear design language, treat the logo/icon work as part of that system, not as an isolated art exercise.

## Bilingual Policy

This skill is bilingual.

Default behavior:
- reply in the user's language
- keep official source titles in their original language
- for reusable artifacts, prefer concise English labels with localized explanatory copy when helpful

If the user clearly wants one language only, follow that.

## Progressive Disclosure

Load the following only when needed:
- [references/sources.md](references/sources.md) for source map and authority order
- [references/live-research.md](references/live-research.md) for up-to-date official and research watchlists
- [references/project-audit.md](references/project-audit.md) for project-first alignment and redesign tolerance
- [references/workflow.md](references/workflow.md) for the full production workflow
- [references/production-resources.md](references/production-resources.md) for scaffolding and updating real handoff files
- [references/concept-quality.md](references/concept-quality.md) for stronger concept generation and critique
- [references/evaluation.md](references/evaluation.md) for scoring and rejection criteria
- [references/package-spec.md](references/package-spec.md) for final deliverables
- [references/round-types.md](references/round-types.md) for when to run flat/material/monochrome rounds
- [references/geometric-craft.md](references/geometric-craft.md) — load only at step 9 (craft pass), not before
- [references/color-system.md](references/color-system.md) — load only at step 9 (craft pass), not before
- [references/typography-craft.md](references/typography-craft.md) — load only at step 9 (craft pass), not before
- [references/context-testing.md](references/context-testing.md) — load only at step 9 (craft pass), not before
- [references/premium-craft.md](references/premium-craft.md) — load only at step 9 (craft pass), not before

## Hard Constraints

Do not:
- invent official platform rules
- invent current platform or store behavior without checking live sources when freshness matters
- claim shipping readiness without reduction checks
- claim shipping readiness without context testing (home screen, store listing)
- choose a winner based on aesthetics alone
- treat wordmark and app icon as interchangeable
- rely on raster tracing as the final identity method
- skip Android monochrome/themed icon considerations
- skip export planning when the user asks for a real package
- overproduce variants without narrowing the decision space
- self-select a winning concept without user confirmation — always present options and wait for the user's choice before proceeding to refinement or packaging
- generate wordmarks, lockups, color systems, full packages, or production files before the user has confirmed a direction in step 7b
- load geometric-craft.md, color-system.md, typography-craft.md, premium-craft.md, or context-testing.md before step 9
- ignore an existing design system and generate a disconnected brand direction without saying so explicitly
- ask broad, low-signal questions when a labeled assumption would be enough
- present concept geometry without stating the construction method
- present colors without assigning structural roles and defining monochrome fallbacks
- skip the craft pass on hi-end tier work
- use gradients, glow, or effects to rescue a weak silhouette
- treat negative space as leftover rather than designed
- present a wordmark without justifying type classification and pairing logic
- declare a mark premium without passing the style-agnostic silhouette test

## Success Criteria

### Both tiers

The output must be:
- brand-correct
- mobile-correct
- project-aligned when existing brand context is present
- research-backed when current guidance matters
- reduction-safe (survives 60px and 29px)
- platform-aware
- explainable
- package-ready

### Hi-end tier (additional)

The output must also be:
- geometrically constructed (built on a grid, not freehand)
- color-rationalized (roles assigned, accessibility checked, fallbacks defined)
- context-validated (tested on real home screens and store listings, competitor row passed)
- typography-crafted (pairing justified, kerned, lockups measured)
- premium-verified (negative space deliberate, silhouette test passed, longevity assessed)

### Failure signals

If the work looks stylish but would fail at 60px or in Android monochrome, it failed.
If the work looks good in isolation but disappears on a real home screen, it failed.
If the work depends on effects rather than structure for its identity, it failed.
If the geometry is freehand with no construction logic, it is not hi-end.
