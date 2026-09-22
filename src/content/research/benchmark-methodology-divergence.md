---
title: "Benchmark Methodology Divergence Across Chinese Model Vendors"
description: "How DeepSeek, Alibaba and other Chinese vendors report benchmark scores differently — versions, tool modes, subsets and product mismatches — and how to read them."
published_date: "2026-09-22"
updated_date: "2026-09-22"
research_question: "To what extent are headline benchmark scores from Chinese model vendors directly comparable, and which methodological differences explain the apparent gaps between them?"
related_entities:
  - gpqa-diamond
  - hle
  - terminal-bench
  - swe-bench
  - deepswe
author_view: true
sources:
  - source_name: "DeepSeek API Change Log — 2026-09-10"
    source_url: "https://api-docs.deepseek.com/updates"
    source_type: official
    published_date: "2026-09-10"
    confidence: high
  - source_name: "Hugging Face model card — Qwen3.8-2.4T-A95B"
    source_url: "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
    source_type: official
    confidence: high
  - source_name: "Hugging Face model card — DeepSeek-V4-Pro"
    source_url: "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
    source_type: official
    confidence: high
  - source_name: "Rein et al. — GPQA: A Graduate-Level Google-Proof Q&A Benchmark"
    source_url: "https://arxiv.org/abs/2311.12022"
    source_type: academic
  - source_name: "Jimenez et al. — SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
    source_url: "https://arxiv.org/abs/2310.06770"
    source_type: academic
---

All facts below are from the China AI Hub database (last verified 2026-09-20) and the primary sources linked at the bottom. Scores are labeled by source type; where one vendor's number cannot be compared to another's, this article explains why rather than forcing a comparison.

## The comparability problem

Headline scores from Chinese vendors look directly comparable — "90.6" and "86.6" on Terminal-Bench, "92.6" and "90.9" on GPQA Diamond — but they are frequently not measuring the same thing. Three independent levers change the number without changing the model: the benchmark version, whether tools are allowed, and which subset of the test is scored. A fourth — which product the score actually describes — is specific to how some Chinese labs publish.

## Lever 1: benchmark versions

Terminal-Bench is the clearest case. DeepSeek reports V4.1-Flash at 90.6 on Terminal-Bench 2.1, and 30.0 on Terminal-Bench 3.0 and 31.2 on Terminal-Bench 4.0 (all vendor-reported, 2026-09-10). One model, three versions, a 60-point spread. A comparison that reads "Terminal-Bench 90.6" from one vendor against "Terminal-Bench 86.6" from another is only valid if both are on 2.1 — and it must say so. The database records benchmark_version separately from model_version precisely to prevent silent mixing.

## Lever 2: tools

The same vendor can report two HLE numbers for the same model: DeepSeek-V4-Pro is listed at 42.7 on HLE, and 60.0 "with tools"; Qwen3.8-Max is listed at 43.6, and 56.2 "with tools". The tool-augmented number is not dishonest — it is a different measurement — but a 17-point gap between the two modes of the same model dwarfs the gaps between competing models. A score is only meaningful if the mode is stated.

## Lever 3: subsets

DeepSeek reports V4.1-Flash at 36.8 on HLE with a footnote: "tested only on the pure-text subset", where the score is 39.1. Subset choice moves the number by several points. When a vendor cites a versionless number without specifying the subset, treat it as a version question, not an answer.

## Lever 4: which product the score describes

This is the subtlest and most consequential divergence in the Chinese ecosystem. Qwen3.8-Max's benchmark scores (Terminal-Bench 2.1 86.6, SWE-bench Pro 67.7, GPQA Diamond 92.6, HLE 43.6, MRCR v2 256K 92.9) are taken from the Hugging Face model card for Qwen3.8-2.4T-A95B — the open-weights release. But the open model is text-only and thinking-only, while the Qwen3.8-Max API flagship accepts image and video input. The scores describe a product with a different capability surface than the one an API customer calls. That is a real, and easily missed, gap between the score and the product.

## Lever 5: what is not published

A missing benchmark is a data point. Vendors publish different subsets: DeepSeek publishes DeepSWE and Codeforces; Alibaba publishes SWE-bench Pro and MRCR. The database holds 5–6 records for the most-published models and 0–1 for others. Counts reflect what vendors chose to publish, which is itself information about where they are confident.

## What the database does about it

China AI Hub records every benchmark result with: score, metric, benchmark version, model version, date, source type (vendor_reported / independent / academic / community) and source URL. It never aggregates across incompatible versions and never ranks models from a single number.

## China AI Hub view

Our assessment: the most underrated risk in model selection is not a wrong score but an unstated methodology. A vendor's headline number is usually accurate as a vendor statement; the failure mode is the reader treating it as a measurement. The three levers above — version, tools, subset — can each move a score by more than the entire gap between leading models. Before any purchase or integration decision, check the benchmark version, the tool mode, the subset, and whether the score describes the product you can actually call. For your own workload, ten private test cases beat a thousand vendor numbers.

## Reading procedure

1. Confirm source type; prefer independent over vendor-reported.
2. Confirm the benchmark version and the model version.
3. Confirm the metric (pass@1, accuracy, rating) and the mode (with/without tools).
4. Confirm the subset if the benchmark has one.
5. Confirm the score describes the product you will actually use.
6. Run a small private eval on your real task.
