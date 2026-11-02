# Selected-PNG vector reconstruction on a later invocation

## Scope and invariants

Use the normal built-in ImageGen workflow for the initial and recolor invocations. Make
its PNG fills, icon boundaries, and lettering clean enough for later reconstruction without
deleting scientific content or flattening meaningful icons. Preserve every
original PNG, even rejected versions. **Those invocations produce no SVG or PDF.** Enter
this route only when the user later invokes the skill to convert an explicitly approved
`vNN.png`, or the unambiguous selected PNG in one **named run directory's** `SELECTED.md`,
to SVG and PDF. If multiple run directories could match, resolve the run before reading
their images. Reconstruct only that version; do not create vector files for all prior
candidates or call ImageGen here.
Keep PNG generation budget separate from vector work. Allow targeted reconstruction passes
until the fidelity gate below passes or a concrete limitation is identified. A pass limit,
time pressure, or successful PDF export never licenses a visibly simplified final artifact.
Deterministic exporter/font debugging is separate; stop after three consecutive attempts with
the same unresolved failure, report it, and do not publish an unchecked PDF.

Reconstruct the approved PNG with actual SVG shapes, paths, groups and visible `<text>`/`<tspan>`
elements. PNG is the visual reference; the technical brief is the scientific reference.
Preserve panel arrangement, prominent icon silhouettes and internal details, geometry, labels,
colors, line weight, visual hierarchy and connector endpoints. Keep a label inventory, a
node/edge inventory, and a list of the large or distinctive icons before rebuilding.
Identify ambiguous glyphs against the brief but disclose any correction; never silently
repair topology in the SVG while presenting it as an equivalent conversion. A corrected
design is a separately named revision.

No embedded/linked bitmap, traced glyph outlines, invisible text overlay, whole-figure image,
or replacement of prominent icons by generic boxes. Pixel identity is not expected:
font antialiasing, hand-drawn contours, and deliberate cleanup of incidental fill pollution
may differ. These allowances do not permit a flatter, emptier, or visibly less polished
redraw. If faithful vectorization is impractical, report that limitation rather than delivering
a raster wrapper or claiming the SVG/PDF are accepted.

**Visual fidelity gate:** Compare the SVG and PDF render side by side with the approved PNG
at native scale and intended printed width. Every large or distinctive icon must retain its
recognizable silhouette, significant internal parts, color treatment, and visual weight;
every connector, label, and group must retain its meaning and placement. Reject substantial
missing artwork, generic replacements, altered spatial balance, or noticeably reduced
legibility even if all labels extract and the scientific topology is intact. Record every
intentional difference, especially uniform flat-fill cleanup. Do not claim a literal 99.99%
pixel match: real text rendering and approved color cleanup can change pixels without losing
visual fidelity. A failed gate leaves the vector pair provisional/failed, never `final`.

## Stage-specific fill cleanup

Keep the existing flat-fill prevention prompt and the PNG hard checks. Vector cleanup
is available only after a separate SVG/PDF request; it is never a reason to accept a
visibly dirty, blurry, or ambiguous newly generated PNG as final.

- **PNG triage:** visible interior speckles, washout, color variation, blurred icon boundaries,
  or malformed glyphs fail PNG acceptance. Record the exact location and intended appearance;
  repair within the bounded ImageGen route. If unresolved, retain the source as provisional
  or rejected. An older PNG explicitly selected by the user for vector work can still be
  reconstructed, but that request does not change its original PNG review status.
- **Ambiguity:** if contamination obscures text, arrowheads or outlines, crosses object
  boundaries, changes scientific color coding, or makes the intended shape/color uncertain,
  do not guess missing content or claim SVG will recover it. Check the technical brief and
  ask about any remaining material ambiguity.
- **SVG reconstruction:** deliberately rebuild each affected background as its intended single,
  opaque, uniform fill. Preserve the semantic palette and containment; do not sample a polluted
  spot as the target color or trace white speckles into extra shapes. Removing recorded
  incidental fill artifacts is allowed appearance cleanup, not a license to redesign nodes,
  change topology, tint neutral major panels, or recolor unrequested surfaces. Preserve deliberate
  icon highlights/cel shading when appropriate; do not flatten all icon artwork or remove
  meaningful white marks. Ask when a mark's meaning cannot be resolved from the brief/reference.
- **Final SVG/PDF:** inspect the actual renders for uniform text-bearing surfaces, stray light
  or dark patches, accidental overlays, gaps and boundary bleed, at native scale and paper width.
  Vector format and exporter success alone cannot establish this: a white shape over a blue
  fill is still possible. Record each source defect's cleanup result and visible deviations.
  No unresolved defect may pass final vector acceptance; inspect ordinary antialiasing
  at edges separately from genuine interior spots.
