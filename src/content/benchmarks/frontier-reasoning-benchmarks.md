---
benchmark_id: frontier-reasoning-benchmarks
benchmark_name: "Frontier Reasoning Benchmarks"
description: "HLE, GPQA Diamond, AIME and ARC-AGI in one place: what each measures, the scores Chinese models publish, and why the four are not interchangeable."
task_type: "Expert knowledge, graduate science, competition mathematics and abstract pattern reasoning"
dataset_size: "HLE 2,500 questions · GPQA Diamond 198 questions · AIME 15 problems per exam · ARC-AGI 400 public training tasks, private eval set"
evaluation_method: "Multiple-choice, short-answer and integer-answer grading; ARC-AGI scored on held-out tasks by exact grid match"
scoring: "Accuracy, except ARC-AGI which reports percentage of tasks solved; AIME is X/15"
caveat: "These four measure different things and are routinely quoted as if they measured one. HLE rewards breadth of expert knowledge, GPQA Diamond rewards graduate science reasoning, AIME rewards competition maths, ARC-AGI rewards abstraction from a handful of examples. A model can top one and trail on another, and the small item counts (15 AIME problems, 198 GPQA questions) mean a few items move the headline by several points."
contamination_notes: "HLE includes a canary string; GPQA is public and likely present in later training corpora; AIME is a fixed annual exam; ARC-AGI's public set is small enough to be memorised, which is why the private set carries the claim."
limitations: "Only HLE and GPQA Diamond have published Chinese-model results in this database. AIME and ARC-AGI are recorded as methodology pages because no tracked model publishes a comparable number. Treat the four as a panel, not a ladder."
member_ids: [hle, gpqa-diamond, aime, arc-agi]
last_verified: "2026-11-05"
evaluations:
  - benchmark: HLE
    model: deepseek-v4-1-flash
    score: 36.8
    model_version: "39.1 on pure-text subset"
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: HLE
    model: deepseek-v4-pro
    score: "42.7 (60.0 with tools)"
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: HLE
    model: qwen3.8-max
    score: "43.6 (56.2 with tools)"
    metric: accuracy
    date: "2026-08"
    source_type: vendor_reported
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - benchmark: HLE
    model: kimi-k3
    score: "43.5 (56.0 with tools)"
    model_version: HLE-Full
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: HLE
    model: kimi-k2.5
    score: "30.1 (50.2 with tools)"
    model_version: HLE-Full
    metric: accuracy
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
  - benchmark: HLE
    model: minimax-m2
    score: "12.5 without tools / 31.8 with tools"
    metric: accuracy
    date: "2025-10"
    source_type: vendor_reported
    source_url: https://github.com/MiniMax-AI/MiniMax-M2
  - benchmark: GPQA Diamond
    model: deepseek-v4-1-flash
    score: 90.9
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: GPQA Diamond
    model: qwen3.8-max
    score: 92.6
    metric: accuracy
    date: "2026-08"
    source_type: vendor_reported
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - benchmark: GPQA Diamond
    model: kimi-k3
    score: 93.5
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: GPQA Diamond
    model: kimi-k2.5
    score: 87.6
    model_version: avg@8
    metric: accuracy
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
  - benchmark: GPQA Diamond
    model: minimax-m2
    score: 78
    model_version: "Artificial Analysis-aligned"
    metric: accuracy
    date: "2025-10"
    source_type: vendor_reported
    source_url: https://github.com/MiniMax-AI/MiniMax-M2
sources:
  - source_name: "Humanity's Last Exam official site"
    source_url: https://lastexam.ai/
    source_type: official
    last_verified: "2026-09-22"
    confidence: high
  - source_name: DeepSeek API Change Log
    source_url: https://api-docs.deepseek.com/updates
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Qwen3.8-2.4T-A95B model card
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi K3 GitHub README
    source_url: https://github.com/MoonshotAI/Kimi-K3
    source_type: official
    last_verified: "2026-09-20"
  - source_name: "GPQA official repository"
    source_url: https://github.com/idavidrein/gpqa
    source_type: official
    last_verified: "2026-09-22"
    confidence: high
  - source_name: "Mathematical Association of America — American Invitational Mathematics Examination (AIME)"
    source_url: https://maa.org/math-competitions/american-invitational-mathematics-examination-aime
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "Mathematical Association of America — Competitions"
    source_url: https://maa.org/math-competitions
    source_type: benchmark_org
    last_verified: "2026-09-29"
  - source_name: "Chollet — On the Measure of Intelligence (introducing ARC)"
    source_url: https://arxiv.org/abs/1911.01547
    source_type: academic
    published_date: "2019-11"
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "ARC-AGI repository (fchollet)"
    source_url: https://github.com/fchollet/ARC-AGI
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "ARC Prize / ARC-AGI"
    source_url: https://arcprize.org
    source_type: benchmark_org
    last_verified: "2026-09-29"
