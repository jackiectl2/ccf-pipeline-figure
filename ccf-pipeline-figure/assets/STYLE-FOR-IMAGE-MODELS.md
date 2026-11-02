# Editorial-comic house style for image models

## Purpose and priority

Use this file only for a conceptual research figure: pipeline, method overview, architecture,
mechanism, or data-flow diagram in which no visual property encodes a measured quantity.

The project's `TECHNICAL_FIGURE_BRIEF.md` is authoritative for scientific meaning, topology,
labels, examples, and result exclusions. This file is authoritative for visual treatment.
An explicit user aesthetic preference may override this style, but never the scientific brief.
Read `references/composition-profiles.md` from the skill root for the selected
`composition_profile`. The open-layout directions in Sections 1 and 8 describe
`topology_first`; for `numbered_regions`, use the selected profile's numbered-region
composition rules and prompt block. All non-composition rules here apply to both profiles.

The flat-fill constraints here remain the generation target. For PNG review before a
separately requested SVG/PDF conversion, follow `references/png-svg-pdf.md` (relative to the
skill root): minor unambiguous fill artifacts may be documented for deliberate later SVG
cleanup, not used alone to trigger more ImageGen edits. This does not relax vector fill
quality or permit pollution that obscures content, crosses boundaries, or changes semantic colors.

The target is a **playful editorial-comic scientific infographic**. The initial structure
pass uses a three-layer color system: a white or near-white page, optional achromatic near-white-gray
major-group fields, and lively but restrained soft color in semantic foreground objects.
Neutral region fields do not require neutral foregrounds or a white/gray card around every
icon-label group. `topology_first` open compositions need no enclosing fields. On a later explicit color-edit
invocation, tint every existing major-group background and, optionally, a small selection of
internal white/gray card surfaces.
The figure should feel like a polished illustrated magazine roadmap or a high-quality
educational comic, without candy-bright colors or large dark background fills.

---

## 1 · Composition (`topology_first` directions plus shared safeguards)

- In `topology_first`, choose composition from the **scientific graph**, without a fixed region count or panel template.
  A true sequence may use an open linear flow; parallel inputs may use aligned lanes and a
  shared merge; stateful mechanisms may use a main path with feedback; hierarchies may use
  nesting or layers; an overview may include a focused detail. Use only the relationships
  present in the brief, not a mandatory mixture of these options.
- In `topology_first`, **there is no fixed number of regions, stages, panels, or badges.** An open composition with no
  enclosing major panels is valid. Semantic grouping, visible outlines, background fields,
  and numbering are separate decisions. Use proximity, alignment, shared baselines, or compact
  headings when sufficient. A boundary needs a real grouping, phase, interface, or system-limit
  purpose; do not enclose every group merely to make a panel mosaic.
- In `topology_first`, use sequence numbers only when an actual ordered procedure benefits from them. Do not
  number parallel modules or a feedback architecture as if they were successive stages.
  Optional panel letters may identify separate views without implying process order. Omit
  badges and banners unless useful; any chosen major-group background stays neutral gray in
  the initial structure pass.
- In `topology_first`, the global layout may be open, layered, cyclic, branched, grouped, or asymmetric as the
  graph requires. A grid is an option, not the default structure imposed on every method.
- Treat the intended image as a deliberately filled rectangle (including a square canvas), not a
  loose cluster placed on a canvas. Arrange the objects, optional groups, and connectors so
  their combined visual envelope reaches a modest, balanced outer margin on all sides.
  Keep purposeful spacing between objects or groups; a large isolated blank corner or edge
  void is not acceptable. Do not add panels, enlarge icons at the expense of labels, or
  delete scientific content merely to fill the rectangle.
  If topology forces unusual whitespace, make its purpose legible through the structure rather
  than leaving an accidental-looking empty quadrant.
