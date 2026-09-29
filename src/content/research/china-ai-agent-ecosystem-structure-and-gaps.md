---
title: "China AI Agent Ecosystem: Structure and Gaps"
author: "SinoAI Hub Research Team"
description: "A dependency analysis of China's 18-agent ecosystem: how tightly each agent is bound to its own vendor's models, where genuinely cross-model agents exist, and the structural gaps that openness has not filled."
published_date: "2026-09-29"
updated_date: "2026-09-29"
research_question: "How dependent is China's AI agent ecosystem on single-vendor model stacks, where do genuinely cross-model (neutral) agents exist, and what structural gaps does that dependency create?"
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
  - coze
  - yuanqi
  - baidu-appbuilder
  - dify
  - fastgpt
  - metagpt
  - manus
  - trae
author_view: true
image: "/images/cc/humanoid-robot.webp"
image_credit: "Syced / CC0, via Wikimedia Commons"
image_source: "https://commons.wikimedia.org/wiki/File:Humanoid_robot_at_Science_Square_Tsukuba.jpg"
sources:
  - source_name: "Open-AutoGLM GitHub repository"
    source_url: "https://github.com/zai-org/Open-AutoGLM"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "DeepSeek Harness documentation"
    source_url: "https://github.com/deepseek-ai/deepseek-harness"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Z.ai GLM Coding Plan pricing page"
    source_url: "https://z.ai/subscribe"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Moonshot AI Kimi Code documentation"
    source_url: "https://github.com/MoonshotAI/kimi-code"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "QwenLM Qwen-Code GitHub repository"
    source_url: "https://github.com/QwenLM/qwen-code"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "MiniMax Agent platform"
    source_url: "https://agent.minimax.io"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Qoder official site"
    source_url: "https://qoder.com/"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Qwen-Agent GitHub repository"
    source_url: "https://github.com/QwenLM/Qwen-Agent"
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: "Coze China official site"
    source_url: "https://www.coze.cn/"
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "Tencent Yuanqi official platform"
    source_url: "https://yuanqi.tencent.com/"
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "Baidu Qianfan AppBuilder documentation"
    source_url: "https://cloud.baidu.com/doc/AppBuilder/index.html"
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "Dify GitHub repository"
    source_url: "https://github.com/langgenius/dify"
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "FastGPT GitHub repository"
    source_url: "https://github.com/labring/FastGPT"
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "MetaGPT GitHub repository"
    source_url: "https://github.com/FoundationAgents/MetaGPT"
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "Manus official site"
    source_url: "https://manus.im/"
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "Trae official site"
    source_url: "https://www.trae.ai/"
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
---

All facts in this article come from the China AI Hub agent database (18 agents, last verified 2026-09-29) and the primary sources linked at the bottom. The "underlying model / platform / MCP" fields cited throughout are the deepened fields added to every agent page; where a field is recorded as "not publicly documented," the article says so rather than inferring.

## Research Question

The natural follow-up to "who builds Chinese AI agents" is "how dependent is each agent on its own vendor's models?" China's agent ecosystem is built by the same six model labs that build the models — plus a set of independent open-source platforms and agent-as-product companies — which raises a specific structural question: is the agent layer a neutral ground where tools compete on quality, or is it a distribution channel where each lab's agent funnels work to that lab's own models? The database's deepened agent fields — `underlying_models`, `framework`, `mcp` — let us measure this dependency directly rather than assert it.

## Methodology

For each of the 18 agents, we classify model binding using the `underlying_models` field and the agent's documented framework:

- **Bound**: the agent is documented to run on the vendor's own model(s), and lists no cross-vendor models.
- **Neutral / multi-model**: the agent documents support for other vendors' models or is model-agnostic by design.
- **Unspecified**: the agent's underlying model is not publicly documented (recorded as such).

We then cross-reference `mcp` and `deployment`/`open_source` fields to test a second, related question: whether the openness that characterizes the developer-facing agents also produces model neutrality, or whether openness and vendor-dependence coexist. This is a classification exercise on recorded fields, not a ranking — the goal is to describe the *structure*, not score the agents.

