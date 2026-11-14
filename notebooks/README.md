# Notebooks

This directory contains Jupyter notebooks for the hypothesis ablation study.

## Notebooks

| Notebook | Purpose | Status |
|----------|---------|--------|
| `Scientific_Agent_Debate_Colab.ipynb` | **Full end-to-end Google Colab reproduction** notebook with all 5 figures and 5 tables pre-rendered | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Subhadip-Mtech-ai/awesome-Scientific-Agent-Debate/blob/main/notebooks/Scientific_Agent_Debate_Colab.ipynb) [REPRODUCED] |
| `00_sanity_check.ipynb` | 10-prompt baseline sanity check (Gate G2) | [TESTED] — Condition A mean Q=3.08, groundedness=0.72 |

## How to run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/00_sanity_check.ipynb
```

Or open in Google Colab:
1. Upload the notebook to Colab
2. Upload `configs/experiment.yaml` and `src/*.py` to the Colab runtime
3. Set `HF_TOKEN` environment variable
4. Run all cells

## Expected output (sanity check)

```
=== Sanity Check Results (n=10) ===
All outputs parseable:        True (expected True)
Groundedness mean:            0.72 (expected > 0.5)
Quality judge mean:           3.08 / 5.0
Quality 95% CI:               (3.08, 2.74, 3.42)
Token count mean/prompt:      487
BASELINE VERIFIED [OK]  -- Full 50-prompt run approved
```
