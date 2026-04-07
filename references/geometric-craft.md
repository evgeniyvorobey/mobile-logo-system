# Geometric Craft

Use this file when constructing, refining, or evaluating logo geometry.

The goal is precision and intentionality in every shape decision, not decoration.

## Construction Grid Systems

Every hi-end mark is built on a grid, not drawn freehand.

### Keyline Grid

Use a keyline grid to constrain the outer silhouette to a repeatable family of shapes.

Standard keyline shapes for mobile icons:
- circle
- square
- vertical rectangle
- horizontal rectangle
- diagonal (rotated square)

The mark's outer boundary should align to one of these keyline shapes or a deliberate hybrid.

Android adaptive icons use a 108dp canvas with a 72dp safe zone (the inner 66.7%).
iOS icons use a 1024x1024 master with Apple's continuous-curvature squircle mask applied automatically.

Rule: design the foreground content to sit comfortably inside the safe zone, not to touch the outer edge.

### Construction Circle Method

Build the mark from a small set of circles with mathematically related radii.

Technique:
1. choose a base radius `r`
2. derive secondary radii as multiples or fractions: `r`, `r/2`, `r * phi`, `r * sqrt(2)`
3. position circles to define curves, intersections, and tangent points
4. extract the final path from the construction, then discard the scaffolding

This produces curves that feel related because they are related.

### Square Module Grid

Divide the canvas into an `n * n` grid (common choices: 8x8, 12x12, 16x16, 24x24).

Rules:
- anchor key vertices to grid intersections
- allow curves to pass through grid points or tangent to grid lines
- use half-module offsets only when a full module creates a shape that feels too rigid

Finer grids (24x24) suit detailed marks.
Coarser grids (8x8) enforce reduction discipline.

For icon work, prefer a grid that divides evenly into the target raster sizes.
A 24x24 grid maps cleanly to 48px (2x), 72px (3x), 96px (4x), 120px (5x), and 1024px.

## Mathematical Proportions

### Golden Ratio (phi = 1.618...)

Use phi to relate:
- width to height of the bounding box
- size of a primary element to a secondary element
- spacing between symbol and wordmark

Do not force phi onto every relationship. Use it where two elements need a natural-looking size hierarchy.

Practical shortcut: the Fibonacci sequence (1, 1, 2, 3, 5, 8, 13, 21, 34...) approximates phi ratios at larger values and is easier to work with on a pixel grid.

### Root Rectangles

- sqrt(2) rectangle (1 : 1.414): the proportion of A-series paper, feels stable and formal
- sqrt(3) rectangle (1 : 1.732): taller, feels more dynamic
- sqrt(5) rectangle (1 : 2.236): elongated, useful for horizontal lockups

Use root rectangles to set bounding proportions for the symbol or for lockup containers.

### Consistent Spacing Scale

Derive all spacing from a single base unit.

Example scale (base = 4px at 1x):
- 4, 8, 12, 16, 24, 32, 48, 64

Apply this scale to:
- internal spacing within the mark
- clear space around the mark
- symbol-to-wordmark gap
- padding inside the icon canvas

Avoid arbitrary spacing values that do not relate to the base unit.

## Optical Corrections

Mathematical alignment is not visual alignment. The following corrections are required for hi-end quality.

### Overshoot

Round and pointed shapes must extend slightly beyond the bounding box of flat-edged shapes to appear the same size.

Correction values:
- circles: extend 2-4% beyond the cap line and baseline
- triangles and pointed vertices: extend 4-8% beyond
- diagonal strokes: extend 1-3% beyond

Without overshoot, round shapes look smaller than square shapes at the same mathematical height.

### Visual Center

The visual center of a shape is slightly above its mathematical center (typically 3-5% of the height).

When centering a symbol inside an icon canvas:
- shift it upward by approximately 3-5% of the canvas height
- verify by eye: the mark should feel centered, not mathematically centered

### Stroke Weight Compensation

Horizontal strokes appear optically thicker than vertical strokes of the same measured width.

Correction: thin horizontal strokes by 5-10% relative to vertical strokes of the same visual weight.

This applies to:
- crossbars in letter-based marks
- horizontal dividers in geometric symbols
- any stroke that reads as "lying flat"

### Corner Radius Progression

When a shape uses rounded corners, every corner radius in the system should come from the same scale.

Example progression: `r`, `r/2`, `r * 2`