- Distinguish named regions from the smaller nodes joined by arrows: in `A → B`, A and B are
  two nodes, whether they sit in the same region or different ones. A node does not need a
  rectangular enclosure: a free-standing semantic object plus a short adjacent label, clear
  spacing, and unambiguous connector anchors remains a distinct node. Give each node a clear
  visual hierarchy and enough room for its label and icon; keep fuller method detail in the
  paired description file rather than adding prose inside the node. Do not let one large icon
  occupy most of the node.
- Use an enclosed card only when the boundary itself carries meaning—for example a record,
  command, state, interface, input/output object, or explicit grouping. Do not draw a white or
  gray rectangle merely to hold an icon and its label. Conventional cards should remain a
  minority unless the scientific brief establishes a genuinely repeated card-like class.
- Show real branches, parallel operations, joins, feedback loops, optional paths, and typed
  boundaries. Never serialize mutually exclusive or parallel operations just to simplify the
  layout.
- Preserve every object, operation, branch, join, loop, and logical relationship in the
  supplied topology; lower arrow-line count only by changing how an already-preserved
  relationship is expressed. Use spatial stage order, containment, aligned lanes, shared
  trunks, typed boundaries, or a short interface label whenever one of these makes that
  relationship equally unambiguous; use an explicit arrow when direction, transfer, causality,
  a cross-stage effect, or feedback would otherwise be unclear. Remove only duplicate or
  decorative connectors—never scientific content. Arrange nodes and route arrows so no arrow
  paths cross. An intentional, clearly connected branch/join or shared-trunk junction is
  allowed; a path passing across another is not. If the first arrangement forces a crossing,
  change the arrangement instead of accepting the crossing.
- When panels help, their sizes need not match. Give the scientifically important branch more room.
- Do not add a standalone overall title banner. Start directly with scientific content; the paper
  caption supplies the figure title.
- No landscapes, roads, trees, or exterior signboards.
- Crop around the scientific content and necessary connectors. `topology_first` does not require numbered regions.
- Decorative elements must stay outside arrow corridors and must not resemble nodes, ports,
  evidence tokens, outcomes, or data-flow arrows.

## 2 · Color: neutral region fields, lively foregrounds, soft panels later

- Keep the three layers distinct during the initial invocation: white or near-white page;
  achromatic near-white-gray major-group fields (required for `numbered_regions`, optional
  for `topology_first`); restrained soft color in icons, mechanism
  objects, state markers, small accent plates, and other compact semantic foreground elements.
  The neutral-field rule applies only to existing major-group fields, not to every object
  or semantic group. Do not introduce fields to satisfy a palette rule.

- **Initial invocation:** use the same pure, achromatic near-white gray for any major-group background
  fills (for example `#F7F7F7`), without hue, colored gradients, or pastel tint. Keep the page
  white or near white and distinguish groups through layout, headings, or justified boundaries.
  Badges are optional in `topology_first`; its open layouts need not have background fields. This is the
  selected structural base to inspect before choosing panel colors.
- **Later explicit “add background colors” invocation:** recolor backgrounds at two levels.
  First, tint every existing major-group background field. Do not create fields, outlines,
  numbers, or new groups if the base is open. Second, optionally tint only a small selection of
  internal pure white or neutral-gray surfaces—such as an ASK panel, command card, or compact T/U/H
  subregion—when doing so improves grouping, hierarchy, or readability. These are examples of
  eligible surfaces, not required labels. Do not color every internal card; untouched white
  space is part of the visual hierarchy. If no major fields exist, only the optional second
  level applies. If neither level has useful eligible surfaces, ask before expanding the edit
  to foreground colors or structure rather than silently inventing a background.
- Use a small coordinated set of **soft, lightly saturated colors**. Pale coral, peach, butter
  yellow, sage or mint, powder blue, and lavender are possible choices, not a quota. Related
  regions may reuse a color; they need not all differ. An optionally colored internal surface
  may harmonize with its containing region while remaining visibly distinct. Do not let the
  whole background become one uniform color or turn nested cards into a rainbow.
