# Geometric Craft — Runtime Checklist

> Full guide with grid systems, proportions math, and platform details: [geometric-craft-guide.md](geometric-craft-guide.md)

## Key Rules

### Construction Grid
Every hi-end mark is built on a grid. Three methods:
- **Keyline grid**: constrain silhouette to circle, square, or rectangle keylines
- **Construction circles**: related radii (r, r/2, r×phi, r×sqrt2) — extract path from intersections
- **Square module grid**: n×n grid (8-24), anchor vertices to intersections. 24×24 maps cleanly to 48/72/96/120/1024px.

### Proportions
- **Golden ratio (phi=1.618)**: relate width/height, primary/secondary sizes, spacing. Don't force it everywhere.
- **Root rectangles**: sqrt2 (1:1.414) = stable; sqrt3 (1:1.732) = dynamic; sqrt5 (1:2.236) = horizontal.
- **Spacing scale**: derive all from a single base (e.g., 4px → 4, 8, 12, 16, 24, 32, 48, 64).

### Optical Corrections
- **Overshoot**: circles 2-4%, points 4-8%, diagonals 1-3% beyond flat edges
- **Visual center**: shift up 3-5% from mathematical center
- **Horizontal strokes**: thin by 5-10% vs vertical strokes
- **Corner radii**: from a single scale (r, r/2, r×2). No arbitrary mixing.
- **Tangent discipline**: G1 minimum at curve junctions. Visible breaks = errors.

### Pixel Alignment
Critical sizes: **29px**, 60px, 120px, 1024px.
- Key edges on whole-pixel boundaries (half-pixel = blur)
- Minimum stroke: 1px at target size (29px ≈ 3.5% of canvas)
- Anti-aliasing at 29px makes 1px stroke appear ~2px fuzzy

### Platform Grids
- **iOS**: 1024×1024 master. Squircle mask clips ~16% corners. Safe zone: r≈460px circle (~90%).
- **Android**: 108×108dp canvas, 72×72dp safe zone. Parallax up to 4dp → critical content inside 64dp. Monochrome = single-color silhouette, no gradients.
- **Both**: design at 1024+, validate at 48px and 29px during construction.

### Symmetry
Bilateral (stability), rotational (motion), radial (completeness), asymmetrical (dynamism). Choose intentionally. Visual center of gravity near optical center unless imbalance is deliberate.

## Checklist

- [ ] Construction grid established (keyline / circle / module)
- [ ] Key vertices aligned to grid
- [ ] Proportions from a consistent system (phi, root rect, spacing scale)
- [ ] Overshoot applied for round/pointed shapes
- [ ] Visual center corrected (3-5% up)
- [ ] Horizontal strokes thinned (5-10%)
- [ ] Corner radii from single scale
- [ ] Tangent continuity G1+ at all junctions
- [ ] Paths clean (minimum anchor points)
- [ ] Pixel alignment validated at 29px and 60px
- [ ] Stroke minimums respected at target sizes
- [ ] Platform safe zones respected (iOS 90%, Android 64dp)
- [ ] Symmetry/balance type intentional
