# Editorial-comic house style for image models

## Purpose and priority

Use this file only for a conceptual research figure: pipeline, method overview, architecture,
mechanism, or data-flow diagram in which no visual property encodes a measured quantity.

The project's `TECHNICAL_FIGURE_BRIEF.md` is authoritative for scientific meaning, topology,
labels, examples, and result exclusions. This file is authoritative for visual treatment.
An explicit user aesthetic preference may override this style, but never the scientific brief.

The target is a **playful editorial-comic scientific infographic**. The initial structure
pass uses near-white neutral-gray region fills; soft color may remain in icons and small
accents. Add soft region background colors only in a later explicit color-edit invocation.
The figure should feel like a polished illustrated magazine roadmap or a high-quality
educational comic, without candy-bright colors or large dark background fills.

---

## 1 · Composition

- Build the figure as **three to six named regions**, not as one long row of boxes.
- Give each region a clear visual identity: rounded or irregular comic-panel boundary,
  near-white neutral-gray background field, numbered badge, bold banner, and a short local
  micro-flow. Keep the panel fill achromatic during the initial structure pass.
- The global layout is a grid, stack, or asymmetric editorial composition. Inside one region,
  a short left-to-right or top-to-bottom flow is fine.
- Distinguish named regions from the smaller nodes joined by arrows: in `A → B`, A and B are
  two nodes, whether they sit in the same region or different ones. Give each node a clear
  internal hierarchy and enough room for its short label and icon; keep fuller method detail
  in the paired description file rather than adding prose inside the node. Do not let one
  large icon occupy most of the node.
- Show real branches, parallel operations, joins, feedback loops, optional paths, and typed
  boundaries. Never serialize mutually exclusive or parallel operations just to simplify the
  layout.
- Keep every necessary logical relationship legible while using as few arrow lines as the
  topology permits. Remove duplicate or decorative connectors; group related nodes or use
  clearly shared trunks where they reduce clutter without changing meaning. Arrange nodes
  and route arrows so no arrow paths cross. An intentional, clearly connected branch/join
  or shared-trunk junction is allowed; a path passing across another is not. If the first
  arrangement forces a crossing, change the arrangement instead of accepting the crossing.
- Non-uniform panels are encouraged. Give the scientifically important branch more room.
- Do not add a standalone overall title banner. Start directly with Region 1; the paper
  caption supplies the figure title.
- No landscapes, roads, trees, or exterior signboards.
- Crop tightly around the numbered method regions.
- Decorative elements must stay outside arrow corridors and must not resemble nodes, ports,
  evidence tokens, outcomes, or data-flow arrows.

## 2 · Color: neutral panels first, soft color later

- **Initial invocation:** use the same pure, achromatic near-white gray for region background
  fills (for example `#F7F7F7`), without hue, colored gradients, or pastel tint. Keep the page
  white or near white and distinguish regions with boundaries, badges, and layout. This is the
  selected structural base to inspect before choosing panel colors.
- **Later explicit “add background colors” invocation:** edit only those region fills. Use a
  small coordinated set of **soft, lightly saturated colors**. Pale coral, peach, butter
  yellow, sage or mint, powder blue, and lavender are possible choices, not a quota. Related
  regions may reuse a color; they need not all differ. Give the colored figure enough light
  variation that its background is not one uniform color.
- White may be used for the page or text cards. Keep the panels distinguishable and readable
  at thumbnail size without making their fills dark or saturated.
- Use near-black or deep navy for text and outlines where needed for contrast, not for large
  background fields. Outlines may be more expressive than ordinary academic line art.
- Reserve stable semantic roles where the science needs them: for example, one color for lane
  A, another for lane B, and muted amber for the principal flow. Keep those mappings
  consistent from input to output. Do not alter those existing science-bearing colors in
  the later panel-fill edit.
- Soft decorative colors are allowed for banners, stickers, and icons, but they must not imply
  nonexistent experimental categories or measured differences.
- Color the icons themselves while preserving contrast with their backgrounds.

## 3 · Comic depth and shape grammar

- Use rounded sticker capsules, playful banners, chunky tabs, speech bubbles, file cards,
  ribbons, tags, badges, and varied silhouettes.
- Keep region background fills flat in the initial neutral stage. Gentle cel shading, small
  highlights, or shallow offset shadows may add depth to icons and other non-panel elements.
