---
title: "The Rise of Chinese AI Agents: What the 2026 Landscape Actually Looks Like"
description: "A structural analysis of China's AI agent ecosystem based on the China AI Hub agent database: who builds what, which categories are contested, and how openness maps to monetization."
published_date: "2026-09-22"
updated_date: "2026-09-22"
research_question: "How is China's AI agent landscape structured in 2026 — which companies build which agent types, and what patterns emerge from the distribution?"
related_entities:
  - autoglm
  - deepseek-harness
  - doubao-app
  - glm-coding-plan
  - kimi-code
  - minimax-agent
  - minimax-code
  - qoder
  - qwen-agent
  - qwen-code
author_view: true
image: "/images/cc/humanoid-robot.webp"
image_credit: "Syced / CC0, via Wikimedia Commons"
image_source: "https://commons.wikimedia.org/wiki/File:Humanoid_robot_at_Science_Square_Tsukuba.jpg"
sources:
  - source_name: "Open-AutoGLM GitHub repository"
    source_url: "https://github.com/zai-org/Open-AutoGLM"
    source_type: official
    confidence: high
  - source_name: "DeepSeek Harness documentation"
    source_url: "https://github.com/deepseek-ai/DeepSeek-Harness"
    source_type: official
    confidence: high
  - source_name: "Z.ai GLM Coding Plan pricing page"
    source_url: "https://z.ai/subscribe"
    source_type: official
    confidence: high
  - source_name: "Moonshot AI Kimi Code documentation"
    source_url: "https://github.com/MoonshotAI/kimi-code"
    source_type: official
    confidence: high
  - source_name: "QwenLM Qwen-Code GitHub repository"
    source_url: "https://github.com/QwenLM/qwen-code"
    source_type: official
    confidence: high
  - source_name: "MiniMax Agent platform"
    source_url: "https://agent.minimax.io"
    source_type: official
    confidence: high
---

All facts in this article come from the China AI Hub agent database (10 agents, last verified 2026-09-20) and the primary sources linked at the bottom. Where the database records a field as null or "not publicly disclosed," the article says so rather than inferring.

## Executive Summary

China's agent ecosystem in 2026 is dominated by the same six frontier labs that lead in models — but their agent strategies diverge sharply. The database records 10 agents across four categories: coding (4), platforms (2), frameworks (2), and autonomous assistants (2). Six of the ten are open source. The clearest structural finding: openness clusters in developer-facing tools, while closed products cluster where a company monetizes directly — a pattern that mirrors the model layer's dual-track strategy.

## What We Know

The database records one agent each from DeepSeek (DeepSeek Harness), ByteDance (Doubao) and Moonshot AI (Kimi Code), two each from Zhipu AI (AutoGLM, GLM Coding Plan) and MiniMax (MiniMax Agent, MiniMax Code), and three from Alibaba (Qoder, Qwen-Agent, Qwen Code).

Category by category:

