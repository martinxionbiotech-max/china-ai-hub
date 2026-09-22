---
title: "GLM and Agent-Oriented AI: How Zhipu Built an Agent Stack Around Open Weights"
description: "An analysis of Zhipu AI's agent-oriented strategy: GLM-5.3 and GLM-5.3-Flash open weights with computer-use capability, the Open-AutoGLM phone agent, and the GLM Coding Plan subscription — and what the combination reveals about where Chinese AI vendors think value will concentrate."
published_date: "2026-09-22"
updated_date: "2026-09-22"
research_question: "How does Zhipu AI's GLM ecosystem operationalize agent-oriented AI, and what does the combination of open weights, a phone agent and a coding subscription reveal about the agent market in China?"
related_entities:
  - glm-5.2
  - glm-5.3
  - glm-5.3-flash
  - autoglm
  - glm-coding-plan
author_view: true
image: "/images/ai/models-glm-5.3.webp"
image_credit: "AI-generated illustration (Seedream)"
sources:
  - source_name: "Z.ai docs — GLM-5.3 model page"
    source_url: "https://docs.z.ai/guides/llm/glm-5.3"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Z.ai docs — GLM-5.3-Flash model page"
    source_url: "https://docs.z.ai/guides/vlm/glm-5.3-flash"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Z.ai pricing"
    source_url: "https://docs.z.ai/guides/overview/pricing"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "GLM-5 GitHub repository"
    source_url: "https://github.com/zai-org/GLM-5"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Open-AutoGLM GitHub repository"
    source_url: "https://github.com/zai-org/Open-AutoGLM"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "AutoGLM-Phone model docs (BigModel)"
    source_url: "https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "GLM Coding Plan docs (BigModel)"
    source_url: "https://docs.bigmodel.cn/cn/coding-plan/overview.md"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

# GLM and Agent-Oriented AI: How Zhipu Built an Agent Stack Around Open Weights

## Executive Summary

Zhipu AI is the only one of China's six frontier labs whose strategy is legible primarily through agents rather than models alone. The GLM ecosystem in September 2026 has four layers: open-weight foundation models with native computer-use capability (GLM-5.3, GLM-5.3-Flash/FlashX); an open-source phone-use agent (Open-AutoGLM, built on AutoGLM-Phone-9B); a commercial coding-agent subscription (GLM Coding Plan) that powers Zhipu's own ZCode and AutoClaw products plus 20+ third-party tools including Claude Code, Codex, Cursor and OpenClaw; and a dual-platform distribution structure (Z.ai internationally, BigModel in China). The distinctive claim in Zhipu's positioning is that agent capability is a property of the model tier itself — GLM-5.3-Flash ships with vision, video, computer-use and agent-capability flags — rather than a wrapper bolted onto a text model. This article examines how the four layers fit together, what the evidence supports, and what the model's limitations imply for anyone building agents on GLM.

## What We Know

The China AI Hub database records the GLM family as follows:

- **GLM-5.2** (2026-06-16): 744B total / 40B active parameters, 1M-token context, open weights (Apache-2.0), text-only, reasoning-only. Now deprecated but still listed on the API pricing page at the same price as GLM-5.3.
- **GLM-5.3** (2026-08-18): same base model as 5.2, 744B/40B, FP8 (BF16 also released), 1M context with 131K max output. All gains come from post-training. Reasoning is always enabled (low/high/max, default max) and cannot be disabled. Text-only input.
- **GLM-5.3-Flash / FlashX** (2026-08-26): 320B total / 18B active; described by Zhipu as the first open-source frontier model combining sparse and linear attention, with mHC hyper-connections and a 30T-token multimodal pre-training corpus. 1M context, 131K max output; vision, video, computer-use and agent-capability flags all true. Open weights, Apache-2.0 per repo metadata.

FACT: the 5.2 → 5.3 transition is a post-training-only upgrade on an unchanged base — an unusual, efficient release pattern worth noting on its own. The Flash model, by contrast, is a different architecture entirely (320B/18B sparse+linear), not a distilled 5.3.

**Agents:**

