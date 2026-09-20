---
model_id: deepseek-v3-2
model_name: DeepSeek-V3.2
provider: deepseek
model_family: DeepSeek-V3
release_date: "2025-12-01"
status: discontinued
open_weight: true
license: MIT
self_hosting: true
api_available: false
official_api: false
known_limitations:
  - "Replaced on the DeepSeek API by the V4 family"
  - "Context window not stated on the official release pages fetched"
  - "Vendor performance claims are qualitative ('GPT-5 level performance'); no numeric scores on the release page"
last_verified: "2026-09-20"
sources:
  - source_name: DeepSeek-V3.2 release
    source_url: https://www.deepseek.com/en/news/deepseek-v3-2/
    source_type: official
    published_date: "2025-12-01"
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek Transparency Center
    source_url: https://www.deepseek.com/en/transparency/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Hugging Face model card — DeepSeek-V3.2
    source_url: https://huggingface.co/deepseek-ai/DeepSeek-V3.2
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

DeepSeek-V3.2 (released 2025-12-01, MIT open weights) is the previous DeepSeek flagship. DeepSeek
claimed "GPT-5 level performance" at release, and that the API-only V3.2-Speciale variant rivaled
Gemini-3.0-Pro with gold-medal results in math/programming olympiads; the release page lists no numeric
scores. V3.2 has been replaced on the DeepSeek API by the V4 family, but the open weights remain
available on Hugging Face.
