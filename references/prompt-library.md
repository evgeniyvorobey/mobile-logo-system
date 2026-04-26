# Prompt Library

Ready-to-use prompts for the mobile logo system skill. Concept prompts stop at the mandatory user-selection gate; after the user chooses a direction, the same brief can continue into craft pass, context testing, and production packaging.

All prompts work in both platforms:
- Codex: prefix with `Use $mobile-logo-system.`
- Claude: prefix with `/mobile-logo-system`

Prompts are written in English, but the skill is bilingual — you can translate or rewrite any prompt in your language and the skill will reply accordingly.

## 1. Premium App From Scratch

Full cycle: research, territories, scoring, craft pass, context test, wordmark, adaptive + monochrome, handoff.

```text
I am building a premium sleep and recovery app for adults aged 25-45. The product
helps users build better sleep habits through personalized routines, ambient
soundscapes, and sleep quality tracking. The tone is calm, trustworthy, and quietly
luxurious — not clinical or gamified.

Do the following:
1. Research current Apple and Android icon guidance before starting.
2. Define 3 concept territories. Each must state the construction method
   (grid type, proportion system), color rationale with assigned roles,
   silhouette logic, and why it survives at 29px and in monochrome.
3. Score all 3 directions using the full evaluation matrix including
   geometric precision, color craft, context survival, and longevity.
4. Recommend the strongest direction in one sentence and ask me to choose.
   Do not run the craft pass until I confirm the direction.
5. After I choose, run the craft pass: verify optical corrections,
   negative space, tangent continuity, and color accessibility (WCAG, CVD).
6. Show the chosen direction on an iOS home screen among 8 real competitor icons
   and in an App Store listing mockup.
7. Propose the wordmark: justify type classification, pairing logic,
   weight matching, and lockup construction.
8. Define the Android adaptive icon split and monochrome layer.
9. List 3 concrete improvement moves for the next refinement round.
```

## 2. Redesign a Generic Existing Icon

Audit current mark, cliche mapping, competitor row test, craft pass, monochrome + Material You.

```text
Our current app icon feels generic — it blends into the category and users
cannot find it on their home screen. The app is a personal finance tracker.

Do the following:
1. Audit the current icon and UI language in the project. Build a style snapshot:
   what is strong, what is weak, what is the redesign tolerance
   (evolutionary / adjacent / reset).
2. Identify specifically why the current icon is generic: category cliches used,
   silhouette uniqueness failure, color conformity.
3. Propose 3 directions — one evolutionary, one adjacent, one stretch.
   For each: state the construction grid, color harmony model, metaphor,
   and how it differentiates from the top 5 competitors in the category.
4. Run a competitor row test: place each direction among 7 real fintech
   app icons. Evaluate which stands out without losing category belonging.
5. Recommend the strongest direction, output the decision matrix with all
   11 scoring dimensions, and ask me to choose before refinement.
6. After I choose, run the full craft pass.
7. Produce the monochrome variant and validate it under Android themed
   icon tinting with warm, cool, and neutral palettes.
```

## 3. Icon System for a Productivity Tool

Geometric precision, 2-color limit, CVD, contrast pairing wordmark, silhouette test, 5-year durability.

```text
Design a logo system for a project management app aimed at small creative teams.
The product is fast, minimal, and opinionated — it is not trying to be Jira.
The visual language is geometric, high-contrast, and uses a monospace typeface
in the UI.

Requirements:
1. The icon must feel native among developer and design tools
   (Figma, Linear, Notion, Arc) — not among enterprise software.
2. Propose 3 concept territories. Each must use a documented construction grid
   (show the grid, not just describe it). Explain overshoot corrections
   and pixel alignment at 48px and 29px.
3. Color palette must use a maximum of 2 colors in the mark. Justify the
   harmony model. Test grayscale and CVD (protanopia, deuteranopia).
4. The wordmark must use a contrast pairing with the symbol. Justify
   type classification, specify kerning adjustments for each letter pair.
5. Recommend the strongest direction and ask me to choose before refinement.
6. After I choose, run the style-agnostic silhouette test: show the chosen
   direction as flat fill, outline only, and cut-out. All three must be recognizable.
7. Place the icon on both iOS and Android home screens. Test with circular
   and rounded-square masks on Android.
8. Answer the 5-year durability question honestly.
```

