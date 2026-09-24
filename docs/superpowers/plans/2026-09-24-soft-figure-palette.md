# Soft Figure Palette Implementation Plan

> **For agentic workers:** This is a focused inline update to the existing skill. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the current image-generation route use soft, lightly tinted colors without requiring a different color for every region.

**Architecture:** Update the operational style file and the matching routing and review language in `SKILL.md`. Preserve the measured legacy vector guidance and scientific color semantics.

**Tech Stack:** Markdown skill instructions; Git.

**Spec:** User direction in this conversation on 2026-09-23 and 2026-09-24: colors should be softer than candy colors, region colors may repeat, and the entire figure background should not be one uniform color.

## Global Constraints

- Keep text and scientific arrows legible.
- Keep colors that encode scientific roles consistent across the figure.
- Do not alter the measured corpus claims or legacy vector palette.
- Push the committed change to the current GitHub branch.

---

### Task 1: Update the image-generation color guidance

**Files:**
- Modify: `ccf-pipeline-figure/assets/STYLE-FOR-IMAGE-MODELS.md`
- Modify: `ccf-pipeline-figure/SKILL.md`

- [x] **Step 1:** Replace the candy-palette requirement and the per-region unique-color requirement with a soft, lightly tinted palette. State that regions may reuse colors while the whole background must show some variation.
- [x] **Step 2:** Update the paste-ready prompt and visual review checks to use the same color rule. Keep scientific role colors stable and ensure readable contrast.
- [x] **Step 3:** Run `quick_validate.py` for the skill, inspect `git diff --check` and the full diff, then commit and push the current branch.
