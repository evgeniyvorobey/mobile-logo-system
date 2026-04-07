# Color System

Use this file when choosing, evaluating, or refining color for a logo system.

Color in a mobile icon is not decoration. It is structure, hierarchy, and identity compressed into a surface smaller than a fingertip.

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

When to use:
- you want contrast without the tension of direct complements
- the mark has three visual elements that need color differentiation

Risk: more complex to balance. Test at small size to ensure the three colors still read as a system.

### Triadic

Three hues evenly spaced at 120-degree intervals.

When to use:
- the brand is playful, creative, or multi-category
- the mark genuinely needs three distinct color roles

Risk: rarely appropriate for premium or restrained brands. Three strong hues at icon size create noise unless carefully controlled by area ratio.

## Color Roles In A Mark

Assign every color a structural role:

- primary: the dominant color, occupies the largest area, carries brand recognition
- secondary: supports the primary, creates internal contrast or depth
- accent: smallest area, draws the eye to the focal point

Area ratio guideline: approximately 60:30:10 (primary:secondary:accent).

At icon size, prefer a maximum of three colors in the mark itself. More than three colors rarely survive reduction to 60px without becoming noise.

## Saturation Strategy

### Full Saturation

High-energy, attention-grabbing. Works for consumer apps competing on a crowded home screen.

Problem: fully saturated colors can appear cheap or aggressive when the brand intent is premium.

### Controlled Saturation

Reduce saturation by 10-30% from pure hue. The color still reads clearly but gains sophistication.

This is the default for premium and craft-sensitive brands.

### Desaturated / Muted

Saturation reduced by 40-60%. Reads as mature, editorial, or luxury.

Problem: may not stand out on a home screen. Test against bright competitor icons.

### Rule

Choose saturation intentionally, not by default. Match saturation to brand positioning:
- mass-market, playful, utility: full to moderate saturation
- premium, professional, editorial: moderate to controlled saturation
- luxury, fashion, culture: controlled to muted saturation

## Color And Accessibility

### Contrast Ratios

WCAG 2.1 defines minimum contrast ratios for text, but the principle applies to icon legibility:
- between the primary mark shape and the icon background: aim for >= 3:1 contrast ratio
- between internal elements of the mark: aim for >= 2:1 to maintain hierarchy at small size

Tools for checking: use the relative luminance formula:
`contrast = (L1 + 0.05) / (L2 + 0.05)` where L1 > L2.

### Color Vision Deficiency (CVD)

Approximately 8% of males and 0.5% of females have some form of color vision deficiency.

Common types:
- protanopia / protanomaly: reduced red sensitivity
- deuteranopia / deuteranomaly: reduced green sensitivity (most common)
- tritanopia / tritanomaly: reduced blue sensitivity (rare)

Design rules:
- never rely on red-green contrast as the sole differentiator between elements
- ensure the mark's internal hierarchy is readable through luminance contrast alone, not just hue
- test the mark under simulated CVD conditions before approving

Quick test: convert the mark to grayscale. If internal structure disappears, the color scheme relies too heavily on hue differentiation and will fail for CVD users.

### Dark Mode and Light Mode

The icon must read correctly against:
- light wallpapers and surfaces (white, cream, light gray)
- dark wallpapers and surfaces (black, dark gray, deep blue)
- system-tinted surfaces (Android Material You dynamic color)

If the mark has a transparent background region (inside the icon canvas), the background color must be chosen to work in both modes.