Do not mix arbitrary radii. A mark with 4px, 7px, and 11px corners looks accidental. A mark with 4px, 8px, and 16px corners looks designed.

iOS applies its own mask corner radius. The foreground artwork should use its own internal radius scale that does not fight the mask curvature.

### Tangent Discipline

Where two curves meet, they must share a tangent line at the junction (G1 continuity or higher).

Visible tangent breaks (cusps, kinks) read as errors in hi-end work.

Where a curve meets a straight edge, the transition should be smooth unless a sharp junction is the deliberate design intent.

## Pixel Alignment

### Target Sizes

The mark will be rasterized at specific sizes. The most critical:
- 29px (iOS Spotlight, Settings)
- 40px (iOS Spotlight on 2x)
- 48px (Android mdpi launcher)
- 58px (iOS Settings on 2x)
- 60px (iOS iPhone on 2x)
- 76px (iOS iPad)
- 80px (iOS Spotlight on 3x)
- 87px (iOS Settings on 3x)
- 120px (iOS iPhone on 2x, actual)
- 152px (iOS iPad on 2x)
- 167px (iOS iPad Pro on 2x)
- 180px (iOS iPhone on 3x)
- 192px (Android xxxhdpi)
- 512px (Google Play store)
- 1024px (iOS App Store)

### Whole-Pixel Boundaries

At small raster sizes, key edges of the mark should fall on whole-pixel boundaries.

Technique:
1. scale the vector master to the target size
2. check whether critical edges (outer silhouette, main internal divisions) land on or near pixel boundaries
3. if they fall on half-pixels, adjust the master geometry slightly or create a size-specific hint layer

Strokes that fall on half-pixel boundaries render as blurred anti-aliased lines. At 29px this destroys legibility.

### Stroke Width Minimums

At small raster sizes, strokes thinner than 1 physical pixel disappear.

Minimum visible stroke widths:
- at 29px: effective stroke must be >= 1px (approximately 3.5% of canvas)
- at 60px: effective stroke must be >= 1px (approximately 1.7% of canvas)
- at 120px: effective stroke can be 1px (approximately 0.8% of canvas)

If a mark relies on fine internal lines, plan a simplified version for small sizes.

### Anti-Aliasing Budget

At small sizes, anti-aliasing consumes a larger percentage of the visible area.

A 1px stroke at 29px uses ~3.4% of the width, but with anti-aliasing it may appear as a 2px fuzzy band using ~6.9%.

Account for this when planning internal detail. If anti-aliased edges will overlap or merge, the detail is too fine for that size.

## Symmetry and Balance

### Types of Symmetry

- bilateral (mirror): most common for app icons, signals stability and trust
- rotational: signals motion or process
- radial: signals completeness or protection
- asymmetrical balance: signals dynamism or forward motion

Choose symmetry type intentionally, not by accident.

### Weight Distribution

Visual weight is affected by:
- size
- darkness/density
- position (lower = heavier, right = lighter in LTR reading)
- texture density
- isolation (surrounded by space = heavier perceived weight)

A balanced mark has its visual center of gravity near its geometric center (adjusted for optical center).

An unbalanced mark is acceptable only when the imbalance is deliberate and the direction of tension is intentional.

### Optical Balance Test

Cover the left half. Cover the right half. Cover the top half. Cover the bottom half.

Each half should feel like it could plausibly be mirrored without creating a lopsided result, unless asymmetry is the point.

## Platform-Specific Grid Rules

### iOS

- master canvas: 1024x1024
- Apple applies a continuous-curvature superellipse mask — do not draw your own rounded rectangle
- the mask clips approximately 16% of the corner area
- keep critical content inside a circle of radius ~460px centered on the canvas (~90% safe zone)
- do not rely on content in the outermost 5% of the canvas
- Apple Human Interface Guidelines recommend a single, simple, recognizable shape

### Android Adaptive

- canvas: 108 x 108 dp
- safe zone: 72 x 72 dp centered (inner 66.7%)
- the system applies various mask shapes (circle, rounded square, squircle, teardrop, etc.)
- foreground layer may shift up to 4dp under parallax
- critical content must survive parallax shift: keep it inside a 64dp centered zone
- background layer is typically a solid color or simple gradient
- monochrome layer: single-color silhouette of the foreground, no gradients

### Shared Rule

Design the master at 1024x1024 or larger, but validate geometry at 48px and 29px during construction, not only at the end.
