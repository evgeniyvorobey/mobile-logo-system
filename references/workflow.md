# Workflow

Full reusable workflow for mobile logo system work.

## Quality Tiers

- **Standard** — Phases 1-6 (user gate), 7, 8 (optional), 9, 11. Skips craft pass, full context testing, motion. 7-dimension evaluation.
- **Hi-end** — All phases including 7.5 (craft pass), full context testing, Phase 10 (motion). 11-dimension evaluation.

Both tiers require Phase 6 (user selection). The skill must never self-select a winner.

Default to standard. See SKILL.md step 1 for tier triggers.

## Phase 1. Discovery

Collect: product name, category, audience, emotional job, usage surfaces, premium vs mass-market, existing assets.

Output: concise brief, constraints, anti-goals.

## Phase 2. Constraint Mapping

Separate deliverables: symbol, wordmark, iOS icon, Android adaptive, Android monochrome, store presentation.

Smallest critical size: `60px` and `29px` as mandatory checkpoints.

## Phase 3. Source Review

Read `sources.md`. Pull: Apple icon guidance, Android adaptive guidance, one HCI source, one premium source if relevant.

Output: research synthesis, constraints, inferences.

## Phase 4. Territory Definition

Generate 3-5 concept territories. Each: name, metaphor, emotional promise, brand fit, mobile fit, risk.

## Phase 5. Core Concepts

Up to 5 concepts — **mark only** (simple schematic SVG or Pencil frame). No wordmarks, lockups, or production files.

Each: mark visual, essential shape logic, risk, small-size survival (60px/29px).

## Phase 6. User Selection (mandatory gate)

1. Brief evaluation summary (matrix or scores).
2. State strongest direction (one sentence).
3. **Ask user to choose.** Do not proceed until they respond.

## Phase 7. Iterative Refinement

Refine chosen concept: tighten silhouette, reduce primitives, rebalance negative space, improve small-size survival, check distinctiveness.

## Phase 7.5. Craft Pass (Hi-end Only)

> Standard tier: skip to Phase 8.

Load craft files **only at this phase**. Run each checklist:

- [geometric-craft.md](geometric-craft.md) — grid, proportions, optical corrections, pixel alignment
- [color-system.md](color-system.md) — roles, contrast, CVD, gradient fallbacks, monochrome
- [typography-craft.md](typography-craft.md) — classification, pairing, weight, kerning, lockups
- [premium-craft.md](premium-craft.md) — negative space, fill ratio, light, focal point, longevity
- [context-testing.md](context-testing.md) — home screens, store listings, competitor row

Output: corrections made, remaining risks, updated mark.

## Phase 8. Optional Specialized Rounds

Only when useful:
- **Flat**: prove core-shape strength without surface treatment
- **Material/premium**: when brand benefits from tactility
- **Monochrome**: Android themed icons, low-color surfaces

See `round-types.md`.

## Phase 9. Packaging

Use `package-spec.md`. Include: rationale, master mark, wordmark guidance, iOS/Android/monochrome notes, export checklist, unresolved risks.

## Phase 10. Motion (Hi-end Only)

> Optional even for hi-end. Recommended for premium brands.

Consider: launch transition, loading states, micro-interactions. Outer silhouette stable — animation inside. Mark must work fully without motion.

## Phase 11. Final Review

- Re-check: small-size, monochrome, context placement, brand fit.
- Note what remains unverified.

### Hi-end additional
- Craft pass results reflected in final mark
- Competitor row passed
- Geometric construction documented
- Color accessibility confirmed

Not ready if: only works enlarged, glossy, or explained. Not ready if context testing not passed.
