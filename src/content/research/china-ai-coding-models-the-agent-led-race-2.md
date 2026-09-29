---
title: "China AI Coding Models 2026 Update: Why the 'Strongest Coding Model' Claim Is Unprovable"
description: "A follow-up to 'Chinese AI Coding Models: The Agent-Led Race' — how benchmark version splits, variant cherry-picking and private test sets have made the 'strongest coding model' claim unverifiable, and what to trust instead."
published_date: "2026-09-29"
updated_date: "2026-09-29"
research_question: "Given the deepened coding benchmark data now in the database, can any vendor's claim to be the 'strongest coding model' in China be independently verified — and if not, what does the divergence actually establish?"
related_entities:
  - glm-coding-plan
  - kimi-code
  - minimax-code
  - qwen-code
  - qoder
  - deepseek-harness
  - deepseek-v4-1-flash
  - deepseek-v4-pro
  - qwen3.8-max
  - kimi-k3
  - glm-5.3
  - minimax-m3
author_view: true
image: "/images/cc/code-screen.jpg"
image_credit: "Sai Kiran Anagani / CC0, via Wikimedia Commons"
image_source: "https://commons.wikimedia.org/wiki/File:CSS_code_on_a_screen_(Unsplash).jpg"
sources:
  - source_name: "DeepSeek API Change Log"
    source_url: "https://api-docs.deepseek.com/updates"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Qwen3.8-2.4T-A95B model card"
    source_url: "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Kimi K3 GitHub README"
    source_url: "https://github.com/MoonshotAI/Kimi-K3"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Moonshot AI Kimi Code documentation"
    source_url: "https://github.com/MoonshotAI/kimi-code"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "QwenLM Qwen-Code GitHub repository"
    source_url: "https://github.com/QwenLM/qwen-code"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Z.ai GLM-5 release notes"
    source_url: "https://github.com/zai-org/GLM-5"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Qoder docs — overview"
    source_url: "https://docs.qoder.com/qoder/overview.md"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

All facts come from the China AI Hub database (benchmarks, models and agents collections, last verified 2026-09-20) and the primary sources linked at the bottom. Every benchmark score quoted here is vendor-reported unless stated otherwise. This article extends the earlier [Chinese AI Coding Models](/research/chinese-ai-coding-models/) analysis with the deepened benchmark and agent data now in the database.

## Research Question

The first article established that China's coding race is real on the product side (five labs, four open-source agents, two commercial subscriptions) but noisy on the numbers side. The follow-up question is sharper: **with the deepened benchmark data now recorded, is the claim "X is the strongest coding model in China" even a verifiable statement?** This article argues it is not — and that the reason is not a shortage of numbers but a surplus of incompatible ones, layered on top of agent products that have no independent evaluation at all.

## Methodology

We examine the coding evidence along three axes: (1) the benchmark score layer, where we test comparability across vendors; (2) the benchmark-version layer, where we test whether "the same benchmark" is actually the same test; and (3) the agent-product layer, where we test whether any independent evaluation exists at all. The method is deliberately skeptical: for any headline "strongest" claim, we ask which specific benchmark, version, subset, tool mode and harness produced it, and whether a competing vendor published a score on that exact configuration. Where no competitor published a matching configuration, the claim is marked unverifiable rather than accepted or rejected.

## Evidence

The database's coding-relevant benchmark records, organized by what they actually test:

**Terminal-Bench — the most contested leaderboard, split by version.** DeepSeek-V4.1-Flash reports 90.6 (2026-09-10) and V4-Pro 87.9 on Terminal-Bench **2.1**; Kimi K3 reports 88.3 and Qwen3.8-Max 86.6 on 2.1; MiniMax-M3 reports 66.0 on 2.1. But GLM-5.3's 28.3 is on Terminal-Bench **3.0**, a different version — a ~60-point gap that is entirely an artifact of the version switch, not capability. On 2.1, DeepSeek leads by ~2 points; on 3.0, GLM's score is not comparable to anyone's 2.1 figure.

**SWE-bench — three different tests wearing one name.** Kimi K2.5 reports 76.8 on SWE-bench **Verified**; Qwen3.8-Max reports 67.7 and MiniMax-M3 59.0 on SWE-bench **Pro**; MiniMax-M2 reports 69.4 Verified and 56.5 Multilingual. "SWE-bench" in a headline could mean any of three variants with different difficulty distributions.

