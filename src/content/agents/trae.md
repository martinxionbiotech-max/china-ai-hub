---
agent_id: trae
agent_name: Trae
company: bytedance
description: "Trae is ByteDance's AI-native IDE. It ships two surfaces: TraeCode, positioned as a '10x AI coding engineer' for developers, and TraeWork, a 'professional AI work assistant' for non-developer knowledge work, with a web edition at work.trae.ai. Framed around 'Ship Faster with Trae,' it integrates AI into coding and general work tasks in a single product line."
agent_type: coding
underlying_models: []
framework: "AI-native IDE with a coding agent (TraeCode) and a work assistant (TraeWork); TraeWork offers a browser-based web edition at work.trae.ai."
tool_calling: true
api: false
pricing: "Not publicly documented on the marketing page (a free tier is offered; subscription tiers are documented in the product)."
deployment: cloud
open_source: false
license: proprietary
documentation: https://www.trae.ai/
use_cases:
  - AI-assisted coding and software development (TraeCode)
  - General knowledge-work assistance (TraeWork)
  - Browser-based AI work via TraeWork Web
limitations:
  - Underlying model(s) powering the coding agent are not named on the public marketing page
  - Public page is thin on feature and pricing detail; detailed documentation requires the product
  - Closed, cloud-first product; no self-hosted or open-source edition documented
last_verified: "2026-09-30"
sources:
  - source_name: Trae official site
    source_url: https://www.trae.ai/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: TraeWork web edition
    source_url: https://work.trae.ai/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: TraeCode IDE page
    source_url: https://www.trae.ai/ide/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
---
**Short answer.** Trae is ByteDance's AI-native IDE, split into two surfaces — TraeCode, a "10x AI coding engineer" for developers, and TraeWork, a "professional AI work assistant" for non-developers, with a browser-based web edition — competing in both the coding-agent and AI-workspace races under a single brand.

**Key facts.**

- Two surfaces under "Ship Faster with Trae": TraeCode (coding agent, with IDE and SOLO autonomous modes) and TraeWork (work assistant, with a web edition at work.trae.ai).
- Framed as spanning both coding and general knowledge work, in contrast to coding-only agents in the database.
- The public marketing page is deliberately sparse: it states the product split and download paths but does not name the underlying model, spell out feature tiers or publish pricing.
- Closed, cloud-first product; no self-hosted or open-source edition documented.
- Sits in ByteDance's agent portfolio alongside [Coze](/agents/coze/) and [Doubao](/agents/doubao-app/), but with a developer-IDE posture.

**What this means.** Trae is ByteDance's entry into the coding-agent and AI-workspace race — a surface-expansion bet that extends the company's agent portfolio from the consumer assistant and no-code platform into the developer IDE.

**What is uncertain.** The underlying model powering the coding agent, pricing tiers, feature depth, and whether TraeCode routes to ByteDance's own models or third-party models are not documented on the public page.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-trae-1 | Trae official site | https://www.trae.ai/ | Official | — | 2026-09-30 | high | — |
| src-agents-trae-2 | TraeWork web edition | https://work.trae.ai/ | Official | — | 2026-09-30 | high | — |
| src-agents-trae-3 | TraeCode IDE page | https://www.trae.ai/ide/ | Official | — | 2026-09-30 | high | — |

## Why it matters

Trae matters as ByteDance's coding-agent and AI-workspace bet. China AI Hub analysis indicates its structural role is surface expansion: ByteDance already has the consumer assistant ([Doubao](/agents/doubao-app/)) and the no-code platform ([Coze](/agents/coze/)), and Trae extends that portfolio into the developer IDE and the general work assistant — the two surfaces where Alibaba ([Qwen Code](/agents/qwen-code/)) and Moonshot ([Kimi Code](/agents/kimi-code/)) already compete.

China AI Hub analysis: the thin public documentation is itself the signal. Unlike ByteDance's model and API pages, which are richly documented, Trae's public page reveals little about model routing or pricing — consistent with a product still consolidating its two surfaces rather than a mature, fully documented platform. The two-surface split (TraeCode for developers, TraeWork for knowledge workers) also means Trae competes on two fronts at once, diluting a clear single-surface identity in exchange for broader reach.

China AI Hub analysis: Trae is positioned as a product bet more than a platform bet — which is why its model routing and pricing sit behind the product rather than in public docs. For a buyer, that means evaluating Trae requires trying the product, not reading a spec sheet — a lower-transparency posture than ByteDance's Ark API or Coze documentation.

## How it differs from Kimi Code and Qwen Code

Trae is a coding *and* work product, against two coding specialists.