- **Disposition:** retain the original PNG unchanged and label its remaining defects. The cleaned
  SVG/PDF pair may be `final` only after all scientific, visual and export checks pass; never
  present that verdict as proof that the source PNG was cleaned. A verified SVG/PDF
  rasterization can be a separately named derivative, not a silent replacement of `vNN.png`.
  If vector cleanup fails, report it rather than granting a waiver.

## Author and export

- Save `vNN.svg` beside the one approved, immutable `vNN.png`; use a fixed `viewBox` matching
  the PNG canvas. Do not overwrite earlier vector files from a prior attempt; retain their
  diagnostics and use a separately named revision when needed.
  Use stable element/group IDs for semantic nodes and edges. Live text includes mathematical
  symbols; a path-only equation is not selectable text. Keep superscripts/subscripts as text.
- Choose installed embeddable fonts that cover every character. Register the same fonts in
  the renderer. Keep SVG text local and self-contained apart from ordinary font selection;
  document font names/files so another machine can reproduce the export. By default, use one
  consistent **comic-style font family** for ordinary visible labels throughout the SVG/PDF;
  on this machine, `Comic Sans MS` regular and bold are available. Use a compatible fallback
  only for glyphs the comic family lacks (for example some mathematical brackets or arrows),
  and record each fallback. Keep mathematical notation, code identifiers, and required
  scientific symbols correct and selectable. Do not shrink labels or change their hierarchy
  merely to fit the comic face; verify placement, clarity, and visual fidelity at paper width.
- Export SVG to PDF using an available text-preserving renderer. Prefer a working local
  Inkscape, or the provided `scripts/export_vector.py` with svglib + ReportLab. This helper
  exports an **already reconstructed SVG**; it does not vectorize PNG. Its intentionally small
  supported SVG subset rejects filters, raster content, stylesheets and reusable symbols;
  expand these to explicit supported primitives or use another verified renderer.
- For the helper, use explicit `font-family` names with corresponding `--font NAME=FILE`
  options (separate names for regular/bold/math faces). Use a project-local environment for
  missing dependencies; never assume svglib is installed or install globally. Dependencies:
  `svglib`, `reportlab`, `pypdf`; Poppler `pdftotext`, `pdffonts`, `pdftoppm` for independent QA.
  Use real installed CSS family names (e.g. `Arial` plus `font-weight="bold"`), not invented
  family aliases which browsers may silently replace. Give regular and bold faces distinct
  family names when both are used: the helper binds one explicit file per family.
  Example: `python scripts/export_vector.py v01.svg --pdf v01.pdf --width-in 6.15
  --font Arial=/absolute/font.ttf --expected-text v01.labels.json`.
  Labels JSON is an independently reviewed list of all visible strings, including repeats.
- The helper fails rather than overwriting a PDF/report; use a new scratch destination for
  repair passes and publish only the verified pair. Preserve failed attempt diagnostics.

## Verify independently

1. Structural: inspect SVG XML for real geometry and real, visible text. No `<image>`, external
   resources, text converted to outlines, or raster fallbacks. Automated checks cannot establish
   that text paths are absent or every glyph is correct: visual inspection is also required.
2. Text: extract from the final PDF with Poppler, compare every label including multiplicity
   against the reviewed inventory. Check accents, Greek symbols, minus/inequalities, subscripts
   and reading order. `pdffonts` must show embedded fonts and Unicode mapping for used text fonts.
   Report failed symbols explicitly; mere presence of some extracted text is insufficient.
3. Rendering: render both the SVG and PDF and view each beside the approved PNG at native
   scale and intended printed width. Apply the visual fidelity gate above to the entire
   canvas, prominent icons, typography, fills, all arrow endpoints, branch/join semantics,
   clipping, and missing SVG features. Include side-by-side previews or equivalent review
   evidence; do not substitute a text/structure check for appearance review.
4. Scientific review remains independent. A faithful copy of a wrong PNG is still wrong. Mark
   that version provisional/rejected and withhold manuscript prose even if export checks pass.
5. When requested, compile an **isolated** LaTeX inclusion proof using `\includegraphics{vNN.pdf}`
   at the actual paper width, then extract and visually inspect its text as well. Never modify
   the actual manuscript as an implicit export step. Real text usually survives PDF inclusion;
   claim this only for the tested PDF, not every later publisher workflow or PDF viewer.

## Handoff

Keep the approved `vNN.png`, its `vNN.svg`, `vNN.pdf`, prompt, description, PNG review,
vector review, independent label/icon inventories, and export report together. Previews
must be named `vNN.svg-preview.png` or
`vNN.pdf-preview.png`, never overwrite the generated PNG. In `vNN.vector-review.md` report
scientific status, fidelity deviations, renderer/fonts, extraction/font evidence, actual size,
and whether a LaTeX inclusion proof was tested. A review may say “text/export passed; scientific
review failed.” Do not equate a PDF extension, vector zooming, or selectable OCR with a genuine
reconstructed figure whose visible labels are real text.
