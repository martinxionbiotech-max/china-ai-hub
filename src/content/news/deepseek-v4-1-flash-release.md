---
title: "DeepSeek releases V4.1-Flash with multimodal vision and lower API prices"
description: "DeepSeek ships V4.1-Flash, the smallest model of its new asymmetric-architecture family, with MIT weights and reduced API pricing as V4-Flash retires."
published_date: "2026-09-10"
type: model_release
trigger_updates:
  - deepseek-v4-1-flash
sources:
  - source_name: "DeepSeek API Change Log — 2026-09-10"
    source_url: "https://api-docs.deepseek.com/updates"
    source_type: official
    published_date: "2026-09-10"
    confidence: high
  - source_name: "DeepSeek — Introducing DeepSeek-V4.1-Flash"
    source_url: "https://www.deepseek.com/en/news/deepseek-v4-1-flash/"
    source_type: official
    published_date: "2026-09-10"
    confidence: high
---

DeepSeek released V4.1-Flash on 2026-09-10, the smallest model of its new "asymmetric architecture" family, with MIT open weights and native multimodal vision. The API change log lists the release alongside a price reduction; V4-Flash and V4-Flash-Vision-Exp are retired, with their model names temporarily routed to V4.1-Flash for compatibility.

The model is a 552B-parameter mixture-of-experts that activates only 8B parameters per token on input (16B on output), with a 1M-token context window and 384K maximum output. DeepSeek reports GPQA Diamond 90.9, Terminal-Bench 2.1 90.6 and DeepSWE v1.1 74.2 (vendor-reported). Off-peak API pricing is $0.15 input / $0.60 output per 1M tokens with $0.003 cache hits.

The same change log entry reversed the earlier statement that DeepSeek-V4-Pro requests would route to V4.1-Flash after 2026-09-14; V4-Pro API service now continues with unchanged billing (see the related news item).
