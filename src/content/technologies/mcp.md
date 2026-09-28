---
image: "/images/ai/technologies-mcp.webp"
image_credit: "AI-generated illustration (Seedream)"
slug: mcp
title: MCP
definition: "Model Context Protocol (MCP) is an open protocol, introduced by Anthropic in 2024, that standardizes how applications expose tools, resources and context to AI models — an analogue of a USB-C port for AI integrations."
related_models:
  - qwen3.8-max
  - kimi-k3
  - glm-5.3
related_companies:
  - deepseek
  - alibaba-cloud
  - zhipu-ai
  - moonshot-ai
  - minimax
related_technologies:
  - ai-agents
  - tool-calling
  - a2a
related_guides: [how-to-choose-a-chinese-ai-model]
last_verified: "2026-09-22"
sources:
  - source_name: "Anthropic — Introducing the Model Context Protocol"
    source_url: "https://www.anthropic.com/news/model-context-protocol"
    source_type: official
  - source_name: "Model Context Protocol specification"
    source_url: "https://modelcontextprotocol.io/"
    source_type: official
---

## Technical background

Before MCP, every model-to-tool integration was bespoke: each agent product re-implemented connectors for GitHub, databases, browsers and business apps. Anthropic released MCP in November 2024 as an open standard to collapse this into one protocol, and it spread rapidly through the agent ecosystem — including adoption by OpenAI and Google — before being donated to an independent foundation.

## How it works

MCP follows a client-server architecture over JSON-RPC. An MCP server exposes three primitives: tools (model-invoked actions), resources (data the model can read), and prompts (reusable templates). The host application runs an MCP client that discovers servers and presents their capabilities to the model. Transports include stdio (local) and streamable HTTP (remote).

## Why it matters

One connector, many consumers: a company can expose its internal systems once via MCP and every MCP-capable agent can use them. It shifts integration cost from O(models × tools) to O(models + tools), and it separates tool security from prompt engineering.

## Chinese adoption

MCP adoption across the Chinese agent ecosystem is broad in the China AI Hub database (last verified 2026-09-22): seven of the ten tracked Chinese agents list MCP support — Qwen Code, Qwen-Agent and Qoder (Alibaba), Kimi Code (Moonshot AI), MiniMax Code (MiniMax), DeepSeek Harness (DeepSeek), and GLM Coding Plan (Zhipu AI). Three (AutoGLM, Doubao App, MiniMax Agent) do not list it. The pattern is telling: the open-source coding agents and frameworks adopted MCP, while the cloud-hosted autonomous products did not document it.

## Major Chinese companies and models

- **Alibaba Cloud** — Qwen Code, Qwen-Agent, Qoder all list MCP support.
- **DeepSeek** — DeepSeek Harness lists MCP support and is open source (MIT).
- **Moonshot AI / MiniMax / Zhipu AI** — Kimi Code, MiniMax Code and GLM Coding Plan list MCP support.

## Practical applications

Connecting coding agents to repositories, issue trackers and CI; giving enterprise agents read access to databases, CRM and ERP; browser and desktop tooling for research agents.

## Limitations

Capability is only as good as the servers behind it; transport and auth patterns still vary; exposing internal tools to models creates real security surface — permissioning must be enforced server-side.

## Deployment considerations

Prefer stdio for local tools and authenticated remote transports for shared services; audit tool descriptions (they drive model behavior); and least-privilege every server.

## What the available evidence actually shows

The database evidences a clean adoption split: seven of ten agents list MCP support, and all seven are open-source coding agents or frameworks, while the three closed cloud products (AutoGLM, Doubao App, MiniMax Agent) do not document it. That split is a recorded fact, not an inference. What the database does not evidence is depth of adoption — "lists MCP support" does not tell us which tools or resources are actually exposed, or how production-hardened the integrations are. China AI Hub analysis indicates MCP is the de facto tool-integration standard among Chinese open-source agents specifically, but the database cannot yet measure how deeply each agent's MCP surface is actually used.

## Future development

MCP is converging with agent-to-agent protocols (A2A) and registry ecosystems; tool-quality filtering and standardized server registries are the active frontiers.

*Labels used above: **Official fact** (from Anthropic's MCP announcement and the China AI Hub database), **Vendor-reported claim** (MCP capability flags), and **China AI Hub analysis** (our synthesis, always introduced as such).*
