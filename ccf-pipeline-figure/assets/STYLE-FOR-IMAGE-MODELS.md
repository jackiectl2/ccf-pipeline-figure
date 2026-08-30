# House style, written as instructions for an image model

**What this is.** The style rules of `ccf-pipeline-figure`, restated as imperatives an image
model can follow. Hand this file to whatever writes the image prompt — Codex, Claude Code,
or a human — together with a brief that says *what* to draw. This file only says *how*.

**Why it is separate from SKILL.md §2.** §2 is the evidential form: every rule carries its
count, its denominator and a `[MEASURED]` or `[INFERRED]` tag, because an agent choosing
between rules has to know which ones are load-bearing. An image model cannot use any of that
and is hurt by it. This file is the same style with the evidence stripped and the mood
changed to imperative.

⚠ **This file deliberately contains no statistics.** Two documents holding the same *number*
drift apart and nobody notices; two documents holding the same *instruction* do not, because
an instruction cannot quietly become false. If you find yourself about to write a count in
here, it belongs in §2 instead.

⛔ **What this file cannot fix.** A figure drawn by an image model has its numbers baked into
pixels: not traceable to an artefact, not regenerated when the experiment reruns, and nothing
warns you when they go stale. **Use this only for figures that carry no measured quantity.**
For anything with a real rate or count in it, generate the figure from committed data
instead — that is what the rest of the skill is for.

---

## 1 · Composition

- Build the figure as **three to six named REGIONS**, not as a left-to-right chain of boxes.
  A chain is the single most common way this genre fails.
- Mark every region **all four ways at once**: a rounded dashed boundary; a pale tinted fill,
  one tint per region; a **numbered badge** — a dark filled circle with a white numeral — at
  the region's top-left; and a **bold banner title** beside that badge, in the heaviest
  weight anywhere in the figure.
- The banner states the reading order. Number the regions 1, 2, 3, 4 and mean it.
- Inside a region the flow is short and **left to right**. The figure as a whole is a grid of
  regions; only the inside of a region is a line.
- Where the figure has two halves that differ in kind — before and after, offline and online,
  training and inference — separate them with **one vertical dashed rule** and name both
  halves above it.
- Panels may be **non-uniform**. Give the region carrying the point more room than the others.
- Draw the branches and the loops. If something iterates, draw the arrow going back. If a
  decision has three outcomes, draw three outcomes fanning out from one node — never three
  boxes in a row, which claims a sequence that does not exist.

## 2 · Colour

- White or near-white ground.
- Region tints: pale, desaturated, roughly 8–12 % saturation. Peach, mint, lavender, warm
  grey, pale blue. One tint per region, never two regions sharing.
- Line art: near-black, thin, and the **same weight everywhere**.
- ⭐ **Exactly one saturated accent colour in the whole figure**, and it marks the thing the
  figure is about — the stage under test, the arrow that moves, the token being tracked.
  Amber or orange works. Everything else is black line art on a pale tint.
- Two semantic colours, separate from the accent and used only for meaning: **green for
  kept / correct / retained**, **red for dropped / wrong / removed**.
- Colour inside formulas and quoted text is cheap and legible: one term in red, another in
  green, inside otherwise black text.
- ⛔ Never colour something because the palette had a spare colour. A colour that carries no
  distinction teaches the reader one that is not there.

## 3 · Line and shape grammar

- **Dashed outline means a set or a phase; solid outline means a single object.** Hold this
  distinction everywhere in the figure.
- Generous corner radius on boxes; larger still on the region containers.
- **Pick one convention and hold it**: either neutral dark outlines with coloured fills, or
  coloured outlines with white fills. ⛔ Doing both at once is what makes a figure read as
  clip art.
- Arrows: solid, one weight, with a clear triangular head. Label them **on** the arrow, in
  bold, and only when the label adds something.
- A dashed rule under a box's title, separating its header from its contents, is worth using
  when a box holds a list.

## 4 · Icons

- **Give every noun a glyph.** A diagram of labelled rectangles reads as a first draft.
- **One visual family throughout** — all flat, or all line, never mixed — at one stroke
  weight. Flat illustrations with an outline and a little shading read warmer than bare line
  glyphs and are a good default.
- Recolour each icon to the role of the thing it labels.
- Conventional glyphs: a stack of documents or a cylinder for a corpus; a small grid of
  squares for chunks or cells; nodes and edges for a graph; a chip or a robot for a model; a
  layered stack for an encoder; a flat avatar for a user; a stacked-disc cylinder for a
  store; a lightbulb for an answer; a target or checklist for a metric.
- **Three offset rectangles mean "many documents."** Use it consistently.
- ⚠ An icon nobody can name is worse than a word. If the reader cannot tell your glyph is a
  retriever, label it.

## 5 · Text

- Region banners are the largest text. Block labels are **one to three words**, noun phrases.
- ⭐ **Put real example content in the figure.** A real question, a real model output, a real
  retrieved document, quoted exactly, inside a bordered box in a monospaced face. This is the
  single highest-value move in the style: a reader who sees the actual string understands the
  pipeline immediately and believes it.
- Show a prompt as a bordered or dashed speech box with the model's mark beside it.
- ⛔ No sentences. Anything that explains the figure belongs in the caption, not in it.
- Dense is fine. Regions are what make density readable — manage it by grouping, never by
  deleting content. Sparse is not the goal.

## 6 · Prohibitions

- ⛔ **No measured quantity.** No rate, no score, no count of runs, no percentage. If the
  figure needs a number to make its point, this is the wrong tool — generate it from data.
- ⛔ No gradients, no 3-D shading, no drop shadows on boxes, no glow.
- ⛔ No legend. If a colour needs explaining, label the thing itself.
- ⛔ No decorative background, no texture, no photographic elements.
- ⛔ No text so small it would be unreadable at one column of a printed page.

---

## 7 · A prompt block you can paste

Append this to whatever brief says what to draw:

> Draw this as a flat vector academic figure on a white background, in the style used by
> top-conference method figures.
>
> Compose it as three to six clearly separated REGIONS, each with a rounded dashed border, a
> pale desaturated tint of its own, a dark circular numbered badge at its top-left, and a bold
> title beside the badge. Do not lay the figure out as a single left-to-right chain of boxes.
> Inside each region the flow runs left to right. Where two halves of the figure differ in
> kind, separate them with one vertical dashed rule and name both halves.
>
> Use near-black line art of a single consistent weight, and exactly one saturated accent
> colour — amber — reserved for the element the figure is about. Use green only for
> kept/correct and red only for dropped/wrong. No other saturated colour anywhere.
>
> Give every noun an icon, all from one visual family, flat with a light outline, recoloured
> to its role. Dashed outlines mean a group; solid outlines mean a single object. Label boxes
> in one to three words. Where the figure shows an input or an output, quote a real example
> string verbatim in a monospaced bordered box.
>
> Do not use gradients, 3-D shading, drop shadows, glows, legends, textures or photographs.
> Do not include any number, percentage, score or measurement. Keep all text large enough to
> read when the figure is one column wide on a printed page.
