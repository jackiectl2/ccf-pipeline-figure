---
name: ccf-pipeline-figure
description: >-
  Read a research-project folder and produce a publication-ready CONCEPTUAL figure from one
  short request: pipeline, framework, architecture, mechanism, data-flow, system diagram, or
  Figure 1 for the Intro/Method rather than Results. Use for 论文流程图 / 框架图 / 机制图 /
  架构图 / pipeline 图 when Codex should derive the technical brief, call its subscription-
  backed built-in image generator, preserve every candidate, explore at most seven fresh
  candidates, then locally refine the best candidate at most three times when needed. Do not use
  for data figures where position, length, angle, or colour encodes a measured quantity.
metadata:
  short-description: One-line project-to-pipeline figure workflow
---

# ccf-pipeline-figure

**One rule decides whether this skill applies at all.** Ask: *does any position, length,
angle or colour in this figure encode a measured quantity?*

- **Yes** → this is a data figure. Stop. Plot it from a results file. Do not use this skill.
- **No** → it encodes structure. Continue.

A hand-placed bar is a number nobody can reproduce. Never draw data in a diagram tool.

---

## Fast path · one short request is enough

This is the default Codex workflow when the user supplies a project folder and asks for a
paper pipeline figure. It is authoritative over later legacy draw.io production notes wherever
the two routes differ. The corpus evidence, scientific rules, composition rules, and honesty
rules later in this file still apply where they do not conflict with this fast path.

Native explicit invocation is:

```text
$ccf-pipeline-figure /path/to/project
$ccf-pipeline-figure /path/to/project — portrait, single-column, emphasize the two evidence lanes
```

In Codex, `/skills` opens the skill picker and `$ccf-pipeline-figure` mentions this skill.
Do not require the user to paste a brief, the image-model style file, or a long generation
prompt. If the path is omitted, use the current working directory. Treat any text after the
path as an aesthetic or emphasis override, not as a requirement to restate the method.

### Tool boundary: built-in image generation only

1. Load and follow the installed system skill named `$imagegen`.
2. Use its subscription-backed **built-in image generation tool**. Do not use an image MCP,
   browser automation, a model website, the CLI/API fallback, a custom SDK runner, or
   `OPENAI_API_KEY`.
3. During the fresh-candidate phase, use new-image generation only. Do not pass
   `referenced_image_paths` or include a prior generated figure as conversation image context.
4. If all seven fresh candidates fail, switch to built-in edit mode for the bounded refinement
   phase defined below. Use the selected best candidate as the sole edit target and preserve every
   already-correct region aggressively.
5. The built-in tool may not expose a model selector. If it explicitly exposes GPT Image 2.5,
   prefer **GPT Image 2.5 Sunburst** for final-quality scientific figures. If it exposes no
   selector, use the built-in host-managed backend and report that fact; never claim a model
   version the tool did not confirm, and never switch to API/CLI merely to force a model ID.

### End-to-end workflow

#### 1. Resolve and inspect the project

- Resolve the project folder first. Read every applicable `AGENTS.md`, `CLAUDE.md`, project
  policy, or equivalent instruction file before other project content.
- Never open a file that project rules prohibit. Never open secrets, credentials, private
  keys, environment files, or unrelated personal data.
- Inventory with `rg --files` before reading. Cover the paper, README files, method/design
  documentation, configuration, experiment and analysis code, tests, examples, and the
  structure of key outputs. Binary artefacts need only structural inspection unless their
  content is necessary and permitted.
- Identify what is knowable before experiments. Results may be inspected only when permitted
  and only to prevent them leaking into the method figure; never turn a posterior observation
  into a method stage or callout.

#### 2. Derive the technical brief automatically

Create or update `<project>/TECHNICAL_FIGURE_BRIEF.md`. It must contain:

- figure purpose and inputs;
- three to six named regions/stages;
- every object, operation, arrow, branch, shared path, and reconvergence;
- exact short labels and documentation-safe real example strings;
- scientific invariants whose topology or meaning cannot change;
- explicit exclusions separating method from results; and
- a source-of-truth table citing the project files behind each part.

The brief is the scientific authority. Do not draw until every arrow can be justified from
code, configuration, tests, or project documentation. Do not ask the user to write this brief
when the project contains enough evidence to derive it.

#### 3. Build the actual generation prompt

After the brief exists, read `assets/STYLE-FOR-IMAGE-MODELS.md` completely. Construct a
self-contained prompt in this order:

1. primary request and pre-experiment purpose;
2. soft-colored editorial-comic visual target near the top;
3. canvas and global reading order;
4. region-by-region scientific topology and exact arrows;
5. branches, shared kernels, typed boundaries, and joins;
6. exact labels and permitted example strings;
7. scientific invariants and method/result exclusions;
8. readability and output intent.

The brief wins on science. The style file wins on palette, icon vocabulary, decoration,
typography, and comic energy. A user-supplied visual preference wins over the style defaults
but never over scientific topology or result exclusions.

#### 4. Save before and after every generation

Use this immutable layout inside the target project:

```text
output/imagegen/<project-name>/<figure-name>/
  v01.prompt.md
  v01.png
  v01.review.md
  v02.prompt.md
  v02.png
  v02.review.md
  ...
  SELECTED.md
```

- Scan existing versions and continue at the next unused number. Never restart at `v01` when
  earlier files exist.
- Save the exact prompt as `vNN.prompt.md` before or immediately after its generation, without
  rewriting it to describe the output retrospectively.
- Copy the generated bitmap from the built-in tool's managed output location to `vNN.png`.
- Inspect it and save the disposition and concrete defects in `vNN.review.md`.
- Record `phase: fresh_candidate` or `phase: local_refinement` in every prompt and review. A
  refinement record also names its exact parent version and the defects it is allowed to change.
- Never overwrite, delete, rename, or silently discard an earlier image, prompt, or review,
  including rejected candidates.
- `SELECTED.md` names the best passing version and explains the choice. It is an index, not a
  replacement for the versioned files.

#### 5. Iterate in two bounded phases, then stop

**Phase A — fresh exploration**

- Generate **at most seven fresh candidates total per invocation**, including the first. Seven is
  a hard exploration ceiling, not a target: stop early as soon as one candidate passes all hard
  scientific and visual checks. The user may explicitly lower this ceiling but may not raise it.
- Every failed fresh candidate receives a concrete review. Feed only the review's targeted
  correction into the next text prompt, then generate again from the brief and style file alone.
  Do not supply any earlier bitmap as a reference during this phase.

**Phase B — local refinement of the best candidate**

- Enter this phase automatically only when the fresh-candidate ceiling is exhausted and none
  passes. Do not ask the user to authorize the transition.
