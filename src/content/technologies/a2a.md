---
image: "/images/ai/technologies-a2a.webp"
image_credit: "AI-generated illustration (Seedream)"
slug: a2a
title: A2A
definition: "Agent2Agent (A2A) is an open protocol announced by Google in April 2025 that lets AI agents from different vendors and frameworks discover, communicate and collaborate with each other."
related_models: []
related_companies:
  - deepseek
  - alibaba-cloud
  - zhipu-ai
related_technologies:
  - ai-agents
  - mcp
related_guides: [how-to-choose-a-chinese-ai-model]
last_verified: "2026-09-22"
sources:
  - source_name: "Google Developers Blog — A2A: A new era of agent interoperability"
    source_url: "https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/"
    source_type: official
---

## Technical background

MCP solved model-to-tool connections; A2A targets the adjacent problem of agent-to-agent communication. Google announced A2A in April 2025 with more than fifty initial partners, positioning it as a complementary standard: MCP for tools, A2A for agents talking to agents.

## How it works

Agents expose an "Agent Card" — a JSON description of capabilities, skills and authentication — discoverable at a well-known URL. Communication uses JSON-RPC tasks: one agent sends a task (or a multi-part message), and the receiving agent streams status and artifacts back. A2A is transport-agnostic and supports long-running, multi-turn agent collaboration.

## Why it matters

Real enterprise work crosses vendor boundaries: a procurement agent, a legal agent and a logistics agent each live in different systems. A2A aims to make cross-vendor agent workflows a configuration problem rather than an integration project. It also separates agent identity and capability discovery from tool calling.

## Chinese adoption

Adoption data in the China AI Hub database is thin: none of the ten tracked Chinese agents (last verified 2026-09-22) lists A2A support explicitly. Chinese agent ecosystems currently favor MCP — seven of ten agents list it, specifically Qwen Code, Qwen-Agent and Qoder (Alibaba Cloud), Kimi Code (Moonshot AI), MiniMax Code (MiniMax), DeepSeek Harness (DeepSeek) and GLM Coding Plan (Zhipu AI) — plus proprietary in-ecosystem orchestration. We report the A2A gap as a data gap rather than inferring a trend.

## Major Chinese companies and models

No verified A2A listings in our database as of 2026-09-22. This section will be updated as vendor documentation confirms support.

## Practical applications

Cross-vendor agent workflows, agent marketplaces with discoverable capabilities, and multi-company supply-chain or procurement automations where each party runs its own agents.

## Limitations

Young protocol with a smaller production footprint than MCP; inter-agent trust, payment and liability models remain unsolved; and without adoption it stays a standard on paper.

## Deployment considerations

If evaluating, treat A2A as a forward option: design internal agent APIs so they could publish an Agent Card later, but build today's integrations on MCP where tool access dominates.

## What the available evidence actually shows

The evidence base for A2A in China is genuinely thin, and China AI Hub records that as a fact rather than inferring a trend. As of 2026-09-22, none of the ten tracked Chinese agents lists A2A support, while seven list MCP. That is a real adoption asymmetry, but it says more about sequencing than about A2A's merits: MCP solves the model-to-tool problem that Chinese coding agents face daily, whereas A2A solves cross-vendor agent orchestration, which Chinese vendors currently handle through proprietary in-ecosystem control planes. The database cannot support a claim that A2A is failing in China — only that vendor documentation has not confirmed adoption. China AI Hub analysis indicates the durable signal to watch is not the announcement trail but whether any major Chinese agent framework actually publishes an Agent Card, since that is the concrete, verifiable artifact of A2A adoption.

## Future development

Likely convergence of MCP and A2A semantics, registry and identity standards, and negotiation protocols (cost, SLAs) between agents. Watch vendor documentation rather than announcements.

*Labels used above: **Official fact** (from the Google A2A announcement and the China AI Hub entity database), and **China AI Hub analysis** (our synthesis, always introduced as such). No vendor A2A adoption claims are recorded for Chinese agents as of 2026-09-22.*
