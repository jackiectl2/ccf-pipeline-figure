# Devices specific to long-context, memory and evaluation figures

Every claim here carries the count of figures that show it, taken from a vision pass over the 77 leading figures of 12 papers in this direction. ⚠ A device seen in fewer than three figures is marked **anecdotal** and must not be described as a convention.

## How a long context is actually drawn

⭐ **The most useful section in this file.** **Twenty-one distinct renderings were recorded**, and all twenty-one are listed below with the file each came from. Pick ONE and commit — mixing two of them in one figure makes the context read as two different objects.

⚠ This paragraph said *ten* until the corpus was re-audited (`assets/audit_corpus.py`). Ten is the number of **conceptual figures** in the same vision pass, which sits two keys away from the renderings in the same JSON. The bullets below were always twenty-one; only the sentence above them was wrong.

- **A horizontal stream of colored shard cards is revealed one shard at a time through the simulator stages.**  
  `01-LIC_simulator_flat_v3.png`
- **A blue full-instruction bar becomes small yellow blocks; rows indexed by turn place those blocks at different disclosure times.**  
  `02-LIC_Conv_Types_v3.png`
- **Each task shows a blue/grey full instruction above a row of short yellow sharded-instruction boxes.**  
  `03-LIC_Tasks_v2.png`
- **History is a vertical stack of colored chat bubbles grouped into single-session and cross-session examples.**  
  `00-main_examples.png`
- **Evidence sessions are mini chat transcripts; their history construction is shown as several boxed sessions converging into a released chat history.**  
  `01-main_annotation_pipeline.png`
- **Long context is a long grey-and-blue horizontal bar, with thin red vertical needle markers; full and last-2K policies are separate stacked lanes.**  
  `09-full_vs_last2K_demonstration.png`
- **The haystack is a tall scrolling document/page glyph with many grey text lines; retained or inserted evidence is highlighted in orange.**  
  `10-HaystackPipeline.png`
- **The context is a verbatim prompt box containing numbered documents; the answer-bearing document is bolded.**  
  `01-qa_example.png`
- **The context is a verbatim numbered-document prompt whose answer document is moved to a different ordinal position.**  
  `02-qa_changing_position.png`
- **The context is a verbatim numbered-document prompt with extra irrelevant documents inserted around the bold answer document.**  
  `03-qa_changing_length.png`
- **The context is a dense verbatim JSON-like key-value list inside a prompt box, with the relevant record emphasized.**  
  `05-kv_retrieval_example.png`
- **Conversation history is a vertical chain of alternating blue and grey speech bubbles; side labels and curved arrows point to earlier persona and event facts.**  
  `00-intro_figure_conv_only_v2.png`
- **An original session is a stack of small document/chat blocks feeding an agent; separate long-term-memory, observation, and reflection boxes represent compressed or retrieved history.**  
  `02-main_v4.png`
- **The history is shown as an input-conversation column of chat bubbles next to a generated response; the rest of the figure plots history-length effects.**  
  `03-minigpt5_results.png`
- **History is abstracted into a horizontal dated timeline of event cards with causal connectors, rather than shown as raw dialogue.**  
  `06-events.png`
- **A verbatim session log is stacked as alternating chat bubbles beside a dense generated summary; the preceding summary is shown as a separate prompt field.**  
  `07-summary_prompt_arxiv.png`
- **A verbatim conversation is a stacked dialogue panel, paired with a right-side observations list extracted from it.**  
  `08-observation_prompt_arxiv.png`
- **The history is a short chat thread in before/after editorial lanes, with removed and revised turns marked by red/green symbols.**  
  `10-conv_edits.png`
- **The active context is alternating chat bubbles; black code-like memory-write boxes visibly append durable facts after a context-pressure alert.**  
  `00-memgpt_diagrams_wide_memory_creation.png`
- **The live chat is overlaid by a dark recall-store search panel listing dated past snippets, then resumes with the retrieved fact.**  
  `01-memgpt_diagrams_wide_memory_search.png`
- **A short chat is paired with a dark working-context replacement command, making a memory edit visible as a before/after state change.**  
  `02-memgpt_diagrams_wide_memory_correction.png`

## The direction's signature

> There is a real but narrow signature: these figures make the input/history itself a manipulable, ordered object—then visualize controlled disclosure, placement, or external memory around it. Generic ML mechanism figures can use boxes and arrows too; they usually do not make a text history's order, length, and recoverability the visual object of study.

### Ordered conversation is rendered as turn-indexed speech or message units, usually with time or session structure,

**10 figures**

- `00-LIC_Teaser.png`
- `02-LIC_Conv_Types_v3.png`
- `00-main_examples.png`
- `00-intro_figure_conv_only_v2.png`
- `02-main_v4.png`
- `07-summary_prompt_arxiv.png`

### Controlled disclosure or position within a long text is made visible as colored shards, document order, or a marked context strip

**8 figures**

- `01-LIC_simulator_flat_v3.png`
- `02-LIC_Conv_Types_v3.png`
- `03-LIC_Tasks_v2.png`
- `09-full_vs_last2K_demonstration.png`
- `10-HaystackPipeline.png`
- `01-qa_example.png`

### Externalized memory is shown as an operational state boundary—write, search, then overwrite/reconcile—in 4 figures: 2402.17753-evaluating-very-long-term-conversational-mem/02-main_v4.png, 2310.08560-memgpt-towards-llms-as-operating-systems/00-memgpt_diagrams_wide_memory_creation.png, 2310.08560-memgpt-towards-llms-as-operating-systems/01-memgpt_diagrams_wide_memory_search.png, and 2310.08560-memgpt-towards-llms-as-operating-systems/02-memgpt_diagrams_wide_memory_correction.png. It is a convention

**4 figures**

- `02-main_v4.png`
- `00-memgpt_diagrams_wide_memory_creation.png`
- `01-memgpt_diagrams_wide_memory_search.png`
- `02-memgpt_diagrams_wide_memory_correction.png. It is a convention in this packet`

### Verbatim prompts and source text are retained as evidence rather than abstracted away

**9 figures**

- `03-LIC_Tasks_v2.png`
- `01-qa_example.png`
- `02-qa_changing_position.png`
- `03-qa_changing_length.png`
- `05-kv_retrieval_example.png`
- `04-persona_appendix.png`

### A single explicit long-context bar with needle ticks is anecdotal (2 figures): 2502.05167-nolima-long-context-evaluation-beyond-litera/09-full_vs_last

⚠ **anecdotal**

- `10-HaystackPipeline.png; it is not a packet-wide convention.`

## What the leading figures of this direction are, by role

| role | n |
|---|---:|
| data_plot | 41 |
| qualitative | 20 |
| conceptual | 10 |
| hybrid | 5 |
| table_image | 1 |

⭐ **Only 15 of 77 leading figures in this direction are structural at all** (conceptual + hybrid). The rest are data plots and qualitative panels. That is the measured base rate a reviewer of this area carries in their head.

## What opens a paper here

| Figure 1 is a… | papers |
|---|---|
| conceptual | 2 — Evaluating Very Long-Term Conversa, MemGPT: Towards LLMs as Operating  |
| data_plot | 6 — NoLiMa: Long-Context Evaluation Be, HELMET: How to Evaluate Long-Conte, Are Emergent Abilities of Large La… |
| qualitative | 1 — LongMemEval: Benchmarking Chat Ass |
| hybrid | 1 — LLMs Get Lost In Multi-Turn Conver |