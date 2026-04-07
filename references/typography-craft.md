# Typography Craft

Use this file when designing, pairing, or evaluating a wordmark alongside a symbol.

A wordmark is not a font choice. It is a piece of engineered lettering that must hold its own as an identity element while supporting the symbol without competing with it.

## Type Classification For Logo Work

Know the structural family before choosing:

### Geometric Sans

Construction: built from circles, squares, and uniform strokes.
Character: modern, clean, rational, tech-friendly.
Examples of the style: Futura, Avenir, Montserrat, Product Sans.
Best paired with: geometric symbols, clean silhouettes, minimal marks.
Risk: can feel cold, generic, or startup-template if not customized.

### Humanist Sans

Construction: stroke modulation inspired by calligraphy, but without serifs.
Character: warm, approachable, readable, human.
Examples of the style: Gill Sans, Frutiger, Myriad, Source Sans.
Best paired with: organic symbols, warm/friendly brands, health and lifestyle.
Risk: can feel too soft for premium or tech positioning.

### Neo-Grotesque

Construction: uniform stroke weight, closed apertures, neutral shapes.
Character: neutral, serious, professional, scalable.
Examples of the style: Helvetica, Arial, Univers, Aktiv Grotesk.
Best paired with: confident symbols that carry personality so the type can stay quiet.
Risk: so neutral it adds nothing — the pairing needs the symbol to do the identity work.

### Slab Serif

Construction: serifs with uniform thickness, often geometric base.
Character: sturdy, grounded, editorial, confident.
Examples of the style: Rockwell, Clarendon, Roboto Slab, Zilla Slab.
Best paired with: bold or chunky symbols, brands with authority or heritage intent.
Risk: can feel heavy at small sizes. Serifs may clog at 29px if the wordmark is part of the icon.

### Modern Serif (Didone)

Construction: extreme thick-thin contrast, unbracketed hairline serifs.
Character: elegant, editorial, luxury, fashion.
Examples of the style: Didot, Bodoni, Playfair Display.
Best paired with: refined or luxury symbols, fashion, beauty, editorial brands.
Risk: hairline strokes disappear at small sizes. Only viable when the wordmark will never appear below ~14px rendered height.

### Display / Custom

Construction: bespoke lettering designed specifically for the brand.
Character: unique, ownable, non-reproducible.
When to use: when the brand can invest in custom lettering and needs maximum differentiation.
Risk: expensive, hard to maintain, and must be drawn by someone who understands optical spacing.

## Symbol-Type Pairing Principles

### Contrast Pairing

The symbol and wordmark come from different structural families.

Example: a geometric symbol with a humanist sans wordmark.

Why it works: the contrast creates visual interest and prevents the lockup from feeling monotonous. Each element has a clear role — the symbol carries the visual identity, the type carries the name.

When to use: when the symbol has strong personality and the type should complement without copying it.

### Harmony Pairing

The symbol and wordmark share the same structural logic.

Example: a geometric symbol with a geometric sans wordmark, using the same stroke widths and corner radii.

Why it works: the lockup feels like a unified system rather than two separate elements.

When to use: when the brand identity is about consistency, precision, or technical confidence.

### Weight Matching

The visual weight of the wordmark must match the visual weight of the symbol.

Weight is determined by:
- stroke thickness
- counter size (internal white space in letters)
- overall density (black-to-white ratio)

Test: place the symbol and wordmark side by side. Squint. They should feel like they belong together in terms of darkness/lightness.

If the symbol is bold and dense, the wordmark should be medium to semibold, not thin.
If the symbol is light and airy, the wordmark should be light to regular, not black.

### Size Relationship

The wordmark height should relate to the symbol height by a deliberate ratio.

Common ratios:
- wordmark cap-height = symbol height: equal partnership
- wordmark cap-height = ~60-70% of symbol height: symbol-dominant (most common for app logos)
- wordmark cap-height = ~40-50% of symbol height: symbol is the primary mark, wordmark is subordinate

Choose the ratio based on whether the brand leads with the symbol or the name.

## Optical Spacing

### Kerning Principles

Default font kerning is optimized for body text, not for display-size wordmarks.

At logo scale, every letter pair must be manually evaluated:

1. round-round pairs (OO, CO, CG): tighten slightly, the curves already create visual proximity
2. straight-straight pairs (HI, MN, IL): standard spacing, the parallel edges define a clear channel
3. round-straight pairs (OI, DO, CL): between the two above
4. open pairs (LA, LT, VA, WA, TA): tighten significantly, the diagonal or overhang creates excess visual space
5. problem pairs (rn vs m, cl vs d): ensure they do not merge into an incorrect letter at small size