- **Coding (4)**: GLM Coding Plan, Kimi Code, MiniMax Code, Qwen Code. The most contested category — every major lab except DeepSeek (whose coding agent runs on Harness) and ByteDance has a dedicated product here.
- **Platforms (2)**: MiniMax Agent (a cloud platform with skills, schedules, websites and research capabilities) and Qoder (a commercial coding platform with IDE, CLI, JetBrains plugin and cloud).
- **Frameworks (2)**: DeepSeek Harness (the Cordis-based "Everything is a Plugin" runtime) and Qwen-Agent (a Python framework with Assistant, FnCallAgent and ReActChat agents).
- **Autonomous assistants (2)**: AutoGLM (the first phone-use agent, open source, runs on-device via ADB/HDC/WebDriverAgent) and Doubao (ByteDance's consumer app, whose "Work" mode operates a virtual desktop autonomously).

## What the Data Shows

**Openness maps to audience.** Six of the ten agents are open source: AutoGLM, DeepSeek Harness, Kimi Code, MiniMax Code, Qwen-Agent and Qwen Code. Every one of them is a developer-facing tool or framework. The four closed products — Doubao, GLM Coding Plan, MiniMax Agent, Qoder — are all either consumer-facing or subscription/commercial platforms.

**Deployment splits the same way.** The three self-hosted agents (DeepSeek Harness, Qwen-Agent, Qwen Code) are all open-source frameworks. The three cloud-only agents (Doubao, GLM Coding Plan, MiniMax Agent) are all closed. Four agents support both (AutoGLM, Kimi Code, MiniMax Code, Qoder).

**Alibaba fields the broadest stack.** Three agents — an open framework (Qwen-Agent), an open multi-protocol coding agent (Qwen Code), and a commercial platform (Qoder). No other company spans framework, open tool and commercial product in the same way.

**Coding agents converge on subscription billing.** GLM Coding Plan is quota-based (Lite/Pro/Max at ¥118/¥538/¥1,078 per month in China, from $18/month internationally). Qoder runs Free/Pro $20/Pro+ $60/Ultra $200 monthly tiers with credit multipliers. Kimi Code and MiniMax Code bill through their parent companies' memberships or token plans. The open-source coding agents are free software, but the models they call are not free — the user pays the model provider.

## What Has Changed

The database timeline records AutoGLM's phone-use debut on 2024-10-25 as the earliest event in this collection. By September 2026 the structural shift is visible: agents stopped being demos and became products with pricing pages. Zhipu's GLM Coding Plan is the clearest example — one subscription that powers not only Zhipu's own clients but 20+ third-party coding tools including Claude Code, Codex and Cursor, positioning Zhipu as infrastructure rather than just a product vendor. Doubao's Work mode marks the same shift on the consumer side: an assistant that plans and executes on a virtual desktop rather than answering prompts.

## Why It Matters

For an international adopter, the practical question is not "which Chinese agent is best" but "which part of the stack do I touch." The database suggests three distinct touch points: (1) open frameworks you run yourself (DeepSeek Harness, Qwen-Agent); (2) open coding tools you point at your own API key or local model (Kimi Code, MiniMax Code, Qwen Code — the last supports OpenAI, Anthropic, Gemini and Qwen APIs plus DeepSeek, MiniMax, Z.AI, Kimi, OpenRouter and local models); and (3) closed subscription products with no self-host option (GLM Coding Plan, Qoder, MiniMax Agent, Doubao).

## Detailed Analysis

Three patterns stand out in the data.

**First, the frontier labs treat agents as model distribution.** GLM Coding Plan ships GLM-5.3's 1M-token context as the product's headline capability. Qwen Code's multi-protocol framework lets a developer use Qwen models alongside competitors' APIs — openness as a distribution strategy rather than a charitable one.

**Second, phone and desktop autonomy remains a niche held by two extremes.** AutoGLM (open, on-device, requires developer mode and ~24GB+ VRAM locally) sits at one end; Doubao Work (closed, cloud, mainland-China focused) at the other. Nothing in between is recorded in the database.

**Third, the coding category is crowded but differentiated by billing, not capability claims.** The database records no independent benchmark data for the agents themselves — only vendor-reported model benchmarks. Differentiation in the agent layer is happening through pricing mechanics (quota windows, credit multipliers) and tool ecosystem access, not through verifiable performance claims.

## Limitations and Uncertainty

This analysis covers 10 agents — a snapshot of the most prominent offerings, not a census. The database's last_verified date is 2026-09-20; agent pricing and availability change quickly. Several fields are structurally limited: the database does not record independent evaluations of agent task performance, only vendor-reported model benchmarks, and Doubao's underlying chat model is not publicly named in official pages. No conclusion here should be read as a ranking.

## China AI Hub View

Our assessment: China's agent market is mirroring its model market — the same labs, the same dual-track logic, one layer up. Open source is the acquisition funnel; closed subscriptions are the monetization. The genuinely distinctive element is the phone/desktop autonomy category, where AutoGLM and Doubao Work operate at opposite ends of the openness spectrum with no middle ground yet. We expect the coding category to consolidate first, because it is the only one where multiple vendors are competing with nearly identical open-source products differentiated mainly by billing mechanics.

## Conclusion

The 2026 Chinese agent landscape is a six-lab ecosystem with coding as its battleground, openness as its developer-facing default, and autonomy as its frontier. Adopters should choose by deployment needs and billing mechanics, not by marketing claims — and treat every performance claim as unverified until independent evaluation data exists.
