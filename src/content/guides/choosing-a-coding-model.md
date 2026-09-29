---
image: "/images/ai/models-deepseek-v4-pro.webp"
image_credit: "AI-generated illustration (Seedream)"
title: "Choosing a Chinese Coding Model: SWE Evidence, Tool Calling and Context"
description: "A decision guide for selecting a Chinese model for software engineering — reading Terminal-Bench, DeepSWE and SWE-bench evidence, and matching tool-calling and context requirements to the right model and coding agent."
published_date: "2026-09-29"
updated_date: "2026-09-29"
related_entities:
  - deepseek-v4-1-flash
  - deepseek-v4-pro
  - glm-5.3
  - glm-5.3-flash
  - kimi-k3
  - minimax-m3
  - qwen3.8-max
  - kimi-code
  - qwen-code
  - qoder
  - deepseek-harness
  - glm-coding-plan
  - terminal-bench
  - deepswe
  - swe-bench
sources:
  - source_name: "China AI Hub — Models database"
    source_url: "https://sinoaihub.com/models/"
    source_type: independent
  - source_name: "China AI Hub — Agents database"
    source_url: "https://sinoaihub.com/agents/"
    source_type: independent
  - source_name: "DeepSeek API Change Log"
    source_url: "https://api-docs.deepseek.com/updates"
    source_type: official
  - source_name: "Z.ai — GLM-5.3 model page"
    source_url: "https://docs.z.ai/guides/llm/glm-5.3"
    source_type: official
---

**Short answer.** For repository-scale software engineering, the highest vendor-reported agentic-coding scores in the database belong to DeepSeek-V4.1-Flash (Terminal-Bench 2.1 = 90.6, DeepSWE v1.1 = 74.2) and DeepSeek-V4-Pro (87.9 / 62.7), with GLM-5.3 close behind on DeepSWE (66.9) and far ahead on security tasks (CyberGym 84.5). Kimi K3 leads the general-capability picture (Terminal-Bench 2.1 = 88.3, DeepSWE = 67.5, GPQA Diamond 93.5). Every coding number here is vendor-reported and several sit on incompatible benchmark versions — so the honest selection procedure is: pick the agent you will actually run, then match its underlying model to your context and output needs, and verify the scores' benchmark version before comparing across vendors.

## Decision criteria

Match your requirement to the field that actually decides it. All figures below are from the China AI Hub database (last verified 2026-09-20) and are vendor-reported unless stated.

| Criteria | Relevance / Notes |
|---|---|
| Terminal-Bench 2.1 score | Terminal/agent task completion; V4.1-Flash 90.6, V4-Pro 87.9, Kimi K3 88.3, Qwen3.8-Max 86.6, MiniMax-M3 66.0 — but GLM-5.3's 28.3 is on Terminal-Bench **3.0**, a different version |
| DeepSWE score | Repository-scale SWE; V4.1-Flash 74.2 (v1.1), GLM-5.3 66.9 (v1.1), Kimi K3 67.5, GLM-5.3-Flash 63.4 (v1.1), V4-Pro 62.7 |
| SWE-bench variant | "SWE-bench" is three tests: Verified (Kimi K2.5 76.8), Pro (Qwen3.8-Max 67.7, MiniMax-M3 59.0, GLM-5.2 62.1), Multilingual — never compare across variants |
| Tool calling | Present on V4.1-Flash, V4-Pro, Qwen3.8-Max, Kimi K3, MiniMax-M3, GLM-5.3 |
| Context window | 1M on V4.1-Flash, V4-Pro, GLM-5.3, GLM-5.3-Flash, Kimi K3, Qwen3.8-Max, MiniMax-M3; 256K on Kimi K2.7-Code |
| Maximum output | DeepSeek 393,216; GLM/Qwen 131,072; Kimi K3 1,048,576 — decides whole-repo rewrite headroom |
| Vision input | Only on the flash/consumer tiers (V4.1-Flash, GLM-5.3-Flash, Kimi K3); V4-Pro and GLM-5.3 are text-only |
| Open weights | MIT (DeepSeek), Apache-2.0 (Zhipu), conditional (Kimi K3) — matters if you must self-host |

## Entity routing

Route by the shape of the job, not by a single leaderboard number.

| Scenario | Best-documented fit | Why |
|---|---|---|
| Whole-repo agentic coding on DeepSeek | [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/) | Current `deepseek-flash` endpoint, 1M context, 393K output, TB 2.1 = 90.6 |
| Legacy DeepSeek checkpoints | [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) | Deprecated; TB 2.1 = 87.9, MIT open weights |
| Text-only flagship, security tasks | [GLM-5.3](/models/glm-53/) | CyberGym 84.5, DeepSWE 66.9, Apache-2.0 |
| Visual coding loops + computer use | [GLM-5.3-Flash](/models/glm-53-flash/) | Vision + video + computer-use flags at $0.15 |
| Long-output whole-repo generation | [Kimi K3](/models/kimi-k3/) | 1M/1M context-output; TB 2.1 = 88.3, DeepSWE = 67.5 |
| Multi-model / multi-protocol routing | [Qwen Code](/agents/qwen-code/) or [Qoder](/agents/qoder/) | Cross-vendor model routing |
| Budget coding, 1M context, flash price | [Qwen3.8-Flash](/models/qwen38-flash/) or [GLM-5.3-Flash](/models/glm-53-flash/) | $0.15 input, 1M context |

