# Context Testing — Full Guide

This is the full educational reference for context testing. The runtime checklist is in `context-testing.md`.

## Mandatory Mockup Contexts

### 1. Home Screen — iOS
Place the icon on a realistic iOS home screen with:
- at least 8 real competitor/category-adjacent icons
- light, dark, and busy/photographic wallpaper

Evaluate: standout without screaming, category belonging, silhouette distinctness, color survival next to similar palettes.

### 2. Home Screen — Android
Place on Android launcher with:
- at least 8 real competitor icons
- Material You themed surface
- circular and rounded-square mask shapes

Evaluate: same as iOS, plus adaptive icon survival across masks, parallax shift (4dp) not clipping content.

### 3. App Store Listing — Apple
Small icon next to app name, subtitle, star rating on white/near-white background.
Evaluate: recognizable at small scale, primary color stands out, competes with nearby results.

### 4. Google Play Listing
Small icon next to app name on white background, in "similar apps" row.
Evaluate: same as App Store, plus monochrome version looks intentional in themed row.

### 5. Notification Bar / Status Bar
Monochrome silhouette in status bar (Android), notification banner (iOS).
Evaluate: legible at ~24dp, reduces cleanly, distinguishable from system icons.

### 6. Settings / System Screens
iOS Settings list (29pt/58px@2x/87px@3x), Android app info.
Evaluate: legible at 29pt, still feels like the brand, holds up in a list.

### 7. Spotlight / Search Results
iOS Spotlight (40pt/80px@2x/120px@3x), Android search/app drawer.
Evaluate: spottable quickly, reads at a glance.

### 8. App Switcher / Multitasking
Icon alongside the app's live screen preview.
Evaluate: reinforces app identity, visual continuity with product UI.

### 9. Splash / Launch Screen
Mark centered on splash screen.
Evaluate: confident at large size, optically centered, color matches icon background.

### 10. Share Sheet / Activity View
Small icon in horizontal scrolling row.
Evaluate: competes with messaging icons, distinguishable at small size.

## Competition Proximity Testing

### Direct Competitor Row
5-7 icons, mark in center. Evaluate: stands out, belongs, not confused with competitor, not derivative.

### Category Wall
20-30 icons from same category. Evaluate: color uniqueness, silhouette uniqueness, category cliché usage, findability on quick scroll.

### Confusion Test
Mark alongside 3 most visually similar competitors.
Evaluate: would user confuse at a glance? What's the single strongest differentiator? If only color, mark is at risk.

## Environmental Testing

### Wallpaper Variation
Test: white, black, gradient, photographic, busy multi-color. Icon must never disappear.

### Device Size Variation
Test: compact phone, large phone, iPad/tablet, foldable inner screen. Proportions correct at all scales.

### Dynamic Color / Theming
Android Material You: test monochrome with warm, cool, neutral palettes. Silhouette must carry identity regardless of tint.

## Practical Rules
- Run lightweight context checks during concept selection, not only at the end
- Early tests can be rough composites
- If mark fails in context, revise the mark, not the context
- Both reduction and context testing must pass
