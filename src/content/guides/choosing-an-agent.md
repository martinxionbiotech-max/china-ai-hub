---
image: "/images/ai/technologies-ai-agents.webp"
image_credit: "AI-generated illustration (Seedream)"
title: "Choosing a Chinese AI Agent: Underlying Models, Tool Calling and MCP"
author: "SinoAI Hub Research Team"
description: "A decision guide for building on Chinese AI agents — how model binding, tool calling, MCP support, deployment and openness decide which of the ten tracked agents fits a given workload."
published_date: "2026-09-29"
updated_date: "2026-09-29"
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
sources:
  - source_name: "China AI Hub — Agents database"
    source_url: "https://sinoaihub.com/agents/"
    source_type: independent
  - source_name: "China AI Hub — Models database"
    source_url: "https://sinoaihub.com/models/"
    source_type: independent
  - source_name: "DeepSeek Harness GitHub repository"
    source_url: "https://github.com/deepseek-ai/DeepSeek-Harness"
    source_type: official
  - source_name: "Qwen Code GitHub repository"
    source_url: "https://github.com/QwenLM/qwen-code"
    source_type: official
---

**Short answer.** The ten agents tracked in the database are mostly distribution channels for their vendor's own models: seven are bound to a single lab's models, and only two are genuinely cross-model — [Qoder](/agents/qoder/) (closed, smart-routes across Qwen, DeepSeek, GLM, Kimi and MiniMax) and [Qwen Code](/agents/qwen-code/) (open, multi-protocol across OpenAI, Anthropic, Gemini, Qwen and others). So the first question is not "which agent" but "am I buying a tool or a model contract." If you need model freedom, pick a cross-model agent; if you have already standardized on one lab's model, its native agent is usually the tightest integration.

## Decision criteria

| Criteria | Relevance / Notes |
|---|---|
| Model binding | 7/10 bound to vendor models; only Qoder and Qwen Code are cross-model; DeepSeek Harness is neutral by architecture |
| Tool calling | Present on all ten agents as a documented capability |
| MCP support | `mcp: true` on 7/10 — every open developer agent; absent on Doubao, MiniMax Agent, AutoGLM |
| Open source | 6/10 open — but 5 of those 6 are still model-bound; only Qwen Code is open *and* cross-model |
| Deployment | Self-hosted (DeepSeek Harness, Qwen-Agent, Qwen Code) vs cloud-only (Doubao, GLM Coding Plan, MiniMax Agent) vs both |
| Computer use / browser | Desktop-capable agents (Kimi Code, MiniMax Code, Qoder, AutoGLM) vs CLI/API-only |
| Underlying model ceiling | A bound agent's ceiling is its vendor's model — Kimi Code's 1M output is K3's; GLM Coding Plan's 1M context is GLM-5.3's |

## The ten agents at a glance

| Agent | Vendor | Underlying model(s) | Binding | Open | MCP |
|---|---|---|---|---|---|
| [AutoGLM](/agents/autoglm/) | Zhipu | AutoGLM-Phone-9B (GLM-4.1V-9B) | Bound | Yes | No |
| [DeepSeek Harness](/agents/deepseek-harness/) | DeepSeek | V4.1-Flash, V4-Pro | Neutral (configurable) | Yes | Yes |
| [Doubao](/agents/doubao-app/) | ByteDance | Not publicly documented | Unspecified | No | No |
| [GLM Coding Plan](/agents/glm-coding-plan/) | Zhipu | GLM-5.3, GLM-5.3-Flash | Bound | No | Yes |
| [Kimi Code](/agents/kimi-code/) | Moonshot | K3, K2.7-Code, K2.7-Highspeed | Bound | Yes | Yes |
| [MiniMax Agent](/agents/minimax-agent/) | MiniMax | M3, M2.7 | Bound | No | No |
| [MiniMax Code](/agents/minimax-code/) | MiniMax | M3, M2.7, M2.7-Highspeed | Bound | Yes | Yes |
| [Qoder](/agents/qoder/) | Alibaba | Qwen, DeepSeek, GLM, Kimi, MiniMax | Neutral (routing) | No | Yes |
| [Qwen-Agent](/agents/qwen-agent/) | Alibaba | Qwen>=3.0 | Bound | Yes | Yes |
| [Qwen Code](/agents/qwen-code/) | Alibaba | Multi-protocol + local | Neutral | Yes | Yes |

## Entity routing

Route by what you actually need the agent to be.

