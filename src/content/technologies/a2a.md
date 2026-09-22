---
slug: a2a
title: A2A
definition: "Agent2Agent (A2A) is an open protocol announced by Google in April 2025 that lets AI agents from different vendors and frameworks discover, communicate and collaborate with each other."
related_models: []
related_companies: []
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

Adoption data in the China AI Hub database is thin: none of the ten tracked Chinese agents (last verified 2026-09-22) lists A2A support explicitly. Chinese agent ecosystems currently favor MCP (seven of ten agents list it) and proprietary in-ecosystem orchestration. We report this as a data gap rather than inferring a trend.

## Major Chinese companies and models

No verified A2A listings in our database as of 2026-09-22. This section will be updated as vendor documentation confirms support.

## Practical applications

Cross-vendor agent workflows, agent marketplaces with discoverable capabilities, and multi-company supply-chain or procurement automations where each party runs its own agents.

## Limitations

Young protocol with a smaller production footprint than MCP; inter-agent trust, payment and liability models remain unsolved; and without adoption it stays a standard on paper.

## Deployment considerations

If evaluating, treat A2A as a forward option: design internal agent APIs so they could publish an Agent Card later, but build today's integrations on MCP where tool access dominates.

## Future development

Likely convergence of MCP and A2A semantics, registry and identity standards, and negotiation protocols (cost, SLAs) between agents. Watch vendor documentation rather than announcements.
