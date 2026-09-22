---
title: "Chinese AI Model Licensing Explained: MIT, Apache and the Three Custom Regimes"
description: "A plain-language breakdown of the five license regimes behind China's open-weight frontier models — MIT, Apache-2.0, and the conditional Kimi, MiniMax and Qwen licenses — with the exact revenue and MAU thresholds that trigger obligations."
published_date: "2026-09-22"
updated_date: "2026-09-22"
research_question: "How do the licenses on China's open-weight frontier models actually differ, and what revenue or usage thresholds change what a commercial adopter owes?"
related_entities:
  - deepseek-v4-pro
  - deepseek-v4-1-flash
  - glm-5.3
  - glm-5.3-flash
  - kimi-k3
  - minimax-m3
  - minimax-m2.7
  - qwen3.8-2.4t-a95b
author_view: true
image: "/images/cc/ai-chip.webp"
image_credit: "mikemacmarketing / CC BY 2.0, via Wikimedia Commons"
image_source: "https://commons.wikimedia.org/wiki/File:Artificial_Neural_Network_with_Chip.jpg"
sources:
  - source_name: "Hugging Face — DeepSeek-V4-Pro model card (MIT)"
    source_url: "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Hugging Face — DeepSeek-V4.1-Flash model card (MIT)"
    source_url: "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "GitHub — zai-org/GLM-5 (Apache-2.0 repo metadata)"
    source_url: "https://github.com/zai-org/GLM-5"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "GitHub — MoonshotAI/Kimi-K3 (Kimi K3 License)"
    source_url: "https://github.com/MoonshotAI/Kimi-K3"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Hugging Face — MiniMax-M3 model card (Community License)"
    source_url: "https://huggingface.co/MiniMaxAI/MiniMax-M3"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Hugging Face — MiniMax-M2.7 model card (custom non-commercial license)"
    source_url: "https://huggingface.co/MiniMaxAI/MiniMax-M2.7"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Hugging Face — Qwen3.8-2.4T-A95B license file (Qwen3.8-Max License)"
    source_url: "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

Every licensing fact in this article comes from the China AI Hub model database (19 models, last verified 2026-09-20) and the primary license sources linked at the bottom. This is not legal advice; license thresholds are quoted from vendor statements and should be re-checked against the license file in the specific model repository before any commercial decision.

## Executive Summary

China's open-weight frontier models do not share a single license. The China AI Hub database records five distinct regimes across the open-weight catalog: MIT (DeepSeek), Apache-2.0 (Zhipu GLM), and three custom "MIT-style" licenses with escalating conditions — the Kimi K3 License, the MiniMax Community License, and the Qwen3.8-Max License. The practical difference is not "open vs closed" but *what a commercial user owes once they cross a revenue or scale threshold*. DeepSeek's MIT asks for nothing. The custom licenses ask for attribution, then authorization, at thresholds ranging from $20M in annual revenue (MiniMax M3) to $50M in trailing-twelve-month revenue for Model-as-a-Service businesses (Qwen).

## What We Know

The database classifies 11 of 19 models as open-weight, 5 as proprietary, and 3 (the Kimi K2.x series) as undisclosed. The open-weight licenses break into five buckets:

- **MIT — DeepSeek.** V3.2, V4-Pro and V4.1-Flash all carry MIT with no revenue trigger, no attribution mandate and no Model-as-a-Service carve-out.
- **Apache-2.0 — Zhipu.** GLM-5.2, GLM-5.3 and GLM-5.3-Flash are Apache-2.0 per the GitHub repo metadata. The database adds a caveat: the repo README has no separate weights-license section, so adopters should verify each model's Hugging Face card before reuse.
- **Kimi K3 License — Moonshot.** A permissive, MIT-style license with two named triggers (details below).
- **MiniMax Community License — MiniMax M3.** Free for non-commercial use; commercial use requires attribution plus conditional authorization.
- **Qwen3.8-Max License — Alibaba.** A custom MIT-style license governing the open Qwen3.8-2.4T-A95B weights, with display and MaaS triggers.

