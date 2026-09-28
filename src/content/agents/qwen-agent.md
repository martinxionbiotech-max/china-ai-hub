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
**What it is.** Qwen-Agent is the Qwen team's open-source Python framework for building LLM applications on Qwen models, shipping built-in Assistant, FnCallAgent and ReActChat agents with a @register_tool decorator. **Why it matters.** It is the framework layer beneath Alibaba's Qwen chat and coding products — the open Apache-2.0 plumbing that [Qwen Code](/agents/qwen-code/) and Qwen Chat build on. **Key characteristics.** Connects to the DashScope API or self-hosted models via vLLM/Ollama; ships BrowserQwen, a Docker-isolated code interpreter, RAG over 1M-token documents, and MCP integration. **What a professional should know.** The framework is free (Apache-2.0) with no subscription of its own — model usage is billed per token through DashScope or free with self-hosted open models; the last GitHub release was v0.0.26 on 2025-05-29.

Qwen-Agent is the Qwen team's open-source Python framework for building LLM applications: it ships built-in Assistant, FnCallAgent and ReActChat agents with a @register_tool decorator, and connects to the DashScope API or to self-hosted models via vLLM/Ollama.

The framework is free under Apache-2.0 with no subscription of its own; model usage is billed per token through DashScope, or free with self-hosted open models.

See the [Alibaba Cloud](/companies/alibaba-cloud/) profile.

## Why it matters

Qwen-Agent is the foundational-framework layer of Alibaba's agent portfolio: it is model-bound (built on Qwen≥3.0 models, per the official README) in a way that [Qoder](/agents/qoder/) (multi-model) and [Qwen Code](/agents/qwen-code/) (multi-protocol) are not. Its relationship to the underlying models is therefore the most direct — its agent abstractions are designed around Qwen's instruction-following, tool-use, planning and memory capabilities. China AI Hub analysis indicates Qwen-Agent matters as the low-level, Qwen-native integration point, and its slowed release cadence (last release 2025-05-29) is itself a documented signal that Alibaba's agent investment has shifted toward Qwen Code and Qoder.

*Labels used above: **Official fact** (from the Qwen-Agent GitHub repo and docs), **Vendor-reported claim** (capability statements by the Qwen team), and **China AI Hub analysis** (our synthesis, always introduced as such).*
