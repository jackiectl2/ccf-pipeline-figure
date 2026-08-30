# Sixteen observed workflows for producing a conceptual paper figure with an agent

> ⭐ **Evidence, not a tool list.** Every workflow below was extracted from a note this
> project opened in full with `get_feed_detail`, or from a repository fetched directly.
> Every step and every claim carries a quote. Nothing here is a summary of a title.
>
> **How this was collected.** 41 keyword searches across six facets
> (tool / agent / output format / production stage / venue / colloquial term).
> 29 returned results, **10 returned nothing at all**, and
> 2 still failed after three attempts. Together they surfaced
> 436 distinct notes, of which **93 were opened and read
> in full**; the rest were requested and refused by the server, and their ids are kept.
> Read-only throughout — `search_feeds` and `get_feed_detail` only; nothing liked,
> saved, commented or published.
>
> **Regenerate**: `python3 literature/figure-refs/stage_b.py`. Raw records:
> `literature/figure-refs/WORKFLOWS.json`, `DETAILS.json`, `SEARCH_LOG.json`.
>
> **Chinese version**: `production-workflows.zh.md`. Both are rendered from the same
> records by the same script, so they cannot drift apart.

⛔ **This is a purposive sample, not a survey of the field.** The keyword list was
chosen to find agent-driven figure production, one platform dominates it, and popular
notes are over-represented by construction. **Everything below describes workflows
observed in this collection.** A device appearing three times here is evidence that it
recurs, not evidence of how common it is among people writing papers. An earlier draft
of this file said "the field has converged"; it had not established that.

⭐ **The searches that returned NOTHING are a finding, not a gap.** `tikz 论文画图`, `computer use 自动 画图`, `claude 画流程图`, `svg 论文配图`, `vsdx 论文`, `论文配图 配色`, `cvpr 主图`, `顶会 插图`, `机制图 论文`, `pipeline 图 论文` each returned zero notes. The platform's vocabulary is organised around **tools and agents**, not around file formats or venues: `drawio` and `论文配图` are dense, while `tikz`, `vsdx`, `svg 论文配图`, `cvpr 主图` and `pipeline 图` are empty. ⚠ **[INFERRED]** That bounds what this collection could ever have contained — a TikZ or Visio practice discussed under other words would not appear here, and W19's TikZ workflow reached this file through GitHub rather than through any of these searches.

⚠ **This file records what was observed. It is not a set of instructions for this
skill.** Which of these apply here, which do not, and why, is SKILL.md §9.

⚠ **These records were rewritten after a cross-model audit failed 22 of the first 23.**
Almost every failure was the same defect: a step or a benefit stated in the record that
the quoted evidence did not support, usually because a fact from the tool's README had
been folded into a record whose evidence was a social-media note. Repository quotes are
now separated and labelled, near-duplicate records were merged, and three records were
moved out of scope. **The direction of the original errors was uniform: they all made
the workflows sound stronger and better verified than the sources say.**

## The 16 workflows at a glance

**V** — is the FINAL artefact vector? ✅ yes · ◐ mixed, raster elements inside ·
? claimed but never checked by the source · ⛔ no.  **E** — can it still be edited as
objects?

| | workflow | ♥ | ends as | V | E |
|---|---|---:|---|:-:|:-:|
| W01 | Model drafts a reference, a converter turns it into .drawio, the human keeps the file | 201 | `drawio` | ◐ | ✅ |
| W02 | Method text compiled to SVG by segmenting a generated raster | 1654 | `svg` | ◐ | ✅ |
| W03 | S-C-S-S: the model writes a four-slot drawing prompt, a human redraws the draft | 4373 | `pptx` | ◐ | ✅ |
| W04 | Write the drawing spec before drawing; emit .drawio; screenshot and iterate | 1726 | `drawio` | ✅ | ✅ |
| W06 | Plan in text, render to pixels, then correct without redrawing | 5959 | `raster` | ⛔ | ⛔ |
| W08 | Reference raster rebuilt as native Visio shapes, with an anti-embed check | 1107 | `vsdx` | ✅ | ✅ |
| W09 | Raster to PPTX by skill, then ungroup repeatedly | 1190 | `pptx` | ◐ | ✅ |
| W10 | Ask the image model to re-emit as SVG, one sub-module at a time | 3363 | `pptx` | ? | ✅ |
| W11 | Semantic cut-out into an editable slide, with the fidelity trade-off as a switch | 8 | `pptx` | ◐ | ✅ |
| W13 | A published figure as the template; replace only the words | 688 | `drawio` | — | ? |
| W15 | Format laundering: SVG -> Inkscape -> EMF -> Visio ungroup | 36 | `vsdx` | ? | ✅ |
| W16 | Text to Mermaid to a vector editor | 3265 | `drawio|svg` | ✅ | ✅ |
| W19 | Natural language to TikZ, compiled and self-checked | — | `tikz` | ✅ | ✅ |
| W22 | Emit the native file format of a real editor (Excalidraw JSON) | 1610 | `excalidraw` | — | ✅ |
| W24 | Install the drawing skill into whichever agent you already use | 334 | `image (unspecified)` | — | — |
| W26 | No skill at all: ask the chat model to write the .drawio file, then screenshot-correct it | 93 | `drawio` | — | ✅ |

**[MEASURED] over these 16 workflows.** The final artefact is fully vector in **4**, mixed in 5, claimed-but-never-checked in 2, never claimed either way in 4, and raster in 1. **13** leave something the author can still edit as objects.

⚠ **That row of numbers is the finding.** Only a minority of these routes end in a figure anyone has established is vector, and several of the most-liked ones simply never ask. **In this collection** `.pptx` and `.svg` are written about as though the extension guaranteed vector content; in these sixteen records it does not.

**[MEASURED]** No author claims a generated raster is the figure they submitted. ⚠ But the weaker version is what the evidence supports: W01 and W03 explicitly call the raster a reference or a blueprint, while W06 and W24 simply present it and say nothing about its status. **Read as 'nobody claims it is final', not as 'everybody calls it a draft'.**

