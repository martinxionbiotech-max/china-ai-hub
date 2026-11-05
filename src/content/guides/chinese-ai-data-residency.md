---
title: "Data Residency and Cross-Border Transfer for Chinese AI"
description: "PIPL, the Data Security Law and hosting regions: where Chinese AI processes your data, when a transfer mechanism is required, and the ICP question nobody."
author: "SinoAI Hub Research Team"
published_date: "2026-11-05"
updated_date: "2026-11-05"
pillar: buying-chinese-ai
order: 4
related_entities:
  - qwen3.8-max
  - glm-5.3
  - deepseek-v4-1-flash
sources:
  - source_name: "Cyberspace Administration of China"
    source_url: "https://www.cac.gov.cn/"
    source_type: official
  - source_name: "Alibaba Cloud Model Studio documentation"
    source_url: "https://www.alibabacloud.com/help/en/model-studio"
    source_type: cloud_doc
  - source_name: "Z.ai platform documentation"
    source_url: "https://docs.z.ai/"
    source_type: official
---

**The short version.** Where a Chinese model processes your data depends on which endpoint you call, not which model you choose. The same model can run in Singapore, Frankfurt or Beijing. The compliance work is choosing the endpoint deliberately — and knowing that a mainland endpoint brings China's data law, and often an ICP filing, into your project.

## Three laws to know by name

| Law | In force | What it governs |
|---|---|---|
| **Cybersecurity Law (CSL)** | 2017 | Network operation, security obligations, incident reporting |
| **Data Security Law (DSL)** | 2021 | Data classification, important data, cross-border transfer |
| **Personal Information Protection Law (PIPL)** | 2021 | Personal data processing, consent, cross-border transfer |

For an AI buyer the practical consequence is simple: if personal data is processed on infrastructure in mainland China, PIPL applies to that processing regardless of where your company sits, and moving the data out again is a regulated transfer.

## The endpoint decides the jurisdiction

Chinese labs and their cloud partners offer regional endpoints. The pattern:

- **Mainland endpoints** — lowest price, full model catalogue, mainland jurisdiction.
- **International endpoints** (Singapore, Frankfurt, US) — USD pricing, narrower catalogue, contract with the international entity.
- **Cloud marketplaces** — the region you deploy into determines the data path.

The model weights may be identical; the legal regime is not. A team that benchmarks on an international endpoint and then switches to the cheaper mainland one for production has changed its compliance position without changing its code.

## When a transfer mechanism is needed

Under PIPL, transferring personal data out of mainland China requires one of three mechanisms:

1. **A CAC security assessment**, for transfers that meet the regulator's thresholds (important data, or large volumes of personal data).
2. **A standard contract** filed with the provincial CAC, for transfers below those thresholds.
3. **A certification** issued by a qualified body.

The thresholds have been adjusted since PIPL took effect, and the direction has been toward lighter obligations for smaller volumes. The point for buyers is not the exact number — it is that the mechanism has to exist *before* the transfer, and it is your obligation as the data exporter, not the vendor's.

Practical consequence: a Chinese model processing EU customer data on a mainland endpoint is a cross-border transfer from China outward only if the data goes in and comes back. In most architectures the more pressing question is the reverse — sending EU personal data *into* China, which is a GDPR transfer requiring its own basis.

## The double transfer problem

An EU company using a mainland Chinese endpoint creates two transfers:

- **EU → China**: personal data leaves the EEA, requiring a GDPR transfer mechanism (SCCs, adequacy — which China does not have — or derogation).
- **China → EU**: the response comes back, and if any personal data is stored or logged in China, the return path is also regulated.

Most teams plan for the first and forget the second. Logs, caches and evaluation datasets kept on the mainland side are storage, not transit.

## The ICP question

Hosting a public-facing service on mainland Chinese infrastructure requires an ICP filing (备案) for the domain, and a commercial service may require an ICP licence. The filing is tied to a mainland entity and a mainland-hosted domain.

For a foreign company this usually means: you cannot put a customer-facing site on a mainland endpoint without a local entity and a filing. Internal API calls from your own servers are a different matter, but the line between "internal" and "public-facing" is drawn by the regulator, not by your architecture diagram.

This is the point where many projects quietly become joint ventures. Better to find out at the design stage.

## A practical decision matrix

| Your situation | Sensible endpoint | Watch for |
|---|---|---|
| Evaluation, no personal data | Any | Nothing much |
| Production, personal data, no China entity | International endpoint or cloud region outside mainland | Model parity, latency, price premium |
| Production, China users, China entity | Mainland endpoint | ICP filing, PIPL obligations, security assessment |
| Regulated data (health, finance) | Region matching your regulator | Whether the vendor will sign your DPA at all |

## Questions to send the vendor

1. In which regions is this specific model served, and are they functionally identical?
2. Is data at rest stored in the region of processing, and for how long?
3. Do you train on customer data by default, and can it be disabled contractually?
4. Which entity processes the data, and which entity is the controller or processor?
5. Will you sign our DPA, and does it cover sub-processors?

Five questions. Vendors with a mature international business answer them from a template; vendors without one answer slowly.

## Our view

**Endpoint choice is an architecture decision disguised as a procurement detail.** It determines latency, price, model availability, legal regime and exit cost. Teams that pick the endpoint last end up rebuilding around it.

**For most foreign buyers, the international endpoint is the correct default, and the price premium is the cost of avoiding a regulatory project.** A mainland endpoint can be 30–50% cheaper and will consume the difference in legal review, filings and engineering time before the first invoice.

**The ICP requirement is the most under-estimated constraint.** It is not a formality; it requires a mainland entity. Any plan that assumes "we will just host it in Shanghai" should be tested against that requirement in week one.

**A vendor that cannot name its sub-processors should not receive personal data.** This is true of every AI vendor, not only Chinese ones, but the disclosure culture is thinner here and the question is more likely to be met with silence.

## What is uncertain

- Regional model parity changes without notice.
- The CAC thresholds have moved and may move again.
- DPA coverage varies by contract tier and is rarely public.

## Next

[How to spot an API reseller](/guides/spotting-chinese-ai-api-resellers/) — where the data actually goes when you buy through an intermediary.
