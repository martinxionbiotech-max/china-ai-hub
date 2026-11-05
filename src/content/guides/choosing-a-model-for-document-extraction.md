---
title: "Choosing a Model for Document Extraction"
description: "Invoices, forms and contracts at volume: what actually decides extraction quality, why structured-output support matters more than benchmark scores, and how to cost it per document."
author: "SinoAI Hub Research Team"
published_date: "2026-11-05"
updated_date: "2026-11-05"
pillar: model-selection-by-workload
order: 6
related_entities:
  - glm-5.3-flash
  - deepseek-v4-1-flash
  - qwen3.8-flash
  - minimax-m3
sources:
  - source_name: "China AI Hub — Models database"
    source_url: "https://sinoaihub.com/models/"
    source_type: independent
  - source_name: "China AI Hub — Pricing database"
    source_url: "https://sinoaihub.com/pricing/"
    source_type: independent
---

**The short answer.** Document extraction is an input-heavy, output-light workload that fails on schema compliance rather than reasoning depth. The model that wins is usually a flash tier with reliable structured output and a low output price — not the flagship. At volume, the decisive variable is cost per document, which is three numbers multiplied: input tokens, output tokens, and the share of documents that need a retry.

## Why this workload is different

Extraction has an unusual shape:

| Property | Typical value | Consequence |
|---|---|---|
| Input | 2,000–20,000 tokens per document (text) or far more (images) | Input price dominates the bill |
| Output | 200–800 tokens of JSON | Output price matters less |
| Turns | One | No cache benefit |
| Failure mode | Malformed JSON, missed field, wrong unit | Retry cost |

That combination inverts the usual advice. For generation-heavy work you buy the cheapest output; here you buy the cheapest **input** that still returns valid JSON, and you optimise the retry rate.

## The three numbers that decide cost

Cost per document = (input tokens × input price) + (output tokens × output price), divided by the first-pass success rate.

A worked example with real list prices, 8,000 input tokens and 400 output tokens:

| Model | Input cost | Output cost | Per document | With 10% retries |
|---|---|---|---|---|
| DeepSeek-V4.1-Flash | $0.00120 | $0.00024 | $0.00144 | $0.00160 |
| GLM-5.3-Flash | $0.00120 | $0.00020 | $0.00140 | $0.00156 |
| Qwen3.8-Flash | $0.00120 | $0.00019 | $0.00139 | $0.00155 |
| MiniMax-M3 | $0.00240 | $0.00048 | $0.00288 | $0.00320 |

At 100,000 documents a month the difference between the first three is under $5 — **which means price is not the selection criterion at this scale.** The retry rate is: a model with 85% first-pass validity costs 12% more than one with 95%, which is more than twice the entire spread between the cheap tiers.

## What actually predicts extraction quality

Four things, in order of observed importance:

**1. Structured-output enforcement.** Whether the model accepts a JSON schema and constrains decoding to it, or merely "tries" to produce JSON. A schema-constrained model that is 10% weaker on benchmarks usually beats a stronger model that occasionally emits prose around the JSON.

**2. Field-level accuracy on your documents.** Invoices from your suppliers, not invoices from a benchmark. Layout, language and abbreviations are domain-specific.

**3. Handling of null and absent fields.** The hardest extraction failure is not a wrong value but a hallucinated one: a field that does not exist in the document, filled in confidently.

**4. Long-tail layout tolerance.** Scanned faxes, rotated pages, two-column contracts. This is where cheap models separate.

## The retry economics

A retry is not just another API call; it is the call plus your parsing, validation and queueing. In most pipelines a retry costs 2–3x a first attempt in engineering terms, even when the token cost is trivial.

Two design choices reduce it more than model selection:

- **Schema-first prompting** with explicit types, enums and required fields, plus a "null is a valid answer" instruction.
- **A validation layer** that checks arithmetic (line items sum to total) and sends only failures back, with the error message attached.

Teams that do this report first-pass rates above 95% on stable document types with flash-tier models.

## Images versus text

If documents arrive as images or PDFs, the input cost is set by vision tokenisation, which is much higher per page. Two approaches:

- **OCR then extract** — a cheap OCR pass produces text, and a text model does the extraction. Lowest cost, loses layout.
- **Vision model directly** — the model sees the page. Higher cost, better on tables and stamps, and it handles layout that OCR flattens.

For invoices with tables, vision usually wins on accuracy; for clean digital PDFs, OCR plus text extraction wins on cost by an order of magnitude.

## Our view

**Do not buy a flagship for extraction.** The task rewards schema compliance and consistency, not reasoning depth. A flash tier at $0.15 input with schema-constrained output will match or beat a $2.00 model on structured extraction, at a tenth of the cost.

**Price is the wrong first filter here; retry rate is the right one.** At 100k documents the whole spread between the cheap tiers is under $50 a month, while a 10-point difference in first-pass validity is worth more than the entire price difference between them.

**The validation layer is the highest-leverage engineering in the pipeline.** Arithmetic checks, enum checks and null-handling catch most failures before they become retries, and they cost nothing per token.

**Test on 50 real documents before you test on 5,000.** Layout variety saturates quickly: the first 50 documents in a category expose the failure modes, and the next 4,950 mostly repeat them.

## Next

[High-volume classification](/guides/choosing-a-model-for-classification/) — the other workload where the cheapest tier usually wins.