- Rank the fresh candidates using scientific correctness first, then the number and severity of
  remaining visual defects. Select one best base and record the choice in its review and
  `SELECTED.md` as provisional.
- Consolidate the relevant defects from all fresh-candidate reviews into a short refinement
  checklist. Each refinement prompt must name only the local changes for the current round and
  explicitly preserve the base candidate's correct topology, composition, labels, palette,
  typography, icons, and unaffected regions.
- Use built-in image edit mode with the current best bitmap as the sole edit target. Save the edit
  as the next immutable `vNN` version; never overwrite the parent. If an edit regresses a correct
  area, keep the earlier best as the parent for the next round rather than compounding the drift.
- Perform **at most three local-refinement rounds**. Stop early when a refinement passes every hard
  check. After the third refinement, stop even if defects remain; select the best version across
  both phases and report every unresolved defect.

The absolute per-invocation ceiling is therefore seven fresh candidates plus three local
refinements. Never restart exploration, open another hidden batch, or continue into an open-ended
loop inside the same invocation.

#### 6. Review each candidate at two levels

**Scientific hard checks** — any failure rejects the candidate:

- arrow direction, branches, shared paths, reconvergences, optional paths, and evidence-type
  boundaries match the brief;
- the global figure is not flattened into a misleading single chain;
- exact labels are present and correctly spelled;
- no experiment result, score, rate, proportion, dataset/sample size, comparison, ablation,
  error analysis, success/failure total, or posterior conclusion appears; and
- decorative marks cannot be mistaken for nodes, ports, arrows, outcomes, or measured data.

**Visual hard checks** — any failure triggers another candidate while budget remains:

- the thumbnail reads as a softly colored editorial-comic infographic, not a grid of black
  text boxes or a restrained corporate flowchart;
- light tints vary across the figure without requiring a unique color for every region; the
  whole background is not one uniform color, and large dark fills are absent;
- every major noun or operation has a recognizable glyph, with varied silhouettes rather
  than repeated document/folder icons;
- no standalone overall title banner, landscape, road, tree, or exterior signboard appears;
  the composition starts directly with Region 1 and is cropped tightly around the numbered
  method regions;
- decorative accents stay inside region boundaries and do not consume a separate row or
  margin; short method-only explanatory lines remain allowed;
- labels remain readable at the intended paper width; and
- decoration supports hierarchy without obscuring the scientific graph.

#### 7. Finish with an auditable handoff

Report the project brief path, every image/prompt/review path created in this invocation, the
fresh-candidate and refinement counts, the selected version and its parent chain, the stopping
reason, and whether the backend model was explicit or host-managed. Do not insert the figure into
a paper, edit LaTeX, create PPTX/SVG/draw.io, commit the project, or push anything unless the user
separately asks for those actions.

---

## 0 · Two things to settle before any rule

### 0.1 Legacy vector route — `ccf-figuresmith-skills` owns its production half

The fast path above is self-contained and does not require `ccf-figuresmith-skills`. Use this
legacy route only when the user explicitly asks for editable/vector output, deterministic
code-native generation, draw.io, or PDF rather than a built-in-imagegen raster.

⭐ **Vector genre and taste → here. Vector production and gating → `ccf-figuresmith-skills`.** Both skills
state the split, in those words. This file deliberately does **not** restate what figuresmith
already covers: two copies of a rule drift apart, and nobody notices until a figure ships
wrong. Where the rule is figuresmith's, you get **one line of invariant plus a pointer** —
enough that this file still works alone, not enough to drift.

**Delegated wholesale. Read them there before shipping anything; none of them is optional.**
Paths are relative to the `ccf-figuresmith-skills` skill directory.

| what | the invariant, in one line | read |
|---|---|---|
| **True printed size** | Draw at the width it will print; `\includegraphics` scaling shrinks every font silently. | SKILL.md rule 2; `references/diagrams.md` §3 |
| **Tool and format** | In the legacy vector route, a script emits `.drawio`; a hand edit forks to `*.manual.drawio` and *that* one ships. | `references/diagrams.md` §1, §2, §2.1 |
| **Icon mechanics** | Recolour the single `fill="currentColor"`; inject a second `fill` and draw.io renders **nothing at all**, silently. | `references/diagrams.md` §5; `assets/icons/` |
| **The text-fit gate** | The generator refuses to emit a label that overflows its box. A gate with known failures stops being read. | `references/diagrams.md` §7; `assets/build_drawio_skeleton.py` |
| **Export flags** | `-x` is required or it hangs forever; never `-e` on a PNG; never `--disable-gpu`; `width_px = frac × text_width_in × dpi`. | `references/diagrams.md` §4 |
| **Iterating** | Review every render and stop at the declared finite cap; never turn refinement into an open-ended generation loop. | SKILL.md rule 5 |
| **Verify on the compiled page** | Find the page from the `.aux`, rasterise it, look at it. Floats move. | SKILL.md rule 6 |
| **Caption discipline** | One line. Everything substantive goes in the body text. | SKILL.md "Caption discipline" |
| **Honesty rules** | Regenerable from committed code plus committed data, in one command. | SKILL.md "Honesty rules" |
| **Working with the user, delivery, Overleaf** | Decide small things yourself, batch the questions, keep the alternatives, don't push. | SKILL.md "Working with the user" / "Delivery" |
| **Where sources live** | Only the exported raster goes in a collaboration repo; generator and sources sit outside it. | `references/diagrams.md` §9 |
| **Environment** | Fonts that do not exist on a cluster fail silently. | `references/environment.md` |

**Kept here, because figuresmith has no equivalent — this is the whole reason the skill exists:**

- **§0.2, the corpus and its grading.** figuresmith's aesthetic bar opens with *"Study real
  exemplars before inventing anything"* — two or three recent papers in the target venue.
  This skill **is** that study, done once over 925 figures,
  narrowed to 82 of this genre, and graded one by one. It replaces the instruction to go
  look with the answer.
- **§1, how many conceptual figures a paper should have** — measured, and it contradicts the
  usual advice.
- **§2.1, regions rather than a chain.** figuresmith says a straight chain is usually wrong;
  §2.1 says what the starred figures draw *instead*, and the four ways they mark it.
- **§2.2, one accent colour that means something**, and the median-4 rule.
- **§2.3, the icon *vocabulary*** — which glyph stands for which noun. figuresmith owns how
  to *render* an icon; it does not say which one to pick.
- **§2.4, verbatim example content** — the highest-lift single move in the style.
- **§3, the devices specific to long-context / memory / evaluation papers.**
- **Step 0, read the working folder first** — including the list of claims the paper may not
  make. A figure that implies a forbidden claim is worse than no figure.
