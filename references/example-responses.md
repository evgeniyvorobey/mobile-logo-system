# Example Responses

Use this file to calibrate what a strong answer from this skill should look like.

These are not templates to copy blindly.
They are quality references for:
- structure
- level of specificity
- project-first reasoning
- live-research awareness
- critique and improvement behavior

Every real response should still adapt to the actual project, files, and brief.

## Example 1: Project-First Concept Generation

User request:
- "Study the current app and propose stronger icon and logo directions without breaking the product feel."

Strong response shape:

```text
Mode: concept generation
Platform scope: iOS + Android
Assumptions:
- No hard reset was requested, so I am treating this as an adjacent redesign rather than a full rebrand.
- The existing icon equity is worth preserving at a silhouette level, but not necessarily at the detail level.

Known facts:
- The current product UI uses rounded geometry, warm low-contrast gradients, and restrained typography.
- The existing icon feels polished but too generic in the wellness category because its outer silhouette reads as a familiar "soft glow" blob.
- Android adaptive and monochrome support are in scope, so the concept cannot depend on lighting effects alone.

Recommendations:
- I would explore three directions, each tied to the current product rather than inventing a disconnected visual language.

- Direction 1: Quiet Halo
  Type: evolutionary
  Core metaphor: protected calm
  Construction method: circle grid — three concentric circles (r, r*0.618, r*0.382) define the outer shell and inner cut
  Color rationale: monochromatic warm (primary: muted amber at 60% area, secondary: deep warm brown at 30%, accent: soft cream highlight at 10%). Analogous to current UI palette. Grayscale conversion preserves hierarchy through value contrast.
  Monochrome mapping: outer shell filled, inner cut as negative space — identity survives in one color.
  Why it fits the project: preserves the product's warm, rounded, reassuring tone
  Silhouette logic: one enclosing outer form plus one unmistakable inner cut
  60px/29px logic: the outer shape remains recognizable even if the internal cut simplifies
  Risk: may still feel too close to category wellness cliches unless the inner cut becomes more proprietary
  Longevity: structural — the identity lives in the circle-cut relationship, not in rendering style

- Direction 2: Folded Light
  Type: adjacent
  Core metaphor: a crafted fold that suggests care, ritual, and transition into rest
  Construction method: golden-ratio rectangle (1:1.618) as bounding box, fold angle at 23 degrees (derived from the diagonal of a 5:12 rectangle, echoing the UI card corner geometry). Key curves built from two related radii (r and r*phi).
  Color rationale: split-complementary (primary: warm terracotta at 55%, secondary: deep indigo at 35%, accent: soft gold at 10%). Internal hierarchy survives grayscale because terracotta and indigo have different luminance values. CVD-safe: tested under protanopia simulation — terracotta shifts but remains distinct from indigo through luminance.
  Monochrome mapping: fold reads as a single notch in the silhouette — shape carries identity without color.
  Why it fits the project: keeps the product's softness but introduces stronger shape memory
  Silhouette logic: asymmetrical outer contour with one directional fold cue
  60px/29px logic: the fold becomes a single decisive notch rather than a detailed crease
  Risk: if over-rendered, it will become premium decoration instead of strong icon geometry
  Longevity: structural — the fold is geometry, not a gradient trick. Style-agnostic silhouette test: passes in flat, outline, and cut-out.

- Direction 3: Lantern Mark
  Type: adjacent
  Core metaphor: contained warmth and guidance
  Construction method: square module grid (12x12), outer container anchored to grid intersections, centered core occupies a 4x4 inner zone. Optical corrections: container extends 3% below geometric baseline (overshoot for the flat bottom edge creates visual stability). Visual center shifted 4% upward.
  Color rationale: complementary (primary: deep teal at 50%, secondary: warm amber core at 35%, background: near-black at 15%). Contrast ratio mark-to-background: 5.2:1. Grayscale: teal and amber resolve to different gray values — hierarchy preserved. CVD: teal-amber pair survives deuteranopia (luminance-driven contrast).
  Monochrome mapping: container outline + solid core mass — reads as a lantern shape in one color.
  Why it fits the project: better distinctiveness while staying emotionally aligned with the current interface
  Silhouette logic: stable container plus a centered light core
  60px/29px logic: container remains primary, core simplifies to one contrasting mass
  Risk: can drift into finance or utility if the proportions become too severe
  Longevity: structural — container + core is archetypal, not trend-dependent.

Evaluation matrix (hi-end tier, all 11 dimensions):
| Direction    | Distinctive | Small size | Brand fit | Platform | Premium | Mono | Wordmark | Geometric | Color | Context | Longevity | Total |
|--------------|-------------|------------|-----------|----------|---------|------|----------|-----------|-------|---------|-----------|-------|
| Quiet Halo   | 3           | 4          | 5         | 4        | 4       | 4    | 4        | 4         | 4     | 3       | 4         | 43    |
| Folded Light | 5           | 4          | 4         | 4        | 4       | 4    | 4        | 5         | 5     | 4       | 5         | 48    |
| Lantern Mark | 4           | 4          | 4         | 5        | 3       | 5    | 3        | 4         | 4     | 4       | 4         | 44    |

- Strongest first move: Direction 2 (Folded Light)
  Why: highest total score. It improves distinctiveness without forcing a full stylistic reset, has the strongest geometric construction, and has the best longevity — the identity lives in shape, not in rendering.
  Highest-risk craft weakness: the fold angle must be precisely controlled or the asymmetry will feel accidental rather than designed.

- Improvement moves for Direction 2:
  1. Tighten the outer silhouette so the fold reads from shape, not rendering. Rationalize curves to G1 tangent continuity at all junctions.
  2. Remove any secondary internal highlight that would clog at 29px. Test pixel alignment at 29px — ensure the notch falls on a whole-pixel boundary.
  3. Align the fold angle with the geometry already present in the UI cards and buttons. Verify consistent corner radius progression (r, r/2, r*2).
  4. Run negative space audit: fill counterforms with contrasting color — ensure trapped spaces are deliberate.
  5. Context test: place on iOS home screen among Calm, Headspace, Sleep Cycle, Pillow, Rise, AutoSleep, Oura, SleepScore — verify differentiation.

Accessibility and legibility considerations:
- The icon should remain identifiable without relying on color contrast alone — verified via grayscale and CVD simulation.
- Internal detail should be treated as optional and removable below 60px.
- A one-color version must preserve the core metaphor before any premium surface treatment is approved.
- Contrast ratio between mark and likely backgrounds: >= 3:1 verified for both light and dark wallpapers.

Next actions:
- I can build Direction 2 in a design tool, run the full craft pass (geometric grid, optical corrections, path cleanliness, tangent continuity), and output a context-tested first concept.
- If you want the safest path, I will start with one evolutionary (Quiet Halo) and one adjacent (Folded Light) direction only.
- One high-leverage question: should the next round preserve the current symbol's recognizability for existing users, or can we prioritize distinctiveness more aggressively?
```