**DeepSWE — DeepSeek leads but coverage is thin.** DeepSeek-V4.1-Flash reports 74.2 on DeepSWE v1.1, Qwen3.8-Max 56.6, Kimi K3 67.5, GLM-5.3 66.9. DeepSeek's lead here is real but rests on a benchmark only a handful of vendors publish.

**Private test sets — unverifiable by construction.** GLM-5.3's headline "50% coding improvement" is measured on Z.ai Code Bench, a private in-house benchmark. DeepSeek's code-agent scores used DeepSeek Harness in minimal mode with DSBench-FullStack/Hard as internal test sets. These cannot be independently reproduced, which is not a criticism of the models — it is a statement about what the numbers can establish.

**AutomationBench — the computer-use dimension.** DeepSeek-V4.1-Flash reports 54.8, GLM-5.3-Flash 48.8, Qwen3.8-Max 27.3, DeepSeek-V4-Pro 31.8. This is the one coding-adjacent benchmark where scores are low across the board, indicating a genuinely hard frontier rather than a vendor gap.

**Agentic and tool-use benchmarks — a separate axis entirely.** Beyond pure coding, the database records scores that test what a coding *agent* must do downstream: MiniMax-M3 reports MCP Atlas 74.2 and BrowseComp 83.5 (tool-use and browsing signals), GLM-5.3 reports CyberGym 84.5 and Agents' Last Exam CLI 28.5, and DeepSeek-V4-Pro reports Agents' Last Exam 25.7. These are not coding scores, but they measure the surrounding capabilities — tool orchestration, browser control, multi-step agent execution — that increasingly decide whether a coding model works in a real agent loop. The divergence here is even starker than on the coding benchmarks: almost no vendor pair publishes on the same agentic benchmark, so the agentic layer is even less comparable than the coding layer.

## Data

The benchmark-version matrix, rendered as what a "strongest" claim would need to survive:

| Benchmark | DeepSeek (top) | Closest rival | Comparable? |
|---|---|---|---|
| Terminal-Bench 2.1 | 90.6 (V4.1-Flash) | 88.3 (Kimi K3) | Yes — but GLM/MiniMax on different versions |
| Terminal-Bench 3.0 | — (no published) | 28.3 (GLM-5.3) | No — different version, no overlap |
| SWE-bench Verified | 76.8 (Kimi K2.5) | — | No — Qwen/MiniMax publish Pro |
| SWE-bench Pro | 67.7 (Qwen3.8-Max) | 59.0 (MiniMax-M3) | Yes — but different vendors than Verified |
| DeepSWE v1.1 | 74.2 (DeepSeek) | 67.5 (Kimi K3) | Yes — but only ~4 vendors publish |
| AutomationBench | 54.8 (DeepSeek) | 48.8 (GLM-5.3-Flash) | Yes — low scores, hard benchmark |

The pattern is structural: **on no single coding benchmark do more than a handful of vendors publish a score on the same version and variant.** The leader changes depending on which benchmark and version you select — DeepSeek leads Terminal-Bench 2.1 and DeepSWE, Kimi leads SWE-bench Verified, and no one leads Terminal-Bench 3.0 against a comparable field. The "strongest" claim is under-determined by the data.

The agent layer's billing mechanics add a further, non-numeric axis of divergence. The coding products the race has migrated to are priced on fundamentally different instruments: GLM Coding Plan is a quota subscription (¥118/¥538/¥1,078 per month in China, from $18/month internationally), Qoder is a credit-tier subscription ($20/$60/$200 per month with 1.6x/1.1x/0.3x model-routing multipliers), Kimi Code bills through Kimi membership ($15–$159/month) or pay-as-you-go API ($3.00/$15.00 per 1M for kimi-k3), MiniMax Code through Token Plan ($22–$132/month), and Qwen Code through an international Coding Plan ($50/month) or China Token Plan (¥39–¥499/month). There is no shared unit that lets a buyer compare these head-to-head — a fact that matters because the agent's *cost* and the model's *score* are the two numbers a developer actually acts on, and only one of them (the score) has any vendor-published data at all.

## Analysis

China AI Hub analysis indicates: the "strongest coding model" claim has become **structurally unverifiable in this ecosystem**, and the cause is methodology divergence, not a shortage of measurement. Four levers — benchmark version (Terminal-Bench 2.1 vs 3.0), variant (SWE-bench Verified vs Pro vs Multilingual), tool mode and subset (HLE with/without tools, pure-text subsets), and private test sets (Z.ai Code Bench, DSBench) — each move a score by more than the gap between leading models. The companion [benchmark-methodology research](/research/benchmark-methodology-divergence/) documented these levers for general benchmarks; the coding data shows they are *more* pronounced, not less, in the highest-stakes category.