- **Step 1, name the regions before opening any tool.**
- **The geometry half of Step 3.** figuresmith mandates looking at the render; it does not
  warn that the eye is *unreliable about geometry* on a rescaled render. That half cost this
  project twenty minutes twice. It is the one rule here that contradicts nothing and is
  covered nowhere else.
- **§5, the failure modes actually seen in this corpus.**

**One sentence is deliberately stated in both files: the data-vs-structure test at the top.**
It has to be, because each skill must be able to refuse a figure on its own. ⚠ **If the two
ever differ, this file is wrong and figuresmith's Step 0 is the authority.**

⭐ **One disagreement, settled by measurement rather than by taste.** figuresmith's
deliverable for a diagram is a raster exported from `.drawio`; this project began with an
**SVG emitted directly by a Python generator**, and a vector deliverable is what was wanted.
The tie-break turned out to be empirical, not aesthetic: **on this machine no SVG rasteriser
preserves the canvas** — `rsvg-convert`, `cairosvg` and `inkscape` are all absent, and
`qlmanage` returns a *square* image with the figure scaled to fill and the right and bottom
edges cut off. The committed PNG of this project's one conceptual figure was such a crop,
missing about a sixth of its width, **while the SVG it came from was measurably clean**.
draw.io exports a vector PDF whose MediaBox equals the canvas, in about four seconds, and
that PDF is what LaTeX wants anyway.

⇒ **For the legacy vector route, generate `.drawio`; ship the PDF.** The evidence is in `figures/diagrams/out/COMPARISON.md`,
and the project's own survey (`FIGURE-WORKFLOW.md` §6) had independently reached the same
route for the hero conceptual figure. Where a project has a different exporter, re-measure
rather than inheriting this conclusion. This does not override the built-in-imagegen fast
path, whose auditable sources are the brief, exact prompt, immutable candidate, and review.

**If `ccf-figuresmith-skills` is not installed** in the project you are working in, every
pointer above dangles. The one-line invariants are then all you have, and they are enough to
avoid the failure but not enough to do it well — say so rather than proceeding as if the
delegated half had been done.

### 0.2 Where these rules came from, and how much to trust each one

⭐ **This is not a style guide assembled from taste.** It was distilled from a corpus that
was built, filtered and graded, and every claim below is marked with its evidence. Rules
marked **[MEASURED]** come from counts over that corpus; rules marked **[INFERRED]** are my
reading of what the measured pattern implies and are the ones to argue with.

**The corpus.** 54 papers, all submitted 2024-05 or later with 2025+ preferred — 42
award-winning papers from NeurIPS / ICLR / ICML / CVPR / ICCV / ACL / EMNLP / AAAI 2024–2026,
plus 12 in the long-context / memory / evaluation direction. Every figure of all 54 was
pulled with the authors' own captions: 925 figures. Two strict binary passes by
`gpt-5.6-sol` opened **every single one** and kept 82 of the one genre.

**Then a human graded those 82**, and the grading is the single most important input here.
⚠ **81 of them, in fact** — `02-tree-naming-convention.png` carries no verdict, and the three
counts below add to 81, not 82:

| verdict | n | what it means |
|---|---:|---|
| ⭐ **S — "draw mine like this"** | **17** | the house style. Weighted heaviest. |
| K — keep | 34 | good of its kind; contributes device statistics only |
| D — drop | 30 | not wanted |

⚠ **The most surprising result, and it should change how you read the rest of this file:**

| source | S | K | D |
|---|---:|---:|---:|
| figures circulating on Chinese social media | **16** | 3 | 2 |
| arXiv award-paper figures | **1** | 31 | 28 |

**16 of 17 stars went to one visual tradition, and 28 of 30 drops were award-paper figures
from top Western venues.** Winning a best-paper award does not make a figure worth
imitating. ⚠ Note the confound honestly: the social-media images are screenshots chosen by
people *because* they were striking, while the arXiv figures are every figure in the paper,
including the dull ones. The selection differs, not only the drawing. But the S set is
internally consistent enough that the style below is real, not an artefact of that.

**Evidence files** (in `literature/`, if this repo has them): `FINAL_PICK.json` (the human
grading), `KEEP.json` (`layout`, `text_density` and provenance per figure), `ROSTER.json`
(the papers and how each award was verified), and the two vision passes that carry the
role verdicts, `award-figs/VISION_A.json` and `amnesia-adjacent/VISION_B.json`.
⚠ **Not** `*/CENSUS.json` — those enumerate the figures but their `role` field is null
throughout, by their own note, and an earlier version of this line sent readers there.

---

### 0.3 The numbers were re-derived, and six of them were wrong

⭐ **`assets/audit_corpus.py` recomputes every count in this file from the committed corpus
JSONs and checks it against the value printed here.** One command:

```bash
python3 .claude/skills/ccf-pipeline-figure/assets/audit_corpus.py literature
```

§6 says a figure must be regenerable from committed code plus committed data. The skill's own
statistics were not: they were typed into prose from four separate vision passes and then
edited. **On the first run, 9 of 15 checks passed and 6 failed**, and a seventh error was found by
hand: the prose under §0.2's own table said 26 of 30 drops were award-paper figures where
the table one line above says 28. A FAIL means this file and the corpus disagree; the corpus
wins.

**The four sets, which is what the prose kept eliding.** A count from one says nothing about
another, and the denominators differ by a factor of eight:

| set | what it is | what rests on it |
|---|---|---|
| **A** `award-figs/VISION_A.json` | 192 figures over 28 award papers, **36 of them conceptual** | §1's census, §2.1's `left_to_right`, §2.2's colour median, §2.4's density median |
| **B** `amnesia-adjacent/VISION_B.json` | 77 figures over 12 long-context / memory / evaluation papers | all of §3, and §1's direction column |
| **K** `KEEP.json` | the 82 figures of this genre kept from both groups, with `layout` and `text_density` | the star-versus-drop comparisons |
| **P** `FINAL_PICK.json` | the same 82, with the human S / K / D grade and a free-text `devices` list | §0.2, §2.3 |

⛔ **From here on, every count in this file names its set.** A bare "9 figures do this" was
the actual defect — not the arithmetic.

**What failed, and what the failures have in common:**