### Tracking (Overall Spacing)

- tight tracking: dense, confident, premium. Works at larger sizes. Risky at small sizes.
- standard tracking: safe, readable. Works at all sizes.
- loose tracking: open, airy, luxury or editorial feel. Works at larger sizes. Can feel scattered at small sizes.

For icon lockups (where the wordmark appears inside or near the icon at small sizes): prefer slightly loose tracking to prevent letters from merging.

For external branding (app name in store listing, marketing): tighter tracking is usually appropriate.

### Baseline Alignment vs Optical Alignment

When the wordmark sits next to the symbol horizontally:
- do not simply align baselines mathematically
- align so the visual center of the wordmark matches the visual center of the symbol
- if the wordmark has descenders (g, y, p, q, j), the baseline should be slightly higher to compensate for the visual weight below

## Lockup Construction

### Horizontal Lockup

Symbol left, wordmark right (LTR reading order).

Construction:
1. set the symbol at its natural size
2. set the wordmark at the chosen size ratio
3. set the gap between symbol and wordmark to a value from the spacing scale
4. verify: the gap should be large enough that the two elements do not merge, but small enough that they read as one unit

Common gap: 50-100% of the wordmark cap-height.

### Stacked Lockup

Symbol above, wordmark below.

Construction:
1. center the symbol horizontally
2. center the wordmark below
3. gap between symbol bottom and wordmark cap-height: 30-60% of the wordmark cap-height
4. the wordmark width should not exceed the symbol width by more than ~30%, or the lockup loses visual unity

### Icon-Only

No wordmark. The symbol must carry full identity.

Use when:
- the app icon at small sizes
- favicon
- notification icon
- any surface where the wordmark would be illegible

### Wordmark-Only

No symbol. The wordmark is the entire identity.

Use when:
- horizontal space is available but vertical space is not
- the brand is name-first (the name is more recognizable than the symbol)
- splash screens, marketing headers

### Clear Space

Define clear space as a function of the lockup, not as an arbitrary pixel value.

Standard approach: clear space = cap-height of the wordmark (or the height of a key element in the symbol) on all four sides.

Nothing — no text, no other graphic, no edge — may enter the clear space zone.

## Case Strategy

### All Lowercase

Character: friendly, approachable, modern, casual.
When to use: consumer apps, social, lifestyle, creative tools.
Risk: can feel unserious for finance, enterprise, or healthcare.

### Title Case

Character: balanced, professional, standard.
When to use: most product brands. Safe default.
Risk: unremarkable if the type choice is also unremarkable.

### ALL UPPERCASE

Character: bold, authoritative, structured.
When to use: luxury, fashion, sports, enterprise, security.
Risk: can feel aggressive. At small sizes, uppercase words are harder to scan than mixed case because of uniform height.

### Custom Case (e.g., camelCase, single-cap)

Character: tech, developer tools, unique.
When to use: when the product name naturally uses unusual casing (e.g., "macOS", "iPhone").
Risk: inconsistent application across platforms and marketing materials.

## Wordmark Customization

### When To Customize

Customize letterforms when:
- a specific letter pair creates an ugly collision or gap that kerning alone cannot fix
- the brand needs a distinctive typographic feature (a ligature, a modified terminal, a branded letter)
- the wordmark must be legally distinct from the base typeface

### Safe Customizations

- adjusting a single terminal (e.g., rounding a stroke end)
- creating a ligature between two letters
- modifying the dot on an 'i' or 'j' to echo the symbol
- adjusting descender or ascender length for lockup fit

### Dangerous Customizations

- changing fundamental letter proportions (readers will sense something is wrong)
- removing recognizable letter features (e.g., removing the crossbar from 'A')
- adding decorative elements that do not survive at small size

Rule: customization should be visible at medium size and invisible at small size. If the customization creates a legibility problem at 14px rendered height, revert it.

## Practical Checklist

Before approving a wordmark:
- [ ] type classification identified and justified
- [ ] pairing logic with symbol stated (contrast vs harmony)
- [ ] visual weight matches symbol weight
- [ ] size ratio defined (cap-height to symbol height)
- [ ] every letter pair visually kerned at logo scale
- [ ] tracking decision justified (tight / standard / loose)
- [ ] horizontal lockup constructed with measured gap
- [ ] stacked lockup constructed with measured gap
- [ ] clear space defined as a function of cap-height
- [ ] case strategy chosen and justified
- [ ] wordmark tested at minimum legible size (typically 12-14px rendered height)
- [ ] wordmark tested in the icon lockup at 60px and 29px (if it appears in the icon)
- [ ] customizations documented and tested at small size
- [ ] font license verified for intended use (app embedding, marketing, web)
