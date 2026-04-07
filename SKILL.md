---
name: mobile-logo-system
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

### 7. Produce rounds intentionally

The default production order is:
1. core concept round
2. selection
3. iterative refinement of 1 chosen concept
4. only if useful: flat round
5. only if useful: material/premium round
6. only if useful: monochrome round
7. package and export checklist

Do not force flat/material/monochrome rounds unless:
- the user asks for them
- the platform package requires them
- the current concept depends on surface effects to survive

### 8. Build stronger concept sets, not just more variants

Read [references/concept-quality.md](references/concept-quality.md) when generating or reviewing directions.

Every first-round concept set should cover purposeful range:
- one project-aligned or evolutionary direction
- one direction that improves distinctiveness without breaking fit
- one stretch direction only if the brief or brand tolerance allows it

Avoid random variation in:
- gradients only
- corner radius only
- minor internal decoration
- trivial color swaps presented as new concepts

### 9. Evaluate aggressively

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

### 10. Improve or question before the next round

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

### 11. Package for shipping

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
- [references/example-requests.md](references/example-requests.md) for realistic request patterns
- [references/example-responses.md](references/example-responses.md) for gold-standard answer shape and level of specificity

## Hard Constraints

Do not:
- invent official platform rules
- invent current platform or store behavior without checking live sources when freshness matters
- claim shipping readiness without reduction checks
- choose a winner based on aesthetics alone
- treat wordmark and app icon as interchangeable
- rely on raster tracing as the final identity method
- skip Android monochrome/themed icon considerations
- skip export planning when the user asks for a real package
- overproduce variants without narrowing the decision space
- ignore an existing design system and generate a disconnected brand direction without saying so explicitly
- ask broad, low-signal questions when a labeled assumption would be enough

## Success Criteria

This skill succeeds when the output is:
- brand-correct
- mobile-correct
- project-aligned when existing brand context is present
- research-backed when current guidance matters
- reduction-safe
- platform-aware
- explainable
- package-ready

If the work looks stylish but would fail at 60px or in Android monochrome, it failed.
