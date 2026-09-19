# Editorial-comic house style for image models

## Purpose and priority

Use this file only for a conceptual research figure: pipeline, method overview, architecture,
mechanism, or data-flow diagram in which no visual property encodes a measured quantity.

The project's `TECHNICAL_FIGURE_BRIEF.md` is authoritative for scientific meaning, topology,
labels, examples, and result exclusions. This file is authoritative for visual treatment.
An explicit user aesthetic preference may override this style, but never the scientific brief.

The target is a **bold, colorful editorial-comic scientific infographic**. It must feel like
a polished illustrated magazine roadmap or a high-quality educational comic, not a restrained
corporate flowchart and not a mostly white page of black text boxes. Publication-ready does
not mean minimalist, monochrome, or low saturation.

---

## 1 · Composition

- Build the figure as **three to six named regions**, not as one long row of boxes.
- Give each region a strong visual identity: rounded or irregular comic-panel boundary,
  colored background field, numbered badge, bold banner, and a short local micro-flow.
- The global layout is a grid, stack, or asymmetric editorial composition. Inside one region,
  a short left-to-right or top-to-bottom flow is fine.
- Show real branches, parallel operations, joins, feedback loops, optional paths, and typed
  boundaries. Never serialize mutually exclusive or parallel operations just to simplify the
  layout.
- Non-uniform panels are encouraged. Give the scientifically important branch more room.
- A decorative overall title is allowed and encouraged. It must not claim a result.
- Decorative elements must stay outside arrow corridors and must not resemble nodes, ports,
  evidence tokens, outcomes, or data-flow arrows.

## 2 · Color: vivid, coordinated, and role-aware

- Use a coordinated **five-to-seven-hue candy/editorial palette**. Good families include coral,
  hot pink, amber, butter yellow, mint, turquoise, sky blue, and violet.
- Major regions should have visibly different color identities. Do not reduce them to nearly
  white tints that disappear at thumbnail size.
- White is permitted inside text cards for legibility, but it must not dominate the canvas.
- Use near-black or deep navy outlines for strong contrast. Outlines may be thicker and more
  expressive than ordinary academic line art.
- Reserve stable semantic roles where the science needs them: for example, one color for lane
  A, another for lane B, and amber/orange for the principal flow. Keep those mappings
  consistent from input to output.
- Extra decorative colors are allowed for region identity, banners, stickers, and icons, but
  they must not imply nonexistent experimental categories or measured differences.
- Color the icons themselves. Do not leave a page of black outline glyphs on white cards.

## 3 · Comic depth and shape grammar

- Use rounded sticker capsules, playful banners, chunky tabs, speech bubbles, file cards,
  ribbons, tags, badges, and varied silhouettes.
- A subtle panel gradient, gentle cel shading, small highlight, or shallow offset shadow is
  allowed when it improves energy and separation.
- Keep the rendering illustrative and flat enough for a paper figure. Avoid photorealism,
  glossy product-render surfaces, glassmorphism, metallic materials, deep perspective, and
  heavy 3-D extrusion.
- Dashed boundaries mean a set, phase, or region; solid boundaries mean a single object.
- Scientific arrows use one unmistakable visual grammar: solid path, clear triangular head,
  high contrast, and consistent direction. Comic motion ticks may decorate an arrow but may
  never create a second ambiguous arrow.
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
- Useful vocabulary includes document stacks, file-type cards, mapping tags, parser funnels,
  checklists, shields or fingerprints, chain links, paired strips, sliders, targets, boundary
  brackets, token chips, balances, magnifiers, matrices, clipboards, forks, satchels, laptops,
  report folders, JSON pages, HTML pages, ribbons, lightbulbs, and gauges.
- An icon nobody can name is worse than a word. Keep a short label when the glyph could be
  ambiguous.

## 5 · Text

- Region banners are the largest text after the decorative title.
- Block labels are short noun phrases, normally one to four words.
- One short **method-only explanatory line** per region is allowed. It may explain what the
  stage does, but it must not report an outcome, advantage, score, rate, or empirical finding.
- Put real documentation-safe example content in a bordered callout when the brief permits it.
  Quote it exactly and distinguish it from a result.
- Use bold, friendly editorial typography with high contrast. Monospaced text is reserved for
  code identifiers and verbatim strings.
- Spell every supplied label exactly. Do not invent extra claims, slogans, or technical terms.

## 6 · Controlled decoration

- Allowed: decorative title plaque, corner stickers, small stars or spark marks, motion ticks,
  tape tabs, scalloped banners, tiny non-semantic doodles, and colored edge accents.
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

Append this after the scientific brief has been converted into exact region and arrow
instructions:

> Render this as a bold, exuberant editorial-comic scientific infographic. It should feel
> like a polished illustrated magazine roadmap: colorful, playful, icon-rich, and immediately
> engaging, while preserving every scientific arrow and boundary exactly. Do not make it a
> minimalist corporate flowchart or a mostly white page of black text boxes.
>
> Compose the method as three to six named comic regions in a grid, stack, or asymmetric
> editorial layout. Give every region a colored background field, rounded or playfully shaped
> boundary, dark numbered badge, bold banner, and short internal micro-flow. Draw every real
> branch, parallel path, shared kernel, loop, optional path, and reconvergence. Do not flatten
> the whole method into a single chain.
>
> Use a coordinated five-to-seven-hue candy palette: coral, pink, amber, butter yellow, mint,
> turquoise, sky blue, and violet as appropriate. Use deep navy or near-black expressive
> outlines. White may appear inside text cards but must not dominate the canvas. Keep any
> science-bearing lane colors consistent; decorative region colors must not imply measured
> categories.
>
> Give every major noun and operation a distinct, easy-to-name cartoon icon from one coherent
> family. Use varied silhouettes rather than repeating document and folder icons. Use colored
> icon fills, thick outlines, sticker capsules, banners, badges, tags, small motion ticks, and
> restrained corner doodles. A decorative title and one short method-only explanatory line
> per region are allowed.
>
> Subtle panel gradients, light cel shading, small highlights, and shallow offset shadows are
> allowed. Do not use photorealism, glossy 3-D rendering, glassmorphism, metallic materials,
> heavy shadows, strong glow, or cinematic scenery. Decorative marks must never resemble
> scientific nodes or arrows.
>
> Render all supplied text verbatim with large readable typography. Include no experimental
> result, metric value, percentage, count, dataset size, empirical comparison, ablation,
> error-analysis finding, or conclusion. The figure must remain readable at its intended paper
> width and scientifically exact under close inspection.
