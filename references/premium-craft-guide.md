# Premium Craft — Full Guide

This is the full educational reference for premium craft. The runtime checklist is in `premium-craft.md`.

## Negative Space As Primary Design Tool

In hi-end marks, negative space is not leftover — it is designed with the same precision as filled shapes.

### Counterform Identity

The shapes created by the empty space inside and around the mark should be intentional.

Test: fill only the negative space with a contrasting color. Does the resulting shape feel deliberate? Does it have its own logic, its own rhythm?

In the best marks, the negative space tells a second story or reinforces the primary one.

### Figure-Ground Ambiguity

Some hi-end marks use intentional ambiguity where the viewer can read the mark as either positive or negative.

When to use: when the brand benefits from depth of meaning, discovery, or intellectual engagement.

Risk: if the ambiguity is too subtle, no one notices it. If it is too obvious, it becomes a gimmick. The threshold is: a casual viewer sees one reading, a focused viewer discovers the second.

### Trapped Space

Small enclosed areas of negative space within a mark.

At hi-end quality:
- trapped spaces must be large enough to remain visible at 60px
- trapped spaces must have clean, deliberate shapes (not accidental byproducts)
- if a trapped space clogs at small size, the mark needs a simplified version for that size

Rule: every trapped space should pass the "is this intentional or accidental?" test.

### Breathing Room

The ratio of filled space to empty space within the mark's bounding box.

Guidelines:
- marks that are too dense (>70% filled) feel heavy, aggressive, or cluttered
- marks that are too sparse (<30% filled) feel weak, unfinished, or invisible at small size
- a hi-end mark typically sits at 40-60% fill ratio, with the empty space contributing to the form

The breathing room inside the icon canvas (padding between mark edge and icon border) follows the same principle. Apple and Android both expect the mark to not fill the entire canvas.

## Material Language

Material language adds perceived physical quality to a flat shape. It communicates craftsmanship, care, and premium intent without adding structural complexity.

### Lighting Direction

All material effects must share a single light source.

Standard choices:
- top-center light: neutral, balanced, no directional bias
- top-left light: the default in most design systems, creates familiar shadow direction

Rules:
- choose one direction and apply it to every element in the mark
- shadows fall opposite the light source
- highlights face the light source
- secondary reflections are subtler than primary highlights

### Subtle Depth

Hi-end depth is almost invisible. It should be felt, not seen.

Techniques:
- inner shadow at 0.5-2% opacity: barely visible lift
- soft gradient with 3-5% luminance shift: surface curvature without obvious gradient
- background-to-foreground layering through slight value difference

Anti-patterns:
- drop shadow with visible offset: feels dated since 2013
- bevel/emboss: almost never appropriate for modern mobile icons
- 3D extrusion: creates a toy-like quality unless the brand is explicitly playful

### Edge Treatment

The boundary between the mark and its background communicates quality.

- sharp, clean edge: technical, precise, confident
- slightly feathered edge (0.5-1px at 1024px): softer, warmer, approachable
- hard-cut with a subtle inner glow: premium, slightly elevated from the surface

The edge must be consistent around the entire mark. Mixed edge treatments (sharp on one side, soft on another) read as errors.

### Surface Texture

Texture at icon size is almost always a mistake. At 60px, any texture becomes noise.

Exception: a very subtle grain or noise overlay (1-3% opacity) applied uniformly can add materiality when viewed at 120px+ without harming smaller renders. This must be validated at every target size.

Rule: if you cannot tell the texture is there at 60px, it is safe. If you can tell, remove it.

## Internal Complexity vs External Simplicity

### The Rule

The outer silhouette must be simple and instantly memorable.
The interior can contain deliberate complexity that rewards closer inspection.

### Why This Works At Icon Size

At 29px, the viewer sees only the outer silhouette. That silhouette must carry the entire identity.
At 120px+, the viewer can appreciate the interior craft.

If the outer silhouette is complex, the mark fails at small size.
If the interior is empty, the mark feels cheap at large size.