| claim as printed | what the data says |
|---|---|
| 82 figures graded | **81** — one carries no verdict |
| direction Figure 1: qualitative 20 %, hybrid — | **10 % and 10 %**, over 10 papers not 12 |
| *not one* starred figure is a plain chain | **one is**, `01-LIC_simulator_flat_v3.png` |
| plain-chain lift 29 % → 0 % | **67 % → 6 %** — the effect is *larger* than was claimed |
| "actor" lift 35 % → 3 % | **12 % → 3 %**, or 41 % → 17 % if you search `icon` instead |
| ten renderings of a long context | **twenty-one** |
| 26 of 30 drops are award-paper figures | **28** — contradicting the table directly above it |

⭐ **The pattern is worth more than the seven corrections.** Not one of them was arithmetic.
Four are a number quoted **without its denominator**, so a count over 36 award figures and a
count over 82 graded ones read identically on the page. One is a **rounded absolute** — "not
one" for "one of seventeen" — which is the most tempting error in this whole file, because the
tidy version is the one that argues better. And one is a number lifted **from the wrong key of
the right file** (10 was the count of conceptual figures, sitting two keys from the 21 it was
printed as).

⚠ **And the direction of the errors is not random: every one of them made the rule sound
stronger than the corpus supports.** That is what you would expect from claims written while
arguing for a style, which is exactly what this file is. Re-run the audit before quoting a
number from here.

---

## 1 · How many conceptual figures a paper should have — [MEASURED]

Read this before planning figures, because the honest answer contradicts the common advice.

**Across 28 award-winning papers, counting every conceptual figure among each paper's first
eight:**

| conceptual figures | papers |
|---:|---:|
| **0** | **10 (36 %)** |
| 1 | 8 |
| 2 | 6 |
| 3 or more | **4 (14 %)** |

**Median: 1. Mean: 1.29. Maximum: 6.**

⛔ **"An archival paper needs 2–3 framework figures" is not what award papers do.** Ten of
twenty-eight carry none at all, and two papers in the corpus won with **zero figures of any
kind**. Only 14 % carry three or more.

**And what Figure 1 actually is:**

| Figure 1 is a… | award papers (n = 28) | the direction (n = 10) |
|---|---:|---:|
| conceptual figure | 39 % | **20 %** |
| **data plot** | 25 % | ⭐ **60 %** |
| qualitative panel | 18 % | 10 % |
| hybrid | 18 % | 10 % |

⚠ **The direction column is 10 papers, not 12** — two of the twelve have no recorded opening
figure. An earlier version of this table printed 20 % for qualitative and a dash for hybrid,
which merged two single-paper cells into one.

⭐ **In the long-context / evaluation direction specifically, the convention is to open with
the result, not with an architecture.** NoLiMa, HELMET, *Lost in the Middle*, RULER and
*Are Emergent Abilities a Mirage* all lead with a data plot. If you are writing in this
area, a hero architecture diagram on page 1 is the *unusual* choice and needs a reason.

**Recommendation [INFERRED]:** one excellent conceptual figure, plus a data plot as Figure 1.
Not three. The second and third conceptual figures dilute rather than add — unless the paper
genuinely has three separable structures, which is what the 14 % have.

---

## 2 · The house style, in full

⭐ **Handing this genre to an IMAGE model?** Use
`assets/STYLE-FOR-IMAGE-MODELS.md` — an operational editorial-comic profile tuned for raster
generation. It preserves the structural evidence in this section but uses soft color, a richer
icon vocabulary, region-bounded decoration, and shallow comic depth. Its palette and region
color rules govern the raster route instead of the measured vector defaults below. It carries
**no statistics on purpose**: counts
stay here; image-model instructions live there.
⛔ It is only for figures carrying no measured quantity — an image model bakes numbers into
pixels, where nothing can check them.

Everything in this section is what the 17 starred figures share. Where a device appears in
the starred set far more than in the dropped set, the lift is given.

### 2.1 Composition: regions, not a chain — [MEASURED, 67 % of drops → 6 % of stars]

⛔ **The single most common failure is five rectangles left to right.** Two thirds of the
dropped figures are a plain axis — 20 of 30 are recorded as `left_to_right` or
`top_to_bottom` — against **one of the seventeen starred**.

⚠ **That one exception is worth naming rather than rounding away**: `01-LIC_simulator_flat_v3.png`
is a starred figure whose layout field is plain `left_to_right`. An earlier version of this
file said *not one* starred figure is a chain, and printed the lift as 29 % → 0 %; neither
number is re-derivable from the corpus. **The effect is real and larger than was claimed —
and it was still stated wrongly.** Run `assets/audit_corpus.py`.

Every starred figure is **3 to 6 named REGIONS**, each holding a short micro-flow:

```
┌─ ❶ Graph building ─────────┐  ╎  ┌─ ❹ Retrieval & generation ──────┐
│ corpus → chunks → graph    │  ╎  │ question → conversion → answer  │
└────────────────────────────┘  ╎  └─────────────────────────────────┘
┌─ ❷ Index construction ─────┐  ╎  ┌─ shaded sub-panel ──────────────┐
│ graph → embeddings → index │  ╎  │ question ⇉ LLM / encoder ⇉ Pri. │
└────────────────────────────┘  ╎  └─────────────────────────────────┘
     Offline                    ╎        Online
```

**How the regions are marked**, all four seen in the starred set:

1. **A dashed boundary** around the region, with a small **numbered circular badge** (❶ ❷ ❸)
   and a short grey label sitting at the region's bottom-right corner.
2. **A pale tinted fill** — peach, mint, lavender, warm grey — one tint per region.
3. **A bold banner title** across the top of the region, in a heavier weight than anything
   inside it: *"The Pipeline of Benchmark Construction"*, *"Tasks with Varying Complexity"*.
4. **A single vertical dashed divider** splitting the whole figure into two named halves —
   `Offline ╎ Online`, `Training ╎ Inference`, `Before ╎ After`.

⭐ **Regions are what let these figures be far denser than a Western arXiv figure without
becoming unreadable.** The reader parses 4 regions, then reads inside one. Density is
managed by grouping, never by deleting content.

**Inside a region**, the flow is short and almost always left-to-right — **29 of the 36
conceptual figures found in the 28 award papers** use `left_to_right` as the dominant axis
**[MEASURED, set A]**. ⚠ That 36 is a different set from the 82 graded figures; see §0.3.
The global composition is a grid of regions; the local composition is a line.

### 2.2 Colour: one accent that means something — [MEASURED, median 4 meaning-carrying colours]

```
ground        white or near-white
region tints  4–6 desaturated pastels, one per region, ~8–12 % saturation
line art      near-black, 1.5–2 px, consistent weight
⭐ accent      ONE saturated hue — amber/orange in most starred figures
semantic      green = kept/correct, red = dropped/wrong  (separate from the accent)
```