- White may be used for the page or semantically justified text cards. Keep any panels
  distinguishable and readable at thumbnail size without making their fills dark or saturated.
- Use near-black or deep navy for text and outlines where needed for contrast, not for large
  background fields. Outlines may be more expressive than ordinary academic line art.
- Reserve stable semantic roles where the science needs them: for example, one color for lane
  A, another for lane B, and muted amber for the principal flow. Keep those mappings
  consistent from input to output. Do not alter those existing science-bearing colors in
  the later panel-fill edit.
- Soft decorative colors are allowed for banners, stickers, and icons, but they must not imply
  nonexistent experimental categories or measured differences.
- Color the icons themselves while preserving contrast with their backgrounds.
- **Flat-fill integrity / 色彩与填充一致性:** every enclosed text-bearing surface—including
  regions, nodes, cards, pills, tags, labels, and callouts—uses one visually uniform,
  continuous, fully opaque fill. Its hue, saturation, and brightness must remain stable from
  edge to center, apart from outline antialiasing. Keep the fill strictly clipped inside the
  outline; adjacent colors must not seep across it or create a halo. Repeated nodes of the same
  semantic class use the same fill.
- Do not treat a pale card as a translucent, illuminated, or painted object. On text-bearing
  surfaces forbid unintended gradients, center white bloom or washout, bright/dark blotches,
  watercolor or airbrush texture, mottling, vignette, reflection, glow, shadow tint,
  translucency, and color bleeding. Soft color means low saturation, not uneven opacity.

## 3 · Comic depth and shape grammar

- Build visual rhythm from a varied semantic foreground grammar rather than a repeated card
  template. Choose among these treatments according to what the node means:
  - inputs and evidence as open mini-scenes, symbolic data strips, document stacks, token
    streams, or other unboxed source objects that do not imply measured values;
  - stateful mechanisms and major transformations as distinctive objects such as networks,
    gears, instruments, shields, magnifiers, or gauges;
  - mathematical or routing operations as compact circles, funnels, chips, gates, brackets,
    or junction symbols;
  - states and outcomes as capsules, badges, tags, meters, or warning shapes;
  - a real ordered sequence as a continuous event belt, ribbon, or shared baseline whose
    individual entities and transitions remain scientifically distinct; and
  - records, commands, interfaces, and explicit groups as the limited cases that justify cards.
- Labels may sit beside, below, or within the meaningful object when legibility permits; do not
  repeat one dominant `centered icon above centered label inside a white rectangle` pattern.
- Use rounded sticker capsules, playful banners, chunky tabs, speech bubbles, file cards,
  ribbons, tags, badges, and varied silhouettes selectively, according to their semantic role.
- Keep region, node, card, pill, tag, label, and callout fills flat in every stage. Gentle cel
  shading or small highlights may add depth **inside icon artwork only**; they may not spill
  onto a text-bearing background or sit behind a label. A shallow offset shadow may separate
  an entire closed object from the page only if the object's interior fill remains uniform.
- Keep the rendering illustrative and flat enough for a paper figure. Avoid photorealism,
  glossy product-render surfaces, glassmorphism, metallic materials, deep perspective, and
  heavy 3-D extrusion.
- Dashed boundaries mean a set, phase, or region; solid boundaries mean a single object.
- Scientific arrows use one unmistakable visual grammar: solid path, clear triangular head,
  high contrast, and consistent direction. Use a balanced medium stroke at final paper
  width: neither a heavy bar nor a faint hairline. Prefer deep charcoal or navy so a
  moderately weighted arrow stays clear against neutral-gray and soft-colored panel fills.
  If arrow color encodes a scientific lane or type, keep those colors consistent and dark
  enough to read. Comic motion ticks may decorate an arrow but may never create a second
  ambiguous arrow.
- Use playful asymmetry without sacrificing alignment of the scientific graph.
- Create liveliness through silhouette, foreground color, scale rhythm, grouping, layering, and
  label placement. Do not obtain it by adding arrows, font tiers, decorative topology, saturated
  major-region fills, or ornamental clutter.

