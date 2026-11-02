# Isolated figure runs

## Fresh-run preflight and reservation

Apply this before every request to draw a conceptual figure **from scratch**. Read project
rules first. Determine a stable ASCII `figure_slug`, preferring the manuscript's figure
label when it exists, otherwise the figure's scientific purpose. Resolve the selected
`composition_profile`. First inspect **all** existing run-directory names and compact
metadata under the project; match prior runs for the same figure even if an older session
used a different slug. Read only `RUN.json` and the minimal profile field in legacy
`SELECTED.md` or `v01.review.md`. Do not open prior Codex PNGs, SVGs, PDFs, prompts, full
reviews, descriptions, briefs, or handoffs during this preflight.

Use the bundled standard-library allocator from the skill root:

```text
python3 scripts/reserve_figure_run.py inspect --project /absolute/project --figure method-overview --profile numbered_regions
python3 scripts/reserve_figure_run.py reserve --project /absolute/project --figure method-overview --profile numbered_regions
```

`inspect` reports every known run plus exact slug matches. Compare the metadata list with
the requested figure's paper label and purpose; if two slugs may refer to the same figure,
resolve that ambiguity before `reserve`. Use the same stable slug for both profiles. The
allocator's duplicate check then protects the exact slug against races.

`numbered_regions` reserves `output/imagegen/<project-name>/<figure_slug>-numbered/`;
`topology_first` reserves `<figure_slug>-flexible/`. The latter means a flexible scientific
layout, not a ban on meaningful regions. The script creates `RUN.json` with the slug and
profile. Each directory owns its own `TECHNICAL_FIGURE_BRIEF.md`, `v01...` files, and
`SELECTED.md`; the project-root brief is not shared or overwritten. `mkdir` is atomic:
if another session claims the same path first, reservation fails instead of joining it.
If the scientific plan calls for a second, distinct conceptual figure, give it a different
`figure_slug` and repeat this preflight/reservation for its own run directory.

- **No same-profile prior run:** reserve the mode-specific directory and begin at `v01`.
  An existing opposite-profile run is expected and causes no warning or cross-reference.
- **Same-purpose, same-profile run found:** remind the user that this mode has already been
  drawn and ask whether this request continues that run or deliberately starts another
  independent run. If the user already explicitly requested a fresh repeat, do not ask
  again. A continuation uses the explicitly identified run and its current versions; a
  fresh repeat uses `reserve ... --new-run`, creating `-02`, `-03`, and so on. It never
  appends new-session candidates to an old run.
- **Unclassified legacy run found:** its profile cannot be inferred safely from an old
  filename alone. Warn about the existing figure and resolve whether it is a continuation
  or a fresh run before writing. Do not inspect its visual content to decide the mode.

An `existing_run` result (exit status 2) means **no directory was reserved**. Do not write
anything to that run. If a reservation races another session, inspect again and use the
same duplicate rule. Never use `mkdir -p` or `exist_ok=True` on a run directory as a way
to claim it.

## Clean-slate evidence boundary

For a fresh run, derive the scientific brief and generation prompt from the active paper's
text, project research/code/data, and applicable project instructions. Do not read or reuse
figures, prompts, reviews, descriptions, briefs, or handoffs produced by **another Codex
figure session**, even when its composition profile differs or its files are mentioned in
project notes. Do not use them as positive examples, negative examples, prompt context, or
ImageGen references. Reviews and local refinements produced **within the current run**
remain available for its own iteration.

A verified original figure that existed in the manuscript before these Codex figure runs
may be inspected briefly for its scientifically valid entities, relationship scope,
caption/label, and intended paper placement. It is not a layout or style template. If the
figure currently included in the manuscript is itself an earlier Codex output, use the
manuscript source to identify its slot and caption but do not inspect or copy its image.
When provenance is uncertain, skip visual inspection and rely on paper text and project
evidence. Do not read a legacy project-root `TECHNICAL_FIGURE_BRIEF.md` to seed a new run.

## Later invocations

Recolor and PNG→SVG→PDF conversion continue **one named run directory**; they do not call
`reserve`. Use its `RUN.json`, run-local brief, `SELECTED.md`, and selected version. If the
request does not identify a run and multiple runs could match, ask which run to continue
before reading their figures or editing. Never copy versions or selections between the
numbered and flexible paths, and never edit the same run concurrently from two sessions.