⭐ **The accent is not decoration — it marks the thing the figure is about.** In the starred
figures the amber is used for: every arrow in the main flow; the graph edges that the method
constructs; the highlighted evidence inside a document; the token being tracked between
regions. Everything else is black line art on a pale tint.

**Median meaning-carrying colours: 4** **[MEASURED, set A, n = 36]**. If you are using more than six, you
are colouring things that do not need distinguishing.

⛔ Never use colour that means nothing. A block coloured because the slide theme had five
colours teaches the reader a distinction that is not there.

### 2.3 Icons carry the nouns — [MEASURED, but weakly: 41 % of stars → 17 % of drops]

⭐ **The starred figures are more than twice as likely to carry a glyph vocabulary**, and a
diagram of labelled rectangles reads as a draft.

⚠ **This is the weakest measurement in the file and its strength was overstated.** The claim
rests on a keyword query over a **free-text** `devices` field — 297 distinct strings across 82
figures — so the number moves with the word you search for: `icon` gives 41 % against 17 %,
`actor` gives 12 % against 3 %. An earlier version printed 35 % → 3 %, which matches neither.
Composition (§2.1) and text density (§2.4) rest on categorical fields and are much firmer
than this. Treat the icon rule as a strong prior, not as a counted fact.

| noun in your paper | the glyph the corpus uses |
|---|---|
| a corpus / dataset | a stack of documents, or a database cylinder |
| a chunk / shard | a small grid of squares, some tinted |
| a graph / structure | nodes and edges, edges in the accent colour |
| a model / LLM | a rounded block with a robot or a provider mark |
| an encoder | a small layered stack |
| a person / user | a flat avatar, often several to mean "users" |
| a store / index | a stacked-disc cylinder |
| an answer / insight | a lightbulb |
| a metric | a target, a checklist, a gauge |
| a prompt | a bordered box showing real text |

**Choosing them — the taste rules, which are this skill's:**

- **Same visual family throughout.** All flat, or all line — never mixed. Same stroke weight.
- **Recoloured to the role** of the thing they label, not left in stock colours.
- ⚠ **An icon nobody can name is worse than a word.** If a reader cannot tell your glyph is
  a "retriever", label it.

**Rendering them is figuresmith's** — the starter set, the `icon()` helper, base64 inlining
so the source stays offline forever, and the single-`fill="currentColor"` invariant whose
violation makes draw.io draw an empty box with no error: `references/diagrams.md` §5.

### 2.4 Text: few words, but real ones — [MEASURED, median text density "medium"]

- **Region banners**: bold, largest text in the figure.
- **Block labels**: 1–3 words, noun phrases. `Question conversion`, `Index`, `Operators`.
- ⭐ **Verbatim example content — 9 of the direction's figures do this** **[MEASURED]**. The
  starred figures show a *real* question, a *real* model output, a *real* retrieved
  document, quoted exactly. **This is the highest-value single move in the whole style.** A
  reader who sees `"Which region of France is Mont St. Michel located?"` inside the box
  understands the pipeline instantly and trusts it, because the figure is showing them the
  actual thing rather than the word "question".
- **Nothing that belongs in the caption.** No sentences.
- ⭐ **Not one of the seventeen starred figures has low text density** **[MEASURED, set P]** —
  0 of 17, against 12 of the 30 dropped. Sparseness is not what makes a figure good here;
  §2.1's regions are what make density survivable.

### 2.5 Captions

**One line**, and every substantive claim in the body text instead. → figuresmith SKILL.md,
"Caption discipline".

---

## 3 · Devices specific to long-context, memory and evaluation papers

These are what this direction's figures carry that a vision or RL paper's would not — each
counted over **set B: 77 figures from 12 long-context / memory / evaluation papers**
**[MEASURED]**. ⚠ That is not the 82 graded figures and not the 36 of set A; a count here
says nothing about either. §0.3 has the four sets.

### 3.1 How to draw a long context — this is the section to read twice

**Twenty-one distinct renderings were recorded**; the eight below are the ones that
generalise, and `references/direction-devices.md` lists all twenty-one with the file each
came from. **Pick one and commit; do not mix them** — two renderings of the same context in
one figure make it read as two different objects.

⚠ Both this file and that one said *ten*. The source file has 21 entries, and 10 is the
number of **conceptual figures** in the same set — a different quantity that sat two keys
away in the same JSON.

| rendering | when it fits |
|---|---|
| **A long horizontal bar**, grey-blue, with thin red vertical ticks marking the needle | when *position within the context* is the variable |
| **Two stacked lanes** of that bar — `full` above, `last-2K` below | when comparing two exposure policies |
| **A tall scrolling document glyph** with many grey text lines, the evidence line highlighted in the accent | when the haystack is a document, not a conversation |
| **A vertical stack of chat bubbles**, grouped and tinted by session | when the haystack is a conversation history |
| **A verbatim prompt box containing numbered documents**, the answer-bearing one bolded | ⭐ when you want the reader to *see* the task; strongest for evaluation papers |
| **A horizontal stream of coloured shard cards**, revealed one per stage | when information is disclosed progressively |
| **A blue full-instruction bar that fragments into small amber blocks**, rows indexed by turn | when a single instruction is split across turns |
| **Boxed sessions converging into one released history** | when several evidence sessions are packed into one context |

### 3.2 Ordered conversation as the mechanism — 10 figures [MEASURED]

⭐ Chronology is not background in this direction; it *is* the mechanism. Render turns as
**turn-indexed message units on a timeline**, with session boundaries and dates visible.
`s₁ … sₜ … sₜ₊ₙ` along an arrow, with probe windows `w₁ … w₈` marked beneath, is the
canonical form.

### 3.3 Controlled disclosure and position as a visible intervention — 8 figures [MEASURED]

If your paper *moves* information — changes where the answer sits, hides it, duplicates it —
the figure must show the move. Coloured shards, document ordinals, a marked strip. **A
manipulation the reader cannot see in the figure will not be believed from the text.**

### 3.4 External memory as a state boundary — 4 figures [MEASURED, "a convention, not a majority"]

Write → search → overwrite/reconcile, drawn as an explicit boundary the data crosses.

### 3.5 Verbatim source text kept as evidence — 9 figures [MEASURED]

See §2.4. In this direction it is close to a requirement.

---

## 4 · The workflow

Steps 0, 1 and the geometry half of Step 3 are this skill's. Steps 2, 4, 5 and 6 are
figuresmith's and are given here only as a checklist with pointers — **do not treat the
one-liner as the rule; go read it.**

⭐ **§9 is the evidence for this workflow**, gathered after the fact: sixteen workflows other
people actually use, which corroborate four of these steps, name one thing we are missing, and
rule several popular routes out on grounds this skill already holds.