## 4 · Icons: varied nouns, one family

- Before drawing, choose exactly three or four discrete icon-size tiers for the whole figure.
  Every icon assigned to one tier uses the same visual bounding-box size, even across different
  regions. Do not resize individual icons to fill spare space or make a local node feel more
  important; use composition, color, outline, and placement instead. A composite icon counts as
  one icon and must fit its assigned tier box.
- Give every major noun and operation a recognizable glyph. A labeled rectangle without a
  visual metaphor should be the exception.
- Let recognizable icons stand directly on the page or an optional group field when no boundary is needed. Pair
  them with a short nearby label and clear connector anchors rather than automatically wrapping
  them in a white card.
- Match icon variety to the method's distinct concepts; there is no panel-derived icon quota.
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

- Before drawing, normally choose exactly three or four discrete text-size tiers for the whole
  figure. Every text item assigned to one tier uses the same final printed size across all
  regions; do not introduce a one-off font size to solve a local layout problem. Text tiers and
  icon tiers are assigned independently, so a primary label need not have a primary-size icon.
  As a default four-tier system relative to the paper body, use 110% for compact region headings,
  100% for primary labels, 85% for secondary labels, and 75% only for nonessential auxiliary
  text. A three-tier figure omits the auxiliary tier.
- A fifth text tier is an exceptional escape hatch, not part of the default system. Use it only
  when indispensable content still cannot fit legibly after improving composition, spacing, and
  wording. It must be the smallest declared size, remain readable at final paper width, and
  appear only on a small minority of isolated, nonessential micro-labels. Never use it for region
  headings, node names, necessary method distinctions, or recurring body text across regions.
  If it starts recurring, revise the layout or wording and promote those items to Tier 4.
- Make the diagram readable with as little text as the scientific topology permits. Keep
  essential region and node names; label an arrow only when its direction or type is unclear.
  Put full explanations in the paired paper-body description file for the writing agent.
- If the composition needs a badge or group heading, keep it compact. Its text may be only
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
- Use one consistent, readable comic-style font family for ordinary headings and labels,
  with bold weight where hierarchy needs it and high contrast throughout. Monospaced text
  is reserved for code identifiers and verbatim strings; scientific symbols may need a
  compatible font when the comic family lacks a glyph. Keep the declared size tiers intact.
- Spell every supplied label exactly. Do not invent extra claims, slogans, or technical terms.

## 6 · Controlled decoration

- Allowed locally beside scientific objects or inside optional groups: small stars or spark marks, motion ticks,
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
- No non-uniform fill, white bloom, washout, unintended gradient, mottling, watercolor or
  airbrush texture, translucency, halo, vignette, reflection, shadow tint, or color bleeding
  inside or across any text-bearing enclosed surface.
- No UI-like wall in which most primary nodes repeat the same white/gray rectangle with a
  centered icon above a centered label, unless the repeated card form itself encodes a genuine
  repeated scientific class.
- No tiny text that becomes unreadable at the intended paper width.

---

## 8 · Paste-ready prompt block

For the initial neutral-structure invocation, append this after the scientific brief has
been converted into exact topology, composition, optional grouping, and connector instructions.
Insert **only** the selected composition profile's prompt block from
`references/composition-profiles.md` immediately after the opening paragraph below and
before the shared size/connector instructions. Never combine the two profile blocks.

