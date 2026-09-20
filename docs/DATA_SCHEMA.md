# DATA_SCHEMA.md — China AI Hub

Field-level schemas for every entity collection. All fields optional unless marked **(req)**. Unknown values MUST use: `null`, `"unknown"`, or `"not publicly disclosed"` — never invented values.

## 0. Cross-cutting conventions

- **Stable ID**: lowercase-hyphen string; immutable; equals content collection filename. Display names are never keys.
- **Dates**: ISO 8601 (`2026-01-15`). Approximate dates use `~YYYY-MM` string with `date_precision` note.
- **Booleans**: use `true/false`; tri-state facts (unknown) use `null`.
- **Source block** (repeatable, on every entity):

```yaml
source_type: official | academic | benchmark_org | cloud_doc | industry_media | community | independent
source_url: https://…
source_name: DeepSeek Official Docs
published_date: 2026-01-15
last_verified: 2026-09-20
confidence: high | medium | low | estimate
```

- **Claim labels** for editorial text: FACT / VENDOR CLAIM / INDEPENDENT FINDING / ANALYSIS / INTERPRETATION / ESTIMATE / UNCERTAINTY.

## 1. Model (src/content/models/)

```yaml
model_id: deepseek-v4-pro        # (req) stable, immutable
model_name: DeepSeek V4 Pro      # (req)
provider: deepseek               # (req) → companies collection id
model_family: DeepSeek           # (req)
version: "4"                     # human version string
aliases: [deepseek-v4]
release_date: 2026-05-01
status: active | preview | deprecated | discontinued   # (req)
architecture: MoE               # sparse MoE, dense, Mamba, unknown
parameter_information:          # object; all subfields nullable
  total_parameters: null
  active_parameters: null
  parameter_precision: null
context_window: 131072          # tokens; null if unknown
maximum_output: 16384
capabilities:                    # each: true|false|null (null = unverified)
  reasoning: true
  coding: true
  math: true
  chinese: true
  english: true
  multilingual: true
  vision: false
  audio: false
  video: false
  tool_calling: true
  function_calling: true
  structured_output: true
  agent_capability: true
  rag: null
  computer_use: null
open_weight: true|false|null
license: MIT | Apache-2.0 | proprietary | custom | null
self_hosting: true|false|null
api_available: true|false|null
pricing:                          # (req if api_available) link object
  input_price_per_1m: 0.28       # USD, null if unknown
  output_price_per_1m: 0.42
  currency: USD
  effective_date: 2026-05-01
  pricing_ref: deepseek           # → pricing collection id
official_api: true|false|null
cloud_providers: [aliyun, volcano_engine, tencent_cloud]   # [] = none documented
regions: [china, global]
benchmark_results:                # list; NEVER mix incompatible versions silently
  - benchmark: MMLU-Pro           # → benchmarks collection id where it exists
    benchmark_version: "1.0"
    score: 85.3
    metric: accuracy
    model_version: deepseek-v4-pro
    date: 2026-05-10
    source_type: vendor_reported | independent | academic | community
    source_url: https://…
known_limitations: [no image input, API requires real-name registration]
notes: ""                        # free text, claim-labeled if analytical
last_verified: 2026-09-20        # (req)
sources: [ …source blocks… ]      # (req, ≥1)
```

**Model data quality gate**: name / provider / version / release date / status / context / pricing / capabilities / license / API / source / verification date all checked; uncertainty marked; nothing guessed.

## 2. Company (src/content/companies/)

```yaml
company_id: deepseek             # (req)
company_name: DeepSeek           # (req)
aliases: [深度求索, DeepSeek AI]
founded: 2023
headquarters: Hangzhou, China
ownership_information: ""        # only with reliable sourcing; else omit
ai_products: [DeepSeek App, DeepSeek API]
foundation_models: [deepseek-v4-pro, deepseek-v4-flash]  # → models ids
agents: []                       # → agents ids
api: [deepseek]                  # → apis ids
open_models: [deepseek-v4-pro]
cloud_distribution: [volcano_engine, aliyun]
major_releases:                  # chronological list
  - name: DeepSeek V4
    date: 2026-05-01
    type: model_release
open_source_projects: [deepseek-vl2]  # repo names/URLs
official_documentation: https://api-docs.deepseek.com/
official_website: https://www.deepseek.com/
related_entities: []             # company ids, with relation labels
last_verified: 2026-09-20        # (req)
sources: [ … ]                    # (req)
```

## 3. Agent (src/content/agents/)

```yaml
agent_id: example-agent          # (req)
agent_name: Example Agent        # (req)
company: deepseek                # → companies id
description: ""                  # (req) 1–3 factual sentences
agent_type: coding | research | browser | computer_use | enterprise | customer_service | marketing | data | multi_agent | autonomous | framework | platform
underlying_models: [deepseek-v4-pro]
framework: langchain | autogen | custom | null
tool_calling: true|false|null
browser_use: true|false|null
computer_use: true|false|null
mcp: true|false|null
memory: true|false|null
planning: true|false|null
multi_agent: true|false|null
api: true|false|null
pricing: ""                      # description or null
deployment: cloud | self_hosted | both | null
open_source: true|false|null
license: null
github: null
documentation: https://…
use_cases: [code generation, code review]
limitations: [requires API key]
last_verified: 2026-09-20        # (req)
sources: [ … ]                    # (req)
```

