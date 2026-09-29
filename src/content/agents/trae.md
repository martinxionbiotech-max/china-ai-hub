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
last_verified: "2026-09-29"
sources:
  - source_name: Trae official site
    source_url: https://www.trae.ai/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: TraeWork web edition
    source_url: https://work.trae.ai/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
---
**What it is.** Trae is ByteDance's AI-native IDE, split into two surfaces: TraeCode, a "10x AI coding engineer" for developers, and TraeWork, a "professional AI work assistant" for non-developers, with a browser-based web edition. **Why it matters.** It is ByteDance's entry into the coding-agent and AI-workspace race, competing with [Kimi Code](/agents/kimi-code/) and [Qwen Code](/agents/qwen-code/) on the developer side while extending into general knowledge work. **Key characteristics.** A "Ship Faster with Trae" framing, a coding agent plus a work assistant under one product line, and a TraeWork Web edition. **What a professional should know.** The public marketing page is thin — it does not name the underlying model powering the coding agent, and pricing tiers are documented in-product rather than on the page — so it is a closed, cloud-first product with fewer publicly documented facts than ByteDance's other agent surfaces.

Trae presents itself as a unified AI work product line: "Ship Faster with Trae" leads to two downloads — TraeCode ("Your 10x AI Coding Engineer") and TraeWork ("Your Professional AI Work Assistant"), plus a TraeWork Web edition at work.trae.ai. This positions the product as spanning both coding and general knowledge work, in contrast to the coding-only agents in the database.

The public marketing page is deliberately sparse: it states the product split and the download paths but does not name the underlying model, spell out feature tiers or publish pricing. As a ByteDance product, Trae sits alongside [Coze](/agents/coze/) and [Doubao](/agents/doubao-app/) in the company's agent portfolio, but with a developer-IDE posture rather than a no-code platform or consumer assistant posture.

See the [ByteDance](/companies/bytedance/) profile.

## Why it matters

Trae matters as ByteDance's coding-agent and AI-workspace bet. China AI Hub analysis indicates its structural role is surface expansion: ByteDance already has the consumer assistant ([Doubao](/agents/doubao-app/)) and the no-code platform ([Coze](/agents/coze/)), and Trae extends that portfolio into the developer IDE and the general work assistant — the two surfaces where Alibaba ([Qwen Code](/agents/qwen-code/)) and Moonshot ([Kimi Code](/agents/kimi-code/)) already compete. The thin public documentation is itself a signal: unlike ByteDance's model and API pages, which are richly documented, Trae's public page reveals little about model routing or pricing, which is consistent with a product still consolidating its two surfaces rather than a mature, fully documented platform. China AI Hub analysis: the thin public documentation is therefore the key signal — Trae is positioned as a product bet (an AI IDE plus a work assistant under one brand) more than a platform bet, which is why its model routing and pricing sit behind the product rather than in public docs. For a buyer, that means evaluating Trae requires trying the product, not reading a spec sheet — a lower-transparency posture than ByteDance's Ark API or Coze documentation. Its two-surface split (TraeCode for developers, TraeWork for knowledge workers) also means it competes on two fronts at once.

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
| Last verified | 2026-09-29 | Official |

## What is uncertain

- The underlying model powering the coding agent is not named on the public marketing page.
- Pricing tiers are not published on the marketing page and require the product.
- Feature detail is thin on the public page; deeper documentation requires using the product.
- Whether TraeCode routes to ByteDance's own models or third-party models is not documented publicly.
- No independent third-party evaluation of Trae is recorded in this database.

*Labels used above: **Official fact** (from the Trae site and TraeWork Web edition), **Vendor-reported claim** (positioning statements by ByteDance), and **China AI Hub analysis** (our synthesis, always introduced as such).*
