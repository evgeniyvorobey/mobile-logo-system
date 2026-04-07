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
  Core metaphor: protected calm
  Why it fits the project: preserves the product's warm, rounded, reassuring tone
  Silhouette logic: one enclosing outer form plus one unmistakable inner cut
  60px/29px logic: the outer shape remains recognizable even if the internal cut simplifies
  Risk: may still feel too close to category wellness cliches unless the inner cut becomes more proprietary

- Direction 2: Folded Light
  Core metaphor: a crafted fold that suggests care, ritual, and transition into rest
  Why it fits the project: keeps the product's softness but introduces stronger shape memory
  Silhouette logic: asymmetrical outer contour with one directional fold cue
  60px/29px logic: the fold becomes a single decisive notch rather than a detailed crease
  Risk: if over-rendered, it will become premium decoration instead of strong icon geometry

- Direction 3: Lantern Mark
  Core metaphor: contained warmth and guidance
  Why it fits the project: better distinctiveness while staying emotionally aligned with the current interface
  Silhouette logic: stable container plus a centered light core
  60px/29px logic: container remains primary, core simplifies to one contrasting mass
  Risk: can drift into finance or utility if the proportions become too severe

- Strongest first move: Direction 2
  Why: it improves distinctiveness without forcing a full stylistic reset and has the best chance of surviving both iOS and Android monochrome constraints.

- Improvement moves for Direction 2:
  1. Tighten the outer silhouette so the fold reads from shape, not rendering.
  2. Remove any secondary internal highlight that would clog at 29px.
  3. Align the fold angle with the geometry already present in the UI cards and buttons.

Accessibility and legibility considerations:
- The icon should remain identifiable without relying on color contrast alone.
- Internal detail should be treated as optional and removable below 60px.
- A one-color version must preserve the core metaphor before any premium surface treatment is approved.

Next actions:
- I can turn these three territories into a scored first concept round.
- If you want the safest path, I will start with one evolutionary and one adjacent direction only.
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

- Highest-risk issue:
  The mark may still be relying on subtle internal contrast that disappears in one color.

- Required fixes before handoff:
  1. Approve a true monochrome icon, not an auto-derived grayscale version.
  2. Add small-size validation at 29px on both light and dark backgrounds.
  3. Document foreground/background responsibility for the adaptive icon package.
  4. Add one line per deliverable stating whether it is final, provisional, or concept-only.

- Suggested handoff package:
  rationale.md
  mark-flat
  mark-monochrome
  wordmark
  ios-icon-notes.md
  android-adaptive-notes.md
  export-checklist.md

Accessibility and legibility considerations:
- The icon must preserve identity without depending on color alone.
- Small-size failure is a usability issue, not just a branding issue.
- Monochrome behavior should be treated as a first-class requirement for Android, not a late export variant.

Next actions:
- I can convert this audit into a concise punch list ordered by shipping risk.
- If you want, I can also mark each current deliverable as pass, revise, or missing.
- One high-leverage question: is the next milestone internal review readiness, or final store submission readiness?
```
