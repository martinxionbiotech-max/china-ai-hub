---
image: "/images/ai/technologies-ai-agents.webp"
image_credit: "AI-generated illustration (Seedream)"
slug: ai-agents
title: AI Agents
definition: "An AI agent is a system in which a language model acts autonomously toward a goal — planning, calling tools, observing results and iterating — rather than producing a single response to a single prompt."
related_models:
  - kimi-k3
  - qwen3.8-max
  - doubao-seed-2-1-pro
  - minimax-m3
related_companies:
  - deepseek
  - alibaba-cloud
  - zhipu-ai
  - moonshot-ai
  - minimax
  - bytedance
related_technologies:
  - mcp
  - a2a
  - tool-calling
  - computer-use
related_guides: [how-to-choose-a-chinese-ai-model]
last_verified: "2026-09-22"
sources:
  - source_name: "Anthropic — Building Effective Agents"
    source_url: "https://www.anthropic.com/engineering/building-effective-agents"
    source_type: official
---

## Technical background

The term "agent" escalated from single-call tool use to multi-step autonomous systems during 2023-2025. The engineering consensus (see Anthropic's "Building Effective Agents") is that agentic patterns — tool loops, planning, multi-agent delegation — are the practical form; "agents" are not a separate model class but a system design on top of capable models.

## How it works

An agent loop is: model plans a step, calls tools (search, code execution, browser, APIs), receives observations, and continues until a stop condition. Supporting machinery includes memory (short- and long-term), planning strategies, and guardrails. Multi-agent systems split roles — planner, coder, reviewer — each with its own model and tools.

## Why it matters

Agents turn language models from answerers into workers: they can operate software, browse the web, and complete multi-hour tasks. Agent capability is now a first-class model attribute — several models in the China AI Hub database list it explicitly.

## Chinese adoption

China's agent ecosystem is deep. The China AI Hub agent database tracks ten Chinese agents (last verified 2026-09-22) spanning coding agents (Qwen Code, Kimi Code, MiniMax Code), frameworks (DeepSeek Harness, Qwen-Agent), autonomous agents (AutoGLM, Doubao App), and coding plans (GLM Coding Plan, Qoder). Seven of ten list MCP support; seven list computer use. On the model side, Kimi K3, Qwen3.8-Max, Doubao Seed 2.1 Pro and MiniMax M3 all list agent capability.

Pricing evidence shows how agents have been productized. GLM Coding Plan runs on GLM-5.3 / GLM-5.3-Flash with 1M-token context and bills ¥118–¥1,078/month in China (from $18/month internationally). Kimi Code runs on Kimi K3 (2.8T-parameter MoE) under Kimi membership. MiniMax Code runs on MiniMax-M3 (~428B/~23B-active MoE). Qoder's Auto tier smart-routes across Qwen3.8-Max, DeepSeek-V4-Pro, GLM-5.3, Kimi K3 and MiniMax M3 with 1.6x/1.1x/0.3x credit multipliers.

## Major Chinese companies and models

- **DeepSeek** — DeepSeek Harness: open-source agent framework (Cordis-based), MIT, self-hosted.
- **Alibaba Cloud** — Qwen Code and Qwen-Agent (open), plus Qoder.
- **Zhipu AI** — AutoGLM (open) and GLM Coding Plan.
- **Moonshot AI** — Kimi Code (open, MIT) with browser/computer use.
- **MiniMax** — MiniMax Code (open) and MiniMax Agent (cloud platform).
- **ByteDance** — Doubao App with computer-use "Work" mode.

## Practical applications

Software engineering (multi-file edits, test loops), web research and form-filling, data extraction pipelines, autonomous computer operation, and customer-support workflows.

## Limitations

Autonomy implies failure modes: loops that burn tokens, tool misuse, and compounding errors over long tasks. Long-horizon reliability is still the open problem. Capability labels in our database are vendor-reported unless independently benchmarked.

## Deployment considerations

Use simpler workflow patterns where they suffice; add budgets, checkpoints and human approval for irreversible actions; sandbox code and browser tools; monitor token spend per completed task, not per call.

## What the available evidence actually shows

The China AI Hub database establishes that agents are a broad, multi-vendor product category in China — ten tracked agents across six companies, with open-source frameworks (DeepSeek Harness MIT, Qwen Code Apache-2.0, Qwen-Agent Apache-2.0, AutoGLM Apache-2.0 code) alongside closed products (Doubao App, GLM Coding Plan, Qoder, MiniMax Agent). What the database does not yet show is independent evaluation of agent reliability: capability flags (agent, tool calling, computer use, MCP) are vendor-reported, and long-horizon reliability is untested against a common benchmark. China AI Hub analysis indicates the structural story — models gaining first-class agent capability while agent products consolidate around MCP and computer use — is well evidenced; the quality story (how reliably these agents complete multi-hour tasks) is not yet measurable from recorded data.

## Future development

Agents are absorbing computer use and browser control as standard tools, standardizing inter-agent communication (MCP, A2A), and moving toward persistent memory and multi-day task execution.

*Labels used above: **Official fact** (from Anthropic's agent engineering guidance and the China AI Hub entity database), **Vendor-reported claim** (capability and pricing figures published by each vendor), and **China AI Hub analysis** (our synthesis, always introduced as such).*
