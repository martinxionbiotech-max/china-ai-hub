---
image: "/images/ai/companies-moonshot-ai.webp"
image_credit: "AI-generated illustration (Seedream)"
company_id: moonshot-ai
company_name: Moonshot AI
description: "Moonshot AI (Beijing, founded spring 2023): Kimi chat assistant, Kimi API Platform, Kimi Work and Kimi Code. Foundation model Kimi K3."
aliases:
  - 月之暗面
  - Kimi
founded: "Spring 2023"
headquarters: "13F, Building 1, JD Technology Building, 76 Zhichun Road, Haidian District, Beijing, China"
funding: "No official funding disclosure located as of 2026-09-22."
ai_products:
  - Kimi (chat assistant, kimi.com / kimi.ai)
  - Kimi API Platform (platform.kimi.ai)
  - Kimi Work
  - Kimi Code
foundation_models:
  - kimi-k3
  - kimi-k2.7-code
  - kimi-k2.7-code-highspeed
  - kimi-k2.6
agents:
  - kimi-code
api:
  - moonshot
open_models:
  - kimi-k3
major_releases:
  - name: Kimi K3
    date: "2026-07-16"
    type: model_release
open_source_projects:
  - Kimi K3
  - Kimi K2.5
  - Kimi K2
  - Kimi-VL
  - Kimi-Audio
  - Moonlight (Muon)
  - kimi-code / kimi-cli
  - WorldVQA / PerceptionBench / CombiBench / Kimi Code Bench 2.0
official_documentation: https://platform.kimi.ai/docs
official_website: https://www.moonshot.ai/
related_entities: []
last_verified: "2026-09-20"
sources:
  - source_name: Moonshot AI official site (EN)
    source_url: https://www.moonshot.ai/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Moonshot AI company profile (CN)
    source_url: https://www.moonshot.cn/about
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi API platform — model list
    source_url: https://platform.kimi.ai/docs/models.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi K3 GitHub README
    source_url: https://github.com/MoonshotAI/Kimi-K3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** Moonshot AI is the Beijing-based company behind the Kimi assistant and the open-weight Kimi K-series models, sold through the Kimi API platform. **Why it matters.** Its flagship [Kimi K3](/models/kimi-k3/) is a 2.8T-parameter MoE with the database's only 1M-token *output* ceiling — the strongest long-context generation position among Chinese flagships. **Key characteristics.** Native vision; open weights under a permissive MIT-style license with revenue-triggered conditions; the [Kimi Code](/agents/kimi-code/) coding agent and kimi-cli. **What a professional should know.** The K3 license requires Model-as-a-Service operators above $20M revenue to sign a separate agreement and products above 100M MAU to display the name — so the openness is conditioned at scale, despite the permissive base text.

Moonshot AI (月之暗面), founded in spring 2023, develops the Kimi assistant and the open-weight Kimi
K-series models. Its API platform is platform.kimi.ai (global; platform.kimi.com in China), with the
API base at api.moonshot.ai. The flagship Kimi K3 (2.8T-parameter MoE, 1M context, native vision,
open weights) was released 2026-07-16.

The company also maintains Kimi K2/K2.5 research releases, the kimi-cli coding agent, and publishes
benchmarks (WorldVQA, PerceptionBench, CombiBench, Kimi Code Bench 2.0). Older API models (kimi-k2.5,
moonshot-v1*, kimi-k2*) have been discontinued.

## Why it matters

China AI Hub analysis: Moonshot AI's structural role is the long-context specialist — Kimi K3 is the only flagship in the database listing a full 1M-token maximum output, which makes it the reference choice for long-form generation and whole-repo rewriting rather than merely long-input analysis. Its open-weight stance (K3, K2.x, Kimi-VL, Kimi-Audio) keeps it in the open ecosystem alongside DeepSeek and Zhipu AI, while its custom license conditions distinguish it from DeepSeek's clean MIT. China AI Hub analysis indicates Moonshot competes on the output-length axis — a differentiated, documented strength — rather than on the price-floor axis where DeepSeek and MiniMax-M3 set the terms. China AI Hub analysis indicates Moonshot's open-weight-plus-conditions stance places it between DeepSeek's clean MIT and the closed labs — open enough to join the self-hosting ecosystem, but with revenue and MAU triggers that bound the openness at scale. Moonshot's models also circulate through third-party surfaces: [Coze](/agents/coze/)'s model node routes to Kimi, and the model-neutral platform [Dify](/agents/dify/) can orchestrate K-series models alongside others.

## Entity hub

### Models

- [Kimi K3](/models/kimi-k3/)
- [Kimi K2.7 Code](/models/kimi-k27-code/)
- [Kimi K2.7 Code Highspeed](/models/kimi-k27-code-highspeed/)
- [Kimi K2.6](/models/kimi-k26/)

### Products

- [Kimi Code](/agents/kimi-code/)
- [Kimi API Platform](/api/moonshot/)

### API

- [Kimi API](/api/moonshot/)

### Agents

- [Kimi Code](/agents/kimi-code/)

### Research / Technology

- [Deep Research](/technology/deep-research/)
- [Function Calling](/technology/function-calling/)
- [Long Context](/technology/long-context/)
- [Mixture of Experts](/technology/mixture-of-experts/)
- [Multimodal AI](/technology/multimodal-ai/)
- [Reasoning Models](/technology/reasoning-models/)

### Comparisons

- [DeepSeek-V4-Pro vs Kimi K3](/comparisons/deepseek-v4-pro-vs-kimi-k3/)
- [Kimi K3 vs MiniMax M3](/comparisons/kimi-k3-vs-minimax-m3/)

### Pricing

- [Moonshot AI pricing](/pricing/moonshot-ai/)

### Benchmarks

- [BrowseComp](/benchmarks/browsecomp/)
- [DeepSWE](/benchmarks/deepswe/)
- [GPQA Diamond](/benchmarks/gpqa-diamond/)
- [HLE](/benchmarks/hle/)
- [MMMU-Pro](/benchmarks/mmmu-pro/)
- [Terminal-Bench](/benchmarks/terminal-bench/)
- [Video-MME](/benchmarks/video-mme/)

## What is uncertain

- No official funding disclosure located.
- The K3 license requires a separate agreement above $20M revenue and UI attribution above 100M MAU — conditioned at scale.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-companies-moonshot-ai-1 | Moonshot AI official site (EN) | https://www.moonshot.ai/ | Official | — | 2026-09-20 | high | — |
| src-companies-moonshot-ai-2 | Moonshot AI company profile (CN) | https://www.moonshot.cn/about | Official | — | 2026-09-20 | high | — |
| src-companies-moonshot-ai-3 | Kimi API platform — model list | https://platform.kimi.ai/docs/models.md | Official documentation | — | 2026-09-20 | high | — |
| src-companies-moonshot-ai-4 | Kimi K3 GitHub README | https://github.com/MoonshotAI/Kimi-K3 | Official documentation | — | 2026-09-20 | high | — |

*Labels used above: **Official fact** (from Moonshot AI's official sites and the Kimi K3 README), **Vendor-reported claim** (model capabilities and pricing published by Moonshot AI), and **China AI Hub analysis** (our synthesis, always introduced as such).*
