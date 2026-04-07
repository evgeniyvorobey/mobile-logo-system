# Evaluation

Use this file to compare directions and reject weak concepts.

## Core Scoring Dimensions

Score each direction from 1-5 on these 11 dimensions.

### Standard tier (7 dimensions — always scored)

1. Distinctiveness
   Does it stand apart from the category?

2. Small-size legibility
   Does it survive at 60px and 29px?

3. Brand fit
   Does it express the actual product and emotional job?

4. Platform readiness
   Can it plausibly become iOS + Android adaptive + monochrome assets?

5. Premium feel
   Does it feel crafted and deliberate without becoming noisy?

6. Monochrome survival
   Can it survive one-color conversion without losing identity?

7. Wordmark compatibility
   Can it pair cleanly with a wordmark without fighting it?

### Hi-end tier (4 additional dimensions)

8. Geometric precision
   Is the mark built on a construction grid? Are proportions intentional? Are optical corrections applied (overshoot, visual center, stroke compensation)?
   See [geometric-craft.md](geometric-craft.md) for the full framework.

9. Color craft
   Are color roles assigned (primary, secondary, accent)? Does the palette survive CVD simulation and grayscale conversion? Are gradient fallbacks defined?
   See [color-system.md](color-system.md) for the full framework.

10. Context survival
    Does the mark work on a real home screen among competitors? Does it hold up in store listings, notification bar, settings, and splash screen?
    See [context-testing.md](context-testing.md) for mandatory mockup contexts.

11. Longevity
    Is the mark's identity structural (shape, proportion, negative space) or stylistic (gradient trend, effect fashion)? Does it pass the style-agnostic silhouette test? Would it look dated in 3 years?
    See [premium-craft.md](premium-craft.md) for the full longevity framework.

## Reduction Tests

Every selected direction must be tested at:
- 1024px
- 180px
- 120px
- 60px
- 48px
- 29px

What to inspect:
- silhouette memory
- detail collapse
- negative space clogging
- whether the metaphor survives without explanation

## Surface Tests

Check:
- light background
- dark background
- monochrome
- flat/no-effects mode

If a mark works only with gradients, glow, shadows, or background tricks, treat that as a warning.

## Category Risk Tests

Ask:
- does this look like a generic wellness app?
- does this look like a meditation app clone?
- does this look like a crypto/finance premium app?
- does this look like a children’s sticker rather than a serious brand mark?

Reject if the concept drifts into the wrong category code.

## Premium Lens

When the task involves premium positioning:

Prefer:
- restraint
- precision
- quiet symbolism
- material confidence
- internal richness

Avoid:
- loud metallic clichés
- generic sparkles
- too many highlight tricks
- complexity on the outer silhouette

## Rejection Triggers

Reject or rework if any of these are true:
- the concept needs explanation to be understood
- the symbol loses identity below 60px
- the symbol becomes a blob in monochrome
- the symbol is mostly trend-driven and weakly tied to the brand
- the symbol is attractive but interchangeable
- the symbol only feels premium because of rendering effects
- the geometry is freehand with no visible construction logic
- the color scheme fails grayscale conversion (internal hierarchy disappears)
- the mark disappears on a real home screen among competitors
- the mark's identity would not survive a trend change (style-agnostic silhouette test fails)
- negative space is accidental rather than designed
- curve junctions have visible tangent breaks (cusps or kinks)

## Suggested Decision Matrix

Standard tier (7 columns):

| Direction | Distinctive | Small size | Brand fit | Platform | Premium | Monochrome | Wordmark | Total |
|-----------|-------------|------------|-----------|----------|---------|------------|----------|-------|

Hi-end tier (all 11 columns):

| Direction | Distinctive | Small size | Brand fit | Platform | Premium | Monochrome | Wordmark | Geometric | Color | Context | Longevity | Total |
|-----------|-------------|------------|-----------|----------|---------|------------|----------|-----------|-------|---------|-----------|-------|

Then add a short note:
- strongest reason to advance
- strongest reason to reject
- highest-risk craft weakness (the specific dimension most likely to cause problems post-launch)

This skill should be able to explain all three.

## Craft Audit Gate

Before a direction advances from selection to refinement, it must pass this gate:

1. construction method stated: what grid or construction system was used?
2. optical corrections listed: what overshoot, visual center, or stroke compensation was applied?
3. color rationale stated: why these specific colors, not just "it looks good"?
4. negative space checked: are counterforms deliberate or accidental?
5. silhouette isolation tested: does the mark work as a flat single-color fill?

If any of these cannot be answered, the direction is not ready for refinement. It needs a craft pass first.