- Keep the rendering illustrative and flat enough for a paper figure. Avoid photorealism,
  glossy product-render surfaces, glassmorphism, metallic materials, deep perspective, and
  heavy 3-D extrusion.
- Dashed boundaries mean a set, phase, or region; solid boundaries mean a single object.
- Scientific arrows use one unmistakable visual grammar: solid path, clear triangular head,
  high contrast, and consistent direction. Make arrow strokes slightly thinner than panel
  and icon outlines, while keeping them visible at final paper width. Comic motion ticks may
  decorate an arrow but may never create a second ambiguous arrow.
- Use playful asymmetry without sacrificing alignment of the scientific graph.

## 4 · Icons: varied nouns, one family

- Give every major noun and operation a recognizable glyph. A labeled rectangle without a
  visual metaphor should be the exception.
- For a normal five-region figure, aim for **at least twelve visibly different icon
  silhouettes** when the method contains that many distinct concepts.
- Do not reuse a document sheet or folder for unrelated concepts merely because it is easy.
  Validation, provenance, pairing, normalization, scoring, diagnosis, branching, packaging,
  and export should look different from one another.
- Keep one coherent illustration family: expressive flat icons with thick outlines, simple
  interior color blocks, and optional light cel shading.
- Keep avatar heads, cartoon people, and other icons modest in size within their nodes. If a
  person or user is part of the method, a small flat avatar may identify that role; do not add
  large mascot-like characters just to fill space.
- Prefer a refined arrangement of small, meaningful elements over an oversized simple glyph.
  Build visual hierarchy through scale, alignment, grouping, and carefully drawn small details.
  Where it clarifies a real object or operation, two or more small icons may lightly overlap
  as one composite illustration. This is optional, not a pattern every node must repeat.
  Keep labels readable, arrows clear, and composite icons from implying extra method stages.
  Do not invent scientific detail to make a node look fuller.
- Useful vocabulary includes document stacks, file-type cards, mapping tags, parser funnels,
  checklists, shields or fingerprints, chain links, paired strips, sliders, targets, boundary
  brackets, token chips, balances, magnifiers, matrices, clipboards, forks, satchels, laptops,
  report folders, JSON pages, HTML pages, ribbons, lightbulbs, and gauges.
- An icon nobody can name is worse than a word. Keep a short label when the glyph could be
  ambiguous.

## 5 · Text

- Make the diagram readable with as little text as the scientific topology permits. Keep
  essential region and node names; label an arrow only when its direction or type is unclear.
  Put full explanations in the paired paper-body description file for the writing agent.
- Keep each numbered badge and its English region title compact. Their text may be only
  slightly larger than primary node labels (at most about 110%); let weight, tint, and
  placement distinguish the heading. Do not enlarge the numeral or make a tall banner that
  takes space needed by node labels, details, icons, or arrows.
- Block labels are short noun phrases, normally one to four words.
- Omit explanatory sentences and default to **no** explanatory line within a region. Add
  at most one short method-only line only when labels, icons, and arrows cannot make a
  necessary scientific distinction clear; it must not report a result.
- Use a bordered callout with documentation-safe example content only when the actual
  example is indispensable to understanding an operation. Quote it exactly and distinguish
  it from a result. Otherwise describe the example in the paired file and paper body.
- Use bold, friendly editorial typography with high contrast. Monospaced text is reserved for
  code identifiers and verbatim strings.
- Spell every supplied label exactly. Do not invent extra claims, slogans, or technical terms.

## 6 · Controlled decoration

- Allowed inside region boundaries: corner stickers, small stars or spark marks, motion ticks,
  tape tabs, scalloped banners, tiny non-semantic doodles, and colored edge accents.
- Decorative accents must not consume a separate row or margin.
- Decoration should make the page feel authored and energetic at first glance.
- Decoration may not cross scientific arrows, conceal arrowheads, split a label, or introduce
  a shape that looks like an unlabelled computation or output.
- Keep the central method graph denser than the decorative margins. Cartoon energy is not a
  license for illegibility.

## 7 · Scientific and visual prohibitions

- No experimental result, measured value, score, rate, percentage, proportion, confidence
  interval, sample count, dataset size, success/failure total, comparison, ablation, error
  analysis, or posterior conclusion.
- No visual encoding of a measured quantity through position, size, angle, length, or color.
- No claim that the method is better, more accurate, more successful, or empirically superior.
- No topology invented for visual convenience. No decorative connector may look causal.
- No photograph, realistic person, cinematic scene, heavy 3-D, strong glow, deep drop shadow,
  glossy interface mockup, watermark, logo, citation, or decorative legend.
