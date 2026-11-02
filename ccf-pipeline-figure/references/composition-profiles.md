# Composition profiles

Choose exactly one profile when planning a **new** conceptual figure. These are visual
composition choices within one skill; do not switch Git branches. The scientific brief,
complete relationship inventory, no-crossing connector policy, final-size typography,
balanced canvas coverage, and staged PNG-first / later selected-version SVG/PDF workflow
apply to both.

The short command tokens are `分区` → `numbered_regions` and `非分区` →
`topology_first`; also accept `3–6分区` and `自由构图`, respectively. Match `非分区` before
`分区`. The latter token means that the figure **may** have scientifically useful regions,
not that regions are prohibited. Example: `画流程图，非分区，6+3` chooses the flexible profile,
six fresh candidates, and up to three refinements. Use a deliberate command token, not an
incidental mention of a region in the method description.

Record `composition_profile: numbered_regions` or `composition_profile: topology_first` in
`TECHNICAL_FIGURE_BRIEF.md`, every new version's prompt/review/description, and `SELECTED.md`.
The chosen profile must govern the actual figure. The later background-color route inherits
the neutral base's profile and may recolor existing surfaces, not change its composition.

## `numbered_regions` — 3–6 命名区域

This preserves the composition treatment present before commit `1ddcf57` (snapshot
`90863f3`). Plan **three to six meaningful named major regions**. Give each a compact
sequence number or badge, short heading, visible boundary, and achromatic near-white gray
background in the initial structure pass. Arrange them as a balanced grid, stack, or
asymmetric editorial composition with short local micro-flows. Start with Region 1; keep
heading and badge compact so content and labels remain readable at final paper width.
Use distinct region sizes where the scientific content warrants it. Preserve branches,
parallel lanes, joins, loops, and cross-region relationships even when the global visual
grammar uses numbered regions. A region number organizes the explanation; it must not
invent a causal order unsupported by the method. If the evidence cannot support 3–6
meaningful regions without misrepresenting the method, say so and offer `topology_first`
before generating rather than fabricating stages.

**Prompt composition block:**

> Compose the supplied method as three to six named comic regions in a balanced grid,
> stack, or asymmetric editorial layout. Give every region the same achromatic near-white
> gray background field, a clear rounded or editorial boundary, compact numbered badge,
> short heading, and its scientifically faithful local flow. Begin with Region 1 and crop
> around the full composition. Keep badges and headings only slightly larger than primary
> node labels. Preserve every real branch, parallel path, shared component, feedback loop,
> optional path, and reconvergence. Use only necessary directional arrows and avoid
> crossings. Fill the rectangular canvas with modest margins and purposeful gutters,
> without a large isolated corner void. Do not remove content or shrink essential labels
> to make the regions fit.

**Review:** Require 3–6 meaningful numbered major regions, neutral major fields in the
initial pass, readable headings and labels, and all common scientific/visual checks.

## `topology_first` — 按科学逻辑自由构图

This is the flexible treatment of commit `1ddcf57`. Derive the graph and reading order,
then choose an open chain, parallel lanes, branch/rejoin, feedback loop, hierarchy,
overview/detail arrangement, or meaningful groups as appropriate. There is no required
region or badge count. Grouping, boundaries, background fields, and numbering are separate
choices; use each only when it clarifies the scientific relationship. Any major background
field used in the initial pass stays achromatic near-white gray. A genuine linear process
may remain linear; do not flatten a non-linear one.

**Prompt composition block:**

> Derive the composition from the supplied scientific graph and reading order. There is
> no fixed number of regions, panels, or badges, and an open layout is valid. Use a genuine
> sequence, parallel lanes, branch/rejoin, feedback, hierarchy, or overview/detail layout
> only when supported by the method. Treat semantic groups, outlines, background fields,
> and numbering as separate choices. Prefer proximity, alignment, shared baselines, or
> compact headings when sufficient. Use a boundary only for a meaningful group, phase,
> interface, or system limit; use sequence numbers only for a real ordered procedure.
> Keep any actual major background field achromatic near-white gray in the first pass.
> Preserve every entity and necessary relationship, with explicit arrows where layout
> alone would be ambiguous. Fill the rectangular canvas with modest margins, without a
> large isolated corner void, invented panel tiles, oversized icons, or tiny labels.

**Review:** Require the composition to match the graph; reject unsupported boundaries,
numbering, or omitted relationships. Open and unnumbered arrangements are valid when clear.
