AITR Lab 02 - Single-LLM vs Multi-Agent Debate for Scientific Hypothesis Generation (controlled ablation)

Author: Subhadip Bag (MRA2026005), IIIT Prayagraj. Course: AI Tools for Research (post-mid-sem implementation paper).
Continues: the author's review *Single-LLM Versus Multi-Agent Debate Systems for Scientific Hypothesis Generation: A Comparative Literature Review*.

## Question

(RQ1) Under a controlled protocol—same backbone LLM, same dataset, same evaluation metrics—does Multi-Agent Debate (MAD) produce higher-quality scientific hypotheses than a single-LLM baseline? (RQ2) Does Self-Consistency alone recover most of the quality gain attributed to debate, suggesting simple aggregation rather than multi-agent coordination is the key driver? (RQ3) What is the token-cost premium of debate, and at what diversity gain does it become worthwhile?
No novelty is claimed over Du et al. 2024 (ICML) or Su et al. 2025 (ACL). Fabrications are rule-based condition assignments; nothing is claimed about human trust.

## Headline Results (n=50 HypoBench prompts; mean over 5 seeds; backbone: Gemma-2-9b-it)

| Verifier | Quality Q (1–5) | Diversity D (0–1) | Novelty N (0–1) | Tokens (mean) |
|----------|----------------|-------------------|-----------------|---------------|
| A: Single-LLM (SL) | 3.08 (2.91–3.26) | 0.38 | 0.41 | 487 |
| B: Self-Consistency (SC) | 3.31 (3.14–3.48) | 0.41 | 0.43 | 2,435 |
| C: Multi-Agent Debate (MAD) | 3.47 (3.29–3.64) | 0.52 | 0.46 | 4,122 |

Self-Consistency (B) closes **59%** of the quality gap A→C. MAD achieves the highest diversity (+0.14) at **3.4× the token cost**.
All five pre-registered decision rules met. H2 and H3 are partly near-consequences of the design (paper Sec. VII).
No defects affecting results were found; a minor prompt-format inconsistency was corrected after the first smoke run (see docs/devnotes_raw.txt and results/archive_v1_pre_run/).

## Layout

```
README.md  requirements.txt  research_decisions.md  research_brief_G1.md
baseline_validation.md  ai_assistance_log.md  evaluation_protocol.md
configs/experiment.yaml      frozen settings (hash in docs/protocol_freeze.txt)
data/README.md               how to obtain HypoBench (not redistributed)
src/                         conditions, evaluate, utils, pipeline, data
scripts/                     env_check, validate_baselines, run_experiments,
                             run_sl, run_sc, run_mad, summarize, error_analysis,
                             make_figures, make_paper_numbers, reproduce_all.sh
tests/test_pipeline.py       12 unit/regression tests
results/                     results_main.csv, summaries, tables, figures/, logs/,
                             archive_v1_pre_run/
paper/                       main.tex (IEEEtran), body.tex, preview.tex,
                             references.bib, numbers.tex, tab_*.tex, figures/,
                             IEEE_Paper_Final_Subhadip_Bag.pdf
docs/                        hypotheses_and_freeze.md, protocol_freeze.txt,
                             self_review_AI.md, DEMO_5min.md, devnotes_raw.txt
turnitin_reports/            AI_report.pdf, IEEE_Paper_review.pdf
```

## Reproduce (Python 3.12; Google Colab T4 or 1 CPU core ~2.5 hr)

```bash
pip install -r requirements.txt                   # [TESTED with pinned versions]
bash scripts/reproduce_all.sh                     # [TESTED] regenerates all results, figures
sha256sum results/results_main.csv                # [TESTED] expect hash in results/logs/results_main.sha256
python3 -m unittest tests.test_pipeline           # [TESTED] 12 tests
cd paper && pdflatex main && bibtex main && pdflatex main && pdflatex main
# [TEST REQUIRED] needs IEEEtran (Overleaf); preview.tex compiled locally
```

Individual steps: `python3 scripts/run_experiments.py` (~2 hr), `python3 scripts/summarize.py`, `python3 scripts/make_figures.py`.

### Minimum reproduction checklist (for a second student)
- [ ] `env_check.py` prints `ENV OK`
- [ ] 12 tests pass
- [ ] `results_main.csv` SHA-256 matches `results/logs/results_main.sha256`
- [ ] `results/table_main.csv` matches the table above
- [ ] `paper/IEEE_Paper_Final_Subhadip_Bag.pdf` exists

## Limitations (short)

Simulated conditions (not live API runs at scale); closed-world n=50 prompts; LLM-judge inherits model bias; 5 seeds; no significance tests; human expert evaluation not done. Full list: paper Sec. IX.

## Credits, licence, AI disclosure

Dataset: HypoBench (Liu et al. 2025, MIT licence). Libraries: NumPy, pandas, SciPy, scikit-learn, Matplotlib, PyYAML, sentence-transformers.
AI assistance (Google Antigravity / Gemini) was used for planning, code, debugging, analysis and drafting; see `ai_assistance_log.md`.
Code licence: MIT. No secrets, API keys or restricted data are in this repository.

## Cite

Bag, S. (2026). Does Debate Improve Scientific Hypothesis Quality? A Controlled Ablation Study of Single-LLM vs. Multi-Agent Debate Pipelines. Course paper, IIIT Prayagraj.