### Step 0 — Read the working folder first

⛔ **Do not start drawing from the user's one-line request.** Read, in this order, whatever
exists:

1. `SUMMARY.md` / `NARRATIVE_REPORT.md` — the claims, and **the list of things the paper may
   not say**. A figure that implies a forbidden claim is worse than no figure.
2. `PAPER_PLAN.md` — the section structure and which figure is expected where.
3. `findings.md` — the actual results and their limits.
4. `experiments/*/out/*.json` — the artefacts, so any number in the figure is real.
5. The code that produced them, when a figure depicts a procedure — the diagram must match
   what the code does, not what the method section wishes it did.

⭐ **Then write one sentence: "this figure exists to make ___ visible."** If you cannot, the
figure has no job and should not be drawn.

### Step 1 — Choose the structure before the tool

Name the regions. Write them as a list before opening any editor:

```
❶ what goes in        ❷ what happens to it       ❸ what comes out
❹ how it is scored    ╎ split: before / after
```

If your list is a single chain, **go back**. A chain is almost always a
misrepresentation — the branches, the grouping and the loop are the content.

### Step 2 — Choose the production mode, then generate

**Built-in-imagegen fast path:** follow the authoritative workflow at the top of this file.
The brief, exact prompt, immutable candidate and review are the reproducibility record. During
fresh exploration, never hand-place corrections or use an earlier bitmap as a reference. After
the seven-candidate ceiling is exhausted, the bounded refinement phase may edit only the selected
best bitmap and must preserve every unaffected region.

**Legacy vector route:** the figure must be regenerable from committed code plus committed
data with one command, and must stay hand-fixable without rerunning anything. Tool choice, the
`.manual` fork, the `FROZEN` marker and dated backups: `references/diagrams.md` §1, §2, §2.1.

⭐ **`assets/house_style.py` is the §2 devices as code**, layered on figuresmith's skeleton
rather than copying it: tinted numbered regions with banner titles, the single-accent
palette, an actor (icon and label emitted as one unit), a verbatim content box, and a
geometry gate. Import it and the composition rules are enforced instead of remembered — it
refuses to write a figure with fewer than three regions, because a two-region figure is
almost always the chain §2.1 rules out. `figures/diagrams/make_instrument_drawio.py` is the
worked example.

Two things that belong to this genre rather than to figuresmith:

- ⛔ **Never type a number into a figure script.** If you catch yourself doing it, find the
  artefact it came from and read it. Where two artefacts must agree, make the generator
  **refuse to draw** on a mismatch rather than picking one.
- ⚠ **If the project has a FigureSpec JSON → SVG generator**, know its ceiling before
  choosing it: boxes, arrows, diamonds and tinted groups, with **no icon primitive and no
  two-level nesting** — which rules out most of §2.

### Step 3 — Look at the rendered PNG. Every time. But do not trust the eye about geometry.

The first half is figuresmith rule 4 and is not optional: use the Read tool on the actual
image, because **gates are blind to meaning**. Things caught only by looking, in this corpus
and this project: four mutually exclusive outcomes drawn as a sequential chain; an ordered
factor sorted alphabetically so the axis read `10-20, 20-30, 30-40, <10`; an icon that
rendered as nothing because its SVG was invalid; a caption counting bands the figure does
not draw.

⚠ **The second half is this skill's, and it cost twenty minutes here.** A rendered image is
shown to you *rescaled*, so judging positions from it is guesswork. Drawing this project's
instrument figure I twice reported it as "cropped at the right edge" from looking at the
render; both times the measurement refuted me — the SVG had **zero elements past the
canvas** and the browser's own `getBBox()` agreed.

⭐ **The two checks catch different things and neither substitutes for the other:**

| ask | tool | catches |
|---|---|---|
| does it *mean* the right thing? | your eyes on the render | a chain that should be a branch, a wrong sort order, a missing icon |
| does it *fit*? | the generator's own geometry gate, or `getBBox()` in a browser | overflow, clipping, collisions |
| ⭐ is the *shipped file* the figure? | the raster's aspect and ink box against the canvas | a rasteriser that squared, scaled or cropped it |

⭐ **`assets/artefact_gate.py` is the third row as code**, and it runs in the generator
rather than in a browser: it checks that the exported PDF and PNG agree with each other,
that no bitmap is embedded in a file claiming to be vector (`data:image/svg+xml` is fine —
that is how icons are inlined — while `image/png` is not), that the file holds as many
elements as the generator emitted, and that it is newer than the script that claims to have
written it. The device is borrowed from the one workflow in §9 that inspects its own output
package rather than its own render.

⛔ **Measuring the source is not measuring the deliverable, and the third row is the one this
project learned the hard way.** `fig_instrument.svg` had nothing past its canvas — measured,
twice, correctly. The PNG exported from it was missing a sixth of its width, because the only
rasteriser on the machine squares the canvas and cuts the overflow. **A clean source and a
broken artefact are entirely compatible**, and the only thing that catches it is measuring
the file you are actually going to ship, then looking at it on a compiled page.

⚠ **And check that the check can fail.** That crop survived because the generator tested
`png.exists()`, which a stale file from an earlier run satisfied. `assets/house_style.py`
compares the raster's aspect to the canvas instead. Before trusting any gate, make it fire
once on the broken input.

```js
// the geometry check, run in the browser on the rendered SVG
document.querySelectorAll('svg text, svg rect').forEach(e => {
  const b = e.getBBox();
  if (b.x + b.width > CANVAS_W) console.log('overflows:', e.textContent);
});
```

⛔ Never report a layout defect from eyeballing a rescaled render. Measure it, then say it.

### Step 4 — Iterate → figuresmith, plus one rule this genre adds

The first version that renders is rarely the one to ship. In the built-in-imagegen fast path,
review it against the saved brief and stop early when it passes. Otherwise explore up to seven
fresh text-only candidates. If all seven fail, select the strongest candidate and run at most
three local edit refinements against the consolidated review defects. The absolute ceiling remains
ten image outputs per invocation, partitioned as seven fresh candidates plus three refinements.
Independent review is optional when the user has authorized delegation; it is not a
precondition for completing an ordinary figure request. The legacy vector route follows
figuresmith SKILL.md rule 5.

⭐ **Change only what is wrong. Say so explicitly, every round.**

> *"Change [the wrong part] to [the right description], and keep every other brief and style
> requirement unchanged."*

During fresh exploration, put that instruction in the next text-only prompt without an image
reference. During bounded refinement, put it in an edit prompt whose sole target is the current
best candidate and list the unaffected regions as invariants.