There is a sixth and seventh category worth naming explicitly: MiniMax's M2.7 family uses a *stricter* custom non-commercial license (not the same as the M3 Community License), and the proprietary models — Doubao Seed 2.1 (Pro/Turbo/Evolving), Qwen3.8-Flash and Qwen3.8-Max (the API flagships) — are closed, with no downloadable weights at all.

## What the Data Shows

The thresholds are the heart of the matter. The database records these obligations verbatim:

**Kimi K3 License** — two triggers: Model-as-a-Service operators with more than $20M in aggregate revenue over any 12-month period must sign a separate agreement with Moonshot; and products with more than 100M monthly active users, or more than $20M in monthly revenue, must display "Kimi K3" in the user interface.

**MiniMax Community License (M3)** — commercial use requires prominent "Built with MiniMax M3" attribution, plus written authorization from MiniMax if yearly revenue exceeds $20M; below that threshold, a one-time notice to api@minimax.io suffices.

**MiniMax M2.7 custom license** — the strictest in the set: MIT-style terms for *non-commercial use only*; any commercial use requires prior written authorization from MiniMax.

**Qwen3.8-Max License** — unrestricted use, copy, modification and sale; but products above 100M MAU or $20M/month revenue must display the model name, and Model-as-a-Service or AI Work Assistant businesses above $50M in 12-month revenue need a separate license from Qwen.

**MIT (DeepSeek) and Apache-2.0 (Zhipu)** — no such triggers in the database record.

Notice the structural similarity across the three custom licenses: each preserves permissive everyday use but attaches an obligation that scales with revenue, MAU, or the MaaS business model. The differences are in *where* the line is drawn — $20M/year (MiniMax) versus $20M/12-months-for-MaaS (Kimi) versus $50M/12-months-for-MaaS (Qwen) — and in *what* is owed (attribution, a notice, a separate agreement, or prior authorization).

## What Has Changed

The licensing landscape has shifted from a binary to a spectrum. The earlier generation of Chinese open models trended toward straightforward MIT or Apache releases. What the 2026 database shows is the emergence of the *conditional permissive* license — a category that did not exist as a distinct pattern in the earlier wave. Three of the six labs (Moonshot, MiniMax, Alibaba) now ship open weights under custom terms that read like MIT plus a monetization guardrail. DeepSeek and Zhipu are the holdouts that still ship standard permissive licenses. This matters because it means "open weights" no longer implies "I can build a business on this without ever talking to the lab again" — for the conditional licenses, scale eventually triggers a conversation.

## Why It Matters

For a buyer or builder, the license is a cost and a risk that does not appear on any pricing page. Two consequences follow from the data.

First, the *floor* is DeepSeek's MIT. Any lab that asks for more than MIT — attribution, authorization, revenue reporting — must justify it with capability, price or ecosystem advantages, because an adopter can always fall back to a DeepSeek model and owe nothing.

Second, the thresholds are low enough to be real, not theoretical. A $20M annual revenue trigger is well within reach of a successful vertical SaaS product built on a Chinese open model. A company that hits the Kimi K3 MaaS trigger or the Qwen $50M/12-month MaaS trigger without having budgeted for a separate license negotiation has created an unplanned commercial dependency. The license, in other words, is part of the total cost of ownership, and it activates precisely at the moment a business starts succeeding.

## Detailed Analysis

We separate the five regimes into three tiers by commercial friction.

**Tier 1 — Zero friction.** MIT (DeepSeek) and, with a verification caveat, Apache-2.0 (Zhipu). These are the only licenses a large enterprise can clear without bespoke negotiation. The Apache-2.0 caveat is important: the database flags that Zhipu's license is read from repo metadata rather than a dedicated weights-license file, which means a rigorous procurement process must still confirm the license applies to the actual weight artifacts, not just the code repository.

**Tier 2 — Attribution-then-threshold.** The Kimi K3 License and Qwen3.8-Max License. Everyday use is permissive, but crossing a scale threshold adds an obligation — display the model name (Kimi at >100M MAU or >$20M/month; Qwen at the same display threshold) and, for MaaS businesses, negotiate a separate agreement (Kimi at >$20M/12-months, Qwen at >$50M/12-months). The display requirement is a subtle marketing extraction: the lab trades permissive terms for brand visibility at scale.

