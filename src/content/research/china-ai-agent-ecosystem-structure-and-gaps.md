---
title: "China AI Agent Ecosystem: Structure and Gaps"
author: "SinoAI Hub Research Team"
description: "A dependency analysis of China's 10-agent ecosystem: how tightly each agent is bound to its own vendor's models, where genuinely cross-model agents exist, and the structural gaps that openness has not filled."
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
---

All facts in this article come from the China AI Hub agent database (10 agents, last verified 2026-09-20) and the primary sources linked at the bottom. The "underlying model / platform / MCP" fields cited throughout are the deepened fields added to every agent page; where a field is recorded as "not publicly documented," the article says so rather than inferring.

## Research Question

The natural follow-up to "who builds Chinese AI agents" is "how dependent is each agent on its own vendor's models?" China's agent ecosystem is built by the same six labs that build the models, which raises a specific structural question: is the agent layer a neutral ground where tools compete on quality, or is it a distribution channel where each lab's agent funnels work to that lab's own models? The database's deepened agent fields — `underlying_models`, `framework`, `mcp` — let us measure this dependency directly rather than assert it.

## Methodology

For each of the 10 agents, we classify model binding using the `underlying_models` field and the agent's documented framework:

- **Bound**: the agent is documented to run on the vendor's own model(s), and lists no cross-vendor models.
- **Neutral / multi-model**: the agent documents support for other vendors' models or is model-agnostic by design.
- **Unspecified**: the agent's underlying model is not publicly documented (recorded as such).

We then cross-reference `mcp` and `deployment`/`open_source` fields to test a second, related question: whether the openness that characterizes the developer-facing agents also produces model neutrality, or whether openness and vendor-dependence coexist. This is a classification exercise on recorded fields, not a ranking — the goal is to describe the *structure*, not score the agents.

## Evidence

The dependency map across all 10 agents:

| Agent | Vendor | Underlying model(s) | Binding |
|---|---|---|---|
| AutoGLM | Zhipu | AutoGLM-Phone-9B (GLM-4.1V-9B family) | Bound |
| DeepSeek Harness | DeepSeek | V4.1-Flash, V4-Pro (configurable provider) | Neutral (by design) |
| Doubao | ByteDance | Not publicly documented (unnamed chat model) | Unspecified |
| GLM Coding Plan | Zhipu | GLM-5.3, GLM-5.3-Flash | Bound |
| Kimi Code | Moonshot | K3, K2.7-Code, K2.7-Code-Highspeed | Bound |
| MiniMax Agent | MiniMax | M3, M2.7 | Bound |
| MiniMax Code | MiniMax | M3, M2.7, M2.7-Highspeed | Bound |
| Qoder | Alibaba | Qwen3.8-Max/Flash, DeepSeek, GLM-5.3, Kimi K3, MiniMax M3 | Neutral (multi-vendor routing) |
| Qwen-Agent | Alibaba | Qwen>=3.0 (framework-level) | Bound |
| Qwen Code | Alibaba | Multi-protocol: OpenAI, Anthropic, Gemini, Qwen, DeepSeek, MiniMax, Z.AI, Kimi, OpenRouter, local | Neutral (multi-protocol) |

The pattern is immediate and lopsided. **Seven of ten agents are bound to their vendor's own models.** Only two are genuinely cross-model: **Qoder** (which smart-routes tasks across Qwen, DeepSeek, GLM, Kimi and MiniMax models by credit tier) and **Qwen Code** (whose multi-protocol framework supports OpenAI, Anthropic, Gemini and Qwen APIs plus DeepSeek, MiniMax, Z.AI, Kimi, OpenRouter and local models). One agent — **DeepSeek Harness** — is neutral by *architecture* (its "Everything is a Plugin" design lets you configure any provider) but its documented pricing mirrors DeepSeek's own flash/V4-Pro tiers, so its neutrality is architectural rather than demonstrated in practice. One agent — **Doubao** — does not publicly name its chat model at all, which is the closed-API posture made explicit.

## Data

The deeper fields sharpen the picture beyond the binding table.

**MCP support is now near-universal on the open agents.** The database records `mcp: true` on seven of ten agents. Every open-source developer agent (DeepSeek Harness, Kimi Code, MiniMax Code, Qwen Code, Qwen-Agent, GLM Coding Plan) documents MCP support; the three closed/consumer surfaces (Doubao, MiniMax Agent, and AutoGLM's phone-use API) do not. This is the MCP asymmetry: the tool-interoperability standard is an *open-agent* phenomenon, which makes sense — MCP is how a neutral agent reaches arbitrary tools, and a bound agent has less need for it.

**Openness and model-neutrality do not travel together.** Six of ten agents are open source, but five of those six are still model-bound (AutoGLM, Kimi Code, MiniMax Code, Qwen-Agent, and DeepSeek Harness in its default pairing). The only open-source *and* cross-model agent is Qwen Code. This is the finding that matters most: **open source in this ecosystem is about code, not about model choice.** A lab will happily open-source its agent while that agent still routes work to the lab's own models.

**Alibaba fields the only two cross-model agents.** Qoder (closed, multi-vendor routing) and Qwen Code (open, multi-protocol) are both Alibaba products. No other vendor ships an agent that meaningfully documents support for a competitor's models. China AI Hub analysis: that concentration is itself a structural fact — the one lab with a broad-enough platform (Model Studio's multi-model hosting plus its own Qwen family) is the only one positioned to sell neutrality.

