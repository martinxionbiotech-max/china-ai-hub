---
title: "Open-Weight vs API: Trade-offs for Chinese Models"
description: "A practical guide to choosing between open-weight self-hosting and API access for Chinese AI models, using license data and prices from the China AI Hub database."
published_date: "2026-09-22"
updated_date: "2026-09-22"
related_entities:
  - deepseek-v4-pro
  - glm-5.3
  - kimi-k3
  - minimax-m3
  - qwen3.8-max
sources:
  - source_name: "China AI Hub — Models database"
    source_url: "https://chinaaihub.com/models/"
    source_type: independent
  - source_name: "DeepSeek — V4.1-Flash announcement"
    source_url: "https://www.deepseek.com/en/news/deepseek-v4-1-flash/"
    source_type: official
  - source_name: "Z.ai — GLM-5 (GitHub)"
    source_url: "https://github.com/zai-org/GLM-5"
    source_type: official
---

The Chinese model ecosystem offers a genuine choice: some flagships are API-only, others ship open weights. This guide lays out the trade-offs using database fields (last verified 2026-09-22).

## The two paths

- **API**: you pay per token, the provider runs everything. Qwen3.8-Max ($2.00/$6.00) and Doubao Seed 2.1 Pro ($6.00/$30.00) are API-only in our database.
- **Open weight**: you download the weights and serve them yourself. DeepSeek-V4-Pro (MIT), V4.1-Flash (MIT), GLM-5.3 (Apache-2.0), Kimi K3 (custom), MiniMax M3 (community) are all open weight.

## When the API wins

- You need capability immediately and lack serving infrastructure.
- Your volume is low or bursty; fixed infrastructure costs would dominate.
- You want the vendor's latest updates without re-deploying.
- You cannot satisfy the license obligations of the open-weight option.

At the database's listed prices, the budget tier is aggressive: $0.15/1M input with $0.50-$0.60 output (GLM-5.3-Flash, DeepSeek-V4.1-Flash). Self-hosting rarely beats that below substantial, steady volume.

## When open weights win

- Data residency or regulatory constraints require on-premises inference.
- Steady, predictable volume makes GPU costs amortize below API prices.
- You need to fine-tune or modify the model (licenses permitting).
- You need deterministic, offline capability.

Self-hosting economics: a 4-bit quantized 30B-class open model runs on a single high-memory GPU; frontier-scale open models need clusters. Quantization is the standard route — and its quality is your responsibility to evaluate.

## Licenses are the fine print

"Open weight" is not one legal category in this ecosystem:
- **MIT** (DeepSeek V3.2/V4-Pro/V4.1-Flash): least restrictive.
- **Apache-2.0** (GLM-5.x): permissive with patent grant.
- **Kimi K3 License**: MIT-style, but Model-as-a-Service operators above $20M revenue must sign a separate agreement; >100M MAU products must display the name.
- **MiniMax Community License**: non-commercial free; commercial use needs attribution plus authorization above revenue thresholds.
- **Qwen3.8-2.4T-A95B**: custom MIT-style with scale-triggered obligations.

A license that is permissive at your scale may not be at your customer's scale. Review the exact text before shipping.

## The hybrid reality

Most serious deployments run both: open-weight models for sensitive or steady workloads, APIs for spikes and frontier capability. The database fields to compare are open_weight, license, self_hosting, api_available and the pricing tables — all of which you can filter on the models page.

## Bottom line

Choose the API when you need speed and simplicity; choose open weights when you need control, residency or fine-tuning — and read the license before you build.
