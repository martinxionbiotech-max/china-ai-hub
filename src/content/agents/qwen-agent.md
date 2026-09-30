---
image: "/images/ai/agents-qwen-agent.webp"
image_credit: "AI-generated illustration (Seedream)"
agent_id: qwen-agent
agent_name: Qwen-Agent
company: alibaba-cloud
description: "Alibaba Qwen team's open-source Python framework for developing LLM applications based on Qwen's instruction following, tool usage, planning and memory capabilities (Apache-2.0). Serves as the backend of Qwen Chat (chat.qwen.ai). Ships example applications including BrowserQwen browser assistant, Docker-isolated Code Interpreter, RAG over 1M-token documents, MCP integration and Gradio GUI."
agent_type: framework
underlying_models: []
framework: "Python framework built upon Qwen>=3.0 models (official README: \"Agent framework and applications built upon Qwen>=3.0\"); (pip install qwen-agent); built-in Assistant / FnCallAgent / ReActChat agents with @register_tool; connects to DashScope API or self-hosted models via vLLM/Ollama"
tool_calling: true
browser_use: true
mcp: true
memory: true
planning: true
api: true
pricing: "Framework free and open source (Apache-2.0). Model usage billed via DashScope API pay-as-you-go per token, or free with self-hosted open models. No subscription of its own."
deployment: self_hosted
open_source: true
license: Apache-2.0
github: https://github.com/QwenLM/Qwen-Agent
documentation: https://qwenlm.github.io/Qwen-Agent/en/guide/
use_cases:
  - Custom LLM applications with tool calling
  - Browser automation assistant (BrowserQwen)
  - RAG over 1M-token documents
  - Code interpreter and PDF-reading assistants
  - MCP tool integration and agent evaluation via DeepPlanning benchmark
limitations:
  - Docker-based code interpreter has only basic sandbox isolation - use with caution in production
  - TIR math demo Python executor is not sandboxed (local testing only)
  - GUI requires Python 3.10+
  - Last GitHub release v0.0.26 on 2025-05-29; repo development cadence has slowed since
last_verified: "2026-09-20"
sources:
  - source_name: Qwen-Agent GitHub repository
    source_url: https://github.com/QwenLM/Qwen-Agent
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Qwen-Agent docs guide
    source_url: https://qwenlm.github.io/Qwen-Agent/en/guide/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
**Short answer.** Qwen-Agent is the Qwen team's open-source Python framework for building LLM applications on Qwen models — built-in Assistant, FnCallAgent and ReActChat agents with a `@register_tool` decorator, connecting to the DashScope API or self-hosted models via vLLM/Ollama. It is the low-level, Qwen-native plumbing that [Qwen Code](/agents/qwen-code/) and Qwen Chat build on.

**Key facts.**

- Apache-2.0 framework built on Qwen≥3.0 models, per the official README ("Agent framework and applications built upon Qwen>=3.0"); `pip install qwen-agent`.
- Ships example applications: BrowserQwen (browser assistant), a Docker-isolated Code Interpreter, RAG over 1M-token documents, MCP integration, PDF-reading assistants and a Gradio GUI.
- Model usage billed per token via DashScope, or free with self-hosted open models via vLLM/Ollama; the framework itself has no subscription.
- Serves as the backend of Qwen Chat (chat.qwen.ai).
- Last GitHub release v0.0.26 on 2025-05-29; development cadence has slowed since.

**What this means.** Qwen-Agent is the framework layer beneath Alibaba's agent portfolio — model-bound (Qwen-native) in a way that [Qoder](/agents/qoder/) (multi-model) and [Qwen Code](/agents/qwen-code/) (multi-protocol) are not, making it the most direct expression of Qwen's own instruction-following, tool-use, planning and memory capabilities.

**What is uncertain.** The slowed release cadence (last release 2025-05-29) leaves open how actively the framework is maintained versus Qwen Code and Qoder, and the Docker-based code interpreter carries only basic sandbox isolation — a production caveat, not a guarantee.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-qwen-agent-1 | Qwen-Agent GitHub repository | https://github.com/QwenLM/Qwen-Agent | Official documentation | — | 2026-09-20 | high | — |
| src-agents-qwen-agent-2 | Qwen-Agent docs guide | https://qwenlm.github.io/Qwen-Agent/en/guide/ | Official documentation | — | 2026-09-20 | high | — |

## Why it matters

Qwen-Agent is the foundational-framework layer of Alibaba's agent portfolio, and the reference for how a Qwen-native agent abstraction differs from a model-agnostic one. Its agent classes (Assistant, FnCallAgent, ReActChat) and the `@register_tool` decorator are designed around Qwen's instruction-following, tool-use, planning and memory capabilities — the framework *assumes* the model's strengths rather than routing around them.

China AI Hub analysis indicates Qwen-Agent matters as the low-level, Qwen-native integration point, and its slowed release cadence (last release 2025-05-29) is itself a documented signal that Alibaba's agent investment has shifted toward [Qwen Code](/agents/qwen-code/) and [Qoder](/agents/qoder/). The framework's own repo confirms this: it now positions Qwen-Agent as "the backend of Qwen Chat" — a stable substrate — rather than as the primary forward-looking agent surface.