- **Open-AutoGLM**: an open-source phone-use agent framework (repo Open-AutoGLM). The VLM sees the phone screen, plans a chain-of-thought action sequence, and executes via ADB (Android), HDC (HarmonyOS NEXT) or WebDriverAgent (iOS). Zhipu dates its Phone Use capability to 2024-10-25 — the earliest phone agent in our database. The underlying model is AutoGLM-Phone-9B, built on the GLM-4.1V-9B family. Code is Apache-2.0, models MIT.
- **AutoGLM 2.0**: the commercial product running agents in cloud virtual phones; the AutoGLM-Phone API (BigModel model id autoglm-phone) is limited-time free as of 2026-09-20, with paid pricing not publicly disclosed.
- **GLM Coding Plan**: a subscription (China: bigmodel.cn/glm-coding) that powers ZCode (Zhipu's coding client), AutoClaw (office agent) and 20+ third-party coding tools. Runs on GLM-5.3 / GLM-5.3-Flash with 1M context. China pricing: Lite ¥118/mo, Pro ¥538/mo, Max ¥1078/mo with per-5-hour credits (2,000/12,000/28,000) plus weekly credits (10,000/60,000/140,000); team seats Standard ¥598 / Advanced ¥1198. International counterpart on Z.AI from $18/month.

## What the Data Shows

**The agent stack is unusually complete.** Most labs expose agent capability through an API or a single coding product. Zhipu exposes it at four levels: raw weights (GLM-5.3-Flash with computer_use true), a framework (Open-AutoGLM), a hosted service (AutoGLM 2.0 cloud phones), and a subscription (GLM Coding Plan). Each layer monetizes differently — weights are free, the framework is open source, the API is promotional-free, the subscription is paid. This is a deliberate funnel: open layers acquire developers, the subscription converts them.

**Agent benchmarks are present but modest and vendor-reported.** GLM-5.3 lists Terminal-Bench 3.0 at 28.3 accuracy, DeepSWE v1.1 at 66.9, Agents' Last Exam (CLI) at 28.5, and CyberGym at 84.5. GLM-5.3-Flash lists Artificial Analysis Intelligence Index v4.1.1 at 57, DeepSWE v1.1 at 63.4, and AutomationBench at 48.8. All scores are vendor-reported and not independently verified; Z.ai Code Bench, cited for the claimed 50% coding improvement from 5.2 to 5.3, is a private in-house benchmark. The database flags this explicitly: agent evaluation remains the least standardized part of the Chinese model ecosystem.

**Phone-agent constraints are carefully documented.** AutoGLM lists concrete boundaries: research/learning use only; sensitive pages (payment, password, banking) cannot be screenshotted and trigger human takeover; Android 7.0+ with developer mode required; local deployment needs roughly 24GB+ VRAM; no persistent memory in the README. The honest constraint list is itself evidence of a production-minded team — the limits are engineering facts, not marketing vagueness.

## What Has Changed

Three shifts are visible across the GLM record:

**From text-only to computer-use in one model generation.** GLM-5.2 (June) is text-only with no agent flags. GLM-5.3-Flash (August) ships with vision, video, computer-use and agent capability in a model that is simultaneously the cheapest GLM API tier ($0.15/$0.50). In the span of ten weeks, agent capability moved from the premium layer to the entry layer.

**The phone agent went from framework to cloud product.** AutoGLM 1.0 (2024) was a local framework for research; AutoGLM 2.0 runs agents in cloud virtual phones for batch operations — notifications, likes, customer-service and attendance workflows. Use cases listed span food ordering, cross-platform price comparison, travel planning and media control.

**Subscription pricing arrived with peak/off-peak mechanics.** The GLM Coding Plan applies the same temporal pricing logic as DeepSeek's API: off-peak costs 50% credits, peak (Mon-Fri 14:00-18:00 UTC+8) costs 2x. The plan revision is dated 2026-07-30; launch date is not publicly disclosed in the fetched sources.

## Why It Matters

Zhipu's structure answers a question the whole market is asking: where does agent value concentrate? Four implications:

- **For agent developers**: GLM-5.3-Flash is the only model in the China AI Hub collection whose cheapest tier carries the full agent-capability flag set (computer_use, vision, video). Building on it means the capability you prototype is the capability you can deploy at scale without switching to a premium tier.
- **For coding-tool vendors**: the GLM Coding Plan's 20+ third-party integrations (Claude Code, Codex, Cursor, OpenClaw) make GLM a drop-in backend for existing tools — but with quota caps and peak-hour multipliers, the effective cost depends on when your agents run.
- **For self-hosters**: open weights for both the flagship (GLM-5.3 FP8/BF16) and the agent-capable flash (GLM-5.3-Flash) mean the agent stack is self-hostable end to end — framework (Open-AutoGLM, Apache-2.0), models (MIT/Apache-2.0), and a local phone agent on ~24GB VRAM.
- **For buyers evaluating agent benchmarks**: the vendor-reported scores here (Terminal-Bench 28.3, DeepSWE 66.9, AutomationBench 48.8) cannot be compared across labs directly — evaluation conditions differ — which is why the China AI Hub benchmark collection tags every vendor-reported score explicitly.

ANALYSIS: the strategic insight is the funnel geometry. Zhipu gives away the weights and the framework, prices the flash API at the market floor, and monetizes only at the subscription layer — while simultaneously being the only lab whose cheapest model is agent-native. If agents are the next platform shift, Zhipu has positioned its cheapest, most open tier exactly where the shift is happening.

## Detailed Analysis

**Model layer.** GLM-5.3's post-training-only upgrade from 5.2 shows disciplined cost management — same 744B base, no retraining, claimed 50% coding improvement. The FP8 open release lowers self-hosting hardware cost versus BF16-only releases. The 1M context with 131K output is table stakes now, but the always-on reasoning (max by default, cannot be disabled) is a cost consideration: reasoning tokens bill as output at $4.40/1M, and there is no way to turn it off to save money.

**Agent layer.** Open-AutoGLM's architecture is worth understanding: the VLM sees the screen and emits planned action sequences executed through OS-level drivers (ADB/HDC/WDA). It is not a browser agent; it is a phone agent. The 24GB VRAM floor for local deployment and the sensitive-page handoff are the two constraints that define where it is deployable — development, research and cloud-phone batch workflows, not consumer payment flows.

**Subscription layer.** The GLM Coding Plan's credit economics (2,000/12,000/28,000 per 5 hours across Lite/Pro/Max, plus weekly pools) mean sustained usage is governed by credit refresh windows, not flat monthly tokens. The peak multiplier (2x, weekdays 14:00-18:00 Beijing) mirrors DeepSeek's API peak pricing — temporal arbitrage is now standard practice across both platforms. FlashX is not yet on the Coding Plan (pay-as-you-go only), and OpenClaw tasks run at secondary priority under load, subject to preemption by coding-agent tasks — a documented constraint that matters for anyone running long agent jobs on the plan.

**Distribution layer.** The dual structure — Z.ai (Singapore PTE) internationally, BigModel (Beijing entity) in China — matches MiniMax's split and is now the standard pattern for Chinese labs serving both markets. Prices differ meaningfully: GLM-5.3 is $1.40/$4.40 internationally versus ¥8/¥28 domestically; Flash is $0.15/$0.50 versus ¥0.8/¥2.8.

## Comparison / Evidence

Within the China AI Hub agent collection (10 agents), Zhipu's two entries (AutoGLM, GLM Coding Plan) sit alongside DeepSeek Harness, Qwen Code/Qoder, Kimi Code, MiniMax Agent/Code, and the Doubao App. Structural comparison:

| Dimension | AutoGLM | GLM Coding Plan | Typical coding agent (e.g., Kimi Code) |
|---|---|---|---|
| Surface | Phone GUI (ADB/HDC/WDA) | Coding tools (20+ integrations) | Code editing + CLI |
| Open source | Yes (code + models) | No (proprietary plan) | Varies |
| Monetization | Free API (promotional) | Subscription, peak/off-peak credits | API pay-as-you-go |
| Underlying model | AutoGLM-Phone-9B (GLM-4.1V family) | GLM-5.3 / 5.3-Flash, 1M context | Kimi K-series |
| Distinctive constraint | No sensitive-page automation | Quota windows + priority preemption | n/a |

DATA: comparison compiled from each agent's database record and official docs, verified 2026-09-20. The phone-GUI surface is unique to AutoGLM in this collection — no other tracked Chinese agent operates through ADB/HDC/WDA phone drivers.

## Limitations and Uncertainty

Four honest gaps. (1) **Benchmark provenance**: every GLM benchmark score here is vendor-reported; none has been independently reproduced by the China AI Hub, and Z.ai Code Bench (the basis of the 50% coding-improvement claim) is private. (2) **AutoGLM paid pricing** is not publicly disclosed — the API is free during a limited-time promotion, so the economics of the phone agent at scale are unknown. (3) **Launch dates**: the GLM Coding Plan's launch date is not stated in fetched sources; only the plan revision date (2026-07-30) is documented. (4) **License caution**: the database records GLM weights as Apache-2.0 "per GitHub repo metadata" with a note that the README has no separate weights-license section — self-hosters should verify per-model HF cards before commercial reuse.

## China AI Hub View

Our assessment: Zhipu is running the most coherent agent-strategy experiment among the six Chinese frontier labs. The bet is explicit — put agent capability in the cheapest open model, give the framework away, monetize the subscription, and accept that open weights cannibalize API revenue in exchange for developer mindshare. The experiment's outcome is not yet knowable: the vendor-reported agent benchmarks are modest (28.3 on Terminal-Bench 3.0), the phone agent's paid economics are undisclosed, and the Coding Plan's quota mechanics will determine whether subscriptions scale. What is knowable now: any team building agent tooling in 2026 has a testable, self-hostable reference stack in GLM-5.3-Flash + Open-AutoGLM at effectively zero licensing cost. That alone makes the ecosystem a baseline to evaluate against, regardless of whether it wins.

## Conclusion

GLM's agent orientation is not a marketing theme; it is a four-layer architecture — agent-native open weights, an open phone-agent framework, a cloud phone product, and a peak/off-peak coding subscription — built on a post-training-only flagship upgrade and a sparse+linear flash model. The strengths (capability at the cheapest tier, end-to-end self-hosting, honest constraint documentation) are as legible as the risks (vendor-reported benchmarks, undisclosed phone-agent pricing, quota-bound subscriptions). For builders, the practical takeaway is simple: the cheapest way to test computer-use agents in 2026 is GLM-5.3-Flash, and the most complete reference implementation of a phone agent is Open-AutoGLM — with the caveat that all performance claims remain vendor-reported until independently verified.

## Sources

See the Sources list in the page metadata — official Z.ai/BigModel docs, GitHub repositories (GLM-5, Open-AutoGLM), pricing pages and the Coding Plan docs, verified 2026-09-20.