### Layered Meaning

A hi-end mark often encodes more than one idea:
- the primary reading (visible to everyone)
- a secondary reading (visible upon inspection)
- a structural reference (the geometry echoes the product's UI, the brand's heritage, or a cultural symbol)

These layers should not compete. The primary reading must be clear.

## Restraint Principles

### Maximum Color Count

In the mark itself (not counting the icon background):
- 1 color: maximum restraint, confident, works in all contexts
- 2 colors: the standard for hi-end marks, allows internal hierarchy
- 3 colors: the practical maximum for icon-size marks, must be justified by structural roles

More than 3 colors in a mark at icon size almost always reads as consumer/playful rather than premium.

### Single Focal Point

The mark should have one element that the eye lands on first. Not two. Not three.

Test: where does the eye go first? If the answer is "everywhere" or "I am not sure," the mark lacks hierarchy.

### Gradient Restraint

A hi-end gradient:
- uses one direction
- uses two stops (occasionally three)
- covers a luminance range of 10-25% (not 0% to 100%)
- serves a purpose: suggesting curvature, light, or depth

A cheap gradient:
- uses multiple directions
- uses many stops creating rainbow effects
- covers the full luminance range
- exists because "flat was boring"

### Detail Budget

Set a detail budget: the maximum number of distinct visual elements in the mark.
Suggested limits:
- mark at icon size: 3-5 distinct elements maximum
- wordmark lockup: the mark elements + the wordmark as one element = 4-6 total

## Craftsmanship Signals

### Consistent Stroke Terminals

If the mark uses strokes, every stroke terminal must follow the same treatment: all round, all flat/butt, or all angled at a consistent angle. Mixed terminals read as a drafting error.

### Deliberate Corner Radius Progression

Every corner radius should come from the same scale. Outer corners are typically larger than inner corners. The radius progression should create a visual rhythm, not a random assortment.

### Intentional Weight Distribution

The visual weight should be distributed according to the mark's meaning:
- centered weight: stability, balance, protection
- top-heavy: authority, overhead, coverage
- bottom-heavy: grounded, sturdy, foundation
- left-heavy (LTR): origin, memory, heritage
- right-heavy (LTR): forward motion, progress, future

### Precise Tangent Relationships

Where curves meet, junction quality matters:
- G0 (positional continuity): acceptable only when a sharp corner is intended
- G1 (tangent continuity): smooth, professional — minimum for hi-end
- G2 (curvature continuity): smoothest possible, preferred for organic shapes

### Path Cleanliness

Vector paths should use the minimum number of anchor points. Signs of unclean paths:
- unnecessary anchor points on straight segments
- handles not aligned to the curve's natural direction
- overlapping paths instead of a single combined path
- visible artifacts where paths were hastily merged

## Longevity Assessment

### Trend Resistance Test

Ask:
- is this mark's distinctive quality structural or stylistic?
- if the current trend disappears tomorrow, does the mark still work?
- could this mark have existed 5 years ago and 5 years from now?

### Timeless Foundations

Marks that last share: simple outer silhouette, meaningful geometry, internal logic independent of rendering fashion, a shape describable in one sentence.

### Style-Agnostic Silhouette Test

Render the mark as: (1) flat single-color fill, (2) outline only, (3) cut-out silhouette.
If recognizable in all three, identity lives in shape. If only one, identity is fragile.

### The 5-Year Durability Question

Will this mark look like a product of its specific year, or could it be from any year in a broader range?

## Anti-Patterns

- metallic textures that become flat-gray noise at small sizes
- excessive beveling
- drop shadows as primary depth
- glossy highlight bubbles (dated since iOS 7, 2013)
- gradient banding
- ornamental borders adding weight without meaning
- sparkles, lens flares, glow effects as identity elements
- more than one shadow per element
- decorative detail in the outer silhouette that clogs at small sizes
- effects that only render correctly on high-DPI screens
