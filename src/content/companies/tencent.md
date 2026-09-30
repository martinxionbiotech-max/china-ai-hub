---
company_id: tencent
company_name: Tencent
description: "Tencent (腾讯): Chinese internet and technology company behind the self-developed Tencent Hunyuan (混元) general and multimodal foundation-model family and the Tencent Yuanqi (元器) agent development platform, sold through Tencent Cloud."
aliases:
  - 腾讯
  - 腾讯云
  - Tencent Cloud
  - 混元
headquarters: "Shenzhen, Guangdong, China"
funding: "Publicly listed (SEHK: 0700)."
ai_products:
  - Tencent Hunyuan (混元) foundation model family
  - Tencent Yuanqi (元器) agent platform
  - Tencent Cloud AI
foundation_models: []
agents:
  - yuanqi
api: []
open_source_projects: []
official_documentation: https://cloud.tencent.com/document/product/1729/10475
official_website: https://www.tencent.com/
related_entities: []
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
**What it is.** Tencent is the Chinese internet and technology company behind the self-developed Hunyuan (混元) general and multimodal foundation-model family and the [Tencent Yuanqi](/agents/yuanqi/) agent platform. **Why it matters.** It is the only agent platform in this database attached to WeChat — the highest-value consumer distribution channel in China — which makes its agent layer a channel-integration play rather than a neutral tool. **Key characteristics.** Hunyuan spans text, image, video, speech and 3D modalities; Yuanqi publishes agents to WeChat official accounts, QQ and other Tencent channels. **What a professional should know.** Hunyuan model details are documented on Tencent Cloud, but the specific Hunyuan version behind a given Yuanqi agent is not stated on the platform's public pages, and agent pricing is not published on the static marketing page.

Tencent (腾讯) is a publicly listed Chinese technology company headquartered in Shenzhen. Its AI stack centers on the Tencent Hunyuan (混元) model family, which Tencent Cloud describes as a self-developed general and multimodal model family spanning text, image, video, speech and 3D, aimed at content production, knowledge Q&A and business automation. The [Tencent Yuanqi](/agents/yuanqi/) platform is the agent-building layer on top of Hunyuan: a zero-code surface for creating agents with knowledge bases, workflows and plugins, and publishing them to WeChat official accounts, QQ and other Tencent channels.

## Why it matters

China AI Hub analysis indicates Tencent's structural role in the agent ecosystem is channel ownership — it is the one lab whose agent platform is fused to WeChat, so its agent layer is less a neutral tool market and more a managed distribution channel for Hunyuan models. Its category skew (WeChat-official-account agents, customer service, government service, IP personas) reflects deployment, not developer tooling.

China AI Hub analysis indicates Yuanqi competes on reach and managed distribution, not on open weights, self-hosting or model choice. Where [Coze](/agents/coze/) spans WeChat, Feishu and Douyin and [Baidu AppBuilder](/agents/baidu-appbuilder/) sells enterprise RAG-and-agent delivery, Yuanqi sells one thing — a Hunyuan-backed agent that lives inside WeChat. That focus is its defining feature and its constraint.

China AI Hub analysis indicates Yuanqi is channel-bound in a double sense — bound to Hunyuan as its model and to WeChat as its distribution — which explains why its transparency is weaker than the open platforms. The buyer of a WeChat agent is buying reach, not model choice, so the platform documents the reach (channel templates, agent square) far more than it documents the model. The weaker model-version and pricing disclosure is a consequence of what the product actually sells, not an oversight.

## How it differs from Coze, AppBuilder and the open platforms

The three managed platforms are each an on-ramp to a different vendor's model and channel; the open platforms differ on openness.

- **[Coze](/agents/coze/)** (ByteDance) spans the widest channel set — WeChat, Feishu, Douyin — on top of Doubao, and adds an enterprise tier (Coze Pro on Volcengine). It competes on breadth.
- **[Baidu AppBuilder](/agents/baidu-appbuilder/)** (Baidu) is enterprise-first: an out-of-the-box RAG/Agent/workflow/UI Builder toolchain with pre-integrated Baidu AI Search and iRAG and full-code OpenAPI/SDK paths. It competes on enterprise application delivery.
- **[Dify](/agents/dify/)** and **[FastGPT](/agents/fastgpt/)** are open, self-hostable, model-agnostic — the neutral alternative.
- **Yuanqi** (Tencent) is consumer-channel-first: the WeChat official-account agent is the flagship, and the categories track real deployment. It competes on reach into one dominant channel.

China AI Hub analysis: the practical consequence is that the three bound platforms are rarely in direct substitution — a brand wanting a Douyin assistant picks Coze, an enterprise wanting RAG delivery weighs AppBuilder, and a publisher wanting an agent inside their WeChat official account reaches for Yuanqi. The model underneath is decided by the channel, not the other way around; the open platforms are the exit when the buyer needs model choice or self-hosting.

## Practical implications and limitations

**For WeChat official-account operators.** Yuanqi is the documented, native path to a 公众号智能体 that ingests historical articles and answers reader questions — the strongest single-channel fit in the database. The cost is that the agent is Hunyuan-backed and cloud-only.

**For enterprises needing managed agent delivery.** Yuanqi's enterprise solutions run through Tencent Cloud, and model usage is billed through Tencent Cloud Hunyuan APIs — so the economics are tied to Tencent's cloud and model stack, not to a neutral platform.

**For buyers who value transparency.** The model-version gap and the old/new version split are real friction: a team standardizing on a specific Hunyuan checkpoint cannot confirm it from public pages, and migration across the split is undocumented. Teams needing that auditability should weigh the neutral, self-hosted platforms ([Dify](/agents/dify/), [FastGPT](/agents/fastgpt/)) instead.

## Entity hub

### Products

- [Tencent Yuanqi (元器) agent platform](/agents/yuanqi/)

### Agents

- [Tencent Yuanqi](/agents/yuanqi/)

### Research / Technology

- [AI Agents](/technology/ai-agents/)
- [RAG](/technology/rag/)
- [Agent ecosystem structure and gaps](/research/china-ai-agent-ecosystem-structure-and-gaps/)

## What is uncertain

- The specific Hunyuan model version behind a given Yuanqi agent is not stated on the platform's public pages.
- Yuanqi pricing is not published on the static marketing page.
- Hunyuan models are not yet tracked as standalone model records in this database.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-companies-tencent-1 | Tencent Yuanqi official platform | https://yuanqi.tencent.com/ | Official | — | 2026-09-29 | high | — |
| src-companies-tencent-2 | Tencent Hunyuan model product page (Tencent Cloud) | https://cloud.tencent.com/product/tclm | Official | — | 2026-09-29 | high | — |
| src-companies-tencent-3 | Tencent Hunyuan official site | https://hunyuan.tencent.com/ | Official | — | 2026-09-29 | high | — |

*Labels used above: **Official fact** (from the Tencent Yuanqi platform and Tencent Cloud Hunyuan pages), **Vendor-reported claim** (model-family and platform statements by Tencent), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party evaluation evidence is currently recorded for Yuanqi agents.*
