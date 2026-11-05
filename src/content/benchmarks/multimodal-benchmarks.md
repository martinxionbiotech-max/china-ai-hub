---
benchmark_id: multimodal-benchmarks
benchmark_name: "Multimodal Benchmarks"
description: "MMMU-Pro and Video-MME compared: what vision and video scores actually measure for Chinese models, the results published, and why resolution settings decide the number."
task_type: "Multimodal reasoning over images, documents and video"
dataset_size: "MMMU-Pro ~3,460 questions · Video-MME 900 videos across short, medium and long durations"
evaluation_method: "Multiple-choice over image or video context; Video-MME optionally with subtitles"
scoring: "Accuracy; Video-MME reported overall and by duration bucket"
caveat: "Both benchmarks are sensitive to how the image or video reaches the model: resolution, frame sampling rate and subtitle availability change scores more than model differences do. MMMU-Pro hardens MMMU against text-only shortcuts by embedding questions in screenshots, but vendors rarely state whether OCR tooling was allowed. Video-MME's short-clip results do not transfer to long-form video."
contamination_notes: "MMMU-Pro was built partly to counter contamination in MMMU; Video-MME is recent enough that contamination is less of a concern than harness variance."
limitations: "Chinese model coverage is partial and uneven: a model missing from the table has published no result, not scored zero."
member_ids: [mmmu-pro, video-mme]
last_verified: "2026-11-05"
evaluations:
  - benchmark: MMMU-Pro
    model: kimi-k3
    score: "81.6 (83.4 with tools)"
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: MMMU-Pro
    model: kimi-k2.5
    score: 78.5
    metric: accuracy
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
  - benchmark: Video-MME
    model: kimi-k3
    score: 90.0
    model_version: "with subtitles"
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: Video-MME
    model: kimi-k2.5
    score: 87.4
    metric: accuracy
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
sources:
  - source_name: "MMMU official repository"
    source_url: https://github.com/MMMU-Benchmark/MMMU
    source_type: official
    last_verified: "2026-09-22"
    confidence: high
  - source_name: Kimi K3 GitHub README
    source_url: https://github.com/MoonshotAI/Kimi-K3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi K2.5 GitHub README
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
    source_type: official
    last_verified: "2026-09-20"
  - source_name: "Video-MME official repository"
    source_url: https://github.com/BradyFU/Video-MME
    source_type: official
    last_verified: "2026-09-22"
    confidence: high
---

**Short answer.** Two benchmarks carry most Chinese multimodal claims: MMMU-Pro for image and document reasoning, Video-MME for video understanding. Both are accurate measures of a system, not a model, and both are dominated by preprocessing choices that vendors rarely disclose.

## What they measure

| Benchmark | Input | What a high score means |
|---|---|---|
| MMMU-Pro | Images, charts, documents, screenshots | Can reason over visual content, not just read OCR text |
| Video-MME | Video, with or without subtitles | Can track events and answer questions across time |

MMMU-Pro exists because the original MMMU could be gamed: many questions were answerable from text alone. Pro version embeds the question inside the image, forcing genuine visual reading.

## MMMU-Pro

Roughly 3,460 questions across six disciplines, with questions presented as screenshots rather than text. The design closes the text-only shortcut and raises the bar for document understanding — invoices, charts, forms, slides.

The undisclosed variables matter: image resolution, whether OCR tools were allowed, and how many images the model may process per question. A vendor comparing its MMMU-Pro score to another's without those settings is comparing preprocessing pipelines.

## Video-MME

900 videos across short, medium and long durations, with questions about events, objects and temporal order. Reported overall and by duration bucket.

The duration breakdown is the useful part: models often handle short clips well and degrade sharply on long video because frame sampling discards exactly the information the question needs. A single overall number hides that curve.

## Why the numbers are hard to compare

Three preprocessing decisions change results more than the model:

1. **Resolution.** Higher resolution improves document and chart reading and multiplies token cost.
2. **Frame sampling.** More frames help long video and increase latency linearly.
3. **Subtitles and OCR.** Audio transcripts can carry a video benchmark without visual understanding.

None of these is consistently published, which is why this page records source type and date beside every result.

## Our read

**MMMU-Pro is the more honest of the two, and still not honest enough.** Embedding questions in screenshots removed the worst shortcut; it did not standardise resolution or tool access, which is where the remaining variance lives.

**Video-MME is where Chinese vendors overclaim most.** Short-clip results are strong across the board and tell buyers almost nothing about long-form video, which is the actual production case — surveillance review, meeting analysis, media monitoring.

**For document-heavy work, benchmark choice matters less than your own sample.** Invoices, forms and tables differ from MMMU-Pro's academic questions; a 20-document test on your own corpus is more predictive than any published score.

**Treat multimodal claims without a named benchmark as marketing.** "Supports images" is a capability flag, not a measurement, and the gap between a demo and a document pipeline is where most projects fail.
