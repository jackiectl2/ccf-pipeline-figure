# Topology-first figure composition implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove mandatory region counts and numbering while retaining scientific completeness, readable text, minimal unambiguous connectors, and balanced canvas coverage.

**Architecture:** The scientific graph determines composition before any grouping treatment is chosen. Update the skill entrypoint and ImageGen prompt together, distinguish historical preferences from requirements, and remove the obsolete region-count gate in the retained local helper. No Figure Smith instructions, backend, hooks, or generation workflow will be invoked.

**Tech Stack:** Markdown instructions, Python unittest, existing skill and corpus validators.

**Spec:** The user's 2026-10-31 request in this chat: cancel fixed partitions and numbering; decide composition from scientific logic; retain content, readability, few arrows, and no large accidental blank areas; check and push.

## Global constraints

- Preserve every necessary entity and scientific relationship, including branches, joins, and feedback.
- Reduce only redundant drawn arrows; retain explicit direction where alternative encodings are ambiguous.
- Keep final-paper-size text tiers, contrast, and legibility checks unchanged.
- Avoid large accidental empty corners without forcing a panel mosaic or deleting content.
- Grouping, outlines, background fields, and numbering are separate optional choices.
- Do not generate images, edit a manuscript, activate Figure Smith, or change the PNG/SVG/PDF workflow.
- Execute inline: the plan template's execution subskills are unavailable in this session.

## Task 1: Remove executable layout quotas

**Files:** `ccf-pipeline-figure/assets/house_style.py`, `ccf-pipeline-figure/scripts/test_house_style.py`.

**Interfaces:** Preserve `Figure.region(x, y, w, h, badge, title, corner='', tint=0)` calls; an empty or null badge omits badge geometry. `Figure.write()` keeps geometry validation but has no region-count gate.

- [x] Add tests using a lightweight fake diagram and `Figure.__new__`, bypassing the legacy backend. Assert writes accept 0, 1, 2, 4, and 7 regions; empty/null badges emit no badge; an explicit badge still renders; overlap and canvas overflow still reject.
- [x] Run `python3 -m unittest discover -s ccf-pipeline-figure/scripts -p 'test_house_style.py' -v`; confirm old quota/badge behavior fails.
- [x] Remove the numeric region gate; conditionally emit badge geometry and give unnumbered titles the freed width. Update only directly related helper documentation.
- [x] Rerun the tests; require all to pass without loading the disabled backend.

## Task 2: Align planning, prompts, reviews, and historical guidance

**Files:** `ccf-pipeline-figure/SKILL.md`, `ccf-pipeline-figure/assets/STYLE-FOR-IMAGE-MODELS.md`, `ccf-pipeline-figure/references/house-style.md`.

**Interfaces:** The technical brief records graph type, reading order, optional groups, and separate reasons for each boundary, fill, or sequence number. The generation prompt and review use those decisions instead of a count or numbered-panel template.

- [x] Replace the required `three to six named regions/stages` with a topology-first composition plan. Allow true chains, parallel lanes, branching/rejoining graphs, feedback loops, hierarchies, and overview/detail layouts as appropriate, not as a quota.
- [x] Replace mandatory panel/badge instructions in both the prose style and paste-ready prompt. Make neutral gray fills conditional on actual background fields; later recoloring must not invent panels in an open composition.
- [x] Update visual review to accept open layouts and reject unsupported boundaries or implied ordering; retain content, arrow, text, whitespace, and scientific checks.
- [x] Reframe historical grid/chain claims as bounded preferences rather than universal rules. Preserve raw corpus records and provenance.
- [x] Manually walk through a true linear method, parallel inputs with fusion, a memory feedback architecture, and a training/inference split. Verify no case requires invented panels or numbered stages and every scientific relationship remains explicit or unambiguous.

## Task 3: Validate and publish

- [x] Run skill validation. The base Python lacks PyYAML; use `uv run --no-project --with pyyaml python /Users/ctl/.codex/skills/.system/skill-creator/scripts/quick_validate.py ccf-pipeline-figure` without changing project dependencies.
- [x] Run `python3 -m unittest discover -s ccf-pipeline-figure/scripts -p 'test_*.py' -v` and `python3 ccf-pipeline-figure/assets/audit_corpus.py`.
- [x] Review `git diff --check` and the complete diff; scan active instructions for residual fixed-count/mandatory-numbering language. Historical statements must be clearly nonbinding.
- [ ] Commit only the scoped changes with the configured noreply identity, push the current main branch, and verify remote HEAD and the installed skill symlink.

## Validation evidence before publication

- New layout tests failed on the previous gate/badge implementation, then passed after the patch.
- All 11 unit tests pass; all 17 existing corpus checks pass; the skill validator passes for the repository and installed symlink.
- The complete sizing-system section, PNG/SVG/PDF extension, and version-preservation/bounded-iteration sections are byte-for-byte unchanged from the previous commit. Scientific completeness, connector minimization, and final-width readability requirements remain present.
- Manual instruction walkthrough: a true sequence can stay open; parallel inputs retain their merge; memory retains its feedback edge; training/inference can use a divider without numbered panels. None requires invented stages or a fixed group count. All still require readable labels and balanced coverage.
- This is instruction/helper validation, not an ImageGen visual acceptance test. No images or manuscripts were generated or changed, and no disabled backend was loaded or invoked.
