---
title: "Chinese AI Coding Models: The Agent-Led Race"
description: "An analysis of China's coding-agent market and vendor-reported coding benchmarks: which labs compete, what the scores do and don't show, and how to read them."
published_date: "2026-09-22"
updated_date: "2026-09-22"
research_question: "How do Chinese labs compete in the coding space — through agents, subscriptions or benchmark scores — and what do the vendor-reported numbers actually establish?"
related_entities:
  - glm-coding-plan
  - kimi-code
  - minimax-code
  - qwen-code
  - qoder
  - deepseek-harness
  - deepseek-v4-1-flash
  - qwen3.8-max
  - kimi-k3
  - glm-5.3
author_view: true
image: "/images/cc/code-screen.jpg"
image_credit: "Sai Kiran Anagani / CC0, via Wikimedia Commons"
image_source: "https://commons.wikimedia.org/wiki/File:CSS_code_on_a_screen_(Unsplash).jpg"
sources:
  - source_name: "DeepSeek API Change Log"
    source_url: "https://api-docs.deepseek.com/updates"
    source_type: official
    confidence: high
  - source_name: "Qwen3.8-2.4T-A95B model card"
    source_url: "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
    source_type: official
    confidence: high
  - source_name: "Kimi K3 GitHub README"
    source_url: "https://github.com/MoonshotAI/Kimi-K3"
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
  - source_name: "Z.ai GLM-5 release notes"
    source_url: "https://github.com/zai-org/GLM-5"
    source_type: official
    confidence: high
---

All facts come from the China AI Hub database (agents, models and benchmarks collections, last verified 2026-09-20) and the primary sources linked at the bottom. Every benchmark score quoted here is vendor-reported unless stated otherwise.

## Executive Summary

Coding is the single most contested category in China's AI market. Five of the six frontier labs field a coding product — as agents, as subscriptions, or both — and coding benchmarks are the most frequently cited numbers in vendor announcements. The database shows two races happening at once: a product race in agents (where differentiation is billing and tooling) and a numbers race in benchmarks (where scores are vendor-reported, version-sensitive and frequently non-comparable). The product race is real; the numbers race is mostly noise.

## What We Know

The agent layer is crowded. Zhipu's GLM Coding Plan is a quota-based subscription running GLM-5.3 with 1M-token context, and it powers 20+ third-party tools including Claude Code, Codex and Cursor. Kimi Code (Moonshot) is an open-source TypeScript terminal agent, successor to the deprecated kimi-cli, with subagents, MCP, browser control and multimodal input. MiniMax Code is an open-source desktop app and CLI. Qwen Code is an open-source multi-protocol agent supporting OpenAI, Anthropic, Gemini and Qwen APIs plus DeepSeek, MiniMax, Z.AI, Kimi, OpenRouter and local models. Qoder (Alibaba) is a commercial platform with IDE, CLI and cloud, smart-routing tasks across model tiers at 1.6x/1.1x/0.3x credit multipliers. DeepSeek Harness is the open-source runtime ("Everything is a Plugin") that powers DeepSeek's own coding agent.

The model layer behind these agents: GLM-5.3, Kimi K3 and K2.7-Code, Qwen3.8-Max, DeepSeek-V4.1-Flash — the same flagships that dominate the general model database.

## What the Data Shows

The database records vendor-reported scores on four coding-relevant benchmarks. Reading them together, three observations hold:

**Terminal-Bench 2.1 is the most contested leaderboard.** DeepSeek-V4.1-Flash reports 90.6 (2026-09-10), DeepSeek-V4-Pro 87.9, Kimi K3 88.3, Qwen3.8-Max 86.6, MiniMax-M3 66.0. Note the version trap: GLM-5.3's 28.3 and GLM-5.2's 4.6 are on Terminal-Bench 3.0, a different benchmark version — the database deliberately labels versions rather than merging rows.

**SWE-bench splits by variant.** Kimi K2.5 reports 76.8 on SWE-bench Verified; Qwen3.8-Max 67.7 and MiniMax-M3 59.0 on SWE-bench Pro; MiniMax-M2 69.4 Verified and 56.5 Multilingual. "SWE-bench" in a headline is three different tests.

**DeepSWE and AutomationBench show DeepSeek ahead but thin coverage.** DeepSeek-V4.1-Flash reports 74.2 on DeepSWE v1.1 and 54.8 on AutomationBench; the next best AutomationBench score in the database is GLM-5.3-Flash at 48.8. But only three or four vendors publish on each — absence of a score is not evidence of absence of capability.

## What Has Changed

The database timeline records the migration from raw model scores to agent products as the headline. Kimi Code replaced the deprecated kimi-cli — a product generation shift. GLM Coding Plan repackaged model access into a cross-tool subscription. Qwen Code made multi-protocol support (running OpenAI/Anthropic/Gemini models inside a Qwen-built agent) a feature, which inverts the usual vendor lock-in logic. The competitive axis moved from "highest score" to "which agent, at what price, with which tooling."

## Why It Matters

For a developer evaluating the Chinese coding stack, the actionable comparison is not benchmark rankings but three practical questions the database answers directly: (1) Can I run it locally or self-host — Kimi Code, MiniMax Code, Qwen Code and DeepSeek Harness are open source; Qoder's CLI/IDE and GLM Coding Plan are closed. (2) What does it cost — subscription (GLM Coding Plan from $18/month international, Qoder Pro $20/month) versus model pay-as-you-go via the agent's API. (3) Which models can it drive — Qwen Code's multi-protocol support is the broadest recorded; Kimi Code is bound to Kimi membership models.

## Limitations and Uncertainty

Every score in this article is vendor-reported and not independently verified — the database labels them as such and records no independent re-evaluations. Benchmark versions are not comparable across vendors when versions differ (the Terminal-Bench 2.1 vs 3.0 split above). Several vendors do not publish on some benchmarks, so coverage gaps are structural. Agent products themselves have no independent evaluation data in the database at all. Any ranking derived from these numbers would be misrepresenting the evidence.

## China AI Hub View

Our assessment: the coding market is where Chinese labs are converging fastest, and the convergence is on product form, not performance claims. Four open-source terminal agents plus two commercial subscriptions competing on billing mechanics is a maturing market; the benchmark noise — version splits, variant cherry-picking, absent scores — is a symptom of how immature the measurement layer remains. We treat the coding agent layer as the single strongest signal of where the Chinese ecosystem is heading: productized, developer-facing, and priced like tools rather than APIs.

## Conclusion

China's coding race is real, but the honest scoreboard is product availability, pricing and model interoperability — not vendor-reported benchmark numbers. Five labs compete; four ship open-source agents; and the numbers that look like rankings are mostly incompatible benchmarks wearing the same name.
