# Composition profile choice implementation plan

**Goal:** Let one installed skill offer the archived numbered-region composition and the current topology-first composition when creating a new figure.

**Architecture:** Keep common scientific, image generation, review, and export rules in the existing skill. Route only composition-specific planning, prompting, and review through a short reference selected once per new figure. Preserve the two existing Git branches as snapshots.

**Tech Stack:** Markdown skill instructions; existing Python skill validator and repository tests.

**Spec:** User request in this chat on 2026-11-01: offer a choice between the 3–6 named-region branch and the current flexible branch without replacing `main` for each project.

## Global constraints

- Do not invoke or load CCF Figure Smith.
- Preserve scientific content, readable final-size labels, minimal unambiguous arrows, balanced canvas coverage, and existing PNG/SVG/PDF workflow.
- Recolor uses the selected base figure's composition and asks no new composition question.
- Selection happens once per new figure, within the existing candidate/refinement question; an explicit user choice requires no redundant question.
- No Git branch switch is needed to choose a composition profile.

---

### Task 1: Add selectable composition profiles

**Files:** Create `ccf-pipeline-figure/references/composition-profiles.md`; modify `ccf-pipeline-figure/SKILL.md` and `ccf-pipeline-figure/assets/STYLE-FOR-IMAGE-MODELS.md`.

**Interface:** `composition_profile` is exactly `numbered_regions` or `topology_first`. It is recorded in the brief and version metadata. The style prompt receives only the selected profile's composition block.

- [x] Document the old 3–6 numbered-panel treatment from commit `90863f3` and the current topology-first treatment in one reference; neither profile may alter common scientific or typography rules.
- [x] Bundle the profile question with the existing candidate/refinement question; use an explicit profile choice without asking again.
- [x] Record the profile in the brief, prompt, review, description, and selection index. Later recolor inherits it from the neutral base.
- [x] Route composition planning, prompt construction, and review through the chosen profile. Remove contradictory unqualified layout directions from the shared paste-ready prompt.

### Task 2: Validate and publish

**Files:** The three instruction files above; no runtime script change is required.

- [x] Validate skill frontmatter, scan the assembled prompt for conflicting profile instructions, run existing unit and corpus checks, and inspect `git diff --check`.
- [x] Commit and push `main`, leaving `codex/3-to-6-named-regions` and `codex/topology-first-composition` unchanged. Verify remote refs.
