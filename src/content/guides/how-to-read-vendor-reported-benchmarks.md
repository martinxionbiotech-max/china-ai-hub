---
title: "How to Read Vendor-Reported Benchmarks"
description: "A guide to interpreting benchmark scores for Chinese AI models: what vendor-reported means, why versions cannot be mixed, and how China AI Hub labels scores by source type."
published_date: "2026-09-22"
updated_date: "2026-09-22"
related_entities:
  - gpqa-diamond
  - hle
  - terminal-bench
  - deepswe
  - swe-bench
  - mmmu-pro
sources:
  - source_name: "China AI Hub — Benchmarks database"
    source_url: "https://chinaaihub.com/benchmarks/"
    source_type: independent
  - source_name: "Rein et al. — GPQA: A Graduate-Level Google-Proof Q&A Benchmark"
    source_url: "https://arxiv.org/abs/2311.12022"
    source_type: academic
  - source_name: "Jimenez et al. — SWE-bench"
    source_url: "https://arxiv.org/abs/2310.06770"
    source_type: academic
---

Benchmark scores are the most misread numbers in the model market. This guide explains how China AI Hub labels them and how to read them without being misled.

## What "vendor-reported" means

A vendor-reported score is one published by the model's maker, not measured by an independent third party. It is not fake — it is unverified. The measurement conditions (prompting, scaffolding, sampling temperature, version choice) are chosen by the party with an interest in the outcome. In the China AI Hub database, every benchmark result carries a source_type: vendor_reported, independent, academic or community. When independent results exist for the same model and benchmark, prefer them.

## Why benchmark versions cannot be mixed

Benchmarks evolve: Terminal-Bench has 2.0, 2.1 and 3.0 generations; SWE-bench has variants and contamination-reduced versions. A score on an old version is not comparable to a score on a new one. Our database records benchmark_version and model_version separately, and we never aggregate across incompatible versions. When a vendor cites a versionless number, treat it as a version question, not an answer.

## The contamination problem

Public benchmarks leak into training data. GPQA was designed to be "Google-proof" against retrieval; SWE-bench and its successors fight contamination through dataset variants. Contamination inflates scores without improving real performance — and it is nearly impossible for an outside observer to detect in a single score. Skepticism, not cynicism: the correct response is to demand conditions and source labels, not to discard benchmarks entirely.

## What the database actually records

The China AI Hub benchmark database (10 benchmarks, last verified 2026-09-22) records per-result: score, metric, benchmark version, model version, date, source type and source URL. Models publish different subsets of benchmarks — the database holds 5-6 records for the most-published models and 0-1 for others. Counts reflect what vendors chose to publish, which is itself information.

## A reading procedure

1. Check source type. Independent > academic > community > vendor-reported, as evidence.
2. Check versions on both axes (benchmark and model).
3. Check the metric — pass@1, accuracy, and task-completion rates are different things.
4. Check the date; scores age as models are updated.
5. Look at what the vendor did not publish. A missing benchmark is a data point.
6. For your own decisions, run a small private eval on your real task. Ten of your own cases beat a thousand vendor numbers.

## Bottom line

Treat vendor-reported scores as vendor statements, not measurements. China AI Hub labels every score by source type precisely so the two can be told apart at a glance.
