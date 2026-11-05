---
model_id: kimi-k3.1-pro-highspeed
model_name: Kimi K3.1 Pro Highspeed
provider: moonshot-ai
model_family: Kimi K3.1 series
status: active
architecture: "High-throughput serving tier of Kimi K3.1 Pro; same model, faster inference path"
context_window: 1048576
capabilities:
  reasoning: true
  coding: true
  vision: true
  tool_calling: true
  structured_output: true
  agent_capability: true
open_weight: true
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 26.0
  output_price_per_1m: 136.0
  currency: CNY
  pricing_ref: moonshot-ai
official_api: true
cloud_providers:
  - Moonshot AI Platform
known_limitations:
  - "Exactly 2x the standard K3.1 Pro price for roughly 2-3x throughput; per-token cost doubles, per-second cost falls"
  - "Priced in CNY; no international USD list at the time of record"
last_verified: "2026-11-05"
sources:
  - source_name: "Kimi API Platform — K3.1 Pro quickstart (highspeed variant)"
    source_url: "https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart.md"
    source_type: official
    last_verified: "2026-11-05"
    confidence: high
  - source_name: "Kimi API Platform — model inference pricing"
    source_url: "https://platform.kimi.ai/docs/pricing/chat.md"
    source_type: official
    last_verified: "2026-11-05"
    confidence: medium
---

Kimi K3.1 Pro Highspeed is the fast serving tier of K3.1 Pro: the same model and context window, priced at **¥26 per 1M input and ¥136 per 1M output** — exactly double the standard tier — with roughly 2–3x the throughput.

## The trade

| | Standard | Highspeed |
|---|---|---|
| Input /1M | ¥13 | ¥26 |
| Output /1M | ¥68 | ¥136 |
| Throughput | baseline | ~2–3x |
| Cost per token | 1x | 2x |
| Cost per second of work | 1x | ~0.7–1.0x |

The per-token price doubles while throughput rises 2–3x, so the cost of a *fixed amount of work* stays roughly flat and the cost of *wall-clock time* falls. Highspeed is therefore a latency purchase, not a throughput optimisation: it pays when a human is waiting, and does nothing for batch pipelines.

## When it is worth it

- Interactive coding assistants and review tools where time-to-first-token is visible.
- Agent loops with many short calls, where per-call overhead dominates total latency.
- Anything with a service-level agreement measured in seconds.

It is not worth it for nightly batch jobs, evaluation runs or document processing — the standard tier produces the same output for half the token cost, and the queue does not care how fast each call returns.

## What to verify

The multiplier is stated as "2–3x" rather than a fixed figure, so the effective cost per unit of work depends on your workload's concurrency. At 2x throughput for 2x price, Highspeed is cost-neutral per unit of work and strictly better on latency; at 3x, it is also cheaper per unit of work. Measure on your own traffic before standardising on it.
