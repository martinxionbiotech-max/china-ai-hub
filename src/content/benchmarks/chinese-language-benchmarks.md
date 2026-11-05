---
benchmark_id: chinese-language-benchmarks
benchmark_name: "Chinese Language Benchmarks"
description: "C-Eval, CMMLU and SuperCLUE explained: what Chinese-language benchmarks measure, why contamination limits them, and why no tracked model publishes clean results."
task_type: "Chinese academic knowledge, professional subjects and composite language capability"
dataset_size: "C-Eval 13,948 questions across 52 subjects · CMMLU 67 subjects · SuperCLUE multi-task aggregate"
evaluation_method: "Multiple-choice and open-ended tasks, aggregated into subject and composite scores"
scoring: "Accuracy by subject, plus a weighted composite for SuperCLUE"
caveat: "All three overlap with pre-training corpora and are contaminated for models trained after publication. Aggregates hide subject-level weakness, and SuperCLUE's weighting is not fully published. A headline Chinese-language score should be treated as an upper bound, not a measurement of capability on your task."
contamination_notes: "C-Eval and CMMLU were released in 2023 and are almost certainly in later Chinese pre-training data. SuperCLUE rotates some subsets but keeps others stable, so its contamination profile is mixed."
limitations: "This database records no C-Eval, CMMLU or SuperCLUE results for tracked models: vendors publish Chinese-language capability in marketing rather than in comparable tables. The absence is itself a finding about disclosure practice."
member_ids: [c-eval, cmmlu, superclue]
last_verified: "2026-11-05"
evaluations: []

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
  - source_name: "Li et al. — CMMLU: Measuring massive multitask language understanding in Chinese"
    source_url: https://arxiv.org/abs/2306.09212
    source_type: academic
    published_date: "2023-06"
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "CMMLU official repository"
    source_url: https://github.com/haonan-li/CMMLU
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "CMMLU dataset card (Hugging Face)"
    source_url: https://huggingface.co/datasets/haonan-li/cmmlu
    source_type: benchmark_org
    last_verified: "2026-09-29"
  - source_name: "SuperCLUE: A Comprehensive Chinese Large Language Model Benchmark"
    source_url: https://arxiv.org/abs/2307.15020
    source_type: academic
    published_date: "2023-07"
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "SuperCLUE official repository (CLUEbenchmark)"
    source_url: https://github.com/CLUEbenchmark/SuperCLUE
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "SuperCLUE official website"
    source_url: https://www.superclueai.com/
    source_type: benchmark_org
    last_verified: "2026-09-29"
---

**Short answer.** Chinese-language benchmarks exist to measure what English benchmarks miss: native fluency, Chinese professional knowledge and culturally specific reasoning. The three most cited — C-Eval, CMMLU and SuperCLUE — are also the most contaminated, and almost no Chinese vendor publishes results in a form that can be compared.

## The three

| Benchmark | Scope | Format | Status here |
|---|---|---|---|
| C-Eval | 52 subjects, 13,948 questions | Multiple choice | No tracked results |
| CMMLU | 67 subjects, Chinese professional knowledge | Multiple choice | No tracked results |
| SuperCLUE | Composite across many task types | Mixed | No tracked results |

That all three columns read "no tracked results" is not an oversight. It is the state of disclosure: Chinese labs report these numbers in launch blog posts with inconsistent settings, and rarely in a form that can be recorded against a model version.

## C-Eval

Released in 2023 as a Chinese counterpart to MMLU, covering humanities, social science, STEM and professional subjects. It quickly became the default Chinese knowledge benchmark and just as quickly became contaminated: the questions are public and later models trained on Chinese web data have seen them.

Its subject breakdown is more useful than the aggregate — a model can look strong overall while being weak in, say, law or medicine, which is exactly what a domain buyer needs to know.

## CMMLU

67 subjects with an emphasis on Chinese professional and cultural knowledge. Same structural strengths and the same contamination problem.

For buyers, the interesting question is not the total but whether a model handles the specific domain: accounting standards, clinical terminology, Chinese legal citations. No aggregate answers that.

## SuperCLUE

A composite that mixes knowledge, reasoning, safety and Chinese-language generation, published as a leaderboard. Its breadth is its value and its weakness: the weighting is not fully published, so a composite score cannot be decomposed into the capabilities a buyer cares about.

## The disclosure problem

Three practices make Chinese-language evaluation unusually hard:

1. **Launch-post reporting.** Numbers appear in a blog post, tied to a date rather than a model version.
2. **Aggregate-only disclosure.** Subject-level results, where the signal is, are rarely published.
3. **Inconsistent prompting.** Few-shot counts and chain-of-thought settings change scores materially and are rarely stated.

## Our read

**The absence of comparable Chinese-language results is a real gap in the market, and an opportunity.** Every serious buyer of a Chinese model needs to know how it handles Chinese contracts, Chinese medical text or Chinese customer service — and no public benchmark answers that credibly.

**Contamination makes aggregate Chinese scores close to useless for model selection.** A 2023 benchmark evaluated on a 2026 model measures memorisation as much as capability. The honest use is as a floor: a model that scores badly is probably bad; a model that scores well may simply have seen the questions.

**Buy your own evaluation set.** Fifty real documents from your domain, scored by your own criteria, will outperform any of these three benchmarks for selection — and it is the only approach that survives contamination.

**Subject-level disclosure is the metric to demand from vendors.** A vendor that will share per-domain results is telling you something about both its model and its transparency; one that shares only a composite is telling you something too.