> Render this as a playful editorial-comic scientific infographic. It should feel like a
> polished illustrated magazine roadmap: icon-rich and engaging, while
> preserving every necessary scientific relationship and boundary. Avoid candy-bright colors and large
> dark background fills. Do not make it a page of black text boxes or a wall of identical
> white cards.
> Use one consistent, readable comic-style typeface for ordinary headings and labels, with
> bold weight where needed; keep scientific symbols correct and all text legible at paper width.
>
> Establish exactly three or four discrete text-size tiers and exactly three or four discrete
> icon-size tiers for this whole figure before drawing. Only in a rare content-dense case may
> text use a fifth tier: first improve composition, spacing, and wording; then use Tier 5 only
> as the smallest readable size for a small minority of isolated, nonessential micro-labels.
> Never use Tier 5 for region headings, node names, necessary method distinctions, or recurring
> body text. If it starts recurring, return those items to Tier 4 and revise the layout. Every
> text item in a tier must have the same final printed size, and every icon in a tier must have
> the same visual bounding-box size, across all regions. Do not create one-off local scales;
> use weight, color, placement, grouping, and shape for emphasis instead. Text and icon tiers
> may be assigned independently.
> Preserve every object and scientific relationship in the supplied topology. Reduce the
> number of drawn arrow lines only by expressing a preserved relationship through clear
> stage order, containment, aligned lanes, shared trunks, typed boundaries, or a short
> interface label; use an explicit arrow whenever direction, transfer, causality, a
> cross-stage effect, or feedback would otherwise be unclear. Omit only duplicate or
> decorative arrows—never scientific content. Place nodes and route remaining arrows so no
> two arrow paths cross. Intentional branch/join or shared-trunk junctions are allowed, but
> crossing paths are not. Rearrange the layout if needed; never erase a necessary relationship
> to simplify the page. Draw arrows at balanced medium weight, neither thick bars nor thin
> hairlines, with clear triangular heads. Prefer deep charcoal or navy for contrast against
> the light panels; preserve any necessary semantic arrow colors at a similarly readable depth.
> Check their visibility at final paper width.
> Treat each arrow-linked item as a separate smaller node, whether two nodes sit in the same
> named region or different ones. A separate node does not require a rectangular enclosure:
> an unboxed semantic object with a nearby short label, clear spacing, and unambiguous connector
> anchors remains a distinct node. Give each node a clear hierarchy of icon, label, and permitted
> method detail. Use an enclosed card only when its boundary itself means record, command,
> state, interface, input/output object, or explicit grouping. Do not draw a white or gray
> rectangle merely to hold an icon and label; conventional cards should remain a minority unless
> the supplied science contains a genuinely repeated card-like class.
>
> Keep three color layers distinct. The page is white or near white. Major-region backgrounds
> follow the selected composition profile and stay achromatic near-white gray in this
> invocation; do not add colored region backgrounds yet. The semantic foreground should
> still feel lively: use restrained soft color in
> icons, distinctive mechanism objects, state markers, small accent plates, banners, and other
> compact foreground elements. Neutral region fields do not require neutral foregrounds or
> white/gray cards around icon-label groups. Use deep navy or near-black for readable text and
> outlines, not large background fields. Keep any science-bearing lane colors consistent;
> decorative colors must not imply measured categories.
>
> Apply strict flat-fill integrity to every enclosed text-bearing surface: every region, node,
> card, pill, tag, label, and callout must contain one uniform, continuous, fully opaque color
> from edge to center. Keep each color clipped inside its outline, with no seepage or halo, and
> use exactly the same fill for repeated nodes of the same semantic class. Soft or pastel color
> means low saturation, not transparency or illumination. Behind text, forbid all unintended
> gradient, center white bloom, washout, bright or dark blotches, mottling, watercolor or
> airbrush texture, glow, highlight, reflection, shadow tint, translucency, vignette, and color
> bleeding. Confine cel shading and highlights to the interior artwork of icons only.
>
> Give every major noun and operation a distinct, easy-to-name cartoon icon from one coherent
> family. Use varied silhouettes rather than repeating document and folder icons. Build a varied
> semantic foreground grammar: inputs may be open mini-scenes or source objects; stateful
> mechanisms should be distinctive instruments, networks, gears, shields, magnifiers, or gauges;
> mathematical and routing operations should be compact circles, funnels, chips, gates, brackets,
> or junctions; states and outcomes may be capsules, badges, tags, meters, or warning shapes; and
> a real ordered sequence may use a continuous event belt, ribbon, or shared baseline while
> preserving every entity and transition. Reserve ordinary cards for the few nodes whose
> boundaries carry scientific meaning. Do not repeat a dominant centered-icon-above-centered-label
> white-card template. Labels may sit beside or below objects. Use colored icon fills, thick
> outlines, sticker capsules, banners, badges, tags, small motion ticks, and restrained corner
> doodles selectively. Keep in-figure text sparse: concise region and node names, and arrow labels
> only when necessary. Do not add explanatory sentences or repeated labels.
> Add one short method-only line to a region only if a necessary distinction otherwise becomes
> ambiguous; leave the fuller explanation for the paper body and paired description file.
> Keep avatar heads, cartoon people, and other icons modest in size within their nodes; never
> let a large simple character or glyph occupy most of a node. Prefer purposeful visual
> detail and readable organization inside each node over oversized decoration. When
> useful, lightly overlap multiple small icons into one composite illustration within a node;
> this is optional and must not imply extra method stages or obscure labels and arrows.
> Make the figure lively through semantic silhouettes, restrained foreground color, scale rhythm,
> grouping, layering, and varied label placement—not by adding arrows, font tiers, decorative
> topology, saturated major-region fills, or ornamental clutter.
> Do not add a standalone overall title banner. The paper caption supplies the figure title.
> No landscapes, roads, trees, or exterior signboards. Crop around the content and necessary
> connectors. Decorative accents stay local to relevant objects or groups and must not
> consume a separate row or margin.
>
> Keep all region and text-card fills flat, without gradients or internal lighting. Light cel
> shading and small highlights may decorate icon artwork only; a shallow offset shadow may sit
> outside a closed object only when its interior fill stays uniform. Do not use
> photorealism, glossy 3-D rendering, glassmorphism, metallic materials,
> heavy shadows, strong glow, or cinematic scenery. Decorative marks must never resemble
> scientific nodes or arrows.
>
> Render the essential supplied labels verbatim with readable typography. Include no experimental
> result, metric value, percentage, count, dataset size, empirical comparison, ablation,
> error-analysis finding, or conclusion. The figure must remain readable at its intended paper
> width and scientifically exact under close inspection. Request a 4K-class raster when
> supported, otherwise the highest available raster resolution, at the paper-slot aspect ratio
> established by the brief. Treat 4K as a resolution target, not a fixed canvas ratio: do not
> force 16:9 or another standard ratio.

