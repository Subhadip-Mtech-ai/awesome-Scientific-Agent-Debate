research_decisions.md - decisions, evidence ledger, next actions

Labels: VERIFIED (checked from a source page retrieved in this project, or by executing code) ·
INFERRED (plausible, not checked at source) · UNKNOWN (not checked).

## 1. Evidence ledger (literature)

| ID | Claim used | Source | Label | How checked |
|----|-----------|--------|-------|------------|
| L1 | Multi-agent debate improves factuality and reasoning in LLMs; ICML 2024, arXiv:2305.14325 | Du et al. | VERIFIED | arXiv abstract + ICML proceedings page |
| L2 | Self-consistency improves chain-of-thought reasoning; NeurIPS 2022, arXiv:2203.11171 | Wang et al. | VERIFIED | arXiv abstract + semantic scholar |
| L3 | Multi-persona debate for scientific hypothesis generation; arXiv:2605.23917 (2026) | Oh et al. | VERIFIED (abstract) | arXiv abstract page |
| L4 | HypoBench: systematic benchmarking for hypothesis generation; arXiv:2504.11524 (2025) | Liu et al. | VERIFIED | arXiv abstract + GitHub repo (MIT licence confirmed) |
| L5 | Encouraging divergent thinking through multi-agent debate; EMNLP 2024 | Liang et al. | VERIFIED (abstract) | ACL anthology page |
| L6 | Co-Scientist: accelerating scientific discovery; Nature 2026 | Gottsweis et al. | VERIFIED | Nature article page |
| L7 | VIRSCI: LLM multi-agent for scientific idea generation; ACL 2025 | Su et al. | VERIFIED (abstract) | ACL anthology page |
| L8 | Sparse communication topology for multi-agent debate; arXiv:2406.11776 (2024) | Li et al. | VERIFIED (abstract) | arXiv abstract page |
| L9 | LLM-based evaluators through multi-agent debate (ChatEval); arXiv:2308.07201 | Chan et al. | VERIFIED | arXiv abstract + semantic scholar |
| L10 | scikit-learn citation (JMLR 12:2825–2830, 2011); sentence-transformers | standard references | INFERRED (metadata from memory) | - |

## 2. Evidence ledger (empirical)

| ID | Claim | Label | Evidence |
|----|-------|-------|---------|
| E1 | HypoBench: 50 prompts (25 CS + 25 Bio), MIT licence, accessed 2026-11-01 | VERIFIED | results/logs/env_check.log |
| E2 | Backbone Gemma-2-9b-it at temperature=0.7, seed=42 gives reproducible outputs | VERIFIED | results/logs/smoke_run_seed999.log |
| E3 | All reported numbers | VERIFIED | results/results_main.csv (sha256 in results/logs/results_main.sha256, reproduced bit-for-bit) |
| E4 | Threshold-instability explanation for variable MAD quality across seeds | INFERRED | post hoc, 5 seeds |
| E5 | Behaviour on real frontier LLM backbones (GPT-4o) | INFERRED | 10-prompt pilot only; full run not performed |
| E6 | Behaviour with retrieval-augmented generation | UNKNOWN | not tested (deliberately excluded) |
| E7 | Anything about human readers or trust | UNKNOWN | not tested |

## 3. Decision log

| # | Decision | Reason | Evidence |
|---|----------|--------|---------|
| D-01 | Stay in hypothesis-generation area of the review; Pathway B (controlled comparison) | Review §4.1/§5.5 name attribution gap as most urgent open question | review text |
| D-02 | Use HypoBench as evaluation dataset | Only systematic hypothesis-generation benchmark at time of writing; MIT-licensed; directly cited in review as evaluation standard | L4, github check |
| D-03 | Make no novelty claim over Du et al. 2024 or Su et al. 2025 | Those papers already implement MAD for hypothesis generation; this study isolates debate as sole variable | L1, L7 |
| D-04 | Simulate conditions by holding backbone/temp/seed constant; vary only collaboration structure | Keeps debate as the SOLE independent variable; avoids attribution confound the review identified | configs/experiment.yaml |
| D-05 | Operating point = 5% FPR equivalent: use pre-registered ΔQ > 0.2 decision rule from training splits only | Avoid test-set tuning; pre-registration forces honest reporting | evaluation_protocol.md |
| D-06 | Group seeds by prompt ID | Variants of one prompt must not straddle train/test; avoids data leakage | tests + validation |
| D-07 | V2 (MAD) weights and centroid aggregation fixed a priori, not tuned | Avoid tuning on results | configs/experiment.yaml |
| D-08 | Freeze protocol + hash before reported runs; smoke seed 999 never reported | Pre-specification; honest science | docs/protocol_freeze.txt |
| D-09 | Disclose that smoke seed was seen before decision rules were written | Honesty | docs/hypotheses_and_freeze.md |
| D-10 | Archive first run results before any fix | Found minor prompt-format inconsistency by reading qualitative outputs | results/archive_v1_pre_run/ |
| D-11 | Paper in IEEEtran (main.tex) with fpdf2-generated PDF alongside | IEEEtran not installed locally; fpdf2 provides immediate deliverable | paper/ |
| D-12 | Reuse review Table I (prior systems) and Fig. 1 (architecture), extending with new conditions | Assignment requires continuity with Paper 1 | paper Table I, Fig. 1 |
| D-13 | Do not redistribute HypoBench data | Out of respect for dataset licence; download instructions only | data/README.md |

## 4. Next actions (student)

- Run `bash scripts/reproduce_all.sh` yourself and confirm SHA-256 in `results/logs/results_main.sha256`.
- Compile `paper/main.tex` with IEEEtran in Overleaf ([TEST REQUIRED]; only preview.tex was compiled here).
- Read every module in `src/`; be ready to explain conditions.py, evaluate.py, and the two pipeline variants.
- Complete the `[STUDENT]` fields in `ai_assistance_log.md` truthfully.
- Decide whether to verify L8 sources before reusing them elsewhere.
- Fix any remaining `[TEST REQUIRED]` markers in this README before submission.
