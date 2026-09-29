---
image: "/images/ai/companies-minimax.webp"
image_credit: "AI-generated illustration (Seedream)"
company_id: minimax
company_name: MiniMax
description: "MiniMax (Shanghai, founded early 2022): MiniMax Code / Design / Audio apps, Talkie (international) / Xingye (China), MiniMax Agent, and the MiniMax open platform. Foundation models MiniMax-M3 and M2.7."
aliases:
  - MiniMax AI
  - 上海稀宇科技有限公司
founded: "early 2022"
headquarters: "Room 1704-1, No. 1699 Gubei Road, Minhang District, Shanghai, China"
funding: "Investor-relations site exists (ir.minimax.cn); funding-round details are not listed on official pages as of 2026-09-22."
ai_products:
  - MiniMax Code
  - MiniMax Design
  - MiniMax Audio
  - Talkie (international) / 星野 (China)
  - MiniMax Agent
  - MiniMax open platform (enterprise/developer API)
foundation_models:
  - minimax-m3
  - minimax-m2.7
  - minimax-m2.7-highspeed
agents:
  - minimax-agent
  - minimax-code
api:
  - minimax
open_models:
  - minimax-m3
major_releases:
  - name: MiniMax-M3
    date: "2026-06-01"
    type: model_release
  - name: MiniMax-M2.7
    date: "2026-03-18"
    type: model_release
  - name: MiniMax-M2
    date: "2025-10-27"
    type: model_release
open_source_projects:
  - MiniMax-M3
  - MiniMax-M2.7
  - MiniMax-M2
  - MiniMax-H3 (video)
  - MiniMax Music 3
  - MSA (MiniMax Sparse Attention)
  - MiniMax-Provider-Verifier
official_documentation: https://platform.minimax.io/docs
official_website: https://www.minimax.io/
related_entities: []
last_verified: "2026-09-20"
sources:
  - source_name: MiniMax official site (international)
    source_url: https://www.minimax.io/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax official site (China)
    source_url: https://www.minimax.cn/about
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax API platform — model overview (CN)
    source_url: https://platform.minimaxi.com/docs/guides/models-intro
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax official release notes
    source_url: https://platform.minimaxi.com/docs/release-notes/models.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** MiniMax is the Shanghai-based Chinese general-AI company behind the M-series agent/chat models ([MiniMax-M3](/models/minimax-m3/), [M2.7](/models/minimax-m27/)), plus video, audio, image and music models. **Why it matters.** MiniMax-M3 lists the cheapest flagship pricing in the database ($0.30/$1.20 per 1M tokens) while shipping open weights and 1M-token context — a cost-efficiency position distinct from both DeepSeek's MIT-open stance and ByteDance's closed premium. **Key characteristics.** The MiniMax Sparse Attention (MSA) architecture claims 9x prefill / 15x decode speedups at 1M context; open weights under the MiniMax Community License; a consumer-app portfolio (Talkie/星野). **What a professional should know.** The Community License is not MIT-style: commercial use requires attribution and, above revenue thresholds, written authorization — read it before commercial deployment.

MiniMax (上海稀宇科技有限公司), founded in early 2022, is a Chinese general-AI company whose products
span chat/agent models (M-series), video (H-series), audio (Speech/TTS/ASR), image generation, music
(Music 3) and consumer apps (Talkie / 星野). The company states it serves users in 230+ countries with
300M+ individual users and 2M+ enterprise clients and developers (vendor claim, CN site).

The current flagship model is MiniMax-M3 (2026-06-01): a ~428B/23B-active MoE with 1M-token context,
multimodal input (text/image/video) and open weights under the MiniMax Community License. API platforms:
platform.minimaxi.com (China, CNY) and platform.minimax.io (international, USD).

## Why it matters

MiniMax's structural role is the cost-efficient challenger that competes on both capability breadth and price without going full-open. It runs a broad product surface — [MiniMax Code](/agents/minimax-code/) and [MiniMax Agent](/agents/minimax-agent/) on the agent side, plus video/audio/image generation — while keeping its flagship M3 at the lowest flagship price point in the database. China AI Hub analysis indicates MiniMax's distinctive bet is architectural efficiency (MSA sparse attention) translating directly into price, which positions it as the value alternative to Alibaba Cloud's integration breadth and ByteDance's consumer premium.

*Labels used above: **Official fact** (from MiniMax's official sites and platform docs), **Vendor-reported claim** (the MSA speedup figures and user counts stated on the CN site), and **China AI Hub analysis** (our synthesis, always introduced as such).*