For the later explicit background-color invocation, use built-in image editing on the selected
neutral figure, not this new-image prompt. Tell the editor to recolor background fills in two
levels. Level 1 is mandatory for existing fields: tint every existing major-group background.
Do not create fields, borders, groups, or numbers when recoloring an open composition.
Level 2 is optional and selective: tint only a small subset of internal pure-white or
neutral-gray surfaces, such as an ASK panel, command card, or compact T/U/H subregion, when the
tint improves grouping, hierarchy, or readability. Do not color every internal card; preserve
all unselected white/gray surfaces exactly. If no major fields exist, Level 1 has no targets;
use only useful eligible Level 2 surfaces. If neither level has targets, ask before expanding
the scope to foreground colors or structural edits. Use a small coordinated set of soft, light colors;
related regions may reuse a tint, and an internal tint may harmonize with its containing region
while remaining distinct. Each selected surface must use one visually uniform, fully opaque
color from edge to center, strictly clipped inside its own boundary, with no gradient, white
bloom, washout, mottling, texture, translucency, halo, or color bleeding between adjacent or
nested surfaces. Change only the fill pixels of the selected backgrounds. Lock all text,
arrows, arrowheads, icons and their existing colors, outlines, banners, boundaries, positions,
dimensions, spacing, canvas size, scientific topology, and existing science-bearing colors.
Reject any edit that changes or rerenders a locked or unselected element, loses contrast, or
introduces an arrow crossing. Ask to preserve the base image's pixel dimensions.
