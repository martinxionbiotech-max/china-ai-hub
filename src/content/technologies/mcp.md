---
image: "/images/ai/technologies-mcp.webp"
image_credit: "AI-generated illustration (Seedream)"
slug: mcp
title: MCP
definition: "Model Context Protocol (MCP) is an open protocol, introduced by Anthropic in 2024, that standardizes how applications expose tools, resources and context to AI models — an analogue of a USB-C port for AI integrations."
related_models: []
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

MCP adoption across the Chinese agent ecosystem is broad in the China AI Hub database (last verified 2026-09-22): seven of the ten tracked Chinese agents list MCP support — Qwen Code, Qwen-Agent and Qoder (Alibaba), Kimi Code (Moonshot AI), MiniMax Code (MiniMax), DeepSeek Harness (DeepSeek), and GLM Coding Plan (Zhipu AI). Three (AutoGLM, Doubao App, MiniMax Agent) do not list it.

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

## Future development

MCP is converging with agent-to-agent protocols (A2A) and registry ecosystems; tool-quality filtering and standardized server registries are the active frontiers.