**[MEASURED]** Four distinct mechanisms are used to reach something editable, not one: **emit the native file format of an existing editor** (W04, W16, W22, W26; W13 aims at this but never establishes that it arrives); **emit editable source that compiles** (W19, into LaTeX); **rebuild a raster into an editor's object model** (W02, W08, W09, W11); and **redraw by hand from a generated blueprint** (W03, and the assembly half of W01). W15 is a fifth, degenerate case: convert between interchange formats until the editor accepts the file. **Nothing in this collection invents an editor.**

**[INFERRED]** The pattern *plan first, render into an object model, look at the render, edit* is stated in full by **three** records — W04, W19 and W26 — and W04 is the only one that says why it works ('to stop the model guessing while it draws'). W06 plans and inspects but never reaches an object model. ⚠ **This is a pattern a few authors converge on, not a convention of the field**; an earlier draft of this file over-read it, and the plan is not always in text — W26's plan is a conversation and a draft picture.

**[MEASURED]** Explicit checks against a named failure mode appear in W03, W04, W06, W08, W11, W19 and W26 — seven of the sixteen. But **exactly one of those checks is automated and structural**: W08 scans the output package for a whole embedded PNG, so a pasted image cannot pass as a rebuild. Two others automate something weaker — W11 renders the export and checks it for misalignment, ghosting and overflow, and W19 has the model self-check the compiled image — and the remaining four are things a human looks for in a render. ⚠ This does not prove the other routes would miss an embedded raster; only that **none of them documents a check that would catch it**.

---

## The records

### W01 · Model drafts a reference, a converter turns it into .drawio, the human keeps the file

**Source** — GTP 半自动化流程出科研绘图. note `n2202d937` · 201 likes.

**Starts from** — A written paper, and a rejection of one-shot generation.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Have GPT produce a reference image — explicitly a 'roughly like this' picture | GPT | raster reference |
| 2 | Convert the reference into an editable .drawio with a third party's draw.io skill; frame, palette and text survive | a draw.io skill | .drawio |
| 3 | Regenerate the icons separately, because they do NOT survive the conversion, and insert them | GPT + manual | PNG icons |
| 4 | Adjust spacing, font, arrows, alignment, icon size and hierarchy by hand | draw.io | final .drawio |

**Ends as** — `drawio` · vector ◐ · still editable ✅

**Buys you** — Quoted: the author rejects one-shot generation for three named reasons — re-prompting breaks what was already right, fine control is hard, and the result does not survive journal revision.

**Costs** — Quoted: the icons are regenerated separately as PNGs and inserted by hand, so the finished `.drawio` carries raster elements; the assembly stage is manual throughout.

<details><summary>Evidence — the note's own words</summary>

> 直接让 GPT “一键生图”其实并不是最理想的方式
>
> 后续修改不够方便。尤其是反复让 AI 改图时，经常会出现“改对了一个地方，又把原本正确的细节改坏了”的情况
>
> 很难精确控制细节。 比如排版、箭头、节点位置、间距这些地方，往往需要反复调整
>
> 不适合后续投稿编辑返修。直接生成的图片分辨率、编辑性都有限制
>
> Step 1｜先让 GPT 帮我搭框架 …先生成一张“大概长这样”的参考图
>
> Step 2｜把参考图转成可编辑的 draw.io …这一步基本可以还原原图的框架、配色和文字
>
> 计算机领域论文的框架图里经常会用到一些小图标，但转成 draw.io 后这些元素不能被一起还原，所以我一般会再让 GPT 单独生成一套 PNG 图标，然后手动插进去
>
> Step 4｜最后自己组装和抠细节 调整间距、字体、箭头、对齐、图标大小、视觉层级
>
> AI负责提高效率，我自己保留最终控制权
>
</details>


### W02 · Method text compiled to SVG by segmenting a generated raster

**Source** — 完全可编辑！论文画图有救了[ICLR2026]. note `n28023443` · 1654 likes · github.com/ResearAI/AutoFigure-Edit (ICLR 2026, MIT).