**Tier 3 — Non-commercial-or-authorize.** MiniMax's two licenses. The M3 Community License is the softer of the two — commercial use is allowed with attribution, escalating to written authorization above $20M/year. The M2.7 license is the hardest line in the entire open-weight set: commercial use of any kind requires prior written authorization. An adopter who treats M2.7 as "open source" and ships it in a commercial product is in breach from day one, not at some future revenue threshold.

## Comparison / Evidence

The side-by-side is the clearest way to see the differences:

| License | Models | Commercial use allowed? | Trigger for extra obligation |
|---|---|---|---|
| MIT | DeepSeek V3.2 / V4-Pro / V4.1-Flash | Yes, unrestricted | None |
| Apache-2.0 | GLM-5.2 / 5.3 / 5.3-Flash | Yes, unrestricted | None (verify per-card) |
| Kimi K3 License | Kimi K3 | Yes | >$20M/12mo (MaaS) → agreement; >100M MAU or >$20M/mo → UI display |
| MiniMax Community | MiniMax M3 | Yes, with attribution | >$20M/yr → written authorization (else one-time notice) |
| MiniMax M2.7 custom | M2.7 / M2.7-Highspeed | No (non-commercial only) | Any commercial use → prior authorization |
| Qwen3.8-Max License | Qwen3.8-2.4T-A95B | Yes, unrestricted | >100M MAU or >$20M/mo → display; >$50M/12mo (MaaS) → separate license |

A notable asymmetry: the *open-weight* Qwen model (Qwen3.8-2.4T-A95B) carries the conditional Qwen license, while the *API* flagships (Qwen3.8-Flash, Qwen3.8-Max) are closed and proprietary. Alibaba thus runs a dual strategy: permissive-enough open weights for the developer ecosystem, and a closed, priced API for the monetized flagship. ByteDance runs the purest closed strategy — all three Doubao models are proprietary with no open weights in the database.

## Limitations and Uncertainty

The license strings in the database are transcribed from vendor sources and dated 2026-09-20; licenses can and do change between releases, and the exact legal text in a specific repository or Hugging Face card is the authoritative document. The database's own flags must be carried forward: Zhipu's Apache-2.0 is sourced from repo metadata with no dedicated weights-license section, and the MiniMax terms are summarized from platform documentation rather than a standalone LICENSE file. We have not performed legal review, and none of this substitutes for one. Finally, the "undisclosed" status of the three Kimi K2.x models means the open-weight picture is not complete — Moonshot has not published weights or license terms for K2.6 and K2.7-Code in the sources we verified.

## China AI Hub View

Our view: the meaningful divide in Chinese model licensing is no longer open versus closed, but *MIT versus conditional-permissive*. DeepSeek's MIT is the reference point that makes every conditional license a deliberate choice rather than a default. The conditional licenses are not anti-developer — they preserve permissive everyday use — but they are a bet that the lab, not the downstream builder, should capture a share of value at the point where a business built on the weights becomes large. The practical advice that follows from the data is specific: if you are a Model-as-a-Service operator, the Kimi K3 ($20M/12mo) and Qwen ($50M/12mo) triggers are the ones to track before you choose weights; if you want zero licensing friction at any scale, only DeepSeek's MIT and (subject to verification) Zhipu's Apache-2.0 deliver that today.

## Conclusion

Chinese AI model licensing in 2026 spans five regimes — MIT, Apache-2.0, and three conditional custom licenses — whose real-world difference is the revenue, MAU and MaaS thresholds that convert a free permissive license into a negotiation. DeepSeek's unconditional MIT is the benchmark against which the conditional licenses are measured, and the thresholds (from MiniMax's $20M/year to Qwen's $50M/12-months for MaaS) are low enough that they will bind real businesses, not hypothetical ones. Anyone choosing a Chinese open-weight model should treat the license file as part of the specification and read it before the pricing page, because the pricing page never shows what the license will cost at scale.