**Model-bound agents track their vendor's capability ceiling.** Kimi Code is bound to K3/K2.7-Code, so its long-horizon whole-repo strength is exactly K3's 1M-token output. GLM Coding Plan is bound to GLM-5.3/5.3-Flash, so its 1M-token context claim is GLM-5.3's context. MiniMax Code defaults to M2.7 in the UI with M3 available. The agent's ceiling is the vendor's model ceiling — there is no fallback to a stronger competitor model within a bound agent.

**Deployment and audience split along the same lines.** The three self-hosted agents (DeepSeek Harness, Qwen-Agent, Qwen Code) are all open-source frameworks; the three cloud-only agents (Doubao, GLM Coding Plan, MiniMax Agent) are all closed. Four agents support both (AutoGLM, Kimi Code, MiniMax Code, Qoder). The self-hosted-open / cloud-closed split is the same pattern the model layer already runs: the developer-facing, do-it-yourself surface is open, and the managed, monetized surface is closed. Where a vendor sits in the agent stack is therefore highly predictive of how its agent is priced and locked — and that, in turn, predicts how dependent the buyer becomes.

## Analysis

China AI Hub analysis indicates: the Chinese agent ecosystem is better described as **a set of model-distribution channels than as a neutral tool market.** Seven of ten agents exist, at least in part, to route usage to the lab's own models — the same strategy, one layer up, that the model labs already run with their open-vs-closed dual tracks. The agent is where a lab converts model capability into a sticky product (a coding agent bound to K3, a subscription plan bound to GLM-5.3) that the lab, not the buyer, controls.

China AI Hub analysis indicates: the scarcity of cross-model agents is the ecosystem's largest structural gap, and it is not accidental. A genuinely neutral agent is a threat to every model vendor, because it lets the buyer swap the model under the tool. The two agents that are neutral — Qwen Code and Qoder — are both from Alibaba, the vendor with the least to lose from model-swapping (it hosts competitors' models on Model Studio anyway, and its own Qwen family is strong enough to win on merit). A bound-agent vendor (Moonshot, Zhipu, MiniMax) has no incentive to build a neutral agent, because neutrality would cannibalize its own model revenue.

China AI Hub analysis indicates: the gap matters most for buyers, who currently have no neutral, open, self-hostable agent that spans the full Chinese model landscape except Qwen Code. That is a single point of concentration: if you want one agent tool that can drive Qwen, DeepSeek, GLM, Kimi and MiniMax models without vendor lock-in, the database records exactly one — and it is built by Alibaba. The counter-position is that this is a feature of the market's maturity stage rather than a failure: Chinese labs are integrating vertically (model → agent → subscription) because vertical integration is how they monetize, and neutrality is a second-order property that only a platform-scale vendor can afford to offer.

## Counterpoints / Limitations

Several counterpoints apply. **First, "bound" is not a defect for most users.** A developer who has chosen DeepSeek's price floor, or K3's output length, or GLM-5.3's open 1M weights, may prefer a bound agent that is optimized for that model. Neutrality is a feature only for buyers who want to hedge or swap; for committed users it is irrelevant.

**Second, the binding classification relies on documented `underlying_models`, which is a snapshot.** Agents change their model support frequently, and a "bound" agent today may add cross-vendor support next month. The database's last_verified date is 2026-09-20.

**Third, neutrality claims are themselves vendor-reported.** Qwen Code's multi-protocol support and Qoder's multi-model routing are documented by Alibaba; the database does not independently test whether a cross-vendor model actually performs well inside those agents. Documented support is not the same as verified quality.

**Fourth, the sample is small and selected.** Ten agents is a snapshot of prominent offerings, not a census; a neutral agent from a smaller, un-tracked vendor could exist and be missing.

**Fifth, "unspecified" (Doubao's unnamed model) is a data gap, not evidence of dependency.** It is consistent with ByteDance's closed posture, but the classification rests on absence of documentation, which is weaker evidence than a documented bound model.

## China AI Hub Interpretation

Our interpretation: **China's agent ecosystem is vertically integrated first, neutral second — and the neutrality is concentrated in a single vendor.** We read the data as showing that the frontier labs treat agents the way they treat open weights: as a distribution and monetization layer for their own models, not as a neutral tool market. The genuinely open question the data raises is whether a neutral-agent layer will emerge at all, or whether the Chinese market settles into six parallel vertical stacks (model + agent + subscription) that interoperate only through APIs and MCP.

We flag the uncertainty directly: the "gap" we describe is a gap relative to a *neutral-market ideal*, not relative to what Chinese buyers demonstrably need. If most Chinese developers are loyal to one vendor's model family, the scarcity of cross-model agents is not a market failure but an efficient reflection of demand. The database cannot tell us which — it records what agents are documented to support, not what buyers actually want. We present the structural observation as evidence-backed, and the "gap" framing as our interpretation of it.

## Conclusion

China's 10-agent ecosystem is structurally dependent: seven agents are bound to their vendor's own models, openness (six open-source agents) does not imply model neutrality, and only two agents — both Alibaba's — are genuinely cross-model. The deepest finding is that MCP and open-source code have spread widely while model-neutrality has not, which means the tool-interoperability layer is standardizing even as the model-selection layer stays vendor-bound. For a buyer who wants one agent across the whole Chinese model landscape, the database records a single neutral option — and it is a reason to watch Alibaba's platform position as much as any individual model's benchmark score.

## Sources

See the Sources list in the page metadata — the binding classification, MCP flags and framework descriptions trace to each agent's official GitHub repository, product page and documentation, verified 2026-09-20.

*Labels used above: **Official fact** (underlying-model, MCP, license and deployment fields from official agent pages), **Vendor-reported claim** (multi-model and multi-protocol support statements), and **China AI Hub analysis** (the binding classification and our interpretation, always introduced as such).*
