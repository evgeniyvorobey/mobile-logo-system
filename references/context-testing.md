# Context Testing — Runtime Checklist

> Full guide with detailed mockup contexts and competition testing: [context-testing-guide.md](context-testing-guide.md)

## Mandatory Contexts

Test the mark in each before calling it production-ready:

1. **iOS home screen** — light, dark, busy wallpaper; 8+ real competitor icons visible
2. **Android home screen** — light, dark; circular + rounded-square masks; parallax-safe
3. **App Store listing** — small icon on white, next to name/rating
4. **Google Play listing** — small icon on white, in "similar apps" row
5. **Notification bar** — monochrome silhouette at ~24dp (if applicable)
6. **Settings / 29pt** — legible, still feels like the brand
7. **Spotlight / search** — spottable at a glance
8. **Splash screen** — confident at large size, optically centered
9. **Share sheet** — small icon in horizontal row, distinguishable

## Competition Testing

- **Competitor row**: mark among 5-7 direct competitors. Must stand out and belong.
- **Confusion test**: alongside 3 most similar competitors. Differentiator must not be color-only.

## Environment Testing

- **Wallpapers**: white, black, gradient, photo, busy. Icon edge always discernible.
- **Devices**: compact phone, large phone, tablet, foldable.
- **Dynamic color**: Android Material You — monochrome with warm/cool/neutral palettes.

## Rules

- Run lightweight context checks during concept selection, not only at the end
- If mark fails in context, revise the mark
- Both reduction and context tests must pass

## Checklist

- [ ] iOS home screen — light wallpaper
- [ ] iOS home screen — dark wallpaper
- [ ] iOS home screen — busy wallpaper
- [ ] Android home screen — light, dark
- [ ] Android adaptive — circular mask
- [ ] Android adaptive — rounded-square mask
- [ ] App Store listing scale
- [ ] Google Play listing scale
- [ ] Notification icon (if applicable)
- [ ] Settings / 29pt
- [ ] Spotlight / search
- [ ] Splash screen
- [ ] Share sheet
- [ ] Competitor row (5-7 icons)
- [ ] Wallpaper variation (white, black, gradient, photo)
- [ ] Dynamic color / themed icon (Android)