| Scenario | Best-documented fit | Why |
|---|---|---|
| Cross-vendor routing, closed product | [Qoder](/agents/qoder/) | Smart-routes tasks by credit tier across five vendors |
| Cross-protocol, open framework | [Qwen Code](/agents/qwen-code/) | OpenAI/Anthropic/Gemini/Qwen + DeepSeek/MiniMax/Z.AI/Kimi/local |
| Configurable-provider open runtime | [DeepSeek Harness](/agents/deepseek-harness/) | "Everything is a Plugin," MCP, self-hosted |
| Whole-repo coding bound to Moonshot | [Kimi Code](/agents/kimi-code/) | Open, MCP, browser/computer-use, 1M context via K3 |
| Subscription coding bound to Zhipu | [GLM Coding Plan](/agents/glm-coding-plan/) | GLM-5.3/5.3-Flash, quota-based, powers 20+ tools |
| Open desktop coding bound to MiniMax | [MiniMax Code](/agents/minimax-code/) | M3/M2.7, MCP, memory, macOS/Windows desktop |
| Phone-use autonomous agent | [AutoGLM](/agents/autoglm/) | AutoGLM-Phone-9B, computer use, ~24GB+ VRAM local |
| Consumer/closed surface | [Doubao](/agents/doubao-app/) | Unnamed chat model, cloud-only, no consumer API |
| Cloud assistant ecosystem | [MiniMax Agent](/agents/minimax-agent/) | M3/M2.7, 24/7 assistant, no self-host |
| Python framework bound to Qwen | [Qwen-Agent](/agents/qwen-agent/) | Qwen>=3.0, RAG, MCP, self-hosted |

## What the evidence shows

The dependency map is lopsided in a way that matters. Seven of ten agents route usage to their lab's own models, and openness does not imply model freedom — five of the six open-source agents are still model-bound. The only open-source *and* cross-model agent is Qwen Code; the only closed cross-model agent is Qoder, and both are Alibaba products. China AI Hub analysis indicates that concentration is structural, not accidental: a genuinely neutral agent lets the buyer swap the model under the tool, which threatens every model vendor — so the one lab with a broad enough platform (Model Studio hosts competitors' models) is the only one positioned to sell neutrality.

MCP support is near-universal on the open agents (7/10) but absent on the three closed/consumer surfaces — the tool-interoperability standard is an open-agent phenomenon, which makes sense because MCP is how a neutral agent reaches arbitrary tools, and a bound agent has less need for it. Deployment splits along the same self-hosted-open / cloud-closed line as the model layer: the do-it-yourself surface is open, the managed surface is closed, and where a vendor sits in the stack is highly predictive of how its agent is priced and locked — which in turn predicts how dependent the buyer becomes.

A second structural finding: model-bound agents track their vendor's capability ceiling. Kimi Code is bound to K3/K2.7-Code, so its long-horizon whole-repo strength is exactly K3's 1M-token output. GLM Coding Plan is bound to GLM-5.3/5.3-Flash, so its 1M-token context claim is GLM-5.3's context. Within a bound agent there is no fallback to a stronger competitor model — the agent's ceiling is the vendor's model ceiling.

## Selection procedure

Work through these steps in order.

1. **Decide model freedom versus integration depth.** If you need to swap models under the tool, the shortlist is two entries — [Qoder](/agents/qoder/) (closed, cross-vendor routing) and [Qwen Code](/agents/qwen-code/) (open, multi-protocol). If you are already standardized on one lab's models, that lab's native agent is the tightest integration.
2. **Check whether you can self-host.** Three agents are self-hosted frameworks ([DeepSeek Harness](/agents/deepseek-harness/), [Qwen-Agent](/agents/qwen-agent/), [Qwen Code](/agents/qwen-code/)); three are cloud-only ([Doubao](/agents/doubao-app/), [GLM Coding Plan](/agents/glm-coding-plan/), [MiniMax Agent](/agents/minimax-agent/)); four support both. If you cannot use a managed cloud endpoint, that cuts the field in half.
3. **Confirm the capability surface you actually need.** MCP is near-universal on the open agents but absent on the closed ones; computer use and browser control are desktop-capabilities (Kimi Code, MiniMax Code, Qoder, AutoGLM). Match the flag to your workload, not to the vendor's pitch.
4. **Trace the underlying model ceiling.** A bound agent's ceiling is its vendor's model: Kimi Code's 1M output is K3's, GLM Coding Plan's 1M context is GLM-5.3's. If your job needs a capability only a different vendor's model has, a bound agent cannot give it to you.
5. **Read the pricing and lock-in before adopting.** Subscription plans carry quota caps, peak-hour multipliers and expiry rules that are separate from pay-as-you-go API pricing, and they are not fully extractable from sign-in-gated pages.

## Limitations

Agent products have no independent evaluation data in the database — every capability here is a vendor-listed capability flag, not a measured result. "Underlying model" is recorded as documented by the vendor; where a field is not publicly stated (Doubao's chat model, several first-release dates) the database records the absence rather than inferring. Model-binding classification is a description of documented fields, not a performance ranking. MCP support being absent on a closed agent means the vendor does not list it, not that it is impossible. DeepSeek Harness is a developer preview — its own SAFETY.md notes it is not security-audited or production-ready.

## Sources

- [China AI Hub — Agents database](/agents/)
- [China AI Hub — Models database](/models/)
- [DeepSeek Harness GitHub repository](https://github.com/deepseek-ai/DeepSeek-Harness)
- [Qwen Code GitHub repository](https://github.com/QwenLM/qwen-code)

*Labels used above: **Official fact** (framework, license, MCP and deployment fields from primary sources and repositories), **Vendor-reported claim** (underlying-model and capability statements published by the vendor), and **China AI Hub analysis** (our synthesis, introduced as such). No third-party evaluation evidence is currently recorded for any of the ten agents.*
