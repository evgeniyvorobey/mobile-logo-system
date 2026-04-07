# Context Testing

Use this file to validate that a mark works in the real environments where it will appear.

A logo that looks excellent on a white artboard but fails on a home screen is not a finished logo. Context testing is not optional for hi-end work.

## Mandatory Mockup Contexts

Every mark that advances past concept selection must be tested in these contexts before it can be called production-ready.

### 1. Home Screen — iOS

Place the icon on a realistic iOS home screen with:
- at least 8 real competitor or category-adjacent app icons visible
- a light wallpaper test
- a dark wallpaper test
- a busy/photographic wallpaper test

What to evaluate:
- does the icon stand out without screaming?
- does it belong in the category (instant recognition of what kind of app this is)?
- does the silhouette remain distinct from adjacent icons?
- does the color survive next to icons with similar palettes?

### 2. Home Screen — Android

Place the icon on a realistic Android launcher with:
- at least 8 real competitor or category-adjacent app icons
- a Material You themed surface (dynamic color)
- test with both circular and rounded-square mask shapes

What to evaluate:
- same as iOS, plus:
- does the adaptive icon foreground survive different mask shapes without clipping critical content?
- does the parallax shift (up to 4dp) cause any visual collision with the background edge?

### 3. App Store Listing — Apple

Show the icon at App Store search-result scale:
- small icon to the left of the app name and subtitle
- next to the star rating and download button
- on a white or near-white background

What to evaluate:
- is the icon still recognizable at this small scale?
- does the icon's primary color stand out against the white listing background?
- does the icon compete well against nearby search results?

### 4. Google Play Listing

Show the icon at Google Play search-result scale:
- small icon to the left of the app name
- on a white background
- alongside similar apps in a "similar apps" row

What to evaluate:
- same as App Store, plus:
- does the monochrome version look intentional in the themed icon row?

### 5. Notification Bar / Status Bar

If the app uses a notification icon derived from the mark:
- show the icon as a small monochrome silhouette in the status bar (Android)
- show the icon in a notification banner (iOS)

What to evaluate:
- is the silhouette legible at notification-icon size (~24dp)?
- does the shape reduce cleanly to this extreme small size?
- is the mark distinguishable from system icons (clock, battery, signal) at a glance?

### 6. Settings / System Screens

Show the icon in:
- iOS Settings list (29pt / 58px @2x / 87px @3x)
- Android app info screen

What to evaluate:
- is the mark legible at 29pt?
- does the icon still feel like the same brand at this minimal size?
- does it hold up in a list of other app icons with varied quality levels?

### 7. Spotlight / Search Results

Show the icon in:
- iOS Spotlight search results (40pt / 80px @2x / 120px @3x)
- Android search/app drawer results

What to evaluate:
- can a user spot their app quickly among search results?
- does the icon read at a glance or require focused inspection?

### 8. App Switcher / Multitasking

Show the icon in the multitasking view where it appears alongside the app's live screen preview.

What to evaluate:
- does the icon reinforce the app's identity when shown next to its own UI?
- is there visual continuity between the icon and the product interface?

### 9. Splash / Launch Screen

Show the mark (or symbol alone) centered on a splash screen.

What to evaluate:
- does the mark feel confident and intentional at large size on a blank surface?
- is the spacing and centering optically correct (not just mathematically centered)?
- does the launch screen color match the icon's background or brand primary?

### 10. Share Sheet / Activity View

Show the icon in the iOS share sheet or Android share target list.

What to evaluate:
- the icon appears at small size in a horizontally scrolling row
- does it compete with messaging app icons (WhatsApp, Telegram, etc.)?
- is it distinguishable at this size?

## Competition Proximity Testing

### Direct Competitor Row

Create a row of 5-7 icons: the mark in the center, surrounded by its direct competitors.

What to evaluate:
- does the icon stand out?
- does it belong (same category feel)?
- does it avoid being confused with any competitor?
- does it avoid looking like a clone or derivative of a market leader?

### Category Wall

Create a grid of 20-30 icons from the same app category.

What to evaluate:
- color uniqueness within the category
- silhouette uniqueness within the category
- whether the mark uses or avoids category cliches
- whether the mark would be findable if a user scrolled past it quickly

### Confusion Test

Show the icon alongside the 3 most visually similar competitors.

What to evaluate:
- would a user who glances quickly confuse this icon with a competitor?
- what is the single strongest differentiator (color, shape, weight, density)?
- if the differentiator is only color, the mark is at risk (colors can shift between devices and modes)

## Environmental Testing

### Wallpaper Variation

Test against at least:
- pure white
- pure black
- a gradient (blue to purple or similar)
- a photographic wallpaper with mixed light/dark regions
- a busy wallpaper with many colors

The icon should never disappear into the wallpaper.
The icon's edge should always be discernible.

### Device Size Variation

Test on:
- iPhone SE / compact screen (smallest icon spacing)
- iPhone Pro Max / large screen (icons further apart)
- iPad (larger icon rendering with different spacing)
- Android compact phone
- Android tablet
- foldable device inner screen

The mark should feel proportioned correctly at all device scales.

### Dynamic Color / Theming

On Android with Material You:
- test the monochrome icon with several user-selected theme palettes
- verify the monochrome layer reads well in warm tones, cool tones, and neutral tones
- ensure the silhouette carries the identity regardless of applied tint

## Practical Rules

- context testing is not a final step — run lightweight context checks during concept selection, not only at the end
- early context tests can be rough composites (screenshot with the icon pasted in) — they do not need to be pixel-perfect mockups
- if a mark looks great in isolation but fails in context, the mark needs revision, not the context
- a mark that passes context testing but fails reduction testing is still not ready
- a mark that passes reduction testing but fails context testing is also not ready
- both must pass

## Context Testing Checklist

Before approving a direction as production-ready:
- [ ] iOS home screen tested (light wallpaper)
- [ ] iOS home screen tested (dark wallpaper)
- [ ] iOS home screen tested (busy wallpaper)
- [ ] Android home screen tested (light, dark)
- [ ] Android adaptive icon tested with circular mask
- [ ] Android adaptive icon tested with rounded-square mask
- [ ] App Store listing scale tested
- [ ] Google Play listing scale tested
- [ ] Notification icon tested (if applicable)
- [ ] Settings / 29pt tested
- [ ] Spotlight / search tested
- [ ] Splash screen tested
- [ ] Share sheet tested
- [ ] Direct competitor row tested
- [ ] Category wall reviewed
- [ ] Wallpaper variation tested (white, black, gradient, photo)
- [ ] Dynamic color / themed icon tested (Android)