## Example 2: Review And Refine An Existing Symbol

User request:
- "This mark is too generic. Keep the same idea, but make it work as a real app icon."

Strong response shape:

```text
Mode: concept refinement
Platform scope: iOS + Android
Assumptions:
- The underlying metaphor should stay intact.
- The user wants refinement, not a new conceptual territory round.

Known facts:
- The current mark communicates the intended idea, but most of its identity comes from gradients and inner glow.
- At small size, the center detail clogs and the outer silhouette becomes interchangeable with other category icons.
- The current version does not yet show a convincing monochrome path for Android themed icons.

Recommendations:
- I would not restart the concept. I would refine it through three controlled moves.

- What is already working:
  The current mark has a calm emotional tone and a good overall massing strategy.

- What is failing:
  The symbol is being carried by rendering, not by silhouette memory.

- Refinement move 1: simplify the outer contour
  Goal: make the symbol recognizable from its edge alone
  Why: if the silhouette is memorable, the concept survives both small sizes and monochrome conversion

- Refinement move 2: reduce the internal structure to one decisive cut or one decisive countershape
  Goal: keep the metaphor while removing decorative clutter
  Why: current internal detail is too fragile for 29px and too dependent on gradient contrast

- Refinement move 3: separate icon logic from premium rendering
  Goal: approve the flat version first, then test whether a premium/material treatment adds value without changing the form
  Why: otherwise the concept may look expensive at 1024px and fail everywhere that matters

- Strongest refinement path:
  Flatten first, then test a premium pass only if the flat master still feels too ordinary.

- Improvement moves after the next round:
  1. Compare a more symmetrical silhouette against a slightly directional silhouette.
  2. Test whether the metaphor reads better from negative space or positive mass.
  3. Prepare the monochrome variant in parallel rather than at the end.

Accessibility and legibility considerations:
- The symbol should remain identifiable on light and dark backgrounds without relying on glow.
- If the concept needs subtle shading to be understood, it is not ready.
- The monochrome layer should preserve weight balance after all color information is removed.

Next actions:
- I can turn this into a flat refinement brief with pass/fail criteria at 180px, 60px, and 29px.
- If useful, I can also propose one adjacent backup direction in case this symbol still feels too generic after cleanup.
- One high-leverage question: which part of the current mark is truly non-negotiable, the metaphor itself or the existing silhouette users already know?
```

