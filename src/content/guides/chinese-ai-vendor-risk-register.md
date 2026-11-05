---
title: "A Vendor Risk Register for Chinese AI Suppliers"
description: "Eight risks that matter with Chinese AI vendors, scored by likelihood and impact, with the monitoring signals and mitigations that actually reduce."
author: "SinoAI Hub Research Team"
published_date: "2026-11-05"
updated_date: "2026-11-05"
pillar: buying-chinese-ai
order: 8
related_entities:
  - deepseek-v4-1-flash
  - glm-5.3
  - kimi-k3
  - qwen3.8-max
sources:
  - source_name: "Cyberspace Administration of China"
    source_url: "https://www.cac.gov.cn/"
    source_type: official
  - source_name: "DeepSeek API documentation"
    source_url: "https://api-docs.deepseek.com/"
    source_type: official
  - source_name: "Alibaba Cloud Model Studio documentation"
    source_url: "https://www.alibabacloud.com/help/en/model-studio"
    source_type: cloud_doc
---

**The short version.** Most AI vendor risk registers are generic: security, continuity, financial. Chinese AI suppliers add four specific exposures — access, jurisdiction, licence and entity — that generic registers miss. This is a register you can paste into a spreadsheet and actually review quarterly.

## The register

| # | Risk | Likelihood | Impact | Signal to watch |
|---|---|---|---|---|
| 1 | Model deprecation with short notice | High | Medium | Changelog frequency, status page |
| 2 | Price change or tier restructuring | High | Medium | Pricing page diffs, invoice deltas |
| 3 | Access cut (payment, KYC, policy) | Medium | High | Failed calls, account notices |
| 4 | Terms change on training or resale | Medium | High | Terms diff, legal newsletter |
| 5 | Cross-border data exposure | Medium | High | Endpoint change, DPA gaps |
| 6 | Entity or ownership change | Low | High | Registry filings, press |
| 7 | Licence restriction on self-hosting | Medium | Medium | Model card, licence text |
| 8 | Quality drift after a silent update | High | Medium | Eval suite regression |

Eight risks. Two of them — deprecation and price change — are near-certain over a two-year horizon, which is why the mitigations matter more than the scoring.

## 1. Model deprecation

Chinese labs ship fast and retire fast. A model that is "flagship" in March can be legacy by September, and the notice period is often measured in weeks.

**Mitigation:** keep an abstraction layer with at least two providers per capability tier; run a quarterly deprecation review against the vendor's changelog; contract for notice periods where possible.

**Signal:** changelog entries, API error codes, documentation pages marked legacy.

## 2. Price change

Chinese model pricing has moved downward overall but not monotonically; tiers get restructured, cache discounts change, and promotional pricing expires.

**Mitigation:** model unit economics with a 30% price-increase scenario; keep the switching cost low; negotiate price validity for committed volume.

**Signal:** a diff of the provider's pricing page, monthly.

## 3. Access cut

The nightmare scenario: the account stops working. Causes range from a failed top-up to KYC re-verification to a policy change on your use case.

**Mitigation:** maintain a second provider that is already integrated; keep a prepaid balance that covers at least a month; know the escalation contact by name.

**Signal:** authentication errors, rate limits that do not match your plan, support tickets that stop being answered.

## 4. Terms change

Terms change quietly. The clause you read at onboarding may not be the clause in force a year later.

**Mitigation:** diff the terms quarterly; put change-notification obligations in the contract; keep a dated copy of the terms you agreed to.

**Signal:** version numbers, "last updated" dates, email notices.

## 5. Cross-border data exposure

Endpoint changes, a new sub-processor, or a support engineer in a different region can move data without anyone deciding to.

**Mitigation:** pin the endpoint in configuration; require sub-processor notification; keep personal data out of prompts where possible; review the DPA annually.

**Signal:** latency changes, new regions in docs, updated sub-processor lists.

## 6. Entity or ownership change

Mergers, restructuring and new affiliates change your counterparty and sometimes your contract's governing law.

**Mitigation:** contract with an entity you have registered-checked; include assignment and change-of-control clauses; monitor registry filings annually.

**Signal:** press releases, registry updates, new names on invoices.

## 7. Licence restriction

Several Chinese open-weight models use custom licences with revenue thresholds, attribution requirements, or non-commercial terms. Self-hosting without reading them is a live risk.

**Mitigation:** legal review of the licence text before deployment; track revenue thresholds against your own; keep the licence version you relied on.

**Signal:** model card updates, licence file changes in the repository.

## 8. Quality drift

Silent model updates — new snapshots behind the same name — can change behaviour without changing the price.

**Mitigation:** a fixed evaluation set run on every deployment; pin model versions where the API allows it; record the version string with every result.

**Signal:** eval score regression, changes in refusal behaviour, tokenisation shifts.

## Scoring that is actually useful

Multiply likelihood (1–3) by impact (1–3) and sort. Then apply two filters:

- **Is it already happening?** Deprecation and price change usually are; treat them as operating conditions, not risks.
- **Can we detect it within a week?** If not, the mitigation is monitoring, not contracting.

## Review cadence

| Frequency | Review |
|---|---|
| Monthly | Pricing diff, status incidents, spend anomaly |
| Quarterly | Terms diff, deprecation review, eval regression |
| Annually | Entity check, licence review, DPA and sub-processors |

Three cadences, and the monthly one catches most of the damage.

## Our view

**The biggest risk is not geopolitical; it is operational.** Buyers worry about access being cut for policy reasons, which is rare and dramatic. The risks that actually bite are deprecation, price restructuring and silent quality drift — mundane, frequent and detectable.

**Two providers per capability tier is the single most effective mitigation.** Not because you will switch often, but because the option to switch changes your negotiating position and your incident response.

**A version string in every log is worth more than a risk workshop.** If you cannot tell which model produced an output, you cannot investigate a regression, a compliance question or a customer complaint.

**Contract terms are a weak control against most of these risks.** They help with notice and liability; they do not prevent a model from being retired. Monitoring and architecture are the real controls.

## What is uncertain

- Notice periods are rarely contractual in self-serve tiers.
- Ownership changes are hard to monitor across jurisdictions.
- Quality drift can be invisible until an eval set is run.

## Back to the pillar

[Buying Chinese AI: access, contracts and vendor risk](/guides/buying-chinese-ai/) — the overview, and the argument for why these eight risks belong in one register.
