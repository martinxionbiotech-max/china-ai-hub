---
agent_id: yuanqi
agent_name: Tencent Yuanqi (腾讯元器)
company: tencent
description: "Tencent's agent development platform (腾讯元器): a platform for building and deploying AI agents (智能体) on Tencent's Hunyuan (混元) foundation models. Supports zero-code agent creation, knowledge bases, workflows and a plugin plaza, with one-click publishing to WeChat official accounts, QQ and other Tencent channels. Category templates include WeChat-official-account agents, customer-service assistants, efficiency tools and IP personas."
agent_type: platform
underlying_models: []
framework: "Zero-code agent builder with knowledge base, workflow orchestration and a plugin plaza; agent templates and an agent square (智能体广场) for discovering and remixing published agents."
tool_calling: true
memory: true
planning: true
api: true
pricing: "Not publicly documented (platform provides a free tier; model usage billed through Tencent Cloud Hunyuan APIs; enterprise solutions priced separately)."
deployment: cloud
open_source: false
license: proprietary
documentation: https://yuanqi.tencent.com/
use_cases:
  - WeChat official-account agents (公众号智能体) answering reader questions
  - Customer-service assistants for government and enterprise
  - Knowledge-base Q&A agents
  - IP personas that mirror a creator's voice
  - Enterprise AI agent solutions on Tencent Cloud
limitations:
  - Public pages do not state the underlying Hunyuan model version behind agents
  - Pricing is not published on the static marketing page; requires a logged-in console
  - Platform is cloud-only; no self-hosted edition
  - A system upgrade split the platform into old/new versions that do not sync directly (per the in-product notice)
last_verified: "2026-09-30"
sources:
  - source_name: Tencent Yuanqi official platform
    source_url: https://yuanqi.tencent.com/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Tencent Hunyuan model product page (Tencent Cloud)
    source_url: https://cloud.tencent.com/product/tclm
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Tencent Hunyuan official site
    source_url: https://hunyuan.tencent.com/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Tencent Hunyuan open platform
    source_url: https://open.hunyuan.tencent.com/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
---
**Short answer.** Tencent Yuanqi (腾讯元器) is Tencent's zero-code agent development platform for building and deploying agents (智能体) on the Hunyuan (混元) model family, with one-click publishing to WeChat official accounts and QQ — the agent surface through which Tencent routes its models into the WeChat ecosystem.

**Key facts.**

- A zero-code agent builder with knowledge bases, workflow orchestration and a plugin plaza, plus an agent square (智能体广场) for discovering and remixing published agents.
- Category templates are channel-led: WeChat-official-account agents, customer-service assistants, efficiency tools and IP personas.
- Publishes agents to WeChat official accounts (公众号智能体), QQ and other Tencent channels — an agent can ingest a public account's historical articles and answer reader questions.
- Built on Tencent's Hunyuan foundation-model family; the public pages do not name the specific Hunyuan model version behind a given agent.
- Cloud-only and proprietary; no self-hosted edition.
- Pricing is not published on the static marketing page; model usage is billed through Tencent Cloud Hunyuan APIs.
- An in-product notice indicates a recent system upgrade split the platform into old/new versions that do not sync directly.

**What this means.** Yuanqi is Tencent's binding layer between its Hunyuan models and the WeChat distribution channel — the most valuable consumer surface in China. A WeChat-official-account agent is not a neutral tool but a Hunyuan-backed extension of the account itself.

**What is uncertain.** The exact Hunyuan model version behind each agent, the full pricing structure, the migration path across the old/new version split, and whether agents can route to non-Hunyuan models are all undocumented on public pages.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-yuanqi-1 | Tencent Yuanqi official platform | https://yuanqi.tencent.com/ | Official | — | 2026-09-30 | high | — |
| src-agents-yuanqi-2 | Tencent Hunyuan model product page (Tencent Cloud) | https://cloud.tencent.com/product/tclm | Official | — | 2026-09-30 | high | — |
| src-agents-yuanqi-3 | Tencent Hunyuan official site | https://hunyuan.tencent.com/ | Official | — | 2026-09-30 | high | — |
| src-agents-yuanqi-4 | Tencent Hunyuan open platform | https://open.hunyuan.tencent.com/ | Official | — | 2026-09-30 | high | — |

## Why it matters

Yuanqi matters because it is the purest expression of channel-integration as an agent strategy in this database. Every large platform binds its agent surface to a distribution asset, but only Yuanqi is attached to WeChat — the channel where Chinese consumers and creators already live. Its category skew (WeChat-official-account agents, customer service, government service, IP personas) reflects deployment, not developer tooling.

China AI Hub analysis indicates Yuanqi's structural role is channel integration: the platform competes on reach and managed distribution, not on open weights, self-hosting or model choice. Where [Coze](/agents/coze/) spans WeChat, Feishu and Douyin and [Baidu AppBuilder](/agents/baidu-appbuilder/) sells enterprise RAG-and-agent delivery, Yuanqi sells one thing — a Hunyuan-backed agent that lives inside WeChat. That focus is its defining feature and its constraint.

China AI Hub analysis: Yuanqi is channel-bound in a double sense — bound to Hunyuan as its model and to WeChat as its distribution — which explains why its transparency is weaker than the open platforms. The buyer of a WeChat agent is buying reach, not model choice, so the platform documents the reach (channel templates, agent square) far more than it documents the model. The weaker model-version and pricing disclosure is not an oversight but a consequence of what the product actually sells.

## How it differs from Coze and Baidu AppBuilder