If the mark has a solid background fill, test it against at least:
- pure white (#FFFFFF)
- pure black (#000000)
- medium gray (#808080)
- a saturated wallpaper (blue, green, red)

## Gradient Rules

### When Gradients Are Justified

Use a gradient only when:
- it adds depth or material meaning (not just "looks nicer")
- the flat version of the mark is already strong on its own
- the gradient direction is consistent with the light source used across the system

Do not use a gradient to rescue a weak shape.

### Gradient Direction Consistency

If the system uses gradients, the light direction must be consistent:
- choose one global light source (top-center or top-left are standard)
- apply the same direction to all gradient fills in the mark
- apply the same direction to any premium surface treatment (highlights, shadows)

Mixed light directions feel accidental.

### Gradient Survival At Small Sizes

At 60px and below, subtle gradients become flat bands or invisible.

Rules:
- the mark must be identifiable with the gradient removed (flat fallback)
- avoid gradients with more than two stops at icon size — banding becomes visible
- avoid radial gradients in small marks — the center highlight compresses to a dot

### Gradient-to-Flat Mapping

For every gradient in the mark, define:
- the flat-fill color that replaces it (typically the gradient's midpoint or dominant color)
- whether the flat version needs any additional contrast aid (a stroke, a different background)

This mapping is required before the mark can be called production-ready.

### Gradient-to-Monochrome Mapping

Gradients disappear entirely in monochrome.

Define what structural element replaces the gradient's visual role:
- a fill/no-fill boundary
- a stroke
- a change in shape density

If the gradient is the only thing creating internal contrast, the mark will fail in monochrome.

## Color Reduction Strategy

### Full Color to Limited Palette

When reducing from a rich palette:
1. identify the signature color (the one users will remember)
2. keep the signature color unchanged
3. reduce secondary colors to neutrals or remove them
4. accent color can stay if it is small enough to survive reduction

### Limited Palette to Two Colors

1. keep the signature color
2. pair it with a neutral (white, black, or a desaturated complement)
3. test: does the mark still have clear internal hierarchy with only two colors?

### Two Colors to Monochrome

1. convert to a single foreground color on a contrasting background
2. replace color-based hierarchy with shape-based hierarchy:
   - filled vs unfilled areas
   - solid vs outline
   - large mass vs small detail
3. test: does the mark's identity survive with no color information at all?

This is the Android monochrome/themed icon requirement. It is not optional.

## Category Color Conventions

Be aware of, but not enslaved by, category color associations:

- finance/banking: blue, dark blue, green
- health/wellness: green, teal, soft blue
- food/delivery: red, orange, warm yellow
- social/communication: blue, purple, gradient
- productivity/tools: blue, gray, orange
- entertainment/media: red, purple, dark
- education: blue, green, orange
- children: primary colors, high saturation, multi-color
- luxury/premium: black, gold, deep jewel tones, restrained palette

Rules:
- using a category-standard color helps with instant recognition of category belonging
- deliberately breaking category color convention can improve distinctiveness but risks confusing initial recognition
- the decision to conform or diverge must be intentional, not accidental

## Platform-Specific Color Considerations

### iOS

- the icon sits on the user's wallpaper and inside folders
- iOS does not apply dynamic tinting to standard icons (as of iOS 18, dark mode tint is separate)
- test the icon's color against the iOS dark mode appearance where icons may sit on a darker surface

### Android

- adaptive icons: the background layer color should work with all mask shapes
- Material You: the system can tint the monochrome icon layer with the user's wallpaper-derived palette
- the monochrome layer is a single-color silhouette — only shape matters, not the specific color

### Store Listings

- App Store: the icon appears at small scale next to the app name on a white or near-white background
- Google Play: the icon appears at small scale on a white background
- test the icon's color at store-listing scale to ensure it does not disappear against the listing background

## Practical Checklist

Before approving a color scheme:
- [ ] signature color identified
- [ ] color roles assigned (primary, secondary, accent)
- [ ] area ratio tested (~60:30:10)
- [ ] contrast ratio >= 3:1 against likely backgrounds
- [ ] internal contrast ratio >= 2:1 between mark elements
- [ ] grayscale conversion test passed (hierarchy survives)
- [ ] CVD simulation tested (protanopia, deuteranopia minimum)
- [ ] dark background test passed
- [ ] light background test passed
- [ ] gradient-to-flat fallback defined (if gradients used)
- [ ] monochrome mapping defined
- [ ] saturation level matches brand positioning