**Rule**: distinguish model / assistant / agent / framework / platform. A chatbot is not automatically an agent; `agent_type` must be defensible.

## 4. API (src/content/apis/)

```yaml
api_id: deepseek                 # (req)
provider: deepseek               # (req) → companies id
api_type: official | cloud_hosted | third_party | self_hosted_endpoint
endpoint: https://api.deepseek.com
authentication: api_key | oauth | enterprise_contract
streaming: true|false|null
function_calling: true|false|null
tool_calling: true|false|null
structured_output: true|false|null
vision: true|false|null
audio: true|false|null
context_limits:                  # per model where needed
  - model: deepseek-v4-pro
    input_limit: 131072
    output_limit: 16384
rate_limits: ""                  # text description + source
regions: [china, global]
cloud_providers: [volcano_engine]
pricing_ref: deepseek            # → pricing id
documentation: https://api-docs.deepseek.com/
last_verified: 2026-09-20        # (req)
sources: [ … ]                    # (req)
```

## 5. Pricing (src/content/pricing/)

One file per provider (id = provider id). Pricing is **time-sensitive**: preserve history.

```yaml
provider_id: deepseek            # (req) → companies id
currency: USD                    # (req) default; per-model overrides allowed
region: global | china | europe  # (req) with note if split pricing
billing_mode: pay_as_you_go | subscription | hybrid
models:                           # (req) current prices
  - model: deepseek-v4-pro
    input_price_per_1m: 0.28
    output_price_per_1m: 0.42
    cached_input_price_per_1m: 0.028
    cached_output_price_per_1m: null
    batch_price_per_1m: null      # discounted batch where offered
    note: ""                     # e.g. "off-peak discount 50–75%"
    effective_date: 2026-05-01
    official_source: https://…
price_history:                    # keep when prices change
  - model: deepseek-v4-pro
    field: input_price_per_1m
    old_value: 0.55
    new_value: 0.28
    effective_date: 2026-05-01
    source: https://…
last_verified: 2026-09-20        # (req)
sources: [ … ]
```

**Pricing quality gate**: currency / region / billing mode / unit (per 1M tokens) / input vs output / cache / batch / effective date / official source all verified before display. Normalize all units to *per 1M tokens* in USD-equivalent with original currency preserved.

## 6. Benchmark (src/content/benchmarks/)

```yaml
benchmark_id: mmlu-pro          # (req)
benchmark_name: MMLU-Pro        # (req)
version: "1.0"
description: ""                  # what it measures, how
evaluations:                     # results list
  - model: deepseek-v4-pro
    model_version: deepseek-v4-pro
    score: 85.3
    metric: accuracy
    date: 2026-05-10
    source_type: vendor_reported | independent | academic | community
    source_url: https://…
limitations: ""                  # known benchmark limits
last_verified: 2026-09-20        # (req)
sources: [ … ]
```

**Rules**: scores never presented as universal rankings; source_type is mandatory per result; incompatible benchmark versions never mixed without explanation.

## 7. Technology (src/content/technologies/)

Editorial + entity hybrid. Frontmatter:

```yaml
slug: mixture-of-experts         # (req) filename
title: Mixture of Experts        # (req)
definition: ""                   # (req) 1–2 sentence, independently understandable
related_models: [deepseek-v4-pro]
related_companies: [deepseek, alibaba-qwen]
related_technologies: [inference]
related_guides: []
last_verified: 2026-09-20
sources: [ … ]
```

Body sections (per master prompt): Definition → Technical background → How it works → Why it matters → Chinese adoption → Major Chinese companies/models → Practical applications → Limitations → Deployment considerations → Future development → Sources. Distinguish global technology vs Chinese implementation vs company-specific implementation.

## 8. Comparison (src/content/comparisons/)

```yaml
title: DeepSeek vs Qwen         # (req)
entities: [deepseek-v4-pro, qwen3-max]   # (req) stable ids
dimensions: [pricing, context, reasoning, coding, chinese, english, multilingual, vision, audio, tool_calling, agent, open_weight, license, api, deployment, documentation, use_cases, availability]
```

**Rules**: no Best/Winner/#1/Worst except for clearly defined objective measurements; no overall ranking; explain trade-offs and workload relevance.

## 9. Guides / Research / News

Frontmatter (req): `title`, `description` (≤160 chars), `published_date`, `updated_date`, `sources` (research/guides required; news required). Research articles additionally: `research_question`, `related_entities`, `author_view` (boolean indicating dedicated section). News: `type: model_release | price_change | company | agent | other`, `trigger_updates: []` (list of entity ids that may need data updates).

## 10. Missingness & validation rules

- `null` = not verified yet; `"unknown"` = researched, no public data; `"not publicly disclosed"` = vendor declines to state.
- A page with >50% null core fields (name/version/status/pricing/context/license/API) is NOT publishable — keep as draft or omit.
- Duplicate detection: check `aliases` + provider + family before creating a new model entry.
- Every published record needs ≥1 L1/L2 source for its core facts (SOURCE_POLICY.md).

## 11. Extensibility (future data product)

Schemas are designed so later phases can add: JSON/CSV export (collections already typed), public API, historical datasets (price_history/benchmark history fields exist), change history (DataUpdateHistory component reads history lists). Do not implement exports in Phase 1.
