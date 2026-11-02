# Isolated Figure Runs Implementation Plan

**Goal:** Keep numbered and flexible figure runs, including their briefs and later edits, in separate directories and prevent fresh runs from using prior Codex figures as references.

**Architecture:** A small standard-library allocator inspects only run metadata and atomically reserves a profile-specific directory. The skill routes all generated artifacts and later recolor/vector work through that directory, while a new run derives its content only from current research sources and eligible original manuscript figures.

**Tech Stack:** Markdown skill instructions, Python standard library, unittest.

**Spec:** User request in this chat on 2026-11-02: isolate 分区 and 非分区 output, warn on same-profile repeats, allow opposite-profile fresh starts, and prohibit influence from earlier Codex figure sessions.

## Constraints

- Do not invoke or load the globally disabled Figure Smith skill.
- Preserve existing output directories and project files; no migration or overwrite.
- `numbered_regions` uses `-numbered`; `topology_first` uses `-flexible` because regions remain optional.
- Each fresh run gets its own brief, PNGs, prompts, reviews, descriptions, and selection index.
- Only run metadata may be read during duplicate preflight; prior Codex images and prompts are excluded from new-run scientific/visual planning.

### Task 1: Reserve independent run directories

**Files:** Create `ccf-pipeline-figure/scripts/reserve_figure_run.py` and `ccf-pipeline-figure/scripts/test_reserve_figure_run.py`.

- [x] Implement read-only inspection of the target figure's run-directory names and compact profile metadata, including cautious legacy detection.
- [x] Reject an implicit same-profile repeat; allow an explicit new run with a new suffix. Use atomic `mkdir` so concurrent sessions cannot claim one run directory.
- [x] Test opposite-profile separation, same-profile duplicate warning, explicit repeat allocation, and concurrent claims.

### Task 2: Route the skill through the reserved directory

**Files:** Modify `ccf-pipeline-figure/SKILL.md`, `ccf-pipeline-figure/assets/STYLE-FOR-IMAGE-MODELS.md`, `ccf-pipeline-figure/references/composition-profiles.md`, and `ccf-pipeline-figure/references/png-svg-pdf.md` as needed.

- [x] Require preflight before every fresh figure request; distinguish new runs from recolor/vector continuation.
- [x] Put `TECHNICAL_FIGURE_BRIEF.md` and every versioned artifact inside the reserved run; scope version numbering and later stages to it.
- [x] Exclude prior Codex figure outputs, prompts, reviews, and briefs from a new run; permit only limited inspection of a verified pre-Codex manuscript original.

### Task 3: Validate and publish

- [x] Run allocator tests, skill validation, existing tests, corpus audit, and `git diff --check`.
- [x] Commit and push `main`; verify the remote branch and clean working tree.