The three managed platforms are each an on-ramp to a different vendor's model and channel. Yuanqi's differentiation is the sharpest because its channel is singular.

- **[Coze](/agents/coze/)** (ByteDance) spans the widest channel set — WeChat, Feishu, Douyin — on top of Doubao, and adds an enterprise tier (Coze Pro on Volcengine). It competes on breadth.
- **[Baidu AppBuilder](/agents/baidu-appbuilder/)** (Baidu) is enterprise-first: an out-of-the-box RAG/Agent/workflow/UI Builder toolchain with pre-integrated Baidu AI Search and iRAG and full-code OpenAPI/SDK paths. It competes on enterprise application delivery.
- **Yuanqi** (Tencent) is consumer-channel-first: the WeChat official-account agent is the flagship, and the categories track real deployment (customer service, government, IP). It competes on reach into one dominant channel.

China AI Hub analysis: the practical consequence is that the three are rarely in direct substitution. A brand wanting a Douyin assistant picks Coze, an enterprise wanting RAG delivery on a managed stack weighs AppBuilder, and a publisher wanting an agent inside their WeChat official account reaches for Yuanqi. The model underneath is decided by the channel, not the other way around.

## Practical implications

**For WeChat official-account operators.** Yuanqi is the documented, native path to a 公众号智能体 that ingests historical articles and answers reader questions — the strongest single-channel fit in the database. The cost is that the agent is Hunyuan-backed and cloud-only.

**For enterprises needing managed agent delivery.** Yuanqi's enterprise solutions run through Tencent Cloud, and model usage is billed through Tencent Cloud Hunyuan APIs — so the economics are tied to Tencent's cloud and model stack, not to a neutral platform.

**For buyers who value transparency.** The model-version gap and the old/new version split are real friction: a team standardizing on a specific Hunyuan checkpoint cannot confirm it from public pages, and migration across the split is undocumented. Teams needing that auditability should weigh the neutral, self-hosted platforms ([Dify](/agents/dify/), [FastGPT](/agents/fastgpt/)) or a cross-model closed agent.

## What the evidence shows

The evidence is strong on Yuanqi's channel integration and weak on its model layer. The official platform page is explicit that it integrates Tencent ecosystem capabilities and publishes to WeChat and 应用宝 (Yingyongbao) channels, and the WeChat-official-account agent is documented across Tencent Cloud's developer community as the flagship use case — grounding the "channel-bound" reading in primary material rather than inference.

The model layer is the gap. The platform is described as built on Hunyuan, and Tencent documents Hunyuan as a self-developed general and multimodal model family, but no public agent page or template names the specific Hunyuan version behind an agent. The in-product notice of an old/new version split is the clearest signal of platform churn, and its migration path is undocumented. China AI Hub analysis indicates this asymmetry — rich channel documentation, thin model documentation — is exactly what a channel-integration strategy predicts: the platform is optimizing for reach, and reach is what it shows.

## Where this fits

| Workload | Relevance |
|---|---|
| WeChat official-account agent (公众号智能体) | High |
| Customer-service assistant for government/enterprise | High |
| Knowledge-base Q&A agent | High |
| IP persona mirroring a creator's voice | High |
| Zero-code agent creation + plugin plaza | High |
| Cross-model routing / non-Hunyuan models | Not documented |
| Self-hosted / on-premises deployment | None (cloud-only, proprietary) |
| Full-code SDK-first development | Low (zero-code surface; API exists) |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | Tencent Hunyuan (混元) family — specific version not stated on public pages | Official |
| Target users | WeChat account operators, enterprises, non-developers | Official |
| Platform | Web platform (yuanqi.tencent.com) | Official |
| OS | Browser-based (web platform) | Official |
| Browser / computer use | Not publicly documented | Not publicly documented |
| Coding | Not publicly documented | Not publicly documented |
| Autonomous task execution | Yes (agent + workflow) | Vendor-reported |
| MCP | Not publicly documented | Not publicly documented |
| Tool calling | Yes (plugins, workflows) | Official |
| Memory | Yes (knowledge base) | Official |
| Workflow | Zero-code builder with knowledge base, workflow, plugin plaza | Official |
| API | Yes (platform API; model usage via Tencent Cloud Hunyuan) | Official |
| Pricing | Not publicly documented on the marketing page | Not publicly documented |
| Region | China | Official |
| Open-source | No — proprietary | Official |
| Deployment | Cloud | Official |
| Limitations | Hunyuan model version unnamed; pricing not published; cloud-only | Official |
| Source | [Tencent Yuanqi](https://yuanqi.tencent.com/) · [Tencent Hunyuan](https://cloud.tencent.com/product/tclm) | Official |
| Last verified | 2026-09-30 | Official |

See the [Tencent](/companies/tencent/) company profile, the [choosing-an-agent guide](/guides/choosing-an-agent/), and the site's [AI agents](/technology/ai-agents/) and [RAG](/technology/rag/) technology pages. For the structural reading of the three bound platforms — Coze, Yuanqi and AppBuilder — see the research on [the agent ecosystem structure](/research/china-ai-agent-ecosystem-structure-and-gaps/) and [the rise of Chinese AI agents](/research/rise-of-chinese-ai-agents/).

*Labels used above: **Official fact** (from the Tencent Yuanqi platform, Tencent Cloud Hunyuan pages and the Hunyuan open platform), **Vendor-reported claim** (capability and publishing statements by Tencent), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party evaluation evidence is currently recorded for Yuanqi agents.*