China AI Hub analysis indicates: the migration to agent products has made the problem worse, not better. The first article showed the competitive axis moving from scores to agents (Kimi Code, Qwen Code, GLM Coding Plan, Qoder, DeepSeek Harness). But the database records **zero independent evaluations of any Chinese coding agent's task performance** — only vendor-reported model benchmarks underneath them. So the layer where the race is actually being decided (the agent product) is exactly the layer with no third-party measurement at all. A buyer can find dozens of vendor numbers for the *models* and no independent numbers for the *agents* those models power.

China AI Hub analysis indicates: the divergence itself is information, and it is information about vendor confidence. Vendors publish where they are strongest and omit where they are not — DeepSeek publishes DeepSWE and AutomationBench (agentic and computer-use tasks), Alibaba publishes SWE-bench Pro and MRCR, Zhipu publishes Terminal-Bench 3.0 and a private Code Bench. The published-set is a revealed-preference map of each lab's confidence, and reading it as such is more useful than trying to force the numbers into a single ranking they cannot support.

## Counterpoints / Limitations

Counterpoints must be weighed. **First, "unverifiable" does not mean "wrong."** A vendor-reported score can be both unverifiable and true; the absence of independent re-measurement is a measurement gap, not evidence of dishonesty. **Second, version divergence can be legitimate.** Terminal-Bench 3.0 is a newer, harder test; a vendor publishing on 3.0 may be *more* rigorous, not less. The problem is comparability, not integrity. **Third, some comparisons are valid.** Within a single benchmark-version (Terminal-Bench 2.1, SWE-bench Pro, DeepSWE v1.1), a handful of vendors do publish comparable scores, and those subsets support narrow, conditional statements — "DeepSeek leads Terminal-Bench 2.1 among the four vendors that publish" — even though they cannot support a global "strongest" claim. **Fourth, the database records only what vendors publish**, so coverage gaps are structural; a vendor's absence from a benchmark is not evidence of absence of capability. **Fifth, the agent layer's lack of independent evaluation is a young-market condition** that could change as third-party agent evaluations (like the public SWE-bench Verified runs emerging elsewhere) standardize.

## China AI Hub Interpretation

Our interpretation: **the honest answer to "who has the strongest Chinese coding model" is that the question, as posed, has no evidence-backed answer — and the more precise question has a partial one.** If you ask "who leads on Terminal-Bench 2.1," the database supports a conditional answer (DeepSeek, among four publishing vendors). If you ask "who has the best coding agent," the database supports no answer, because the agent layer has no independent evaluation. The gap between these two statements is where most of the marketing lives.

We read the coding category as the clearest demonstration of the site's central methodology point: **measurement is harder than capability, and in a market where the measurement layer is fragmented, the capability claims are only as strong as their weakest methodological link.** A "strongest coding model" claim is only meaningful if it states the benchmark, version, variant, tool mode and harness — and even then, it is a claim about a score on a test, not a claim about your codebase.

We flag the uncertainty that matters most for decision-making: **we cannot tell a buyer which Chinese coding agent will perform best on *their* repository.** No amount of vendor benchmark data answers that, because repository-scale performance depends on codebase specifics, harness configuration and integration — none of which a headline score captures. Our position is that ten private test cases on your real codebase outrank a thousand vendor numbers, and the coding category is where that principle bites hardest.

## Conclusion

The deepened data confirms and sharpens the first article's finding. China's coding race is real on the product side — five labs shipping agents and subscriptions — but the "strongest coding model" claim is unverifiable as stated, because benchmark versions (Terminal-Bench 2.1 vs 3.0), variants (SWE-bench Verified vs Pro vs Multilingual), and private test sets fragment every leaderboard, and the agent layer that now decides the race has no independent evaluation at all. What the divergence does establish is where each lab is confident: DeepSeek in agentic terminal and computer-use tasks, Alibaba in repository-scale SWE-bench Pro, Zhipu in a private code benchmark it does not share. For a buyer, that confidence map — not any headline ranking — is the actionable signal.

## Sources

See the Sources list in the page metadata — benchmark rows trace to the DeepSeek change log, the Qwen3.8-2.4T-A95B model card, the Kimi K3 README, the GLM-5 release notes, and the agent product pages, verified 2026-09-20.

*Labels used above: **Official fact** (benchmark versions, variants and scores as published), **Vendor-reported claim** (all scores and private-benchmark improvement claims), and **China AI Hub analysis** (the unverifiability argument, always introduced as such).*
