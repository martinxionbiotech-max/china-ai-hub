---
image: "/images/ai/technologies-deep-research.webp"
image_credit: "AI-generated illustration (Seedream)"
slug: deep-research
title: Deep Research
definition: "Deep research is an agentic workflow in which a model autonomously plans a research question, performs many rounds of search and document reading, and produces a cited, structured report — compressing hours of human research into minutes."
related_models:
  - deepseek-v4-pro
  - kimi-k3
  - qwen3.8-max
related_companies:
  - deepseek
  - moonshot-ai
  - alibaba-cloud
related_technologies:
  - ai-agents
  - reasoning-models
  - synthetic-data
related_guides: [how-to-read-vendor-reported-benchmarks]
last_verified: "2026-09-22"
sources:
  - source_name: "OpenAI — Introducing deep research"
    source_url: "https://openai.com/index/introducing-deep-research/"
    source_type: official
---

## Technical background

OpenAI's "deep research" (February 2025) made the pattern a product category: a reasoning model drives iterative search over the open web, reads sources, and synthesizes a long cited report. The underlying machinery combines search APIs, browser or document tools, and long-context synthesis.

## How it works

A loop: decompose the question into sub-questions → search → read and judge sources → extract evidence → branch into follow-ups → synthesize with citations. Quality depends on the search substrate, source-ranking, and the model's ability to discard low-quality material rather than just summarize it.

## Why it matters

It moves models from answering to investigating — relevant for market research, due diligence, academic literature review, and competitive analysis. It also raises the bar for what "original content" means: the reports themselves are generated, so their value lives in the workflow, source quality and editorial judgment.

## Chinese adoption

No dedicated "deep research" product in the China AI Hub database as of 2026-09-22 — this is a data gap we report rather than paper over. The building blocks exist in the tracked ecosystem: reasoning models (DeepSeek-V4-Pro and V4.1-Flash, Qwen3.8-Max, GLM-5.3, Kimi K3), agent frameworks with browser and MCP support (DeepSeek Harness, Qwen-Agent, Kimi Code), and 1M-token contexts for long-document synthesis. DeepSeek-V4-Pro's 393,216-token maximum output and Kimi K3's 1M-token output are the concrete capacities that would underpin cited-report generation.

## Major Chinese companies and models

None listed as a dedicated deep-research product (verified absence, 2026-09-22). This section updates when vendors document it.

## Practical applications

Industry and market reports, evidence-grounded literature reviews, regulatory and policy research, and open-source-intelligence style briefings.

## Limitations

Source quality is the ceiling — generated reports can be fluent and wrong; citation fabrication remains a real failure mode; and evaluation of research reports is itself unsolved. Published output needs human review before use.

## Deployment considerations

Log the search and reading trail for auditability; enforce source allow-lists for regulated domains; and treat every claim in a generated report as unverified until a human checks the citation.

## What the available evidence actually shows

The evidence supports a negative claim cleanly: no Chinese vendor ships a dedicated deep-research product recorded in the database as of 2026-09-22. The evidence also supports a conditional claim: the component parts (reasoning models, agent frameworks, 1M-token contexts, 393K+ output ceilings) all exist and are documented. What the evidence cannot support is any prediction about timing or which lab will package them first. China AI Hub analysis indicates deep research in China is currently a capability assembled from parts rather than a named product, and the database will reflect that distinction until a vendor documents a dedicated offering.

## Future development

Expect deep research to absorb citation-verification models, internal knowledge bases via MCP, and interactive follow-up — turning reports into living documents.

*Labels used above: **Official fact** (from OpenAI's deep research announcement and the China AI Hub database), and **China AI Hub analysis** (our synthesis, always introduced as such).*
