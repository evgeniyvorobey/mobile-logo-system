# Premium Craft

Use this file when the work demands hi-end quality, premium positioning, or when evaluating whether a mark achieves true craftsmanship rather than surface decoration.

Premium is not an effect applied on top. It is a structural property of the mark itself.

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

This is the core principle of hi-end icon work.

### The Rule

The outer silhouette must be simple and instantly memorable.
The interior can contain deliberate complexity that rewards closer inspection.

Example:
- outer shape: a simple, confident geometric form
- inner detail: a carefully constructed countershape, a meaningful intersection, a secondary symbol revealed by negative space

### Why This Works At Icon Size

At 29px, the viewer sees only the outer silhouette. That silhouette must carry the entire identity.

At 120px+, the viewer can appreciate the interior craft. That craft makes the mark feel rich and considered rather than generic.

If the outer silhouette is complex, the mark fails at small size.
If the interior is empty, the mark feels cheap at large size.

### Layered Meaning

A hi-end mark often encodes more than one idea:
- the primary reading (visible to everyone)
- a secondary reading (visible upon inspection)
- a structural reference (the geometry echoes the product's UI, the brand's heritage, or a cultural symbol)

These layers should not compete. The primary reading must be clear. The secondary layers are discoveries, not puzzles.

## Restraint Principles

Premium means knowing what to leave out.

### Maximum Color Count

In the mark itself (not counting the icon background):
- 1 color: maximum restraint, confident, works in all contexts
- 2 colors: the standard for hi-end marks, allows internal hierarchy
- 3 colors: the practical maximum for icon-size marks, must be justified by structural roles

More than 3 colors in a mark at icon size almost always reads as consumer/playful rather than premium.

### Single Focal Point

The mark should have one element that the eye lands on first. Not two. Not three.

Everything else in the mark supports that focal point through contrast, framing, or negative space.

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

Set a detail budget: the maximum number of distinct visual elements (shapes, intersections, color changes) allowed in the mark.

Suggested limits:
- mark at icon size: 3-5 distinct elements maximum
- wordmark lockup: the mark elements + the wordmark as one element = 4-6 total

If you need to count, the mark is probably too complex.

## Craftsmanship Signals

These are the details that separate hi-end work from competent work.

### Consistent Stroke Terminals

If the mark uses strokes, every stroke terminal (endpoint) must follow the same treatment:
- all round terminals, or
- all flat/butt terminals, or
- all angled terminals at a consistent angle

Mixed terminals read as a drafting error.

### Deliberate Corner Radius Progression

Every corner radius in the mark should come from the same scale (see geometric-craft.md).

Additionally:
- outer corners are typically larger than inner corners
- the radius progression should create a visual rhythm, not a random assortment
- if a mark has 3 corners with radius 8px and 1 corner with radius 6px, the 6px looks like a mistake

### Intentional Weight Distribution

The visual weight (density of filled vs empty area) should be distributed according to the mark's meaning:
- centered weight: stability, balance, protection
- top-heavy: authority, overhead, coverage
- bottom-heavy: grounded, sturdy, foundation
- left-heavy (in LTR context): origin, memory, heritage
- right-heavy (in LTR context): forward motion, progress, future

Unintentional weight imbalance reads as carelessness.

### Precise Tangent Relationships

Where curves meet other curves, or curves meet straight edges, the junction quality matters:
- G0 (positional continuity): curves touch but have a visible angle change — acceptable only when a sharp corner is intended
- G1 (tangent continuity): curves share a tangent at the junction — smooth, professional
- G2 (curvature continuity): curves share both tangent and curvature rate — the smoothest possible junction, used in automotive and industrial design

For hi-end marks, G1 is the minimum. G2 is preferred for organic or flowing shapes.

### Path Cleanliness

The vector paths should use the minimum number of anchor points to describe the shape.

Signs of unclean paths:
- unnecessary anchor points on straight segments (a straight line needs exactly 2 points)
- handles that are not aligned to the curve's natural direction
- overlapping paths instead of a single combined path
- visible artifacts where paths were hastily merged

Clean paths scale perfectly. Dirty paths create rendering artifacts at extreme sizes.

## Longevity Assessment

A hi-end mark should not look dated within 2-3 years.

### Trend Resistance Test

Ask:
- is this mark's distinctive quality structural (shape, proportion, negative space) or stylistic (gradient style, shadow style, texture trend)?
- if the current design trend that inspired this mark disappears tomorrow, does the mark still work?
- could this mark have existed 5 years ago without looking ahead of its time? Could it exist 5 years from now without looking outdated?

Structural distinctiveness survives trends. Stylistic distinctiveness expires with them.

### Timeless Foundations

Marks that last share these properties:
- simple outer silhouette
- meaningful geometry
- internal logic that does not depend on rendering fashion
- a shape that can be described in one sentence

### Style-Agnostic Silhouette Test

Render the mark as:
1. a flat single-color fill
2. an outline only
3. a cut-out silhouette (black on white)

If the mark is recognizable in all three renderings, its identity lives in the shape, not in styling.
If it is only recognizable in one rendering, the identity is fragile and trend-dependent.

### The 5-Year Durability Question

Imagine this mark appearing in a design retrospective article in 5 years.

- will it look like a product of its specific year (the 2024 gradient, the 2025 glassmorphism), or will it look like it could be from any year in a broader range?
- timeless marks can appear in a retrospective without embarrassment
- trend-locked marks date their brand

## Anti-Patterns

These signal non-premium work:

- metallic textures that become flat-gray noise at small sizes
- excessive beveling that makes the mark feel like a game icon
- drop shadows as the primary depth mechanism
- glossy highlight bubbles (dated since iOS 7, 2013)
- gradient complexity that creates visible banding on screens
- ornamental borders or frames that add weight without meaning
- sparkles, lens flares, or glow effects as identity elements
- more than one shadow per element
- shadows that are darker and more visible than the highlight
- decorative detail in the outer silhouette that clogs at small sizes
- effects that only render correctly on high-DPI screens

## Premium Craft Checklist

Before approving a mark as hi-end quality:
- [ ] negative space shapes are deliberate and clean
- [ ] counterforms pass the "fill the negative space" test
- [ ] fill ratio is in the 40-60% range (or intentionally outside it with justification)
- [ ] single consistent light direction throughout the mark
- [ ] depth effects are subtle (felt, not seen)
- [ ] edge treatment is consistent around the entire mark
- [ ] outer silhouette is simple and memorable
- [ ] interior rewards closer inspection without being necessary for recognition
- [ ] color count is 3 or fewer in the mark itself
- [ ] single focal point confirmed
- [ ] gradient (if any) is restrained and has a defined flat fallback
- [ ] detail budget respected (3-5 distinct elements maximum)
- [ ] stroke terminals consistent
- [ ] corner radii from a single scale
- [ ] weight distribution is intentional
- [ ] curve junctions are G1 or better
- [ ] vector paths are clean (minimum anchor points)
- [ ] style-agnostic silhouette test passed (flat, outline, cut-out)
- [ ] 5-year durability question answered honestly
- [ ] no anti-patterns present
