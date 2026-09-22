---
title: "Chinese AI APIs Compared: Six Official Platforms, One Convergence and a Few Real Differences"
description: "A comparison of the six official Chinese AI API platforms — DeepSeek, Ark, Model Studio, Moonshot, MiniMax and Z.ai — on authentication, protocol compatibility, model routing, regions and rate limits."
published_date: "2026-09-22"
updated_date: "2026-09-22"
research_question: "How do the six official Chinese AI API platforms differ in practice on authentication, protocol compatibility, model routing, regions and rate limits?"
related_entities:
  - deepseek-v4-pro
  - deepseek-v4-1-flash
  - doubao-seed-2-1-pro
  - doubao-seed-2-1-turbo
  - doubao-seed-evolving
  - glm-5.3
  - glm-5.3-flash
  - kimi-k3
  - kimi-k2.7-code
  - minimax-m3
  - minimax-m2.7
  - qwen3.8-max
  - qwen3.8-flash
author_view: true
image: "/images/cc/code-screen.jpg"
image_credit: "Sai Kiran Anagani / CC0, via Wikimedia Commons"
image_source: "https://commons.wikimedia.org/wiki/File:CSS_code_on_a_screen_(Unsplash).jpg"
sources:
  - source_name: "DeepSeek API docs"
    source_url: "https://api-docs.deepseek.com/"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Volcengine Ark — product overview"
    source_url: "https://docs.volcengine.com/docs/ark/product-overview?lang=zh"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Alibaba Cloud Model Studio — OpenAI-compatible API"
    source_url: "https://www.alibabacloud.com/help/en/model-studio/compatibility-of-openai-with-dashscope"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Moonshot AI — Kimi API overview"
    source_url: "https://platform.kimi.ai/docs/api/overview.md"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "MiniMax API — Anthropic-compatible API"
    source_url: "https://platform.minimax.io/docs/api-reference/text-anthropic-api.md"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Z.ai docs — Quick Start"
    source_url: "https://docs.z.ai/"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

All facts in this article come from the China AI Hub API database (six platforms, last verified 2026-09-20) and the official documentation linked at the bottom. Rate limits and features are quoted from vendor docs as of the verification date and change frequently; re-check before building.

## Executive Summary

The six official Chinese AI API platforms — DeepSeek, Volcengine Ark (ByteDance), Model Studio (Alibaba), Moonshot (Kimi), MiniMax and Z.ai (Zhipu) — have converged on OpenAI compatibility: every one of them exposes an OpenAI-style Chat Completions endpoint, and four also expose the newer Responses API, four an Anthropic-compatible endpoint. The real differences are narrower and more operational: how authentication keys are scoped (region-bound at Alibaba, AK/SK at Ark, ANTHROPIC_API_KEY-style at MiniMax), which regions are served (from "not stated" at DeepSeek and Moonshot to six named regions at Alibaba), and whether the platform routes third-party models (Ark hosts DeepSeek and GLM; the others serve only their own family).

## What We Know

The six platforms and their headline properties:

- **DeepSeek API** — `api.deepseek.com`, Bearer API key, OpenAI-compatible plus a native Responses API and an Anthropic-compatible endpoint at `/anthropic`. Serves only DeepSeek models (V4-Pro and V4.1-Flash). Peak/off-peak pricing.
- **Volcengine Ark** — `ark.cn-beijing.volces.com/api/v3`, Bearer API key plus AK/SK, Responses API and OpenAI-compatible Chat API. Serves the Doubao Seed family and also hosts third-party models including DeepSeek and GLM.
- **Model Studio** — `dashscope-us.aliyuncs.com/compatible-mode/v1`, region-bound `DASHSCOPE_API_KEY`, OpenAI-compatible. Serves the Qwen family across six named regions.
- **Moonshot (Kimi)** — `api.moonshot.ai/v1`, `MOONSHOT_API_KEY` Bearer, OpenAI Chat Completions, Responses and an Anthropic-compatible Messages endpoint. Serves the Kimi K-series.
- **MiniMax** — `api.minimax.io/anthropic`, API key passed `ANTHROPIC_API_KEY`-style, Anthropic-compatible plus OpenAI endpoints. Serves the M-series.
- **Z.ai** — `api.z.ai/api/paas/v4/chat/completions`, Bearer API key, OpenAI-compatible (plus Responses and Anthropic protocols for GLM-5.3). Serves the GLM family.

## What the Data Shows

**Protocol compatibility is the convergence.** OpenAI Chat Completions is universal. The Responses API is supported by DeepSeek, Ark, Model Studio and Moonshot. An Anthropic-compatible endpoint exists at DeepSeek, MiniMax, Moonshot and Z.ai (for GLM-5.3). This means a developer standardized on OpenAI SDKs can reach all six platforms with minimal changes, and one standardized on the Anthropic SDK can reach four of them.

**Authentication splits into three scoping models.** Most platforms use a single Bearer key. Alibaba's Model Studio makes keys region-bound — a key created for one region does not cross to another. Ark offers AK/SK access-key authentication in addition to the Bearer key. MiniMax asks developers to pass the key through the `ANTHROPIC_API_KEY` convention, which makes it a drop-in for Anthropic clients.

**Region coverage is the sharpest divide.** Model Studio lists six regions (Beijing, Singapore, Hong Kong, Tokyo, US Virginia, Frankfurt). Ark serves China (cn-beijing). MiniMax and Z.ai serve both international and China endpoints. DeepSeek and Moonshot do not state serving regions in official documentation — a material gap for data-residency or latency planning.