## 4. Premium Health and Wellness App

Cliche avoidance, 4 territories, G1 tangent check, negative space audit, color accessibility, measured lockups.

```text
Create a hi-end logo system for a women's health app focused on hormone tracking,
cycle insights, and holistic wellness. The brand must feel medically credible
but warm — not clinical, not generic wellness.

Key constraints:
- Must avoid: generic leaf, generic heart, pink-only palette, soft blob shapes
  (these are category cliches).
- Must feel: precise yet human, premium without being cold, science-backed
  without being sterile.
- Premium positioning is mandatory: quiet luxury, not loud branding.

Workflow:
1. Research current competitors in the category. Map the cliche landscape:
   what shapes, colors, and metaphors are overused.
2. Define 4 concept territories that deliberately avoid cliches.
   Each must state: construction method, color roles (primary/secondary/accent),
   metaphor, emotional job, primary risk, and longevity assessment.
3. Score using the full matrix. Reject any direction that fails the
   style-agnostic silhouette test or would look dated in 3 years.
4. Recommend the strongest direction and ask me to choose before refinement.
5. After I choose, run the craft pass on the chosen direction: geometric grid, optical corrections,
   negative space audit (fill counterforms with color — are they deliberate?),
   tangent continuity (G1 minimum), path cleanliness.
6. Define the color system: contrast ratios, CVD simulation, gradient-to-flat
   and gradient-to-monochrome fallbacks.
7. Wordmark: choose a typeface that signals medical credibility without
   clinical coldness. Justify the pairing. Construct horizontal and
   stacked lockups with measured proportions.
8. Context test: iOS home screen (light + dark + photo wallpaper),
   App Store listing, Settings at 29pt, competitor row of 7 icons.
9. Android adaptive icon: foreground/background split, safe-zone discipline,
   monochrome layer with intentional simplification.
10. Prepare the full handoff package.
```

## 5. Children's Educational App

Dual audience (parents + kids), CVD mandatory, corner radius progression, category wall.

```text
Design a logo and icon system for a children's reading app (ages 4-8).
Parents choose the app, children use it. The icon must appeal to both:
trustworthy and smart for parents, fun and inviting for kids.

Constraints:
- Must survive without relying on a character or mascot (the icon must work
  as geometry, not illustration).
- Maximum 3 colors. Must pass CVD simulation — children with color vision
  deficiency must still recognize the icon.
- Must work at 29px — children's app icons are often shown in parental
  control lists at small sizes.

Steps:
1. Audit the category: what do top children's education apps look like?
   Where is the white space for differentiation?
2. Define 3 territories. For each: metaphor, construction grid,
   color roles with accessibility rationale, reduction rule at 29px.
3. Score the directions, recommend the strongest one, and ask me to choose.
   The recommended direction must pass: small-size test, monochrome test,
   CVD test, and the "would a parent trust this?" test.
4. After I choose, run the craft pass. Pay special attention to corner radius progression
   (children's apps often use generous radii — make this intentional, not random).
5. Wordmark: choose a typeface that is friendly but not babyish.
   Parents should not feel embarrassed to have this on their phone.
6. Context test: place among real children's app icons on a home screen.
   Also test in the App Store "Kids" category listing.
7. Android monochrome: verify the shape reads clearly under Material You tinting.
8. Prepare the handoff package with all platform variants.
```

## 6. Quick Audit and Production Fix

No redesign — evaluation only. Prioritized punch list ordered by shipping risk.

