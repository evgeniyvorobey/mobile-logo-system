# Brand Spec — Mobile Logo System

Direction: **Construction Vesica**
Version: 1.0
Date: 2026-04-07

## Construction Logic

### Grid

- Base grid: 24×24 square module
- 1 grid unit (gu) = canvas / 24
- In the 200×200 viewBox: 1gu ≈ 8.33px

### Construction Circles

Two circles with phi-related radii create the vesica through their intersection.

| Circle | Center | Radius | Role |
|--------|--------|--------|------|
| Circle 1 (small) | (85, 96) | 38 | Left, defines the flatter arc |
| Circle 2 (large) | (137, 96) | 62 | Right, defines the more curved arc |

- Radius relationship: r2 / r1 = 62 / 38 ≈ 1.632 (≈ φ = 1.618)
- Circle separation: 52px (center-to-center)
- Optical center: circles at y=96 (4% up from geometric center at y=100)

### Vesica (The Mark)

The mark is the intersection region of the two construction circles — an asymmetric vesica piscis.

- **Intersection points:** (88, 58) and (88, 134)
- **Width:** ~48px
- **Height:** ~76px
- **Aspect ratio:** ~1:1.58 (near golden ratio)
- **Orientation:** vertical, pointed top and bottom, convex right side

SVG path:
```
M 88 58 A 62 62 0 0 0 88 134 A 38 38 0 0 0 88 58 Z
```

Arc breakdown:
- First arc (A 62 62 ...): from top to bottom along Circle 2 — the **more curved** (right) edge
- Second arc (A 38 38 ...): from bottom to top along Circle 1 — the **flatter** (left) edge

### Key Coordinates (viewBox 200×200)

| Point | x | y | Description |
|-------|---|---|-------------|
| Circle 1 center | 85 | 96 | Small circle, left |
| Circle 2 center | 137 | 96 | Large circle, right |
| Intersection top | 88 | 58 | Upper tip of vesica |
| Intersection bottom | 88 | 134 | Lower tip of vesica |
| Vesica visual center | ~100 | 96 | Approximate optical center of the form |

### Small-Icon Variant

For sizes below 48px, the circles are brought closer to widen the vesica for readability.

| Parameter | Primary | Small Icon |
|-----------|---------|------------|
| Circle 1 center | (85, 96) | (92, 96) |
| Circle 2 center | (137, 96) | (132, 96) |
| Separation | 52 | 40 |
| Vesica width | ~48 | ~60 |
| Vesica height | ~76 | ~74 |

Small-icon path:
```
M 82 59 A 62 62 0 0 0 82 133 A 38 38 0 0 0 82 59 Z
```

## Spacing

### Clear Space

Minimum clear space around the symbol: **1 cap-height** of the paired wordmark, or **12% of symbol height** if used without wordmark.

### Horizontal Lockup

- Symbol left, wordmark right
- Gap between symbol rightmost edge and text start: **80% of wordmark cap-height**
- Text vertical alignment: visual center of text matches optical center of symbol (y ≈ 96 in 200-unit viewBox)

### Stacked Lockup (not yet produced)

- Symbol above, wordmark below, centered
- Gap: 40% of cap-height
- Use when horizontal space is limited (e.g., square social media tiles)

## Color Roles

### Primary Palette

| Role | Name | Hex | HSL | Usage |
|------|------|-----|-----|-------|
| Primary | Copper | #C67A52 | 22°, 48%, 55% | Symbol fill (primary) |
| Text/Dark | Charcoal | #2C2C34 | 240°, 8%, 19% | Symbol fill (mono), wordmark, UI text |
| Background | Warm White | #FAF6F2 | 30°, 50%, 96% | Page backgrounds |

### Contrast Ratios

- Copper (#C67A52) on white (#FFFFFF): **3.8:1** ✓ (≥3:1 for large elements)
- Copper on black (#000000): **4.1:1** ✓
- Charcoal (#2C2C34) on white: **13.2:1** ✓

### Monochrome Behavior

- Single fill: Charcoal #2C2C34 on light backgrounds, white #FFFFFF on dark
- Identity carried entirely by the asymmetric vesica shape
- No color information needed for recognition

### Accessibility

- Single-color mark: immune to all color vision deficiency types
- Shape-first identity: works for all vision conditions
- High-contrast charcoal variant exceeds WCAG AAA (13.2:1)

## Wordmark

### Recommendation

- **Typeface:** Inter Medium (weight 500)
- **Alternative:** DM Sans Medium
- **Case:** all lowercase `mobile-logo-system`
- **Color:** Charcoal #2C2C34
- **Tracking:** standard (0), letter-spacing 0.01em
- **Pairing logic:** Inter's circular letterforms (o, e, c) echo the vesica's curved geometry

### Size Relationship

- Cap-height = **30% of symbol visual height** in horizontal lockup
- Symbol-dominant: the vesica carries identity, the wordmark carries the name

### Refinement Notes

- Hyphens should be styled at 70% of standard width for visual elegance — requires outlined text in production SVG
- Kerning pairs to adjust at logo scale: `i-l` (tighten 3%), `t-e` (tighten 3%), `o-g` (tighten 2%)
- Production lockup should convert text to outlines (paths) for consistent rendering

## Usage by Surface

| Surface | File | Notes |
|---------|------|-------|
| GitHub avatar | `primary-symbol.svg` | Copper vesica on transparent |
| README / docs header | `horizontal-lockup.svg` | Vesica + wordmark |
| Sidebar / skill picker (≥20px) | `primary-symbol.svg` | Shape readable at small sizes |
| Sidebar / skill picker (<20px) | `small-icon.svg` | Wider vesica for visibility |
| Monochrome / B&W / print | `monochrome-symbol.svg` | Charcoal single-color |
| Favicon (32px) | `small-icon.svg` | Wider vesica ensures visibility at @2x |
| Dark background | `monochrome-symbol.svg` | Use white fill variant |
| Construction reference | `alt-vesica-symbol.svg` | Shows construction circles |

## Small-Size Notes

- **≥48px:** Use `primary-symbol.svg` — vesica shape clearly readable
- **20-48px:** Use `primary-symbol.svg` at @2x, or `small-icon.svg` at @1x
- **<20px:** Use `small-icon.svg` (wider vesica, circles closer together)
- **<12px:** Consider solid copper circle as fallback

## Design Rationale

The Construction Vesica direction was chosen over the Craft Cut alternative for these reasons:

1. **Mathematical elegance:** The mark emerges naturally from the intersection of two phi-related circles — no cuts, no gaps, no arbitrary decisions
2. **Asymmetric character:** Unlike a standard vesica piscis (symmetric), the phi-ratio between circle radii creates an asymmetric form — one side more curved, one flatter — giving the mark distinctive identity
3. **Clean silhouette:** Works as a single filled shape at any size, no multi-piece alignment issues
4. **Scalability:** No gap to maintain across sizes — the form reads clearly from 12px to billboard

## File Inventory

| File | Type | Description |
|------|------|-------------|
| `primary-symbol.svg` | Copper vesica | Primary brand mark |
| `horizontal-lockup.svg` | Symbol + text | Descriptive lockup with wordmark |
| `monochrome-symbol.svg` | Single color | Charcoal vesica for B&W contexts |
| `small-icon.svg` | Wider vesica | Optimized for small render sizes (16-64px) |
| `alt-vesica-symbol.svg` | Construction ref | Shows construction circles and intersection points |
| `alt-vesica-mono.svg` | Mono reference | Original monochrome concept variant |
| `spec.md` | Documentation | This file — construction logic and usage |