**Model routing separates Ark from the rest.** Ark is the only platform in the set that hosts third-party models (DeepSeek and GLM) alongside its own Doubao family. The other five are single-vendor. This makes Ark the closest thing to a Chinese model router in the official-platform category.

**Rate limits differ by an order of magnitude.** Ark's flagship Doubao models are documented at 500 RPM / 1,000,000 TPM. Model Studio's global regions are documented at 30,000 RPM / 5,000,000 TPM for qwen3.8-max and qwen3.8-flash (Beijing and Singapore limits are dynamic, tiered by spend). DeepSeek publishes concurrency limits rather than RPM (2,500 for V4.1-Flash, 500 for V4-Pro).

## What Has Changed

Two shifts stand out relative to the earlier generation of Chinese APIs. First, the Responses API and Anthropic compatibility have spread — the market is no longer "OpenAI-compatible or nothing." DeepSeek, Moonshot and Z.ai now offer multiple protocol surfaces, which lowers migration cost and reflects competition for developers already invested in a non-OpenAI stack. Second, Ark's hosting of third-party models means the boundary between "a lab's API" and "a multi-model marketplace" has begun to blur — a lab is now reselling a rival's models, which is a structural change, not an incremental one.

## Why It Matters

For a developer or enterprise choosing an API, the comparison matters because the cost of the *wrong* choice is a rewrite, not a configuration change. Three practical questions follow from the data. First, where does inference need to run? If data residency requires a specific region, only Model Studio, MiniMax and Z.ai document that choice; DeepSeek and Moonshot leave it unanswered in official docs. Second, which SDK are you standardized on? OpenAI compatibility gets you everywhere; Anthropic compatibility reaches four of six. Third, do you need one platform to serve multiple vendors? Only Ark does that today, and it does so at the cost of being a China-region, Volcengine-bound service.

## Detailed Analysis

We read three structural patterns.

**Pattern one: compatibility is table stakes, differentiation is operational.** Every platform has OpenAI compatibility, so it cannot be a differentiator. What differs is the *shape* of the key, the *scope* of the region, and the *granularity* of the rate limit — all operational details that surface only when a workload scales or a compliance requirement appears.

**Pattern two: Alibaba is the global-first platform.** Six named regions, region-bound keys, the highest documented rate limits (30,000 RPM / 5,000,000 TPM globally), and a managed product at qwencloud.com. Alibaba's cloud-distribution background shows in the API design. ByteDance's Ark is the inverse — a single cn-beijing region, which reflects a domestic-first posture.

**Pattern three: MiniMax and Moonshot optimize for migration.** MiniMax's Anthropic-style auth and endpoint, and Moonshot's triple protocol surface (OpenAI + Responses + Anthropic), are both designed to let a developer point an existing Anthropic or OpenAI client at a Chinese model with a one-line base-URL and key change. This is an acquisition strategy, not a technical coincidence.

## Comparison / Evidence

| Platform | Auth | Regions | Protocols | Third-party models |
|---|---|---|---|---|
| DeepSeek | Bearer key | Not stated | OpenAI + Responses + Anthropic | No |
| Ark | Bearer + AK/SK | China (cn-beijing) | Responses + OpenAI Chat | Yes (DeepSeek, GLM) |
| Model Studio | Region-bound key | 6 regions | OpenAI (+ Anthropic on qwen3.8-flash) | No |
| Moonshot | Bearer key | Not stated | OpenAI + Responses + Anthropic | No |
| MiniMax | ANTHROPIC_API_KEY-style | International + China | Anthropic + OpenAI | No |
| Z.ai | Bearer key | International + China | OpenAI (+ Responses/Anthropic on GLM-5.3) | No |

Two caveats on the evidence. First, "not stated" for regions is itself a finding — it is not a claim that DeepSeek or Moonshot runs nowhere, only that official documentation does not disclose it. Second, rate-limit numbers are not directly comparable across platforms because they are expressed in different units (RPM/TPM versus concurrency), so we report them rather than rank them.

## Limitations and Uncertainty

The database records capabilities and limits as published by each vendor on 2026-09-20; several are documented incompletely. Structured-output support is recorded as null at MiniMax and Z.ai, meaning it is neither confirmed nor denied by the sources we verified, not that it is absent. The Ark third-party model list may be incomplete — the database records DeepSeek and GLM as hosted, but the exact set of third-party models on Ark is subject to change. And rate limits, pricing and region coverage are all moving targets; the authoritative source is each platform's live documentation.

## China AI Hub View

Our view: for most international developers, the practical shortlist is DeepSeek, Model Studio and Z.ai — DeepSeek for price and permissive licensing, Model Studio for region coverage and throughput, Z.ai for GLM's balance. Ark matters mainly if you need a single platform to reach multiple Chinese model families from within China. MiniMax and Moonshot are best for teams already invested in the Anthropic SDK or in long-context workloads respectively. The deeper point is that the Chinese API market has reached the same state as the model market: the interfaces have converged, so the decision is now about the operational details — key scoping, region disclosure, rate limits and routing — that no benchmark table captures.

## Conclusion

The six official Chinese AI API platforms have converged on OpenAI compatibility (all six) and increasingly on the Responses and Anthropic protocols (four each), which collapses the interface question and pushes the real decision onto operational specifics: region coverage (from "not stated" to six regions), key scoping (region-bound at Alibaba, AK/SK at Ark), model routing (Ark's third-party hosting), and rate limits that span an order of magnitude. The choice of API platform, like the choice of model, is now a decision about price, region and license — not about which vendor's SDK you must learn.