**[MEASURED]** This is the single most-endorsed correction rule in the sixteen workflows
surveyed in §9 — the 3839♥ note gives it verbatim as *"最好的纠错方式"*, and the 5959♥ note
states the same constraint from the other side: let the model *"只改配色/字体，不重画主体"*.
It exists because the failure it prevents is the one every author complains about, in the
words of the 201♥ note: **"改对了一个地方，又把原本正确的细节改坏了"** — that author abandoned
fully-automatic generation over exactly this.

⚠ **It applies to a generator too, not only to an image model.** When a round of edits
touches the layout code, change the thing that was named and leave the rest; a rewrite that
happens to fix the reported defect while silently re-flowing everything else is the same
failure wearing different clothes, and the geometry gate will not catch it because the new
layout is internally consistent.

### Step 5 — Verify on the compiled page → figuresmith

Compiling without errors does not mean the figure sits well; floats move. Find the page from
the `.aux`, rasterise it, read it, and check the **log** rather than the existence of a PDF.
→ figuresmith SKILL.md rule 6.

### Step 6 — Size it at the true printed width → figuresmith

⚠ **The most repeated failure in figure work**, and the one thing to suspect first whenever
fonts look slightly small: draw at 10 inches, include at a 6.5 in `\linewidth`, and every
font silently shrinks by 35 %. Keep `width_in` and `\includegraphics[width=…]` in sync.
→ figuresmith SKILL.md rule 2 and `references/diagrams.md` §3, which has the `frac` argument
this rule needs and the bug that shipped without it.

⚠ **The genre-specific corollary**: **text and size are proportional.** §2 asks for a dense
figure — regions, icons, verbatim example content — so this genre's figures are usually the
paper's *widest*. Decide the width in Step 1, when you name the regions, not after drawing.

---

## 5 · Failure modes, each seen in this corpus

| failure | why it happens | the fix |
|---|---|---|
| ⛔ **Mutually exclusive outcomes drawn as a chain** | the generator lays nodes out in the order they were declared | branch them; a chain claims a sequence that does not exist |
| ⛔ **Five boxes left to right** | it is what a first draft looks like | §2.1 — regions |
| **Labelled rectangles, no icons** | icons feel like decoration | §2.3 — but read the caveat there; this is the file's weakest measurement |
| **Rainbow with no meaning** | the palette had N colours | §2.2 — median 4, each meaning something |
| **Text where a caption belongs** | the figure is explaining itself | move it to the body |
| **An icon that renders as an empty box** | a second `fill` was injected into the SVG | figuresmith `references/diagrams.md` §5 — nothing warns you |
| **Fonts too small** | the figure was scaled on inclusion | Step 6 |
| ⛔ **A shipped raster that is not the canvas** | the rasteriser squared or cropped it, and the generator only checked that a file existed | Step 3, third row — measure aspect and ink box, and delete the old file first so the check can fail |
| **A "framework" that is a bar chart** | the caption says overview, the figure is data | the test at the top of this file |
| ⚠ **Two mismatched nodes** | reported as the single most common failure of AI figure generators | check every arrow's source and target by eye |

---

## 6 · Honesty → figuresmith, plus one rule this genre adds

The honesty rules are figuresmith's and they are not style preferences — violating them puts
a false claim in a paper. Read them there: SKILL.md "Honesty rules".

⭐ **What this genre adds.** A conceptual figure looks like it carries no data, which is
exactly why a number smuggled into one is never checked. So: **every number that appears in
a conceptual figure is read from a committed artefact at draw time**, and where two artefacts
must agree, the generator **exits rather than drawing** on a mismatch. The figure and the
sentence about the figure read the same file, or they will drift and a reviewer will find it.

---

## 7 · Working with the user → figuresmith

Decide small things yourself and batch the questions; offer several options on anything
aesthetic and keep the alternatives; back up before redrawing something already approved;
comment out rather than delete; a labelled placeholder is a legitimate deliverable.
→ figuresmith SKILL.md "Working with the user" and "Delivery".

---

## 8 · Reference files

**This skill's** — the corpus, dissected:

- `references/house-style.md` — the starred set dissected figure by figure, with the device
  table, the tint palettes and the icon vocabulary in full.
- `references/direction-devices.md` — every recorded way this corpus draws a long context, a
  conversation history, a memory store and a controlled intervention, with file counts.
- `references/census.md` — the per-paper figure counts, the Figure-1 role distribution, and
  the method by which both were measured.
- `assets/audit_corpus.py` — ⭐ **re-derives every number in this file from the corpus and
  fails on any that disagrees.** Run it before quoting a statistic from §0–§3.

- `assets/artefact_gate.py` — opens the shipped file and asks whether it is what it claims
  to be: exports that agree, no embedded bitmap, enough elements, not stale. The checks the
  other two gates structurally cannot make.
- `assets/house_style.py` — §2 as importable primitives on top of figuresmith's skeleton:
  regions, the single accent, actors, verbatim boxes, and a build-time geometry gate that
  checks off-canvas and overlap for **text as well as boxes**. Its own first version exempted
  text, passed a figure clean, and the render then showed a pill written across a banner.

**figuresmith's** — the production half, which this file delegates to:

- `references/diagrams.md` — tool choice, font scaling with `frac`, the verified export
  flags, icon mechanics, the text-fit gate, where sources live.
- `references/environment.md` — fonts that fail silently, headless rendering.
- `assets/build_drawio_skeleton.py` — a working generator with the text-fit gate and
  `--export` to print the exact verified export command.
- `assets/icons/` — Bootstrap Icons (MIT) starter set.

---

## 9 · What sixteen observed workflows say about Step 0–6

⭐ **This skill's §2 was measured from 82 graded figures. Its Step 0–6 was not measured from
anything** — it came from `ccf-figuresmith-skills` and from GitHub, because an earlier attempt
to search the Chinese figure-craft community was blocked at login and gave up. That gap is now
filled: 41 keyword searches over six facets, 436 notes surfaced, **93 opened and read in full**,
16 workflows extracted with a verbatim quote behind every step, and five rounds of cross-model
audit that failed 22 of the first 23 records before any of them passed.

**The record is `references/production-workflows.md`** (and `.zh.md`). It documents what
other people do rather than what this skill does, so read it as evidence, not as rules.
⚠ Its raw records — `WORKFLOWS.json`, `DETAILS.json`, `SEARCH_LOG.json` and the generator
`stage_b.py` — stayed in the project they were collected in,
`ARIS-Auto-Research/amnesia-conference/literature/figure-refs/`.

⛔ **It is a purposive sample, not a survey.** A device appearing three times there is evidence
that it recurs, not evidence of how common it is.

