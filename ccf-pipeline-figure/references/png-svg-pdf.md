# Experimental raster-first vector reconstruction

## Scope and invariants

Use the normal built-in ImageGen workflow first; do not simplify its prompt, icons or style
to make subsequent tracing easier. Preserve every original PNG, even rejected versions.
Keep PNG generation budget separate from vector work. Default to at most three visual
reconstruction passes per candidate, then hand off a clearly identified provisional result.
Deterministic exporter/font debugging is separate; stop after three consecutive attempts with
the same unresolved failure, report it, and do not publish an unchecked PDF.

Reconstruct the saved PNG with actual SVG shapes, paths, groups and visible `<text>`/`<tspan>`
elements. PNG is the visual reference; the technical brief is the scientific reference.
Preserve panel arrangement, node silhouettes, geometry, labels, colors and connector endpoints.
Keep a label inventory and a node/edge inventory before rebuilding. Identify ambiguous glyphs
against the brief but disclose any correction; never silently repair topology in the SVG while
presenting it as an equivalent conversion. A corrected design is a separately named revision.

No embedded/linked bitmap, traced glyph outlines, invisible text overlay, whole-figure image,
or unreported replacement of lively icons by generic boxes. Pixel identity is not expected:
font substitution, hand-drawn contours and icon shading may differ. Document those differences
and visually judge whether identity, topology and readability survive. If faithful vectorization
is impractical, report that limitation rather than delivering a raster wrapper.

## Author and export

- Save `vNN.svg` beside immutable `vNN.png`; use a fixed `viewBox` matching the PNG canvas.
  Use stable element/group IDs for semantic nodes and edges. Live text includes mathematical
  symbols; a path-only equation is not selectable text. Keep superscripts/subscripts as text.
- Choose installed embeddable fonts that cover every character. Register the same fonts in
  the renderer. Keep SVG text local and self-contained apart from ordinary font selection;
  document font names/files so another machine can reproduce the export.
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
3. Rendering: render the PDF and view it beside the original PNG at native scale and intended
   printed width. Check the entire canvas, typography, icon fidelity, fill integrity, all arrow
   endpoints, branch/join semantics, clipping and any missing SVG feature. Inspect SVG render
   too when a different engine will be used by the recipient.
4. Scientific review remains independent. A faithful copy of a wrong PNG is still wrong. Mark
   that version provisional/rejected and withhold manuscript prose even if export checks pass.
5. When requested, compile an **isolated** LaTeX inclusion proof using `\includegraphics{vNN.pdf}`
   at the actual paper width, then extract and visually inspect its text as well. Never modify
   the actual manuscript as an implicit export step. Real text usually survives PDF inclusion;
   claim this only for the tested PDF, not every later publisher workflow or PDF viewer.

## Handoff

Keep `vNN.png`, `vNN.svg`, `vNN.pdf`, prompt, description, PNG review, vector review, independent
label inventory and export report together. Previews must be named `vNN.svg-preview.png` or
`vNN.pdf-preview.png`, never overwrite the generated PNG. In `vNN.vector-review.md` report
scientific status, fidelity deviations, renderer/fonts, extraction/font evidence, actual size,
and whether a LaTeX inclusion proof was tested. A review may say “text/export passed; scientific
review failed.” Do not equate a PDF extension, vector zooming, or selectable OCR with a genuine
reconstructed figure whose visible labels are real text.