## Evidence

The dependency map across all 18 agents:

| Agent | Vendor | Underlying model(s) | Binding |
|---|---|---|---|
| AutoGLM | Zhipu | AutoGLM-Phone-9B (GLM-4.1V-9B family) | Bound |
| Baidu AppBuilder | Baidu | ERNIE (文心) | Bound |
| Coze | ByteDance | Doubao 2.1 (default); also DeepSeek, Kimi via model node | Neutral (multi-model platform) |
| DeepSeek Harness | DeepSeek | V4.1-Flash, V4-Pro (configurable provider) | Neutral (by design) |
| Dify | LangGenius | Model-agnostic (hundreds of LLMs) | Neutral (by design) |
| Doubao | ByteDance | Not publicly documented (unnamed chat model) | Unspecified |
| FastGPT | Labring | Model-agnostic (via AI Proxy) | Neutral (by design) |
| GLM Coding Plan | Zhipu | GLM-5.3, GLM-5.3-Flash | Bound |
| Kimi Code | Moonshot | K3, K2.7-Code, K2.7-Code-Highspeed | Bound |
| Manus | Butterfly Effect | Not publicly documented (orchestrates third-party models) | Neutral (multi-model) |
| MetaGPT | DeepWisdom | Model-agnostic (OpenAI / Azure / Ollama / Groq) | Neutral (by design) |
| MiniMax Agent | MiniMax | M3, M2.7 | Bound |
| MiniMax Code | MiniMax | M3, M2.7, M2.7-Highspeed | Bound |
| Qoder | Alibaba | Qwen3.8-Max/Flash, DeepSeek, GLM-5.3, Kimi K3, MiniMax M3 | Neutral (multi-vendor routing) |
| Qwen-Agent | Alibaba | Qwen>=3.0 (framework-level) | Bound |
| Qwen Code | Alibaba | Multi-protocol: OpenAI, Anthropic, Gemini, Qwen, DeepSeek, MiniMax, Z.AI, Kimi, OpenRouter, local | Neutral (multi-protocol) |
| Tencent Yuanqi | Tencent | Hunyuan (混元) | Bound |
| Trae | ByteDance | Not publicly documented | Unspecified |

With the eight added agents, the picture shifts in an important way. **Eight of eighteen agents are bound to their vendor's own models** — the six labs' coding and assistant agents (AutoGLM, GLM Coding Plan, Kimi Code, MiniMax Agent, MiniMax Code, Qwen-Agent) plus the two cloud platform agents (Tencent Yuanqi, Baidu AppBuilder). **Eight are neutral** — but the new neutral agents are *not* Alibaba's: they are the open-source platforms **Dify**, **FastGPT** and **MetaGPT** (model-agnostic by design), the multi-model platform **Coze**, and the model-orchestrating **Manus**. The earlier finding that neutrality was concentrated in Alibaba's two agents was an artifact of tracking only the model labs' own agents; the independent platforms and product companies are where the neutral layer actually lives. Two agents — **Doubao** and **Trae** — do not publicly name their underlying model at all (Unspecified), the closed-API posture made explicit.

## Data

The deeper fields sharpen the picture beyond the binding table.

