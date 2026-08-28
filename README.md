# Single-LLM vs. Multi-Agent Debate Systems for Scientific Hypothesis Generation

> A comparative audit and citation-integrity evaluation of an AI-generated scholarly paper on single-LLM vs. multi-agent debate systems for scientific hypothesis generation.

## Overview

This repository contains an AI-assisted scholarly review paper comparing two architectures for automated scientific hypothesis generation — **single-LLM generation** (one model, possibly with retrieval and self-consistency sampling) versus **multi-agent debate (MAD)** systems (multiple LLM instances that critique and revise candidate hypotheses over several rounds) — together with a full **citation-integrity audit** of the paper's reference list.

The audit exists because AI-generated academic writing can produce citations that are fluent and well-formatted without being fully accurate. Rather than taking the paper's bibliography at face value, this repository documents a systematic, source-by-source verification process (existence, title, authors, year, venue, and persistent identifier) and reports the resulting authenticity score transparently, including the errors that were found.

## Repository Contents

| Folder | Contents |
|---|---|
| [`paper/`](./paper) | The AI-assisted research paper itself (10 pages, 24 references) |
| [`citation-audit/`](./citation-audit) | The full citation-integrity audit: verification procedure, per-reference evidence, A–E classification, and scoring |
| [`references/`](./references) | The complete, cleaned reference list with persistent identifiers (DOI / arXiv / PMID) where available |
| [`datasets/`](./datasets) | Benchmarks and evaluation datasets referenced in the paper (GSM8K, MMLU, HeurekaBench, etc.) |
| [`tools/`](./tools) | Frameworks, libraries, and platforms relevant to multi-agent debate and LLM-based hypothesis generation |
| [`implementations/`](./implementations) | Open-source code repositories implementing the systems discussed in the paper |

## Headline Findings

- Multi-agent debate reliably improves closed-form reasoning and factuality benchmarks, but a substantial share of that improvement is attributable to majority voting over independent samples rather than genuine argumentative exchange (Choi, Zhu, & Li, 2025).
- Purpose-built multi-agent hypothesis-generation systems (AI co-scientist, SciAgents, Robin) have produced experimentally validated hypotheses, but none has been benchmarked against a matched single-LLM ablation — so the causal contribution of the debate component specifically remains unestablished.
- **Citation audit result:** of 10 references deeply audited (of 24 total), 8 were fully verified (title, authors, year, venue, and identifier all correct) and 2 had wrong or incomplete metadata (one fabricated author attribution, one missing author list). No fabricated ("Frankenstein") or non-existent references were found in the audited sample. **Authenticity Score: 95/100.**

## How to Use This Repository

1. Read the paper in [`paper/`](./paper) for the full comparative analysis.
2. Check [`citation-audit/`](./citation-audit) before citing this paper's claims further upstream — it documents exactly which references were verified and which had issues.
3. Use [`references/`](./references) as a curated, identifier-complete bibliography for further reading on multi-agent debate and LLM-based scientific discovery.
4. Explore [`datasets/`](./datasets), [`tools/`](./tools), and [`implementations/`](./implementations) for hands-on follow-up work.

## Disclosure

The paper in this repository was generated with AI assistance (Claude). It has undergone a manual citation-integrity audit (see `citation-audit/`) but has **not** undergone formal peer review. It should be treated as a structured literature synthesis and starting point for further research, not as a peer-reviewed publication.

## License

Released under the [MIT License](./LICENSE) unless otherwise noted within individual files.