Relevant comparisons: [DeepSeek-V4-Pro vs Qwen3.8-Max](/comparisons/deepseek-v4-pro-vs-qwen38-max/), [Kimi K3 vs Kimi K2.7-Code](/comparisons/kimi-k3-vs-kimi-k27-code/), [GLM-5.3 vs GLM-5.3-Flash](/comparisons/glm-53-vs-glm-53-flash/), [Qwen3.8-Max vs GLM-5.3](/comparisons/qwen38-max-vs-glm-53/).

## What the evidence shows

The benchmark layer records a numbers race with a version trap at its center. DeepSeek-V4.1-Flash, DeepSeek-V4-Pro, Kimi K3 and Qwen3.8-Max all publish Terminal-Bench **2.1** scores clustered between 86 and 91 — a genuinely contested leaderboard. GLM-5.3 and GLM-5.2 publish on Terminal-Bench **3.0** (28.3 and 4.6 respectively), which is not comparable to the 2.1 figures and the database deliberately labels the version rather than merging rows. The same split runs through SWE-bench, where "Verified," "Pro" and "Multilingual" name different tests with different difficulty.

On the repository-scale dimension, DeepSWE is the most consistent cross-vendor signal and it clusters tightly: V4.1-Flash 74.2, Kimi K3 67.5, GLM-5.3 66.9, GLM-5.3-Flash 63.4, V4-Pro 62.7. The general-reasoning coding support is strong too — Kimi K3 posts GPQA Diamond 93.5 and Qwen3.8-Max 92.6, which matters because real coding is a mix of recall, reasoning and tool orchestration, not a single leaderboard. GLM-5.3's CyberGym 84.5 stands out as the strongest security-task signal in the collection, though it too is vendor-reported.

The product layer is where the practical decision actually lives. Five of six frontier labs field a coding agent, and the competitive axis has moved from "highest score" to "which agent, at what price, with which tooling." Four agents are open source ([Kimi Code](/agents/kimi-code/), [MiniMax Code](/agents/minimax-code/), [Qwen Code](/agents/qwen-code/), [DeepSeek Harness](/agents/deepseek-harness/)); two are closed subscriptions ([GLM Coding Plan](/agents/glm-coding-plan/) from $18/month international, Qoder Pro $20/month). A model's coding score only matters through the agent that calls it — and most agents are bound to their vendor's own models, which is why the model and agent choices are usually one decision, not two.

China AI Hub analysis indicates the coding market is where Chinese labs are converging fastest, and the convergence is on product form, not performance claims: four open-source terminal agents plus two commercial subscriptions competing on billing mechanics is a maturing market, while the benchmark noise — version splits, variant cherry-picking, absent scores — is a symptom of how immature the measurement layer remains.

## Selection procedure

Work through these steps in order, and stop at the first one that settles the choice.

1. **Pick the agent first, not the model.** Coding scores only matter through the agent that calls them, and most agents are bound to their vendor's models. If you will run [Kimi Code](/agents/kimi-code/), your model is Kimi K3 or K2.7-Code; if you will run [GLM Coding Plan](/agents/glm-coding-plan/), your model is GLM-5.3 or GLM-5.3-Flash. Decide the tool, and the model follows.
2. **If you need model freedom, shortlist Qwen Code or Qoder.** These are the only two cross-vendor agents — Qwen Code open and multi-protocol, Qoder closed and credit-tier-routing. Everything else is single-vendor.
3. **Check the benchmark version before comparing.** A Terminal-Bench 2.1 score (DeepSeek, Kimi, Qwen) is not comparable to a Terminal-Bench 3.0 score (GLM). SWE-bench "Verified" is not SWE-bench "Pro" is not "Multilingual." If two numbers carry different versions, they are not a ranking.
4. **Match output headroom to the deliverable.** Whole-repo rewrite or long generated diffs need the 393K–1M output ceiling (DeepSeek, Kimi K3); code review and summarization need only the 131K tier.
5. **Decide vision before you commit to a flagship.** If your coding loop includes screenshots or UI work, V4-Pro and GLM-5.3 are text-only — you want V4.1-Flash, GLM-5.3-Flash or Kimi K3.
6. **Verify the number against your own task.** Run a small private eval on ten of your real cases; the vendor numbers are a filter, not a decision.

## Limitations

Every coding benchmark score in the database is vendor-reported and carries no independent re-measurement. Benchmark versions are not comparable across vendors when they differ (Terminal-Bench 2.1 vs 3.0, SWE-bench Verified vs Pro vs Multilingual). Several vendors do not publish on some benchmarks, so an absent score is a coverage gap, not evidence of absence — Qwen3.8-Flash and Kimi K2.7-Code publish zero benchmark rows despite being coding-positioned products. Agent products themselves have no independent evaluation data in the database at all. DeepSeek-V4-Pro's deprecation status is itself conflicting across official pages — resolve it against the current change log before committing a production integration. For your own decision, run a small private eval on your real task; ten of your own cases beat a thousand vendor numbers.

## Sources

- [DeepSeek API Change Log](https://api-docs.deepseek.com/updates)
- [Z.ai — GLM-5.3 model page](https://docs.z.ai/guides/llm/glm-5.3)
- [Z.ai — GLM-5.3-Flash model page](https://docs.z.ai/guides/vlm/glm-5.3-flash)
- [China AI Hub — Models database](/models/) and [Agents database](/agents/)

*Labels used above: **Official fact** (pricing, licenses, context windows from primary sources), **Vendor-reported claim** (all benchmark scores, published by the model vendor and not independently re-measured), and **China AI Hub analysis** (our synthesis, introduced as such). No third-party benchmark evidence is currently recorded for the coding models in this guide.*