**MCP support is now near-universal on the open agents.** The database records `mcp: true` on eleven of eighteen agents — every open-source developer and platform agent (DeepSeek Harness, Kimi Code, MiniMax Code, Qwen Code, Qwen-Agent, GLM Coding Plan, Qoder, Dify, FastGPT) plus two closed cloud platforms (Coze, Baidu AppBuilder). The exceptions are the consumer/phone surfaces (Doubao, MiniMax Agent, AutoGLM's phone-use API, Tencent Yuanqi, Manus, Trae) and the research framework MetaGPT. This is the MCP asymmetry: the tool-interoperability standard is largely an *open-agent* phenomenon, which makes sense — MCP is how a neutral agent reaches arbitrary tools, and a bound agent has less need for it.

**Openness and model-neutrality now do travel together — but only outside the model labs.** Nine of eighteen agents are open source. Among the six model labs' open agents (AutoGLM, Kimi Code, MiniMax Code, Qwen-Agent, DeepSeek Harness, Qwen Code), five are still model-bound; only Qwen Code is both open and cross-model. But the three independent open platforms — Dify, FastGPT and MetaGPT — are open source *and* model-neutral by design. The finding therefore splits: **inside the labs, open source is about code, not model choice** (a lab happily open-sources an agent that still routes to its own models); **outside the labs, openness and neutrality coincide**, because an independent platform has no model of its own to funnel to.

**The neutral layer is concentrated outside the model labs.** Within the six labs, Alibaba still fields the only two cross-model agents — Qoder (closed, multi-vendor routing) and Qwen Code (open, multi-protocol) — because it is the one lab with a broad-enough platform (Model Studio's multi-model hosting plus its own Qwen family) to sell neutrality without cannibalizing itself. But the neutral layer as a whole is now dominated by the independent players: Dify, FastGPT, MetaGPT and Manus are all cross-model, and none is a model lab. China AI Hub analysis: the concentration of neutrality has moved — it used to look like a single vendor's property, and it is now revealed as a property of independence from model ownership.

**Model-bound agents track their vendor's capability ceiling.** Kimi Code is bound to K3/K2.7-Code, so its long-horizon whole-repo strength is exactly K3's 1M-token output. GLM Coding Plan is bound to GLM-5.3/5.3-Flash, so its 1M-token context claim is GLM-5.3's context. MiniMax Code defaults to M2.7 in the UI with M3 available. The two cloud platform agents extend the same pattern: Tencent Yuanqi is bound to Hunyuan and Baidu AppBuilder to ERNIE, so neither can route around its vendor's model. The agent's ceiling is the vendor's model ceiling — there is no fallback to a stronger competitor model within a bound agent.

**Deployment and audience split along the same lines.** The self-hosted agents are all open-source frameworks — DeepSeek Harness, Qwen-Agent, Qwen Code, MetaGPT — plus Dify and FastGPT, which support both; the cloud-only agents (Doubao, GLM Coding Plan, MiniMax Agent, Tencent Yuanqi, Baidu AppBuilder, Coze, Manus, Trae) are all closed. Four existing agents support both (AutoGLM, Kimi Code, MiniMax Code, Qoder), as do Dify and FastGPT. The self-hosted-open / cloud-closed split is the same pattern the model layer already runs: the developer-facing, do-it-yourself surface is open, and the managed, monetized surface is closed. Where a vendor sits in the agent stack is therefore highly predictive of how its agent is priced and locked — and that, in turn, predicts how dependent the buyer becomes.

## Analysis

China AI Hub analysis indicates: the Chinese agent ecosystem is better described as **two layers — a model-labs layer that is a set of model-distribution channels, and an independent layer that is a neutral tool market.** Eight of eighteen agents exist, at least in part, to route usage to a vendor's own models — the same strategy, one layer up, that the model labs already run with their open-vs-closed dual tracks. The agent is where a lab converts model capability into a sticky product (a coding agent bound to K3, a subscription plan bound to GLM-5.3) that the lab, not the buyer, controls. But alongside it sits an independent layer — Dify, FastGPT, MetaGPT, Manus — that owns no model and competes precisely by being neutral.

China AI Hub analysis indicates: the scarcity of cross-model agents *within the model labs* is structural and not accidental. A genuinely neutral agent is a threat to every model vendor, because it lets the buyer swap the model under the tool. The only lab that fields neutral agents is Alibaba — Qwen Code and Qoder — the vendor with the least to lose from model-swapping (it hosts competitors' models on Model Studio anyway, and its own Qwen family is strong enough to win on merit). A bound-agent vendor (Moonshot, Zhipu, MiniMax, Tencent, Baidu, ByteDance) has no incentive to build a neutral agent, because neutrality would cannibalize its own model revenue. The neutral layer therefore had to come from outside — and it did: Dify, FastGPT, MetaGPT and Manus are all cross-model, and none owns a foundation model.

China AI Hub analysis indicates: the buyer's neutral-option picture has changed materially. A buyer who wants one neutral, open, self-hostable agent now has several independent choices — Dify (general workflows), FastGPT (knowledge-base RAG) and MetaGPT (multi-agent framework) — in addition to Alibaba's Qwen Code. The earlier "single point of concentration" reading is revised: the neutral layer is no longer one vendor's product but a small cluster of independent open platforms. What remains true is that no *model lab other than Alibaba* ships a neutral agent, so the labs' own surfaces stay vendor-bound while neutrality is supplied by independents.

## Counterpoints / Limitations

Several counterpoints apply. **First, "bound" is not a defect for most users.** A developer who has chosen DeepSeek's price floor, or K3's output length, or GLM-5.3's open 1M weights, may prefer a bound agent that is optimized for that model. Neutrality is a feature only for buyers who want to hedge or swap; for committed users it is irrelevant.

**Second, the binding classification relies on documented `underlying_models`, which is a snapshot.** Agents change their model support frequently, and a "bound" agent today may add cross-vendor support next month. The database's last_verified date is 2026-09-29.

**Third, neutrality claims are themselves vendor-reported.** Qwen Code's multi-protocol support and Qoder's multi-model routing are documented by Alibaba, and Dify, FastGPT and MetaGPT's model-agnosticism is documented by their own READMEs; the database does not independently test whether a cross-vendor model actually performs well inside those agents. Documented support is not the same as verified quality.

**Fourth, the sample is still selected.** Eighteen agents is a broader snapshot but not a census; a neutral agent from a smaller, un-tracked vendor could exist and be missing. The expansion to independent platforms is itself a selection choice — it widened the neutral set precisely because it added non-lab players.

**Fifth, "unspecified" (Doubao's and Trae's unnamed models) is a data gap, not evidence of dependency.** It is consistent with ByteDance's closed posture, but the classification rests on absence of documentation, which is weaker evidence than a documented bound model.

## China AI Hub Interpretation

Our interpretation: **China's agent ecosystem is vertically integrated in its labs and neutral in its independents — the two halves of the market are splitting cleanly.** The frontier labs treat agents the way they treat open weights: as a distribution and monetization layer for their own models, not as a neutral tool market. But the neutral layer, once invisible because only the labs were tracked, turns out to exist — and to be supplied by companies that own no model. The genuinely open question is no longer whether a neutral layer will emerge, but whether the labs will try to absorb it (by acquiring or bundling against the independents) or whether the market keeps its two-layer structure.

We flag the uncertainty directly: the "gap" we describe is a gap relative to a *neutral-market ideal*, not relative to what Chinese buyers demonstrably need. If most Chinese developers are loyal to one vendor's model family, the scarcity of cross-model agents is not a market failure but an efficient reflection of demand. The database cannot tell us which — it records what agents are documented to support, not what buyers actually want. We present the structural observation as evidence-backed, and the "gap" framing as our interpretation of it.

## Conclusion

China's 18-agent ecosystem splits into two layers. Inside the six model labs, the structure is still dependent: eight agents are bound to their vendor's own models, and only Alibaba ships a cross-model agent. But the neutral layer — once invisible — is now populated by independent open platforms and product companies (Dify, FastGPT, MetaGPT, Manus, Coze) that own no foundation model. The deepest finding is unchanged at the lab layer: MCP and open-source code have spread widely while model-neutrality has not — but it is now clear that the tool-interoperability and model-selection layers are standardizing on opposite sides of the market, with the labs standardizing their vendor-bound stacks and the independents standardizing neutrality. For a buyer who wants one agent across the whole Chinese model landscape, the neutral options are now the independents first, and Alibaba's Qwen Code among the labs.

## Sources

See the Sources list in the page metadata — the binding classification, MCP flags and framework descriptions trace to each agent's official GitHub repository, product page and documentation, verified 2026-09-29.

*Labels used above: **Official fact** (underlying-model, MCP, license and deployment fields from official agent pages), **Vendor-reported claim** (multi-model and multi-protocol support statements), and **China AI Hub analysis** (the binding classification and our interpretation, always introduced as such).*