- No tiny text that becomes unreadable at the intended paper width.

---

## 8 · Paste-ready prompt block

For the initial neutral-structure invocation, append this after the scientific brief has
been converted into exact region and arrow instructions:

> Render this as a playful editorial-comic scientific infographic. It should feel like a
> polished illustrated magazine roadmap: icon-rich and engaging, while
> preserving every necessary scientific relationship and boundary. Avoid candy-bright colors and large
> dark background fills, and do not make it a page of black text boxes.
>
> Compose the method as three to six named comic regions in a grid, stack, or asymmetric
> editorial layout. Give every region the same achromatic near-white gray background fill
> (for example `#F7F7F7`), with no pastel tint or colored gradient. Add a rounded or playfully
> shaped boundary, contrasting numbered badge, bold banner, and short internal micro-flow. Draw every real
> branch, parallel path, shared kernel, loop, optional path, and reconvergence. Do not flatten
> the whole method into a single chain.
> Keep each region number and English title only slightly larger than primary node labels
> (at most about 110%). Use bold weight and placement for hierarchy, with compact badges and
> heading bands that preserve space for the method content.
> Keep the connector count as low as the scientific topology permits. Omit redundant arrows,
> group related nodes, and use clear shared trunks when appropriate. Place nodes and route
> arrows so no two arrow paths cross. Intentional branch/join or shared-trunk junctions are
> allowed, but crossing paths are not. Rearrange the layout if needed; never erase a necessary
> relationship to simplify the page. Keep arrow strokes slightly thinner than panel/icon
> outlines while clearly visible at final paper width.
> Treat each arrow-linked item as a separate smaller node, whether two nodes sit in the same
> named region or different ones. Give each node a clear hierarchy of icon, label, and
> permitted method detail.
>
> Keep the page white or near white. Region backgrounds stay neutral gray in this invocation;
> do not add region background colors yet. Soft color may appear in icons, banners, or small
> accents. Use deep navy or near-black for readable text and outlines, not large background
> fields. Keep any science-bearing lane colors consistent; decorative colors must not imply
> measured categories.
>
> Give every major noun and operation a distinct, easy-to-name cartoon icon from one coherent
> family. Use varied silhouettes rather than repeating document and folder icons. Use colored
> icon fills, thick outlines, sticker capsules, banners, badges, tags, small motion ticks, and
> restrained corner doodles. Keep in-figure text sparse: concise region and node names, and
> arrow labels only when necessary. Do not add explanatory sentences or repeated labels.
> Add one short method-only line to a region only if a necessary distinction otherwise becomes
> ambiguous; leave the fuller explanation for the paper body and paired description file.
> Keep avatar heads, cartoon people, and other icons modest in size within their nodes; never
> let a large simple character or glyph occupy most of a node. Prefer purposeful visual
> detail and readable organization inside each node over oversized decoration. When
> useful, lightly overlap multiple small icons into one composite illustration within a node;
> this is optional and must not imply extra method stages or obscure labels and arrows.
> Do not add a standalone overall title banner. Start directly with Region 1; the paper caption
> supplies the figure title. No landscapes, roads, trees, or exterior signboards. Crop tightly
> around the numbered method regions. Decorative accents are allowed only inside region
> boundaries and must not consume a separate row or margin.
>
> Keep the near-white gray region fills flat, without gradients. Light cel shading, small
> highlights, and shallow offset shadows may decorate non-panel elements. Do not use
> photorealism, glossy 3-D rendering, glassmorphism, metallic materials,
> heavy shadows, strong glow, or cinematic scenery. Decorative marks must never resemble
> scientific nodes or arrows.
>
> Render the essential supplied labels verbatim with readable typography. Include no experimental
> result, metric value, percentage, count, dataset size, empirical comparison, ablation,
> error-analysis finding, or conclusion. The figure must remain readable at its intended paper
> width and scientifically exact under close inspection.

For the later explicit panel-color invocation, use built-in image editing on the selected
neutral figure, not this new-image prompt. Tell the editor to change **only** the region
background fills to a small coordinated set of soft, light colors. Related regions may reuse
a tint. Keep the page white or near white. Preserve all text, icons, arrows, boundaries,
positions, dimensions, and existing science-bearing colors. Reject any edit that changes
content or introduces an arrow crossing.