**Starts from** — The paper's method section as text; optionally a reference figure for style transfer.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Method text -> a raster draft | an LLM image model | figure.png |
| 2 | Segment the draft into icons and text regions | SAM3 | masks + coordinates |
| 3 | Remove backgrounds and build a placeholder template | RMBG-2.0 | transparent icons/*.png + template.svg |
| 4 | Reassemble template plus icons into one file, editable in a bundled browser canvas | SVG-Edit | final.svg |

**Ends as** — `svg` · vector ◐ · still editable ✅

**Buys you** — Quoted: it goes from method TEXT to an editable file, and it takes style from a named reference figure. ⚠ Not unique in either respect **within this collection** — W04 also separates a style reference from a content source, and W13 also uses a published figure as a template. What no other record here does is both, from text alone, with no human drawing step.

**Costs** — ⚠ **Not wholly vector, despite the note's claim.** The repo's own pipeline reassembles `icons/*.png` into `final.svg`, so the icons are raster inside an SVG wrapper. Repo also states CUDA 12.6 / PyTorch 2.7 for SAM3, ~20 minutes and ~$0.50 per run, 4K or the output blurs, and that Gemini's ToS blocks mainland-China users.

<details><summary>Evidence — the note's own words</summary>

> 直接把论文的 method section → 生成「可编辑 SVG」科研插图
>
> 不是 PNG，是可编辑 SVG！图里的 文字 / 框 / 箭头 / 布局 全是矢量
>
> 支持风格迁移（Style Transfer）·给一张参考论文图·生成结果直接“长得像那篇顶会论文”
>
> SAM3 自动分割图元·自动识别 icon / 模块 / 箭头
>
> 内置 SVG 编辑器·浏览器里直接拖、改、调
>
</details>

<details><summary>Evidence — the repository's own README (a different source from the note above)</summary>

> SAM3 detects and segments distinct icons and text regions
>
> RMBG-2.0 for background removal
>
> Output: Transparent icons/*.png, template.svg
>
> Every component is editable—text, shapes, and layout can be modified losslessly
>
> SAM3 requires Python 3.12+, PyTorch 2.7+, and CUDA 12.6
>
> 4K option for optimal performance...using 1K or 2K resolutions will result in...unusually blurry
>
> Stage 1: Image Generation — Model: LLM (Gemini, GPT-Image-2, or Claude via OpenRouter); Output: figure.png; Cost: ~$0.50 per run
>
> Stage 4: Assembly — Input: Template SVG + transparent icons; Tool: LLM-based optimization (optional, 0+ iterations); Output: final.svg
>
> Runtime: approximately 20 minutes per run
>
> Geographical restriction: Gemini's Terms of Service do not permit access...by users in mainland China
>
</details>

### W03 · S-C-S-S: the model writes a four-slot drawing prompt, a human redraws the draft

**Source** — ChatGPT+Gemini+PPT 科研复杂模型绘图方法 · and independently 「Codex生成可编辑svg格式的图」(205♥). note `n1102ca6b` · 4373 likes.

**Starts from** — Whatever exists: code, the paper, the abstract, or the project folder.

| # | step | tool | produces |
|---|---|---|---|
| 1 | A model summarises the core workflow and technical route from the raw material | ChatGPT / Codex | prose summary |
| 2 | Restructure it into a drawing prompt with four named slots: Subject, Composition, Structure, Style | ChatGPT / Codex | S-C-S-S prompt |
| 3 | An image model renders a first draft, regenerated a few times if unattractive | Gemini | raster draft |
| 4 | Redraw in PowerPoint with native shapes; separately generated transparent icons; Illustrator only for irregular anchors | PowerPoint / Illustrator | figure |
| 5 | Keep correcting against the paper while redrawing: missing modules, wrong arrows, hierarchy, misread logic | manual | final |

**Ends as** — `pptx` · vector ◐ · still editable ✅

**Buys you** — Quoted: the draft is declared unsuitable as the paper's final version and is used as a blueprint for redrawing. **Two independent authors describe the same four-slot framework**, which makes it an independently recurring device rather than one person's habit. It is not thereby a convention of the field; two is two.

**Costs** — Quoted: the redraw is manual, across up to three tools. Icons enter as separately generated images, so the result is not wholly vector.

<details><summary>Evidence — the note's own words</summary>

> S – Subject（主体）：图中要呈现的核心对象
>
> C – Composition（构图）：整体布局、信息块之间的关系
>
> S – Structure（结构细节）：每个模块的内部元素、箭头走向
>
> S – Style（风格渲染）：配色、图形风格、边框、质感等
>
> 不管是代码、文章还是摘要，我会先把所有相关材料丢给 ChatGPT，让它总结出研究的核心流程和技术路线
>
> AI 会根据 prompt 输出结构完整但风格多变的“初稿图”
>
> 可以看出图片风格还是挺美观的（如果不好看可以多生成几次）
>
> 这张图通常不适合作为论文最终版本，但非常适合作为 PPT / Illustrator 重绘的“蓝本”
>
> 绝大部分图形可用 PPT 形状绘制完成（如矩形、圆角框、流程箭头）
>
> 少部分复杂图标可用 ChatGPT / Gemini 单独生成透明背景小图
>
> 极少数不规则结构用 Illustrator 调整锚点精修
>
> 在重绘阶段，我会随时根据论文内容修正：模块是否缺失，箭头是否传达正确
>
> 【第二位作者，205♥】我会让它按这个结构重组内容：S – Subject（主体）… C – Composition（构图）… S – Structure（结构细节）… S – Style（风格渲染）
>
> 【第二位作者】先用 AI 把整体框架和视觉草稿跑出来，后面再到 PPT 或 AI里重新绘制、描图和微调
>
</details>


### W04 · Write the drawing spec before drawing; emit .drawio; screenshot and iterate

**Source** — 自写drawioskill，9分钟复刻计算机顶会插图. note `n080331c1` · 1726 likes · github.com/Will-hxw/drawio-diagram-builder-skill; the same shape is implemented independently by github.com/M1n-n9/academic-figures-drawer (surfaced by a separate 940♥ note) and by github.com/Agents365-ai/drawio-skill (135♥ note).

**Starts from** — The paper or project context, plus a reference figure — kept apart on purpose.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Separate the inputs: which is the CONTENT source, which is the STRUCTURE source, which is only a VISUAL STYLE reference | the skill | classified inputs |
| 2 | Fix the constraints BEFORE drawing: canvas size, module regions, font, palette, arrow direction, icon meaning, connection semantics | the skill | a drawing spec |
| 3 | Emit editable .drawio XML directly, rather than embedding the reference image | the skill | .drawio |
| 4 | Load it in a local preview, screenshot, and compare against the reference and the spec | browser preview | screenshot |
| 5 | Fix the XML from what the screenshot exposed, then re-preview | the skill | revised .drawio |

**Ends as** — `drawio` · vector ✅ · still editable ✅

**Buys you** — Quoted, and the reason for the whole design: 'to stop the model guessing while it draws'. Its named screenshot checks are text overflow, arrow direction and connection, missing or misplaced icons, alignment of highlight and background blocks, module hierarchy and reading order, and whether the .drawio still opens. A second implementation adds the rule to check readability at the paper's two-column size.

**Costs** — Quoted, by its own author: a first-draft generator whose output should not go into a paper or a defence unchecked.

<details><summary>Evidence — the note's own words</summary>

> 这次的重点不是让 AI 直接生成一张静态图片，而是让 Agent 生成可二次编辑的 drawio 源文件
>
> 先理解输入 把论文内容、项目上下文、参考图、风格要求拆开处理，区分哪些是内容来源，哪些是结构来源，哪些只是视觉风格参考
>
> 在真正画图前，先明确画布大小、模块区域、字体、配色、箭头方向、图标含义、连接语义等约束，避免模型边画边猜
>
> 最终产物以 .drawio 为主，而不是把参考图嵌进去糊弄
>
> 通过本地预览页面加载 drawio 文件，截图后对照参考图和设计规格
>
> 每一轮都会根据截图暴露出来的问题继续修改 XML，再重新预览、截图、比对
>
> ✅ 文字是否超出文本框 ✅ 箭头方向和连接关系是否正确 ✅ 图标是否缺失或错位 ✅ 高亮块、背景块是否对齐 ✅ 模块层级和阅读顺序是否清楚 ✅ drawio 文件本身是否还能正常打开和继续编辑
>
> 这个流程目前更适合作为科研绘图初稿生成器，它生成的结果不建议不检查就直接放进论文或答辩里
>
> 【第二实现，940♥】字体、线宽、圆角、箭头和间距必须保持一致，并且要在论文双栏尺寸下检查可读性，避免文字过小、模块失衡和信息冗余
>
> 【第二实现，940♥】已有组件与论文贡献要有明确区分，可使用低饱和度配色表达不同语义，再用一种克制的强调色突出原创模块
>
> 【第三实现，135♥】AI 会直接帮你改图，而不是重新画一遍
>
</details>


### W06 · Plan in text, render to pixels, then correct without redrawing

**Source** — Gemini科研图一键三步走 · with the constrained-edit instruction from 「被两万多人看过AI绘图prompt分享」(3839♥) and the project-folder input from 「gpt-image-2+codex半自动科研绘图」(604♥). note in `DETAILS.json` · 5959 likes.

**Starts from** — The abstract or key points; or, in the 604♥ variant, the project folder itself.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Ask the language model for a TEXT sketch — an element list with positions and arrow relations — not an image | Gemini 3 / Codex | textual layout plan |
| 2 | Feed that plan to the image model with a named genre and a colour cap | NanoBanana / gpt-image-2 | raster figure |
| 3 | Correct by constrained edit, never regeneration: change only the named part and keep the rest unchanged; or let it change only colour and font without redrawing the subject | same model | corrected raster |
| 4 | Check by hand what the model gets wrong: arrow direction, abbreviation case, scale bars, units, and whether the science is right | manual | final raster |

**Ends as** — `raster` · vector ⛔ · still editable ⛔

**Buys you** — Quoted: the plan is separated from the render, and correction is constrained so the model may not redraw the subject. The 604♥ author states where the time actually goes: not the drawing, but turning your own paper into something a model can draw correctly. **[INFERRED]** that the constrained edit answers W01's complaint about re-prompting breaking what was already right — that connection is mine, not either author's.

**Costs** — The deliverable is a raster and nothing downstream can edit it. ⚠ Unlike W01 and W03, **neither author here calls the output a draft** — they present it as the figure. The prompt caps the palette at 3-4 colours.

<details><summary>Evidence — the note's own words</summary>

> Step1：丢论文摘要/要点给Gemini，要求输出“元素清单+位置+箭头关系”的简化草图文字版
>
> Step2：把草图文字喂给NanoBanana，指定“期刊机制图/综述封面风，统一配色，带清晰注释”
>
> 让模型只改配色/字体，不重画主体
>
> 人工检查：箭头方向、缩写大小写、比例尺、单位
>
> 颜色控制在3-4个主色内，避免过度渐变
>
> 【3839♥】最好的纠错方式是直接追问：“Please change [错误部分] to [正确描述], keep the rest unchanged.”
>
> 【3839♥】把你的长文本/实验设计丢给 AI (Gemini / DeepSeek)，让它先总结成简短的英文描述
>
> 【604♥】先让 Codex 直接读取我的项目文件夹，先理解这篇工作到底在讲什么、主线是什么、哪些模块该放进图里
>
> 【604♥】最耗时间的不是最后点生成，也不是最后微调，而是你得先把自己的论文内容整理成一种“AI 能理解、而且能画对”的表达
>
> 【604♥】重点检查科学逻辑、模块关系和文字表达，避免图看起来对，但内容不够严谨
>
</details>


### W08 · Reference raster rebuilt as native Visio shapes, with an anti-embed check

**Source** — 科研绘图Skill来了，参考图秒变Visio编辑图. note in `DETAILS.json` · 1107 likes · visio-image-rebuilder; a second implementation is github.com/pengjunchi0/codex-visio-paper-figure-skill.

**Starts from** — A PNG screenshot of a figure — a model diagram, a flow chart, or a multi-panel scientific figure.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Decompose the reference structurally first: page proportion, panel layout, data-flow arrows, dashed feedback, repeated elements — big panels before small details | the skill | structure |
| 2 | For multi-panel figures, emit a Panel A/B/C list as a drawing contract before drawing | the skill | panel contract |
| 3 | Rebuild as native Visio rectangles, arrows, connectors and groups, with all text editable | Visio COM + PowerShell scaffold | .vsdx |
| 4 | ⭐ Run a packaging check that scans the .vsdx for a whole embedded PNG, so a pasted image cannot masquerade as a rebuild | the skill | pass/fail |
| 5 | Back up before editing, export a PNG preview afterwards, and reconcile the shape count | the skill | backup + preview |

**Ends as** — `vsdx` · vector ✅ · still editable ✅

**Buys you** — ⭐ **The only automated STRUCTURAL check in the collection.** Several records describe checks a human performs on the render; this one inspects the output file itself — it scans the `.vsdx` package for a whole embedded PNG, so a pasted image cannot pass as a rebuild, and reconciles the shape count to confirm something was really built.

**Costs** — Quoted from the second implementation's own README: Windows, Microsoft Visio, PowerShell, and PowerPoint for the PPTX export. Unavailable on macOS.

<details><summary>Evidence — the note's own words</summary>

> 把论文模型图、流程图、多面板科学图还原成Visio原生矩形、箭头、连接线和分组，文字全部可编辑
>
> 反“整图嵌入”红线：内置检查工具，扫描.vsdx包结构里有没有偷懒贴的整张PNG，杜绝AI用贴图冒充还原
>
> 参考图结构化拆解：自动梳理页面比例、面板布局、数据流箭头、虚线反馈和重复元素，先画大面板再抠小细节
>
> 对多面板模型图先产出Panel A/B/C清单作为绘图契约
>
> 顶刊风格默认值：Times New Roman字体、0.9-1.2pt主边框、低饱和模块配色、统一箭头样式
>
> COM自动化绘图脚手架：内置PowerShell脚手架脚本
>
> 备份+预览+包检查：改图前自动备份原文件，改完导出PNG预览、核对shape数量
>
</details>

<details><summary>Evidence — the repository's own README (a different source from the note above)</summary>

> Native Shape Reconstruction: 矩形、圆形、线条、箭头、连接线
>
> Windows。Microsoft Visio。PowerShell。Microsoft PowerPoint，用于 PPTX 导出
>
> Not ideal for charts with real data; 最好使用脚本或让 Agent 提取数据后用脚本绘图
>
</details>

### W09 · Raster to PPTX by skill, then ungroup repeatedly

**Source** — 不擅长画图？AI生图不能改？直接转可编辑PPTX. note in `DETAILS.json` · 1190 likes · github.com/Lancelot-Xie/img2pptx.

**Starts from** — One raster. If you have none: summarise the project to markdown with Codex or Claude Code, then have GPT draw from that.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Get a raster — GPT Image-2 draws something beautiful, blurry and uneditable | GPT Image-2 | figure.png |
| 2 | Hand it to Codex with the img2pptx skill | Codex + img2pptx | .pptx |
| 3 | Open in PowerPoint, right-click, ungroup or convert to shapes | PowerPoint | shapes |
| 4 | ⚠ Ungroup REPEATEDLY — the reconstruction nests vector groups layer upon layer | PowerPoint | leaf shapes |
| 5 | Send further edits back through Codex, which still holds the vector elements | Codex | revised pptx |

**Ends as** — `pptx` · vector ◐ · still editable ✅

**Buys you** — Quoted: a direct answer to 'the AI figure is pretty but I cannot change it' — the note's own framing. It recovers an object model from pixels.

**Costs** — Quoted: the repeated-ungroup step, which the author flags three times over. The repo adds that fidelity depends on the PowerPoint version, OS, fonts and SVG importer, and that local raster crops are used where an element cannot be reliably vectorised — so the output is not guaranteed wholly vector.

<details><summary>Evidence — the note's own words</summary>

> 首先，需要有一张原始参考图，可以是AI生成的，比如让GPT Image2为你设计一下图，画出一个美观但是模糊且不能编辑的图
>
> 丢给codex，让他用刚才安装的这个img2pptx skill将其转换为PPTX
>
> 最后只需要用powerpoint打开文件，右键选择取消组合或者全部转换为形状，就能得到完全可编辑的论文图
>
> 想要编辑底层就必须选中区域多次取消组合❗️❗️❗️
>
> 因为重构逻辑里面是矢量元素一层层组合得到的
>
> 所有矢量图形都有保存，Codex可以单独进行修改和优化
>
> 可以先用Codex或Claude Code总结项目/论文得到一个markdown文件，然后丢给GPT，选择创建图片
>
</details>

<details><summary>Evidence — the repository's own README (a different source from the note above)</summary>

> SVG 中不包含嵌入式 <image> 元素
>
> Fidelity dependent on PowerPoint version, OS, fonts, and SVG importer
>
> Local raster crops used only when elements cannot be reliably vectorized
>
</details>

### W10 · Ask the image model to re-emit as SVG, one sub-module at a time

**Source** — 如何用GPT Image2生成复杂图片放入PPT编辑. note in `DETAILS.json` · 3363 likes.

**Starts from** — An existing raster figure, or the architecture code.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Generate the image first; do NOT ask for SVG in one shot | GPT Image-2 | raster |
| 2 | Then instruct: output the image in vector SVG format | GPT Image-2 | svg |
| 3 | If the vector quality is poor, cut the figure into sub-module boxes, upload them, and ask for each separately — about three at a time before it breaks | GPT Image-2 | per-module svg |
| 4 | Drag the SVG into PowerPoint, size it, right-click convert to shape | PowerPoint | shapes |
| 5 | ⚠ Shrink every text box's font BEFORE editing | PowerPoint | final |

**Ends as** — `pptx` · vector ? · still editable ✅

**Buys you** — Quoted: the divide-and-conquer discovery is the transferable part — whole-figure SVG generation fails where per-module generation succeeds, with a practical batch limit of about three. The note names no skill or repository, though absence of mention is not evidence that none is needed.

**Costs** — Quoted: 'dozens of experiments' to find the recipe. ⚠ Asking a model to 'output SVG' does not establish that the result contains native vector primitives rather than a traced or embedded raster; the note does not check.

<details><summary>Evidence — the note's own words</summary>

> 想要一次性生成SVG格式有点难度。可以先生成image，再prompt(写指令)让模型生成SVG格式
>
> 指令：以矢量图形 SVG 格式输出图像
>
> 如果遇到模型生成的矢量图质量不好，可以尝试将想要生成的image分成一个一个的子模块，分批次生成
>
> 一般同时生成三个图像分块没有问题，太多了会崩
>
> 得到svg之后，将svg拖入ppt，可以先调整图片大小，右键点convert->shape (转换形状)
>
> 这里建议在编辑图片之前先选中所有可编辑框把字体拉小
>
> 根据反复几十次的实验
>
</details>


### W11 · Semantic cut-out into an editable slide, with the fidelity trade-off as a switch

**Source** — 一键把流程图变成可编辑PPT了！完全开源 · with the exemption prompt from 「gpt出图然后codex 转成可编辑ppt」(412♥). note in `DETAILS.json` · 8 likes · github.com/G820G/figure-to-ppt.

**Starts from** — One image of a finished flow, framework, mechanism or architecture figure.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Recognise the text and rebuild it as editable text boxes | the skill | text boxes |
| 2 | Cut out complex elements by smallest SEMANTIC object rather than by rectangle crop, so neighbours do not stick together | the skill | per-object cut-outs |
| 3 | Optionally nativise arrows: reliable curves and polylines become editable connectors, complex ones stay as transparent images | the skill | connectors |
| 4 | Forbid the failure mode explicitly in the prompt — do not paste the image as a full-page background — and exempt what must not be redrawn: formulae, simulation plots, system photographs | prompt | constraints |
| 5 | Render the export and check it automatically for misalignment, ghosting and overflow | the skill | checked pptx |

**Ends as** — `pptx` · vector ◐ · still editable ✅

**Buys you** — ⭐ Quoted: it exposes the fidelity-versus-editability trade-off as a SWITCH the user sets, rather than hiding it. And the 412♥ prompt states what must NOT be vectorised, which is the half most recipes omit.

**Costs** — Quoted: arrow nativisation is explicitly lossy, and complex elements stay raster — so the deliverable is mixed by design, not vector.

<details><summary>Evidence — the note's own words</summary>

> 文字自动识别并重建为可编辑文本框
>
> 细胞、颗粒、图标等复杂元素按最小语义对象独立抠图
>
> 不再简单使用矩形裁剪，避免把相邻图形粘在一起
>
> 可将可靠识别的曲线、折线和箭头转换为可编辑 PPT 连接线
>
> 复杂箭头仍保留为独立透明图片，优先保证视觉效果
>
> 关闭：视觉还原度更高 开启：箭头更容易编辑，但可能有轻微视觉差异
>
> 导出后自动渲染检查，减少错位、重影和越界问题
>
> 【412♥】不要把图片直接作为整页背景粘贴
>
> 【412♥】图片中的文字必须识别并转为可编辑文本框，不能做成图片
>
> 【412♥】保证公式、仿真图、系统图不强行用原生形状重画
>
</details>


### W13 · A published figure as the template; replace only the words

**Source** — GPT结合Draw.io绘制流程图. note in `DETAILS.json` · 688 likes.

**Starts from** — A reference paper figure you like, plus your own content.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Upload the reference and instruct the model to treat it as a template, preserving layout, hierarchy, grouping, arrow relations, title and annotation positions | GPT | constraint |
| 2 | Have it extract keywords, module titles, mechanism elements, method steps and result phrases from your content and substitute them for the original text | GPT | substitution |
| 3 | Constrain the edit: text only, structure unchanged, only minimal box-size changes to fit the new text | prompt | constraint |
| 4 | Emit complete draw.io XML and paste it into draw.io | GPT -> draw.io | .drawio |

**Ends as** — `drawio` · vector — · still editable ?

**Buys you** — Quoted: structure and content are separated as far as they can be — the structure is a fixed input and only the words vary. The substituted text is required to come from the paper or its minimal compression.

**Costs** — ⚠ The prompt demands XML that opens in draw.io; **opening is not the same as being made of editable primitives**, and draw.io XML can carry an embedded image. Unlike W08 there is no check, so neither the vector nor the object-editable property is established. ⚠ [INFERRED] It also inherits a published figure's layout wholesale — fine as scaffolding, a provenance question if shipped unchanged. The note itself does not raise this.

<details><summary>Evidence — the note's own words</summary>

> 请将我上传的参考论文插图作为模板，在高还原其布局、层级、分组、箭头关系、标题与注释位置的前提下
>
> 根据我提供的[内容]自动提取关键词、模块标题、机制要素、方法步骤和结果短语，对图中原有文字进行对应替换
>
> 仅替换文字内容，尽量不改结构；所有替换文字必须来自论文内容或其最小压缩表达
>
> 仅允许为适应文字长度做最小幅度的框大小与排版调整
>
> 最终只输出可直接保存并在 draw.io 打开的完整 XML
>
</details>


### W15 · Format laundering: SVG -> Inkscape -> EMF -> Visio ungroup

**Source** — ChaGPT+Gemini+Visio画图一键三步走. note in `DETAILS.json` · 36 likes.

**Starts from** — An SVG the target editor refuses to open.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Ask the image model for the figure in a named venue style, explicitly requesting clean vector graphics, white background and editable SVG | Gemini | svg |
| 2 | Try dragging the SVG straight into Visio; if it will not open, continue | Visio | maybe done |
| 3 | Open the SVG in Inkscape and Save As -> Enhanced Metafile (EMF) | Inkscape | .emf |
| 4 | Import the EMF into Visio and right-click ungroup | Visio | editable shapes |

**Ends as** — `vsdx` · vector ? · still editable ✅

**Buys you** — Quoted: a pure format-compatibility recipe for when the editor you have will not accept the vector format you have. The EMF hop is the whole trick.

**Costs** — Inkscape and Visio are both required and neither is installed on this machine.

<details><summary>Evidence — the note's own words</summary>

> Generate a scientific figure in CVPR/ICCV paper style, clean vector graphics, white background, clear arrows, professional color scheme, editable SVG format
>
> 让Gemini输出SVG代码，下载SVG格式文件。（此时可以尝试直接拖入Visio编辑，如果打不开继续下一步）
>
> 下载Inkscape，打开SVG文件。然后：文件 → 另存为 → Enhanced Metafile（EMF）格式
>
> 将EMF文件导入Visio，右键取消组合
>
> 即可对所有模块：✅ 修改文字 ✅ 调整颜色 ✅ 改变箭头 ✅ 编辑结构
>
</details>


### W16 · Text to Mermaid to a vector editor

**Source** — 🧠流程图神器｜一键生成 + 可编辑！ · with the clinical recipe from 「用 Mermaid 自动生成科研流程图」(86♥) and the theming skills from 「让 Mermaid 一键变好看的方法」(26♥). note in `DETAILS.json` · 3265 likes.

**Starts from** — The process written out in words.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Ask a language model for Mermaid code for the described flow, marking counts where they belong | DeepSeek / Kimi / any LLM | mermaid source |
| 2 | Optionally have the model emit already-themed Mermaid rather than the default style | Pretty-mermaid-skills | themed mermaid |
| 3 | Either render at mermaid.live and export SVG, or paste into draw.io via Insert -> Mermaid | mermaid.live / draw.io | svg or .drawio |
| 4 | Edit the shapes in draw.io | draw.io | final |

**Ends as** — `drawio|svg` · vector ✅ · still editable ✅

**Buys you** — Quoted: one author's stated reason for preferring it over draw.io is version control and automatic generation, which is a real argument against hand-dragging. The route needs no skill and no repository beyond a chat model and an editor. **[INFERRED]** that this makes it the cheapest path here; no source compares costs.

**Costs** — Quoted from the same author: draw.io 'is very strong, dragging is comfortable', so the trade is expressiveness for automatability. ⚠ [INFERRED] Mermaid's vocabulary is flow charts; this collection contains no example of a Mermaid figure carrying regions, tints, icons or verbatim content blocks.

<details><summary>Evidence — the note's own words</summary>

> 直接让 DeepSeek 生成 Mermaid 流程图代码
>
> 打开 draw.io → 创建画布 → 调整图形 → 插入 → Mermaid → 粘贴代码 → 插入
>
> 【86♥】请根据以下纳入与排除标准生成一个 Mermaid 格式的流程图，展示患者筛选过程，并在每一步标注 n=?
>
> 【86♥】点击左上角 “Export” → 选择 “SVG” 下载图像
>
> 【26♥】把 Mermaid 美化这一步，直接交给 AI…它吐出来的就是已经美化好的 Mermaid 代码，不是那种裸奔的默认样式
>
> 【26♥】draw.io 也可以，很强，拖拽很爽，但不适合版本管理，也没法自动生成
>
</details>


### W19 · Natural language to TikZ, compiled and self-checked

**Source** — chingswy/Skill-Research-Figure (prior art, GitHub, 154 stars). github.com/chingswy/Skill-Research-Figure.

**Starts from** — A natural-language description of the method.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Understand the method, then confirm the structure with the user over one or two rounds before drawing | Claude | agreed structure |
| 2 | Generate a standalone .tex | Claude | figure.tex |
| 3 | Compile and self-check the resulting image | pdflatex + a rasteriser | PDF/PNG |
| 4 | Show it and iterate | Claude | final .tex |

**Ends as** — `tikz` · vector ✅ · still editable ✅

**Buys you** — The source lives in the paper's own toolchain. ⚠ [INFERRED] that this makes fonts and sizes match the document; the repo does not claim it.

**Costs** — Repo: needs a TeX distribution — `需要安装 pdflatex`. **[INFERRED]** that every adjustment costs a recompile, since the repo describes no visual editor; it does not say so.

<details><summary>Evidence — the repository's own README (a different source from the note above)</summary>

> 理解方法 → 确认结构(1-2轮) → 生成TikZ → 编译验证 → 展示迭代
>
> 生成完整可编译的 standalone .tex 文件
>
> 需要安装 pdflatex
>
> rsvg-convert 转 PNG，AI 自检布局和箭头
>
</details>

### W22 · Emit the native file format of a real editor (Excalidraw JSON)

**Source** — 博士生codex用科研绘图skills（4）. note in `DETAILS.json` · 1610 likes · Excalidraw-Diagram-Generator, under GitHub's own awesome-copilot.

**Starts from** — A description of the diagram, given to Codex with the skill installed.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Generate the diagram directly in the editor's native JSON | Excalidraw-Diagram-Generator | .excalidraw JSON |
| 2 | Drag the file onto excalidraw.com and edit it there | excalidraw.com | editable diagram |

**Ends as** — `excalidraw` · vector — · still editable ✅

**Buys you** — ⭐ The general form of the .drawio move: emit the file format of an existing editor, so editability is inherited rather than engineered. The note's own contrast case makes the point — a sibling skill outputs HTML that looks good but cannot be edited, so adjusting it means going back to chat.

**Costs** — The note verifies only that the file opens and is editable. **It makes no vector claim at all**, which is why the column reads unknown rather than unverified.

<details><summary>Evidence — the note's own words</summary>

> Excalidraw-Diagram-Generator github官方出的，在awesome-copilot下
>
> 可生成.excalidraw Json格式，拖到excalidraw.com里就可以打开直接编辑
>
> Architecture-diagram-generator 直接输出架构图，缺点是生成后不能编辑，想微调需要再聊天。优点是输出形式html文件
>
> 以上依旧挑选github上受广泛认可（k star以上）的skills
>
</details>


### W24 · Install the drawing skill into whichever agent you already use

**Source** — 高质量材料科研图 AI 自动生成 Skill. note in `DETAILS.json` · 334 likes · github.com/Grenzlinie/materials-science-figure-skill.

**Starts from** — A sentence saying what you want drawn; the skill classifies whether it is a schematic, a flow chart or a mechanism figure.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Install with one command, then choose which agent to install into — Codex, Claude Code, Cursor or Gemini CLI | npx skills add | installed skill |
| 2 | Export the image API key and base URL in the shell profile | shell | configured |
| 3 | Talk to the agent to generate, or to edit an existing image | the agent | figure |

**Ends as** — `image (unspecified)` · vector — · still editable —

**Buys you** — ⭐ Quoted: the skill is agent-agnostic and installs into four different agents rather than shipping for one. ⚠ **Only the conceptual branch is recorded here.** The same skill has a second, separate branch in which a data file is drawn by preset matplotlib scripts; that branch is a data-figure workflow with a different output and is not classified by the row above. Recorded because the skill draws the line this collection otherwise blurs.

**Costs** — Needs an image API key. ⚠ The note states **no** vector or editability property for the conceptual branch. An image-generation model and a NanoBanana key strongly suggest a raster, but suggestion is not a source claim, so the row says unknown rather than guessing.

<details><summary>Evidence — the note's own words</summary>

> 内置多种材料科学绘图 prompt，自动化识别你的需求（示意图、流程图、机理图）
>
> npx skills add https://github.com/Grenzlinie/materials-science-figure-skill --skill nanobanana-image-generation
>
> 然后 follow 提示 选择你希望安装到的编程 agent 上（codex, cc, cursor, gemini cli 等）
>
> 现在支持根据本地数据文件，AI 调用预设 matplotlib 脚本自动精确画图，内置 Nature  Science 风格的配色，无需手动调整
>
> 当然也可以绘制其他任意图片，或者进行已有图片编辑、修改
>
> export NANOBANANA_API_KEY='sk-zk2xxx' # 替换你的 gemini api key或者第三方apikey
>
> export NANOBANANA_BASE_URL='https://api.zhizengzeng.com/google'
>
</details>


### W26 · No skill at all: ask the chat model to write the .drawio file, then screenshot-correct it

**Source** — 用 ChatGPT + draw.io 快速画复杂框架图. note in `DETAILS.json` · 93 likes.

**Starts from** — Your own thinking, explained to the model first.

| # | step | tool | produces |
|---|---|---|---|
| 1 | Explain your reasoning and logic to the model before anything is drawn | GPT | shared understanding |
| 2 | Have it generate a draft image with its own image tool | GPT image | raster draft |
| 3 | Ask it to write the .drawio FILE AS CODE from that draft, with the requirement stated explicitly: importable, displays correctly, editable | GPT | .drawio |
| 4 | Open it, find what is wrong, screenshot it back to the model repeatedly, and adjust by hand as well | draw.io + GPT | corrected .drawio |

**Ends as** — `drawio` · vector — · still editable ✅

**Buys you** — ⭐ The same screenshot-correction loop as W04 with **no dedicated conversion tooling** — no skill and no repository, only a chat model and draw.io itself. The author says outright that a well-made skill would probably be better and that this is already good enough. **[INFERRED]** that this shows the loop rather than the packaging is what carries the route; one working un-packaged example does not establish that.

**Costs** — Quoted: iteration is manual, and the author also adjusts by hand. Nothing verifies the file beyond opening it.

<details><summary>Evidence — the note's own words</summary>

> 前置：把自己的思路和逻辑跟ai讲清楚
>
> 1.先用gpt自己的image生成草稿
>
> 2.让他根据这个草稿生成drawio文件，提示词如下：我想把他导入draw.io 变成可以编辑的图，你可以帮我用代码写一下这个文件吗？确保他可以导入drwoio，正常显示，可以编辑
>
> 3.根据他生成的drawio文件，打开看有什么问题，不断截图给他叫他修改，也可以自己手动调整
>
> 其实我觉得如果有大佬做一个精致的skill可能可以获得更好的体验，但是目前这个我已经比较满意了
>
</details>


---

## Read and deliberately NOT counted as workflows

Kept because deleting them would hide what the sweep actually returned.

### The manual control — template PPT, draw.io, ProcessOn — 深度学习画模型结构图的三个必用, 7 likes

Not an agent workflow at all. Kept because its author had tried the AI routes first and reported a hit rate, which is the only measured comparison in the collection.

> 各种AI画图软件（真的是小红书里面能搜到的所有能生图的网址）都尝试了但是10次里面就只有1次还行
>
> 深度学习画图主要靠人力，其他工具纯辅助
>

### Redrawing a published figure as a study exercise — Nano-banana改造篇|爆改CVPR25流程图, 35 likes

A daily practice for learning the genre, not a route to a figure of your own: the output is a raster derived from someone else's published figure.

> 🍄每日学习科研绘图！Day4｜2025.12.4
>
> 这次我继续用 Banano 对论文原始流程图进行了 重新绘制优化
>

### The floor case: one prompt, two formats demanded, nothing verified — 读博｜codex画论文图｜可编辑的viso图, 307 likes

The whole procedure is one sentence, and nothing about it is checked — the note asks for `.vsdx` and `.svg` but never shows that either opened, was editable, or was vector. Moved out of the workflow list on a cross-model audit: a request is not a replayable method. Kept because the collection should contain its weakest case, not only its best ones.

> 你的论文上下文+为这个论文生成主图，必要时可以调用bizard skill科研画图
>
> 学术风格，用英文，要文字清楚，不要公式。框图清晰对称。输出viso和svg版本
>

### Install by URL, then hand over the code or the data table — Codex科研画图真的可行，一键出图skill分享, 262 likes

The lightest installation path seen — the agent fetches the skill from a pasted URL with no package manager. ⛔ Moved out because its input is code or a data table and it asks the model to RECOMMEND a chart type: that is data plotting, not a conceptual figure. The author reports n = 2 and states no format or editability property.

> 你就复制skill在GitHub上地址，然后发给Codex，他自己就会下载了
>
> 下载完了，你就把你的代码或者数据表格发给他，让他帮你生成推荐图形与画图
>
> 他就会自动产生符合sci论文标准的图片了，博主试验了两次，两次结果都还可以
>

### An export setting, not a workflow — Draw.io 导出流程图，别再只会用 PNG 了！, 38 likes

One step rather than a route, but the only note in the sweep that states export settings concretely, and it is directly relevant to anything ending in `.drawio`.

> 流程图想要清晰，优先选 SVG 矢量格式
>
> 导出时建议保留这几个选项：✅ 包含绘图副本 ✅ 嵌入图片 ✅ 嵌入字体
>
> 论文 / PPT / 后期编辑优先 SVG，日常分享再导 PNG
>

### Data figures: describe the data, get plotting CODE — 教你用Claude生成Nature级科研图, 664 likes

⛔ A DATA figure workflow, outside this skill's genre entirely. Recorded because it is the boundary: a figure whose positions encode measured numbers must come from a script that reads them. ⚠ Its own '600dpi 矢量' conflates raster resolution with vector output.

> 根据[描述你的数据]生成Python代码创建组合图表
>
> 明确指定图表尺寸和比例(常用：单栏7cm，双栏14cm)
>
> 先要求单图代码，确认OK后再要组合图
>
> Claude生成的代码≠会自动运行，需要你自己执行
>
