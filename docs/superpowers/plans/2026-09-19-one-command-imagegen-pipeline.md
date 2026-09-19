# One-Command ImageGen Pipeline Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn `ccf-pipeline-figure` into a one-line Codex skill that reads a project folder, derives a method brief, generates a colorful comic-style technical roadmap with the built-in image generator, preserves every candidate, and stops after a bounded number of attempts.

**Architecture:** Keep the existing skill and evidence corpus, but add an authoritative Codex built-in-imagegen fast path at the top of `SKILL.md`. The fast path owns project discovery, brief generation, prompt construction, immutable versioned artifacts, review, selection, and stopping. Update the image-model style file to make editorial-comic styling the raster default, and add Codex UI metadata plus a user-scope symlink for native skill discovery.

**Tech Stack:** Codex agent skills, built-in `$imagegen` / `image_gen`, Markdown, YAML, Git.

**Spec:** User request in the 2026-09-19 Codex thread; `ccf-pipeline-figure/SKILL.md`; `ccf-pipeline-figure/assets/STYLE-FOR-IMAGE-MODELS.md`.

## Global Constraints

- Update the existing `ccf-pipeline-figure` skill; do not create another skill.
- Use Codex's subscription-backed built-in image generation only; do not use image-generation MCP, browser automation, CLI, API, or `OPENAI_API_KEY`.
- Preserve every generated image, exact prompt, and review; never overwrite or delete an earlier candidate.
- Generate at most ten fresh candidates per invocation; the user may request a smaller finite cap from one to ten.
- Generate every candidate from text only; do not pass earlier images as references or edit targets.
- Keep scientific topology and method/result separation authoritative over decoration.
- Work on a new Git branch so `main` retains the old skill.

---

### Task 1: Add the one-line built-in-imagegen workflow

**Files:**
- Modify: `ccf-pipeline-figure/SKILL.md`
- Create: `ccf-pipeline-figure/agents/openai.yaml`

**Interfaces:**
- Consumes: `$ccf-pipeline-figure <project-folder> [short preferences]`.
- Produces: project brief, versioned image/prompt/review triples, and a selected-candidate record.

- [x] **Step 1:** Update the skill description and add the authoritative fast path, tool boundary, versioning scheme, review rubric, and ten-candidate default cap.
- [x] **Step 2:** Add UI metadata with a one-sentence `$ccf-pipeline-figure` default prompt and keep implicit invocation enabled.
- [x] **Step 3:** Check the workflow for contradictions with later draw.io/vector guidance and mark the mode boundary explicitly.

### Task 2: Make editorial-comic styling the raster default

**Files:**
- Modify: `ccf-pipeline-figure/assets/STYLE-FOR-IMAGE-MODELS.md`

**Interfaces:**
- Consumes: a scientifically grounded `TECHNICAL_FIGURE_BRIEF.md`.
- Produces: a positive, operational image prompt with vivid color, varied iconography, readable labels, and decoration that cannot be mistaken for topology.

- [x] **Step 1:** Replace low-saturation/single-accent defaults with a coordinated, high-energy editorial-comic palette and explicit icon-diversity requirements.
- [x] **Step 2:** Permit decorative titles, short method-only explanatory lines, cel shading, shallow offset shadows, and restrained panel gradients.
- [x] **Step 3:** Preserve bans on experimental results, photorealism, heavy 3-D, ambiguous decorative arrows, and unreadable text.

### Task 3: Validate native Codex discovery and repository state

**Files:**
- Create locally, outside Git: `$HOME/.agents/skills/ccf-pipeline-figure` symlink to the repository skill folder.

**Interfaces:**
- Consumes: the updated skill directory.
- Produces: native `$ccf-pipeline-figure` discovery in Codex and a validated Git commit.

- [x] **Step 1:** Run the official skill quick validator.
- [x] **Step 2:** Run targeted text checks for the built-in-only boundary, immutable versioning, and finite iteration cap.
- [x] **Step 3:** Create the user-scope skill symlink without touching the official system `$imagegen` skill.
- [ ] **Step 4:** Review the diff, commit on `feature/one-command-imagegen-pipeline`, and push that branch once a GitHub remote is available.