### 9.1 What the collection corroborates

| our step | what corroborates it |
|---|---|
| **Step 1** — name the structure before opening the tool | **[MEASURED]** The most-developed draw.io workflow in the collection (W04, 1726♥) exists for exactly this reason, in its author's words: fix canvas, regions, font, palette, arrow direction and connection semantics first, **"避免模型边画边猜"** — to stop the model guessing while it draws. |
| **Step 2** — generate, never hand-place; emit `.drawio` | **[MEASURED]** Every workflow that reaches something editable does it by emitting the native format of an editor that already exists, or by rebuilding a raster into one. **Not one invents an editor.** `.drawio` is the most common choice. |
| **Step 3** — look at the render, every time | **[MEASURED]** W04's screenshot checklist is ours almost item for item: text overflowing its box, arrow direction and connection, missing or misplaced icons, alignment of highlight blocks, module hierarchy and reading order, and whether the file still opens. Arrived at independently. |
| **Step 6** — size at the true printed width | **[MEASURED]** A second draw.io implementation (940♥) states the rule in the same shape: check readability at the paper's two-column size, and **fix overflow and spacing before reducing any font**. |
| **§2.2** — one restrained accent colour | **[MEASURED]** The same implementation: low-saturation colours for semantics, **"再用一种克制的强调色突出原创模块"**. |

⇒ **[INFERRED]** Step 0–6 was not measured, but it turns out not to be idiosyncratic. Its
riskiest-looking rules are the ones others reached independently.

### 9.2 What it says we are missing

⭐ **One finding is worth more than the rest of this section.**

**[MEASURED]** Of the sixteen workflows, **exactly one checks its own output file rather than
its own picture**: `visio-image-rebuilder` (W08, 1107♥) scans the saved package for a whole
embedded PNG, so a pasted raster cannot pass itself off as a rebuild, and reconciles the shape
count to confirm something was really constructed. Seven records describe some check; the other
six look at a *render*.

⛔ **We have the same hole.** `assets/house_style.py` gates geometry and figuresmith gates text
fit — both read the *generator's* intent. Neither opens the shipped file and asks whether it is
what it claims to be. This project has already been bitten by exactly that class of defect
twice: a PNG that was a cropped stand-in for its SVG, and a success check (`png.exists()`) that
a stale file satisfied. **A check on the artefact is a different kind of check from a check on
the drawing, and we only have the second.**

Three smaller gaps, each [MEASURED] as present in the collection and absent here:

- **An append-only defect log and an asset ledger** (W04's implementation keeps both). Our §7
  mentions a `notes.md`; nothing enforces it and none exists.
- **The constrained-edit instruction** — *"change [the wrong part] to [the right description],
  **keep the rest unchanged**"* (W06, from a 3839♥ note). Step 4 says to iterate; it does not
  say to forbid redrawing what was already right, which is the failure every author complains
  about.
- **Divide and conquer when generation degrades** (W10, 3363♥): whole-figure vector generation
  fails where per-module generation succeeds, with a practical batch limit of about three.

### 9.3 What does not apply to the legacy vector route, and why

These observations explain why the old deterministic route rejected generated rasters. The
new fast path deliberately permits a raster only for a no-measurement conceptual figure and
compensates with an exact text brief, saved prompt, immutable versions, explicit review, and a
finite retry budget. The other exclusions below still apply to the legacy vector route.

| ruled out | which rule rules it out |
|---|---|
| **A model-generated raster containing measured quantities** (W06, W24, and the raster half of W01/W03) | §6 — every measured number must be read from a committed artefact at draw time. A generated raster cannot provide that guarantee. The built-in-imagegen fast path therefore forbids measured quantities rather than pretending to trace them. |
| **Hand-assembly in PowerPoint or Illustrator** (W03, and W01's step 4) | Same rule. The moment a human nudges an anchor point, one command no longer reproduces the figure. figuresmith's `.manual` fork exists for exactly this and requires the hand-edited file to be marked and frozen. |
| **Using a published figure as a layout template** (W13) | ⚠ [INFERRED] Not covered by an existing rule, and it should be: it inherits another paper's composition wholesale. Fine as scaffolding, a provenance question if shipped. |
| **The Visio routes** (W08, W15) | Windows, licensed Visio, PowerShell; W15 also needs Inkscape. None is available here. ⭐ **Take W08's structural check, not its stack.** |
| **The PPTX routes** (W09, W10, W11) | Not ruled out on principle — see §9.4. |

### 9.4 The PPTX question, answered on the same standard as the `.drawio` decision

**[MEASURED] It is real and it is popular.** Four independent records in the collection route a
raster into an editable PowerPoint: `img2pptx` (1190♥), the SVG-then-convert-to-shape recipe
(3363♥), `figure-to-ppt` (8♥), and `image-to-editable-ppt` (412♥). It is the most-represented
single answer to "the AI figure is pretty but I cannot change it".

**[MEASURED] What the collection establishes it buys**: selective object-level editability from
a picture — recognised text becomes real text boxes, reliable arrows can become native
connectors, and elements stay individually selectable.

**[MEASURED] What the collection establishes it costs**: repeated ungrouping to reach leaf
objects; an extra image-to-SVG pass with a batch limit of about three; shrinking every font
before editing; and an explicit fidelity-versus-editability switch where native arrows are
easier to edit but look different. ⛔ **And none of the four establishes that the result is
vector.** `figure-to-ppt` says outright that complex elements stay raster; `img2pptx`'s repo
says local raster crops are used where an element cannot be reliably vectorised; the SVG recipe
asks a model to "output SVG" and never checks what is inside it.

⇒ **The answer is no, and the reason is not taste.** The `.drawio` decision here was made on a
measurement — draw.io exports a PDF whose MediaBox equals the canvas, in about four seconds, on
this machine, where no SVG rasteriser preserves the canvas at all. **The PPTX route cannot be
held to that standard here**: scripted authoring needs `python-pptx` and headless conversion
needs LibreOffice, and **neither is installed** — PowerPoint and Keynote are present as GUI
applications only. ⚠ **That is a dependency-level finding, not an end-to-end test.** The
`.drawio` side was measured end to end and the PPTX side was not, so the honest comparison is:
one route is verified to work here, the other is unverified here and unverified for vector
output in every note that describes it.

⭐ **What to take from it anyway**: the anti-paste prompt from W11/W12 — *"do not paste the
image as a full-page background"*, and the list of things that must **not** be redrawn
(formulae, simulation plots, photographs). That exemption list is the half most recipes omit,
and it is the same instinct as §0's data-versus-structure test.
