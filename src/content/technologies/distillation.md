---
image: "/images/ai/technologies-distillation.webp"
image_credit: "AI-generated illustration (Seedream)"
slug: distillation
title: Distillation
definition: "Knowledge distillation is a training technique in which a smaller 'student' model learns to imitate the outputs of a larger 'teacher' model, transferring capability at a fraction of the serving cost."
related_models: []
related_companies:
  - deepseek
related_technologies:
  - synthetic-data
  - quantization
related_guides: [open-weight-vs-api]
last_verified: "2026-09-22"
sources:
  - source_name: "Hinton, Vinyals & Dean — Distilling the Knowledge in a Neural Network"
    source_url: "https://arxiv.org/abs/1503.02531"
    source_type: academic
  - source_name: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
    source_url: "https://arxiv.org/abs/2501.12948"
    source_type: academic
---

## Technical background

Distillation dates to Hinton, Vinyals and Dean (2015): train a small model to match a large model's output distribution, not just labels. In the LLM era it became the standard way to spread frontier behavior — DeepSeek-R1's paper showed distilled small models matching far larger models on reasoning benchmarks, reshaping cost expectations industry-wide.

## How it works

A teacher model generates outputs (or logits) on a corpus; a student model trains to reproduce them, usually alongside standard next-token training. For reasoning, the teacher's chain-of-thought becomes the training signal. The result inherits the teacher's style and much of its knowledge, though not its full generality.

## Why it matters

Distillation is the main bridge between frontier-scale training and affordable deployment: open-weight models in the tens-of-billions of parameters now carry behaviors that required orders of magnitude more compute to originate. It also matters for licensing and data policy — distilled models inherit obligations and contamination risks from their teachers.

## Chinese adoption

The Chinese open-model ecosystem runs on distillation. DeepSeek-R1's distilled variants are the canonical example, and the technique underlies the open small-model families from Qwen (A3B-class MoE variants) and Zhipu (GLM-5.x open releases) listed in our company database. Practically every open Chinese model family ships a distilled small tier.

## Major Chinese companies and models

- **DeepSeek** — DeepSeek-R1 distillation pipeline documented in the R1 technical report; V4 open releases continue the lineage.
- **Alibaba Cloud** — Qwen open families include small active-parameter variants (35B-A3B etc.).

## Practical applications

Local and on-device models, cost-sensitive API tiers, domain-specialized small models, and reasoning-capable open models for self-hosting.

## Limitations

Students inherit teacher blind spots and biases; distilled chains of thought can be unfaithful; capability transfer is uneven across domains; and contamination from teacher training data can transfer silently.

## Deployment considerations

When choosing a distilled open model, check its lineage and license chain; benchmark on your tasks rather than inheriting the teacher's benchmark claims; and treat vendor-reported scores from small models with the same scrutiny as any other.

## Future development

Iterative distillation loops (teacher → student → new teacher), distillation with verifiers, and on-device reasoning models are the active frontier.
