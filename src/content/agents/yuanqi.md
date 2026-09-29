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
last_verified: "2026-09-29"
sources:
  - source_name: Tencent Yuanqi official platform
    source_url: https://yuanqi.tencent.com/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Tencent Hunyuan model product page (Tencent Cloud)
    source_url: https://cloud.tencent.com/product/tclm
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Tencent Hunyuan official site
    source_url: https://hunyuan.tencent.com/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
---
**What it is.** Tencent Yuanqi (腾讯元器) is Tencent's agent development platform for building and deploying AI agents (智能体) on the Tencent Hunyuan (混元) model family. **Why it matters.** It is the agent surface through which Tencent routes its Hunyuan models into the WeChat ecosystem — the most valuable distribution channel in China — letting operators publish agents directly to WeChat official accounts. **Key characteristics.** Zero-code agent creation with knowledge bases, workflow orchestration and a plugin plaza; template categories for WeChat-official-account agents, customer-service assistants, efficiency tools and IP personas. **What a professional should know.** The platform is cloud-only, its public pages do not state the exact Hunyuan model version behind an agent, and its pricing is not published on the static marketing page — model usage is billed through Tencent Cloud Hunyuan APIs.

Tencent Yuanqi is the agent-building layer of Tencent's AI stack. Operators create agents from templates or from scratch, attach a knowledge base, wire workflows and plugins, and publish to Tencent channels — most notably WeChat official accounts (公众号智能体), where an agent can ingest a public account's historical articles and answer reader questions. The platform's agent square (智能体广场) surfaces categories that reflect its real-world deployment patterns: legal and tax Q&A, government-service customer service, education and IP-persona agents.

The platform is built on Tencent's Hunyuan (混元) foundation model family, which Tencent describes as a self-developed general and multimodal model family spanning text, image, video, speech and 3D. The agent pages and templates do not, however, name the specific Hunyuan model version behind each agent — a documentation gap consistent with the platform's closed, managed posture. An in-product notice also indicates the platform recently underwent a system upgrade that split it into old and new versions running on separate logic that do not sync directly.

See the [Tencent](/companies/tencent/) profile.

## Why it matters

Yuanqi matters as Tencent's structural move to bind its Hunyuan models to WeChat's distribution. The other large platforms in the database — [Coze](/agents/coze/) (ByteDance), [Baidu AppBuilder](/agents/baidu-appbuilder/) — follow the same pattern, but Yuanqi is the one attached to the highest-value consumer channel, WeChat. China AI Hub analysis indicates its role is channel integration: a WeChat-official-account agent is not a neutral tool but a Hunyuan-backed extension of the account, which is why the platform's categories skew toward customer service, government service and creator IP rather than developer tooling. That positioning is the platform's defining feature — it competes on reach and managed distribution, not on open weights or self-hosting. China AI Hub analysis: this makes Yuanqi channel-bound in a double sense — bound to Hunyuan as its model and to WeChat as its distribution — which explains why its model-version and pricing transparency are weaker than the open platforms: the buyer of a WeChat agent is buying reach, not model choice, and the platform documents the reach more than the model.

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
| Last verified | 2026-09-29 | Official |

## What is uncertain

- The specific Hunyuan model version behind a given agent is not stated on the platform's public pages.
- Pricing is not published on the static marketing page and requires a logged-in console.
- The exact scope of the old/new version split and its migration path is not documented publicly.
- Whether Yuanqi agents can route to non-Hunyuan models is not documented on the public pages.
- No independent third-party evaluation of Yuanqi agents is recorded in this database.

*Labels used above: **Official fact** (from the Tencent Yuanqi platform and Tencent Cloud Hunyuan pages), **Vendor-reported claim** (capability and publishing statements by Tencent), and **China AI Hub analysis** (our synthesis, always introduced as such).*
