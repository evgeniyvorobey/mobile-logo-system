# Workflow

This is the full reusable workflow for mobile logo system work.

## Quality Tiers

This workflow supports two tiers:

- **Standard** — Phases 1-6 (user gate), 7, 8 (optional), 9, 11. Skips craft pass, full context testing, and motion. Uses 7-dimension evaluation.
- **Hi-end** — All phases including 7.5 (craft pass), full context testing in Phase 11, and Phase 10 (motion). Uses 11-dimension evaluation.

Both tiers require Phase 6 (user selection) before proceeding. The skill must never self-select a winner.

Default to standard. See SKILL.md step 1 for tier selection triggers.

## Phase 1. Discovery

Collect:
- product name
- category
- user audience
- emotional job
- usage surfaces
- premium vs mass-market intent
- existing assets or legacy brand equity

Output:
- a concise brief
- constraints list
- anti-goals

## Phase 2. Constraint Mapping

Separate the deliverables:
- symbol
- wordmark
- iOS app icon
- Android adaptive icon
- Android monochrome/themed icon
- store presentation

Document the smallest critical size.
If no size is specified, treat `60px` and `29px` as mandatory reduction checkpoints.

## Phase 3. Source Review

Read official platform and research sources from `sources.md`.

At minimum, pull:
- Apple icon guidance
- Android adaptive icon guidance
- one HCI/perception source
- one premium/luxury source if “premium” matters

Output:
- a short research synthesis
- explicit constraints
- explicit inferences

## Phase 4. Territory Definition

Generate 3-5 concept territories.

Each territory must include:
- name
- metaphor
- emotional promise
- why it fits the brand
- why it fits mobile
- risk

Good territory examples:
- protected light
- ritual object
- folded page/moon
- crafted ember
- story sanctuary

Bad territory examples:
- generic leaf
- generic sparkle luxury
- generic mascot without brand reason

## Phase 5. Round 1 - Core Concepts

Create up to 5 concept directions. **At this stage: mark only — simple schematic SVG or Pencil frame. No wordmarks, lockups, color systems, or production files.**

For each:
- show the mark as a simple SVG (schematic-level geometry is sufficient)
- explain what is essential to the shape
- state the risk
- note small-size survival logic (how the shape reads at 60px and 29px)

Wordmarks, lockups, and production files are created only after the user selects a direction in Phase 6.

Goal:
- maximize concept diversity
- minimize random stylistic noise

## Phase 6. User Selection (mandatory gate)

**Present the concepts and wait for the user to choose.**

1. Show a brief evaluation summary (decision matrix or top-line scores).
2. State which direction you consider strongest and why (one sentence).
3. Ask the user to pick a direction or request changes.
4. **Do not proceed** to refinement until the user responds.

If the user requests modifications, iterate on the concept and re-present before moving on.

Do not select based only on “looks best”.
Do not self-select a winner and continue to packaging.

## Phase 7. Iterative Refinement

Refine the user's chosen concept.

Typical refinement loop:
1. tighten silhouette
2. reduce primitive count
3. rebalance internal negative space
4. improve small-size survival
5. check category distinctiveness

Refinement should be iterative, not a full restart.

## Phase 7.5. Craft Pass (Hi-end Only)

> Standard tier skips this phase entirely. Move from Phase 7 to Phase 8.

After the concept is refined but before specialized rounds, run a dedicated craft pass.

Read [geometric-craft.md](geometric-craft.md), [color-system.md](color-system.md), [typography-craft.md](typography-craft.md), and [premium-craft.md](premium-craft.md).

### Geometric Craft

1. verify or establish a construction grid (circle grid, square module, keyline)
2. align key vertices and curves to the grid
3. apply optical corrections:
   - overshoot for round and pointed shapes (2-8%)
   - visual center offset (3-5% upward)
   - horizontal stroke thinning (5-10%)
