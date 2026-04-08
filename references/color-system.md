# Color System — Runtime Checklist

> Full guide with harmony models, saturation strategy, and platform details: [color-system-guide.md](color-system-guide.md)

## Key Rules

### Color Roles
Assign every color a structural role:
- **primary**: dominant, largest area, brand recognition
- **secondary**: supports primary, creates contrast/depth
- **accent**: smallest area, draws eye to focal point

Area ratio: ~60:30:10. Max 3 colors in the mark at icon size.

### Saturation
Match to positioning: mass-market → full; premium → controlled (−10-30%); luxury → muted (−40-60%).

### Contrast
- Mark vs background: >= 3:1
- Internal elements: >= 2:1
- Grayscale test: internal hierarchy must survive without hue

### CVD (Color Vision Deficiency)
Never rely on red-green contrast alone. Ensure hierarchy through luminance. Quick test: convert to grayscale — if structure disappears, fix it. Simulate protanopia + deuteranopia minimum.

### Dark/Light Mode
Test against: white, black, medium gray, saturated wallpaper. Icon edge must always be discernible.

### Gradients
- Only when flat version is already strong
- One direction, consistent with system light source
- Two stops max at icon size
- Define flat fallback and monochrome fallback
- If gradient is the only internal contrast, mark fails monochrome

### Monochrome Reduction
Full → limited → two → single color. At each step, hierarchy must survive via shape, not color. Android monochrome/themed icon is not optional.

### Category Conventions
Be aware of, not enslaved by: finance=blue, health=green, food=red/orange, social=blue/purple, luxury=black/gold. Breaking convention must be intentional.

## Checklist

- [ ] Signature color identified
- [ ] Color roles assigned (primary, secondary, accent)
- [ ] Area ratio ~60:30:10
- [ ] Contrast >= 3:1 vs backgrounds
- [ ] Internal contrast >= 2:1
- [ ] Grayscale test passed
- [ ] CVD simulation tested (protanopia, deuteranopia)
- [ ] Dark background test passed
- [ ] Light background test passed
- [ ] Gradient-to-flat fallback defined (if gradients used)
- [ ] Monochrome mapping defined
- [ ] Saturation matches brand positioning