- **[Kimi Code](/agents/kimi-code/)** is a coding agent bound to Moonshot's K3/K2.7-Code models, with a documented 1M-token output ceiling from K3.
- **[Qwen Code](/agents/qwen-code/)** is an open, multi-protocol coding agent (OpenAI/Anthropic/Gemini/Qwen plus DeepSeek/MiniMax/Z.AI/Kimi/local), notable for model choice.
- **Trae** is a closed, cloud-first IDE that splits into TraeCode (coding) and TraeWork (general work), with the underlying model undisclosed.

China AI Hub analysis: the contrast is transparency and scope. Kimi Code and Qwen Code document their models (bound to Moonshot, or multi-protocol), so a buyer can reason about the model ceiling; Trae documents neither model nor pricing publicly, so the buyer cannot — but Trae spans general knowledge work through TraeWork, which the two coding specialists do not. Trae competes on breadth of surface; the coding specialists compete on model transparency and depth.

## Practical implications

**For developers.** TraeCode offers IDE and autonomous SOLO modes, but the model powering it is undisclosed — a developer cannot confirm the model ceiling from public docs and must try the product to evaluate it.

**For non-developers.** TraeWork and its web edition extend the same brand into general knowledge work — a surface the coding specialists do not cover — but with the same sparse public documentation.

**For evaluators.** Trae is a closed, cloud-first product with no self-hosted edition, so it is not an option for teams that need data control or model transparency; those teams must look to [Qwen Code](/agents/qwen-code/) (open, multi-protocol) or [Kimi Code](/agents/kimi-code/) (open, but Moonshot-bound).

## What the evidence shows

The evidence for Trae is thin by design. The official site establishes the two-surface structure ("Ship Faster with Trae" leading to TraeCode and TraeWork downloads, plus a TraeWork Web edition) and the TraeCode IDE page documents the IDE/SOLO mode distinction — but the page stops there. No underlying model, no pricing tiers, no feature depth.

China AI Hub analysis indicates this is a transparency gap relative to ByteDance's own other surfaces: Coze documents its Doubao default and its model node, and the Ark API documents its pricing and model tiers, but Trae documents neither. The asymmetry is consistent with a product still consolidating two surfaces, and it means the database can record Trae's structure and positioning but not its model or economics — which is exactly the information a buyer most needs to reason about a coding agent.

## Where this fits

| Workload | Relevance |
|---|---|
| AI-assisted coding (TraeCode, IDE + SOLO) | High |
| General knowledge work (TraeWork + web) | High |
| Browser-based AI work (TraeWork Web) | High |
| Model-transparent coding | Low (model undisclosed) |
| Self-hosted / open-source deployment | None (closed, cloud-first) |
| Multi-protocol model routing | Not documented |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | Not publicly documented | Not publicly documented |
| Target users | Developers (TraeCode); knowledge workers (TraeWork) | Official |
| Platform | IDE (TraeCode); work assistant (TraeWork); web (TraeWork Web) | Official |
| OS | Desktop IDE + browser (web edition) | Official |
| Browser / computer use | Yes (TraeWork Web) | Vendor-reported |
| Coding | Yes (TraeCode) | Vendor-reported |
| Autonomous task execution | Yes (coding agent, work assistant) | Vendor-reported |
| MCP | Not publicly documented | Not publicly documented |
| Tool calling | Yes (coding tools) | Vendor-reported |
| Memory | Not publicly documented | Not publicly documented |
| Workflow | Coding agent + work assistant under one product line | Vendor-reported |
| API | Not publicly documented | Not publicly documented |
| Pricing | Not publicly documented on the marketing page | Not publicly documented |
| Region | Global | Official |
| Open-source | No — proprietary | Official |
| Deployment | Cloud | Official |
| Limitations | Underlying model unnamed; thin public docs; closed product | Official |
| Source | [trae.ai](https://www.trae.ai/) · [TraeWork Web](https://work.trae.ai/) | Official |
| Last verified | 2026-09-30 | Official |

See the [ByteDance](/companies/bytedance/) company profile, the [choosing-a-coding-model guide](/guides/choosing-a-coding-model/), the [choosing-an-agent guide](/guides/choosing-an-agent/), and the site's [AI agents](/technology/ai-agents/) and [tool calling](/technology/tool-calling/) technology pages. For the structural reading of Trae against the coding specialists, see the research on [the agent-led coding race](/research/china-ai-coding-models-the-agent-led-race-2/) and [Chinese AI coding models](/research/chinese-ai-coding-models/).

*Labels used above: **Official fact** (from the Trae site, TraeWork Web edition and TraeCode IDE page), **Vendor-reported claim** (positioning statements by ByteDance), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party evaluation evidence is currently recorded for Trae.*
