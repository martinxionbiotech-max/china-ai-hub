---
slug: deep-research
title: Deep Research
definition: "Deep research is an agentic workflow in which a model autonomously plans a research question, performs many rounds of search and document reading, and produces a cited, structured report — compressing hours of human research into minutes."
related_models: []
related_companies: []
related_technologies:
  - ai-agents
  - reasoning-models
  - synthetic-data
related_guides: []
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

No dedicated "deep research" product in the China AI Hub database as of 2026-09-22 — this is a data gap we report rather than paper over. The building blocks exist in the tracked ecosystem: reasoning models (DeepSeek-V4, Qwen3.8-Max, GLM-5.3, Kimi K3), agent frameworks with browser and MCP support (DeepSeek Harness, Qwen-Agent, Kimi Code), and 1M-token contexts for long-document synthesis.

## Major Chinese companies and models

None listed as a dedicated deep-research product (verified absence, 2026-09-22). This section updates when vendors document it.

## Practical applications

Industry and market reports, evidence-grounded literature reviews, regulatory and policy research, and open-source-intelligence style briefings.

## Limitations

Source quality is the ceiling — generated reports can be fluent and wrong; citation fabrication remains a real failure mode; and evaluation of research reports is itself unsolved. Published output needs human review before use.

## Deployment considerations

Log the search and reading trail for auditability; enforce source allow-lists for regulated domains; and treat every claim in a generated report as unverified until a human checks the citation.

## Future development

Expect deep research to absorb citation-verification models, internal knowledge bases via MCP, and interactive follow-up — turning reports into living documents.
