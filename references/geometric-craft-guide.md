# Geometric Craft — Full Guide

This is the full educational reference for geometric construction. The runtime checklist is in `geometric-craft.md`.

## Construction Grid Systems — Details

### Keyline Grid
Standard keyline shapes for mobile icons: circle, square, vertical rectangle, horizontal rectangle, diagonal.

Android adaptive: 108dp canvas, 72dp safe zone (inner 66.7%).
iOS: 1024x1024 master with continuous-curvature squircle mask applied automatically.

Rule: design foreground to sit inside the safe zone, not touch the outer edge.

### Construction Circle Method
Build from circles with related radii:
1. choose base radius `r`
2. derive: `r`, `r/2`, `r * phi`, `r * sqrt(2)`
3. position circles to define curves, intersections, tangent points
4. extract final path, discard scaffolding

Produces curves that feel related because they are related.

### Square Module Grid
Divide canvas into `n * n` grid (common: 8x8, 12x12, 16x16, 24x24).

Rules:
- anchor key vertices to grid intersections
- allow curves to pass through grid points or tangent to grid lines
- half-module offsets only when full module feels too rigid

A 24x24 grid maps cleanly to 48px (2x), 72px (3x), 96px (4x), 120px (5x), 1024px.

## Mathematical Proportions — Details

### Golden Ratio (phi = 1.618...)
Use to relate: width/height of bounding box, primary/secondary element sizes, symbol-wordmark spacing.
Don't force it everywhere. Fibonacci sequence (1,1,2,3,5,8,13,21,34...) approximates phi and works better on pixel grids.

### Root Rectangles
- sqrt(2) (1:1.414): A-series paper, stable, formal
- sqrt(3) (1:1.732): taller, dynamic
- sqrt(5) (1:2.236): elongated, horizontal lockups

### Consistent Spacing Scale
Derive all spacing from a single base unit. Example (base=4px at 1x): 4, 8, 12, 16, 24, 32, 48, 64.
Apply to: internal spacing, clear space, symbol-wordmark gap, icon canvas padding.

## Optical Corrections — Details

### Overshoot
Round/pointed shapes must extend beyond the bounding box of flat-edged shapes:
- circles: 2-4% beyond cap line and baseline
- triangles/pointed: 4-8% beyond
- diagonals: 1-3% beyond

### Visual Center
Slightly above mathematical center (3-5% of height). Verify by eye.

### Stroke Weight Compensation
Horizontal strokes appear thicker than vertical. Thin horizontals by 5-10%.
Applies to: crossbars, horizontal dividers, any "lying flat" stroke.

### Corner Radius Progression
Every radius from the same scale. Example: `r`, `r/2`, `r * 2`. 
Do not mix arbitrary radii (4px, 7px, 11px = accidental; 4px, 8px, 16px = designed).
iOS mask has its own radius — foreground uses its own internal scale.

### Tangent Discipline
Where curves meet: shared tangent (G1 minimum). Visible breaks read as errors.
Curve-to-straight transitions should be smooth unless sharp junction is deliberate.

## Pixel Alignment — Details

### Target Sizes
Critical raster sizes:
- 29px (iOS Spotlight/Settings)
- 40px, 48px, 58px, 60px, 76px, 80px, 87px
- 120px, 152px, 167px, 180px, 192px
- 512px (Google Play), 1024px (iOS App Store)

### Whole-Pixel Boundaries
Key edges should land on whole pixels. Half-pixel = blurred anti-aliased line. At 29px this destroys legibility.

### Stroke Width Minimums
- 29px: >= 1px (≈3.5% of canvas)
- 60px: >= 1px (≈1.7% of canvas)
- 120px: >= 1px (≈0.8% of canvas)

If mark relies on fine lines, plan simplified version for small sizes.

### Anti-Aliasing Budget
At 29px, a 1px stroke uses ~3.4% width but with AA appears as ~6.9% fuzzy band. Account for this when planning internal detail.

## Symmetry and Balance — Details

### Types
- bilateral (mirror): stability, trust — most common for app icons
- rotational: motion, process
- radial: completeness, protection
- asymmetrical balance: dynamism, forward motion

### Weight Distribution
Affected by: size, darkness/density, position (lower=heavier, right=lighter in LTR), texture density, isolation.

### Optical Balance Test
Cover each half separately. Each should feel plausibly mirrorable unless asymmetry is intentional.

## Platform-Specific Grid Rules

### iOS
- master: 1024x1024
- Apple squircle mask clips ~16% of corner area
- safe zone: circle r≈460px centered (~90%)
- don't rely on content in outermost 5%

### Android Adaptive
- canvas: 108x108dp, safe zone: 72x72dp
- various mask shapes (circle, rounded square, squircle, teardrop)
- foreground may shift up to 4dp (parallax) — critical content inside 64dp zone
- background: solid color or simple gradient
- monochrome: single-color silhouette, no gradients

### Shared
Design master at 1024+ but validate at 48px and 29px during construction, not only at the end.