## How it differs from Qwen Code and Qoder

The three Alibaba surfaces are a ladder from framework to product.

- **[Qwen-Agent](/agents/qwen-agent/)** is the *framework* — a Python library of agent classes and examples (BrowserQwen, Code Interpreter, RAG), Qwen-native, self-hosted, Apache-2.0.
- **[Qwen Code](/agents/qwen-code/)** is the *open client* — a multi-protocol TypeScript coding agent (CLI, desktop, browser, chat) where the user brings any model, open-source and free.
- **[Qoder](/agents/qoder/)** is the *closed product* — a commercial platform with Auto-tier multi-model routing, Expert teams, governance and scheduled automations.

China AI Hub analysis: Qwen-Agent is where the Qwen-native design lives, Qwen Code is where model-optionality lives, and Qoder is where governance lives. Qwen-Agent's model-bound design is the opposite of Qwen Code's model-agnostic stance — the framework optimizes for Qwen's specific capabilities, while the client maximizes provider choice. A researcher building a custom Qwen application reaches for Qwen-Agent; a developer who wants one client across many models uses Qwen Code; an enterprise buying managed routing buys Qoder.

## Practical implications

**For builders.** Qwen-Agent is the lowest-level, most flexible path — you assemble Assistant/FnCallAgent/ReActChat with `@register_tool`, connect to DashScope or self-hosted vLLM/Ollama, and ship examples like BrowserQwen or RAG-over-1M-tokens as starting points. The framework is free; you pay only for model usage.

**For production.** The Docker-based code interpreter has only basic sandbox isolation and the TIR math demo executor is not sandboxed (local testing only), so production deployments must add their own isolation rather than trust the examples.

**For maintenance planning.** The slowed release cadence (v0.0.26 on 2025-05-29) is a real signal — teams building new work on Qwen-Agent should weigh whether their needs are better served by the more actively developed Qwen Code.

## What the evidence shows

The evidence is strong on what the framework is and honest about its maintenance state. The GitHub repo and docs document the agent classes, the `@register_tool` decorator, the DashScope/vLLM/Ollama connectivity, the example applications (BrowserQwen, Code Interpreter, RAG, MCP, Gradio) and the Qwen Chat backend role; the README explicitly scopes it to Qwen≥3.0 models.

The gap is sandboxing and cadence. The code interpreter's "basic sandbox isolation" and the un-sandboxed TIR executor are explicit limitations, and the last release predates the database's other Qwen surfaces by more than a year. China AI Hub analysis indicates the honest reading is "stable, Qwen-native substrate, no longer the leading edge" — Qwen-Agent is where the Qwen-native design is preserved and where Qwen Chat's backend lives, but the forward investment has visibly moved to Qwen Code and Qoder, so builders should treat it as foundational rather than cutting-edge.

## Where this fits

| Workload | Relevance |
|---|---|
| Custom Qwen-native LLM applications (tool calling) | High |
| Browser automation (BrowserQwen) | High |
| RAG over 1M-token documents | High |
| Self-hosted deployment (vLLM/Ollama) | High |
| MCP integration and agent evaluation (DeepPlanning) | High |
| Production sandboxed code execution | Moderate (basic isolation only) |
| Actively updated agent surface | Low (cadence slowed since 2025-05-29) |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | Qwen>=3.0 models (framework-level; not pinned to a single model) | Official |
| Target users | Developers building LLM applications | Official |
| Platform | Python framework (pip install qwen-agent) | Official |
| OS | Cross-platform (Python 3.10+ for GUI) | Official |
| Browser / computer use | Browser (BrowserQwen) | Vendor-reported |
| Coding | Yes (Docker-isolated Code Interpreter example) | Vendor-reported |
| Autonomous task execution | Yes (planning, ReActChat agent) | Vendor-reported |
| MCP | Yes | Official |
| Tool calling | Yes (@register_tool) | Official |
| Memory | Yes | Official |
| Workflow | Assistant / FnCallAgent / ReActChat agents; RAG over 1M-token documents | Official |
| API | Yes (DashScope API, or self-hosted via vLLM/Ollama) | Official |
| Pricing | Framework free; model usage per token | Vendor-reported |
| Region | Not publicly documented | Not publicly documented |
| Open-source | Yes — Apache-2.0 | Official |
| Deployment | Self-hosted | Official |
| Limitations | Code interpreter only basic sandbox; slowed release cadence (last 2025-05-29) | Official |
| Source | [Qwen-Agent GitHub](https://github.com/QwenLM/Qwen-Agent) | Official |
| Last verified | 2026-09-20 | Official |

See the [Alibaba Cloud](/companies/alibaba-cloud/) company profile, the [Qwen Code](/agents/qwen-code/) client, the [Qoder](/agents/qoder/) platform, and the site's [AI agents](/technology/ai-agents/) and [tool calling](/technology/tool-calling/) technology pages.

*Labels used above: **Official fact** (from the Qwen-Agent GitHub repo and docs), **Vendor-reported claim** (capability statements by the Qwen team), and **China AI Hub analysis** (our synthesis, always introduced as such).*
