---
benchmark_id: c-eval
benchmark_name: C-Eval
description: "A Chinese evaluation suite of 13,948 multiple-choice questions across 52 disciplines and four difficulty levels, for measuring advanced knowledge and reasoning of foundation models in a Chinese context."
task_type: "Multiple-choice knowledge and reasoning questions across 52 disciplines (humanities, science, engineering)"
dataset_size: "13,948 multiple-choice questions across 52 disciplines; four difficulty levels (middle school, high school, college, professional); plus the C-Eval Hard subset"
evaluation_method: "Closed-book multiple-choice; models answer exam-style questions spanning 52 disciplines at four difficulty levels"
scoring: "Accuracy (% correct); reported as an overall average and per-discipline / per-level breakdowns"
contamination_notes: "The complete C-Eval test set was released to the community in July 2025, so models trained after that date may have seen the answers."
limitations: "Multiple-choice format cannot assess free-form generation, open-ended reasoning or factual grounding. Scores on C-Eval Hard and the full set are not interchangeable. No Chinese model in the China AI Hub database currently publishes a C-Eval score, so this page records no evaluations."
last_verified: "2026-09-29"
sources:
  - source_name: "Huang et al. — C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models"
    source_url: https://arxiv.org/abs/2305.08322
    source_type: academic
    published_date: "2023-05"
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "C-Eval official repository (HKUST-NLP)"
    source_url: https://github.com/hkust-nlp/ceval
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "C-Eval benchmark website"
    source_url: https://cevalbenchmark.com/
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
---

**Short answer.** C-Eval is a Chinese-language, multiple-choice evaluation suite that tests a foundation model's knowledge and reasoning across 52 disciplines at four difficulty levels — middle school, high school, college and professional. It is the reference benchmark for "does this model actually know Chinese curriculum and professional content", not for chat quality, coding or generation.

## What it measures

C-Eval measures breadth of Chinese knowledge and reasoning. Its 13,948 multiple-choice questions are drawn from exam-style material spanning the humanities, science and engineering, and are graded across four ascending difficulty levels. A model that scores well on C-Eval has demonstrated that it can answer a wide range of Chinese-domain knowledge questions — the kind of breadth that matters for tutoring, content generation and general assistant work in Chinese.

The suite also ships **C-Eval Hard**, a subset of the most challenging subjects that requires advanced reasoning rather than recall. This split matters when reading scores: a headline "C-Eval 90%" usually refers to the full average, while "C-Eval Hard" is a stricter, more discriminating signal. Treating the two as the same number is a common reading error.

## How it works

C-Eval is a **closed-book multiple-choice** benchmark. A model is given a question with several answer options and must select the correct one. There is no web access, no tool use and no open-ended component — the entire signal comes from whether the model picks the right option.

Scoring is **accuracy**: the percentage of questions answered correctly, reported as an overall average and as per-discipline and per-level breakdowns. Because the test spans 52 disciplines, the average is a breadth measure, and the per-discipline rows reveal where a model is strong or weak (for example, a model may score well on humanities but poorly on professional engineering).

The benchmark was introduced by HKUST researchers and accepted to NeurIPS 2023, and is maintained in the `hkust-nlp/ceval` repository with a public leaderboard on `cevalbenchmark.com`. It is also integrated into the widely used `lm-evaluation-harness`, which means many of the numbers circulating for C-Eval come from a common harness rather than a single vendor's custom setup.

## What it does NOT measure

Three gaps are worth stating explicitly. First, the multiple-choice format means C-Eval does **not** measure free-form generation, instruction-following, factual grounding or any open-ended reasoning quality — a model can score well by ranking options without producing a single fluent sentence. Second, it does not measure coding, agentic behaviour or multimodal understanding. Third, as a static suite with a now-public test set, C-Eval carries a **contamination risk** for models trained after the July 2025 release of the full test set; a post-2025 training run may simply have memorised the answers.

C-Eval is also a *dataset*, not an independent evaluation service. Scores are self-reported by model builders (or reproduced by third parties on their own harnesses); the benchmark itself does not verify them.

## Chinese model results

**Not publicly documented.** As of 2026-09-29, no model page in the China AI Hub database publishes a C-Eval score. The models tracked here — [Qwen3.8-Max](/models/qwen38-max/), [GLM-5.3](/models/glm-53/), [Kimi K3](/models/kimi-k3/) and others — publish results on HLE, GPQA Diamond, Terminal-Bench, SWE-bench and similar international or coding benchmarks, but not on C-Eval. Accordingly, this page records **no evaluations**, and we do not import C-Eval numbers from third parties or vendor marketing. Treat any C-Eval figure you see elsewhere as outside this database until a tracked model publishes one.

## How to read C-Eval results

China AI Hub analysis: a C-Eval score is a breadth-of-Chinese-knowledge signal, not a general-intelligence ranking. Before citing one, confirm (1) whether it is the full set or C-Eval Hard, (2) whether it is an overall average or a specific level, and (3) the training cutoff relative to the July 2025 test-set release. The same discipline that applies to every benchmark here — match versions, subsets and modes before comparing — applies to C-Eval; see [Benchmark Methodology Divergence](/research/benchmark-methodology-divergence/) and [How to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Where C-Eval sits among Chinese benchmarks

C-Eval is one of three prominent Chinese-native benchmarks, each answering a different question. **C-Eval** is the curriculum-based multiple-choice knowledge suite; **CMMLU** is the multitask-understanding analogue, structured like MMLU with few-shot settings and China-specific subjects; **SuperCLUE** is the team-run comprehensive system that adds agent and safety tracks on top of knowledge. The three are complementary, not interchangeable — C-Eval says "does the model know Chinese exam content", CMMLU says "does the model understand Chinese-domain tasks", and SuperCLUE says "is the model good all-round in Chinese".

Two methodology events shaped how C-Eval numbers should be read. First, C-Eval was accepted to NeurIPS 2023, which fixed its design as an academic reference. Second, and more consequentially for contamination, the full test set was released to the community in July 2025 — before that, evaluation was effectively self-reported against a partially held-out set. The release enabled community reproduction via `lm-evaluation-harness`, but it also means post-2025 models may have seen the answers. Any C-Eval figure should state which set (full or C-Eval Hard) and the model's training cutoff relative to that release.

## Related entities

- Models: [Qwen3.8-Max](/models/qwen38-max/) · [GLM-5.3](/models/glm-53/) · [Kimi K3](/models/kimi-k3/) — Chinese general-purpose flagships that would be the natural C-Eval candidates.
- Comparison: [Qwen3.8-Max vs GLM-5.3](/comparisons/qwen38-max-vs-glm-53/).
- See all [benchmarks](/benchmarks/).

*Labels used on this page: **Official fact** (benchmark design and methodology from the primary paper and official repository), **China AI Hub analysis** (our synthesis of what the methodology means for reading scores, introduced as such). No **vendor-reported claim** or **third-party evidence** is recorded for this benchmark, because no tracked Chinese model has published a C-Eval result.*