## Example 3: Export And Readiness Audit

User request:
- "Audit what we have and tell me if this logo system is actually ready to ship."

Strong response shape:

```text
Mode: export/readiness audit
Platform scope: iOS + Android
Assumptions:
- I am evaluating shipping readiness, not aesthetic preference.
- Anything not visibly validated is treated as unverified, not approved.

Known facts:
- A primary mark and wordmark exist.
- The iOS icon composition is defined.
- The Android adaptive split is partially defined, but the monochrome path is still unresolved.
- Reduction checks are visible at 180px and 60px, but 29px evidence is missing.

Recommendations:
- Current status: not yet shipping-ready

- Ready:
  Primary mark direction is coherent and fits the product.
  Wordmark pairing is stable enough for handoff.

- Not ready:
  Android monochrome/themed icon logic is not proven.
  29px reduction evidence is missing.
  The current package does not clearly separate what is visually validated from what is still conceptual.

- Craft audit:
  Geometric: the mark appears to use a grid, but two curves on the upper left have a visible tangent break (G0 instead of G1). Three unnecessary anchor points on the right edge suggest the path was not cleaned after initial construction.
  Color: contrast ratio mark-to-background is 4.1:1 (passes >= 3:1). However, internal contrast between primary and secondary elements is only 1.6:1 — below the 2:1 threshold. Grayscale conversion causes the secondary element to merge with the primary. CVD (deuteranopia): the green-to-blue internal contrast fails.
  Typography: wordmark uses a geometric sans (appropriate for the product), but kerning between "r" and "a" is too tight at logo scale, creating a visual merge. No lockup proportions are documented.
  Negative space: the counterform inside the mark is accidental — filling it with a contrasting color reveals an irregular, meaningless shape.
  Longevity: style-agnostic silhouette test — flat fill: pass. Outline only: fail (the inner detail disappears). Cut-out: partial pass. The identity is partially dependent on rendering, not fully structural.

- Context test results:
  iOS home screen (light wallpaper): the icon is visible but does not stand out — the outer silhouette is too similar to three competitor icons in the wellness category.
  iOS home screen (dark wallpaper): pass — contrast is sufficient.
  App Store listing scale: the mark is legible but the internal detail is not visible at listing size.
  Competitor row (Calm, Headspace, Sleep Cycle, Pillow, Rise): the icon ranks 4th in distinctiveness out of 6.

- Highest-risk issue:
  The mark may still be relying on subtle internal contrast that disappears in one color. The negative space is accidental, not designed.

- Punch list ordered by shipping risk:
  1. [critical] Approve a true monochrome icon, not an auto-derived grayscale version.
  2. [critical] Fix internal contrast ratio: increase to >= 2:1 or redesign the secondary element.
  3. [critical] Add small-size validation at 29px on both light and dark backgrounds.
  4. [high] Fix the tangent break on the upper-left curves (G1 minimum).
  5. [high] Clean the vector path: remove 3 unnecessary anchor points.
  6. [high] Redesign the counterform to be a deliberate shape.
  7. [medium] Fix "r-a" kerning in the wordmark.
  8. [medium] Document foreground/background responsibility for the adaptive icon package.
  9. [medium] Document lockup proportions (horizontal and stacked).
  10. [low] Add one line per deliverable stating whether it is final, provisional, or concept-only.

- Package status:
  rationale.md: provisional
  mark-flat: revise (craft issues above)
  mark-monochrome: missing
  wordmark: revise (kerning, lockup docs)
  ios-icon-notes.md: provisional
  android-adaptive-notes.md: missing
  reduction-checks.md: incomplete (29px missing)
  export-checklist.md: not ready

Accessibility and legibility considerations:
- The icon must preserve identity without depending on color alone — currently fails this test (internal contrast too low, CVD failure).
- Small-size failure is a usability issue, not just a branding issue.
- Monochrome behavior should be treated as a first-class requirement for Android, not a late export variant.

Next actions:
- I can fix items 1-6 in the next craft pass and re-test.
- If you want, I can also propose a monochrome layer design and re-run the context test after fixes.
- One high-leverage question: is the next milestone internal review readiness, or final store submission readiness?
```