---

**Short answer.** Four benchmarks get quoted as evidence of "frontier reasoning": HLE, GPQA Diamond, AIME and ARC-AGI. They test four different capabilities, they are reported under four different conventions, and only two of them have Chinese-model results in this database. Reading them as a single scoreboard is the most common mistake in Chinese model evaluation.

## What each one actually tests

| Benchmark | What it rewards | Format | Items |
|---|---|---|---|
| HLE | Breadth of expert knowledge, resistance to search | Mixed MCQ and short answer | 2,500 |
| GPQA Diamond | Graduate-level science reasoning | 4-option MCQ, 198 questions | 198 |
| AIME | Competition mathematics, end-to-end derivation | 15 integer-answer problems | 15 per year |
| ARC-AGI | Abstraction from a few examples | Grid-transformation puzzles | 400 public, private eval |

The distinction matters commercially. A model that leads HLE is broad; one that leads GPQA is scientifically precise; one that leads AIME is a strong mathematical reasoner; one that leads ARC-AGI generalises from tiny samples. None of these is "general intelligence", and a buyer selecting for a contract-review pipeline should weight none of them heavily.

## HLE

Humanity's Last Exam was built as a frontier-resistant knowledge test: expert-written questions across disciplines, designed so that search alone does not answer them. Vendors commonly report two numbers — with and without tool access — and the gap between them is often larger than the gap between models.

The practical reading: HLE is a breadth test, and breadth is cheap to improve with retrieval. A high no-tools score is the more interesting number; a high with-tools score mostly tells you the model is good at using a browser.

## GPQA Diamond

198 graduate-level science questions written to be Google-proof, drawn from physics, chemistry and biology. It is the most stable of the four because the item count is large enough for the score to be meaningful and the format is uniform.

Its limit is domain narrowness: strong GPQA performance says a model handles technical reasoning carefully, not that it handles your domain. Chinese labs report it consistently, which makes it one of the few genuinely comparable numbers across vendors — provided the tool-access setting is stated.

## AIME

Fifteen problems, integer answers, no partial credit. The exam is public and annual, so the year *is* the version: "AIME 90%" without a year is uninterpretable, and the shift toward AIME 2025 reflects contamination pressure as much as difficulty.

AIME's real value is diagnostic: it isolates multi-step mathematical derivation from knowledge recall. Its real weakness is sampling noise — one problem is 6.7 percentage points.

## ARC-AGI

ARC-AGI asks a model to infer a transformation rule from two or three examples and apply it to a new grid. It is the least saturated benchmark in this group and the hardest to game with scale alone, which is why it attracts attention disproportionate to its commercial relevance.

For buyers it is close to useless as a selection criterion — almost no production workload resembles ARC puzzles. Its value is as a canary: a lab that improves on ARC-AGI is probably improving genuine abstraction rather than memorisation.

## Comparability

Three rules apply across all four:

1. **Tool access must be stated.** HLE and GPQA both have with-tools variants; mixing them creates fake improvements.
2. **Item counts bound precision.** 15 items cannot support a claim of a 2-point difference; 198 can support roughly a 7-point one.
3. **Year and version are part of the name.** AIME by year, HLE by tool setting, GPQA by split (Diamond vs main), ARC-AGI by public or private set.

## Our read

**HLE is the most over-weighted benchmark in the Chinese model market.** It measures breadth of expert knowledge, which retrieval systems solve, and it is reported in two modes that vendors choose between when publishing. A buyer who selects on HLE is selecting on a number that partly measures browsing skill.

**GPQA Diamond is the most useful of the four for technical buyers.** It is large enough to be stable, narrow enough to be honest, and consistently reported. If you must pick one reasoning benchmark to track across Chinese vendors, pick this one.

**AIME and ARC-AGI are diagnostic, not commercial.** They tell you something real about a lab's capability trajectory and almost nothing about whether a model will work in your product. Track them for signal about the vendor, not for selection.

**The panel beats any single number.** A model strong on GPQA and weak on AIME is a careful reasoner without mathematical depth; the reverse suggests a maths specialist. Reading two together tells you more than reading either twice.