4. establish a corner radius scale and apply it consistently
5. verify tangent continuity at all curve junctions (G1 minimum)
6. clean vector paths: remove unnecessary anchor points
7. validate pixel alignment at critical raster sizes (29px, 60px, 120px)

### Color Craft

1. assign structural color roles (primary, secondary, accent)
2. verify area ratio (~60:30:10)
3. check contrast ratios (mark vs background >= 3:1, internal elements >= 2:1)
4. test grayscale conversion: does internal hierarchy survive?
5. simulate CVD (protanopia, deuteranopia minimum)
6. define gradient-to-flat and gradient-to-monochrome mappings
7. test on dark and light backgrounds

### Typography Craft (if wordmark is in scope)

1. justify type classification choice
2. justify pairing logic (contrast vs harmony)
3. verify visual weight match between symbol and wordmark
4. kern every letter pair at logo scale
5. construct horizontal and stacked lockups with measured proportions
6. define clear space as a function of cap-height
7. test wordmark legibility at minimum size

### Premium Craft

1. audit negative space: fill counterforms with color — are they deliberate shapes?
2. verify fill ratio (40-60% typical for hi-end)
3. check for single consistent light direction
4. confirm single focal point
5. count distinct visual elements (3-5 maximum in the mark)
6. verify stroke terminals are consistent
7. run style-agnostic silhouette test (flat, outline, cut-out)
8. answer the 5-year durability question

### Context Validation

1. place the mark on an iOS home screen (light and dark wallpaper)
2. place the mark on an Android home screen (test with multiple mask shapes)
3. show the mark at App Store / Google Play listing scale
4. test at Settings / 29pt scale
5. run a direct competitor row comparison (5-7 icons)

See [context-testing.md](context-testing.md) for the full context testing protocol.

Output from the craft pass:
- a list of corrections made
- a list of remaining craft risks
- updated mark with all corrections applied

## Phase 8. Optional Specialized Rounds

Run these only when useful:

- Flat round
  Use when the mark depends on surface treatment or must prove core-shape strength.

- Material/premium round
  Use when the brand genuinely benefits from tactility, warmth, or premium craft cues.

- Monochrome round
  Use whenever Android themed icons or low-color surfaces matter.

See `round-types.md`.

## Phase 9. Packaging

Prepare the shipping package using `package-spec.md`.

At minimum, package:
- chosen concept rationale
- master mark
- wordmark guidance
- iOS app icon notes
- Android adaptive icon notes
- monochrome icon notes
- export checklist
- unresolved risks

## Phase 10. Motion Consideration (Hi-end Only)

> Standard tier skips this phase. Optional even for hi-end but recommended for premium brands.

When the brand can benefit from animation, consider how the mark could animate:
- app launch transition (icon to splash screen)
- loading states (pulsing, rotating, morphing)
- micro-interactions within the product UI

Motion-ready principles:
- the mark should have a clear element hierarchy that can be animated sequentially
- the outer silhouette should be stable — animation should happen inside the silhouette, not change it
- the mark should work fully without animation — motion is an enhancement, never a requirement

Document:
- which element could animate first (the focal point)
- what kind of motion fits the brand (smooth ease, spring, linear, organic)
- constraints: the animated version must reduce to the static mark gracefully

Motion consideration is optional but recommended for premium brands. Skip it only when the user explicitly wants static-only output.

## Phase 11. Final Review

Before concluding:
- re-check small-size screenshots
- re-check monochrome viability
- re-check context placement (home screen, store listing)
- confirm the winner still matches the original brand job
- note what remains unverified

### Hi-end additional checks
- verify craft pass results are reflected in the final mark
- confirm competitor row comparison passed
- verify geometric construction is documented
- confirm color accessibility checks passed

If the design only works when enlarged, glossy, or explained, it is not ready.
If the design has not passed context testing (at tier-appropriate depth), it is not ready.
If the design has craft issues flagged but uncorrected (hi-end tier), it is not ready.