```text
Audit the current logo system in this project and tell me if it is actually
ready to ship. Do not redesign anything — just evaluate what exists.

Check:
1. Reduction: test at 1024px, 180px, 120px, 60px, 48px, 29px.
   Log what survives, what collapses, what is optional.
2. Geometric craft: is the mark built on a grid? Are optical corrections
   applied? Are there tangent breaks or unnecessary anchor points?
3. Color: are contrast ratios sufficient? Does grayscale conversion
   preserve hierarchy? Does the palette survive CVD simulation?
4. Monochrome: does the Android monochrome layer exist?
   Is it a deliberate design or an auto-derived grayscale?
5. Context: place the icon on an iOS and Android home screen among
   real competitors. Does it stand out? Does it belong?
6. Longevity: run the style-agnostic silhouette test (flat, outline, cut-out).
   Is the identity structural or effect-dependent?
7. Wordmark: is the pairing justified? Is kerning correct at logo scale?
8. Package completeness: list every deliverable as pass / revise / missing.

Output a prioritized punch list ordered by shipping risk.
Do not suggest a redesign unless something is fundamentally broken.
```

## 7. Android-First With Monochrome Focus

Monochrome-first workflow, 5 Material You palettes, all mask shapes, parallax test, iOS secondary.

```text
We are shipping an Android-first utility app (file manager / system tool category).
The icon must be optimized for Android adaptive icons and Material You theming.
iOS is secondary but must work.

Priority order:
1. The monochrome / themed icon layer is the primary deliverable, not an afterthought.
   Design it first: a single-color silhouette that carries the full identity.
2. Build the full-color version from the monochrome foundation, not the other way around.
3. Foreground/background split: the foreground must survive all mask shapes
   (circle, squircle, rounded square, teardrop). Test parallax shift (+/- 4dp).
4. Construction: use a grid that maps cleanly to 48dp (mdpi) and 108dp canvas.
   Show the safe zone (72dp). Apply optical corrections.
5. Color: maximum 2 colors on the foreground layer. The background must be a single
   flat color that works with all system mask shapes.
6. Test the monochrome icon under 5 different Material You palettes
   (warm red, cool blue, neutral gray, earth green, vibrant purple).
7. Context: Android launcher with circular mask, launcher with squircle mask,
   themed icon row, notification bar silhouette.
8. iOS adaptation: adjust the composition for the squircle mask. Verify at 29pt.
9. Wordmark: only if needed. The app name in the launcher is usually sufficient
   for utility apps.
```

## 8. Brand Refresh With Equity Preservation

Structural vs stylistic separation, recognizability criterion, old/new side-by-side, evolutionary only.

```text
Our app has 2M+ active users. The current icon is recognizable but looks dated —
it was designed 4 years ago and relies on gradients and glow effects that feel
like a previous design era.

Critical constraint: users must still find their app on the home screen after
the update. The silhouette must remain recognizable. The refresh is evolutionary,
not a reset.

Steps:
1. Audit the current mark. Document: what is the recognizable silhouette?
   What elements are carrying the identity (shape, color, internal structure)?
   What elements are purely stylistic (gradients, shadows, effects)?
2. Separate structural identity from stylistic treatment:
   render the current icon as a flat single-color fill. This is the equity
   that must survive.
3. Propose 3 evolutionary refinements. Each must:
   - preserve the core silhouette within a recognizability threshold
   - remove dated stylistic elements
   - improve geometric construction (rationalize freehand curves onto a grid)
   - improve small-size survival (remove detail that clogs at 29px)
   - modernize without chasing the current trend
4. Score using the full matrix. Add a specific "recognizability preservation"
   criterion: would an existing user find this icon after the update?
5. Recommend the strongest refinement and ask me to choose before craft work.
6. After I choose, run the craft pass on the chosen refinement: grid construction, optical corrections,
   negative space, color accessibility, path cleanliness.
7. Context test: show old and new icons side by side on a home screen.
   The transition should feel like the same brand evolved, not a different app.
8. Define the monochrome path. If the old icon never had one, explain
   what simplification was required.
9. Prepare the handoff package with before/after comparison notes.
```
