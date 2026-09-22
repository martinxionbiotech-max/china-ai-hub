---
title: "DeepSeek reverses V4-Pro retirement and keeps the API service running"
description: "The 2026-09-10 change log says DeepSeek-V4-Pro API service continues past the earlier 09-14 cutoff 'in response to user demand', with billing unchanged."
published_date: "2026-09-10"
type: company
trigger_updates:
  - deepseek-v4-pro
sources:
  - source_name: "DeepSeek API Change Log — 2026-09-10"
    source_url: "https://api-docs.deepseek.com/updates"
    source_type: official
    published_date: "2026-09-10"
    confidence: high
---

On 2026-09-10 the DeepSeek API change log reversed an earlier statement that DeepSeek-V4-Pro requests would be answered by V4.1-Flash from 04:00 UTC on 2026-09-14. The updated text states DeepSeek V4-Pro API service now continues past that date "in response to user demand", with the billing method remaining unchanged; V4-Flash and V4-Flash-Vision-Exp are genuinely retired.

This resolves a conflict the database had flagged: the DeepSeek news page and the change log previously disagreed on whether V4-Pro API service would continue. The model remains listed as deprecated in the database, with off-peak pricing of $0.66 input / $1.98 output per 1M tokens.
