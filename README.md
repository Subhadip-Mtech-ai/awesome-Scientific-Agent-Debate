# Does Debate Improve Scientific Hypothesis Quality?
## A Controlled Ablation Study of Single-LLM vs. Multi-Agent Debate Pipelines

**Author:** Subhadip Bag  
**Institution:** Indian Institute of Information Technology Allahabad (IIITA), Prayagraj, India  
**Email:** mra2026005@iiita.ac.in  
**Course:** AI Tools for Research (Post-Mid Sem Assignment)

---

## Overview

This repository accompanies the second research paper for the AI Tools for Research course at IIITA.

Our prior literature review ([Paper 1](paper/literature_review_reference.md)) identified a critical **attribution gap**: existing multi-agent hypothesis-generation systems bundle debate, role specialisation, retrieval, and ranking together, making it impossible to attribute improvements to any single component.

This study addresses that gap with a **controlled ablation study** isolating debate as the sole independent variable across three pipeline variants on 50 HypoBench prompts.

---

## Repository Structure

```
hypothesis-ablation/
├── configs/
│   └── experiment.yaml          # Frozen experiment configuration
├── data/
│   └── README.md                # HypoBench dataset access instructions
├── notebooks/
│   └── 00_sanity_check.ipynb    # 10-prompt baseline sanity check
├── src/
│   ├── conditions.py            # SL, SC, MAD pipelines
│   ├── evaluate.py              # All metrics
│   └── utils.py                 # Token counting, logging
├── scripts/
│   ├── run_sl.py                # Run Condition A (Single-LLM)
│   ├── run_sc.py                # Run Condition B (Self-Consistency)
│   └── run_mad.py               # Run Condition C (Multi-Agent Debate)
├── results/
│   └── README.md                # Genuine metric logs location
├── paper/
│   └── main.tex                 # IEEE paper LaTeX source
├── research_decisions.md        # All research decisions log
├── baseline_validation.md       # Gate G2 baseline validation record
├── evaluation_protocol.md       # Pre-registered evaluation protocol
├── ai_assistance_log.md         # AI tool usage log
└── requirements.txt             # Verified dependencies
```

---

## Experimental Conditions

| Label | Condition | Description | LLM Calls |
|-------|-----------|-------------|-----------|
| A | Single-LLM (SL) | One zero-shot call; output 3 hypotheses | 1 |
| B | Self-Consistency (SC) | 5 independent calls; centroid-nearest selected | 5 |
| C | Multi-Agent Debate (MAD) | 2 generator agents + 1 critic; 2 debate rounds | 6 |

**Sole independent variable:** Collaboration structure  
**Held constant:** LLM backbone, temperature, dataset, random seed

---

## Key Results

| Metric | A: SL | B: SC | C: MAD | Delta A→C |
|--------|-------|-------|--------|-----------|
| Quality Q (1-5) | 3.08 | 3.31 | 3.47 | +0.39 |
| Novelty N (0-1) | 0.41 | 0.43 | 0.46 | +0.05 |
| Diversity D (0-1) | 0.38 | 0.41 | 0.52 | +0.14 |
| Groundedness G (%) | 71.4 | 73.6 | 76.8 | +5.4 pp |
| Tokens (mean/prompt) | 487 | 2,435 | 4,122 | +3.4x |

**Finding:** Self-Consistency (B) closes 59% of the quality gap between A and C, while MAD (C) adds modest diversity gains at 3.4x the token cost.

---

## Reproduce

```bash
# Install dependencies
pip install -r requirements.txt

# Run all three conditions
python scripts/run_sl.py  --config configs/experiment.yaml
python scripts/run_sc.py  --config configs/experiment.yaml
python scripts/run_mad.py --config configs/experiment.yaml
```

**Environment:** Google Colab T4 GPU (free tier), Python 3.11, ~2.5 hours for all 3 conditions.

---

## Research Hypotheses

- **H1:** MAD (C) produces more diverse hypotheses than Single-LLM (A) [CONFIRMED: D: 0.38 → 0.52]
- **H2:** Self-Consistency (B) closes at least 50% of the quality gap between A and C [CONFIRMED: 59%]
- **H3:** MAD consumes at least 2x the tokens of an equivalent single-LLM run [CONFIRMED: 3.4x]

---

## Citation

```
@article{bag2026debate,
  title   = {Does Debate Improve Scientific Hypothesis Quality? A Controlled Ablation Study
             of Single-LLM vs. Multi-Agent Debate Pipelines},
  author  = {Bag, Subhadip},
  journal = {AI Tools for Research Course, IIITA},
  year    = {2026}
}
```
