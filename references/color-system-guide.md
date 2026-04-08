# Color System — Full Guide

This is the full educational reference for color craft. The runtime checklist is in `color-system.md`.

## Color Harmony Models

### Monochromatic

One hue, multiple values and saturations.

When to use:
- the brand identity is anchored to a single signature color
- the mark must feel restrained and premium
- the icon must survive tinting (Android themed icons)

Risk: can feel flat or lifeless without sufficient value contrast.

### Analogous

Two to three hues adjacent on the color wheel (within ~60 degrees).

When to use:
- the brand needs warmth, naturalness, or continuity
- gradient-based marks where the transition must feel organic

Risk: low contrast between hues. The mark may lose internal hierarchy at small sizes.

### Complementary

Two hues opposite on the color wheel (~180 degrees apart).

When to use:
- the mark needs strong internal contrast
- the icon must pop against varied home screen wallpapers
- the brand wants to feel energetic or bold

Risk: direct complements at full saturation vibrate visually. Offset one hue slightly or reduce saturation of one side.

### Split-Complementary

One base hue plus the two hues adjacent to its complement.

When to use: contrast without the tension of direct complements. Risk: more complex to balance.

### Triadic

Three hues evenly spaced at 120-degree intervals.

When to use: playful, creative, or multi-category brands. Risk: rarely appropriate for premium.

## Saturation Strategy

### Full Saturation
High-energy, attention-grabbing. Works for consumer apps. Problem: can appear cheap or aggressive for premium.

### Controlled Saturation
Reduce saturation by 10-30%. Default for premium and craft-sensitive brands.

### Desaturated / Muted
Saturation reduced by 40-60%. Reads as mature, editorial, luxury. Problem: may not stand out on a home screen.

### Rule
Match saturation to brand positioning:
- mass-market, playful, utility: full to moderate
- premium, professional, editorial: moderate to controlled
- luxury, fashion, culture: controlled to muted

## Color And Accessibility — Details

### Contrast Ratios
WCAG 2.1 minimum contrast principles:
- mark vs background: >= 3:1
- internal elements: >= 2:1

Formula: `contrast = (L1 + 0.05) / (L2 + 0.05)` where L1 > L2.

### Color Vision Deficiency (CVD)
~8% of males, ~0.5% of females have CVD.
- protanopia/protanomaly: reduced red sensitivity
- deuteranopia/deuteranomaly: reduced green sensitivity (most common)
- tritanopia/tritanomaly: reduced blue sensitivity (rare)

Rules: never rely on red-green contrast alone. Ensure hierarchy through luminance, not just hue. Quick test: convert to grayscale.

### Dark Mode and Light Mode
Test against: white, black, medium gray, saturated wallpaper (blue, green, red).

## Gradient Rules — Details

### When Justified
Only when it adds depth/material meaning, the flat version is already strong, and direction matches the system's light source.

### Direction Consistency
One global light source. Same direction for all gradient fills and surface treatments.

### Small-Size Survival
At 60px and below, subtle gradients become flat bands. The mark must be identifiable with gradient removed. Avoid >2 stops at icon size. Avoid radial gradients in small marks.

### Gradient-to-Flat Mapping
For every gradient, define: the flat-fill replacement color, whether the flat version needs additional contrast aid.

### Gradient-to-Monochrome Mapping
Define what structural element replaces the gradient's visual role: fill/no-fill boundary, stroke, or shape density change.

## Color Reduction Strategy

### Full → Limited: keep signature color, reduce secondary to neutrals, keep accent if small enough.
### Limited → Two: keep signature + neutral, test hierarchy.
### Two → Monochrome: single foreground on contrasting background, replace color hierarchy with shape hierarchy (filled vs unfilled, solid vs outline, large vs small). This is the Android monochrome requirement.

## Category Color Conventions

- finance/banking: blue, dark blue, green
- health/wellness: green, teal, soft blue
- food/delivery: red, orange, warm yellow
- social/communication: blue, purple, gradient
- productivity/tools: blue, gray, orange
- entertainment/media: red, purple, dark
- education: blue, green, orange
- children: primary colors, high saturation, multi-color
- luxury/premium: black, gold, deep jewel tones

Rules: using category-standard helps recognition; breaking convention improves distinctiveness but risks confusion. Decision must be intentional.

## Platform-Specific Color Considerations

### iOS
- icon sits on wallpaper and in folders
- no dynamic tinting for standard icons (as of iOS 18)
- test against dark mode appearance

### Android
- adaptive icons: background color must work with all mask shapes
- Material You: system tints monochrome layer with wallpaper palette
- monochrome layer: single-color silhouette, only shape matters

### Store Listings
- App Store: small icon on white/near-white background
- Google Play: small icon on white background
- test at store-listing scale for visibility
