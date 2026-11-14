# Evaluation Protocol (Pre-Registered)

**Status: FROZEN — committed before viewing any results**  
**Frozen date:** 2026-11-01  
**Author:** Subhadip Bag, mra2026005@iiita.ac.in

---

## 1. Research Question

Under a controlled protocol (same LLM backbone, same dataset, same evaluation metrics),
does Multi-Agent Debate (MAD) produce higher-quality scientific hypotheses than
single-LLM generation with an equivalent inference budget?

## 2. Hypotheses to Test

| ID | Hypothesis | Metric | Threshold |
|----|-----------|--------|-----------|
| H1 | MAD (C) produces more diverse hypotheses than SL (A) | Diversity D | ΔD > 0.05 |
| H2 | Self-Consistency (B) closes ≥50% of the quality gap between A and C | Quality Q | % gap ≥ 50% |
| H3 | MAD consumes at least 2x the tokens of SL | Tokens | Ratio ≥ 2.0 |

## 3. Primary Metric

**Quality (Q):** LLM-judge score 1–5 (plausibility, specificity, relevance)
- Mean over 50 prompts
- Judge model: gpt-4o-mini (separate from generator)
- Answer order randomised to mitigate position bias [Chan et al., 2023]

## 4. Test Set

- Dataset: HypoBench [Liu et al., 2025]
- N prompts: **50** (25 CS + 25 Biomedical)
- Seed: **42**
- Split: **all 50 prompts** (no train/test split; this is a generation/evaluation study)

## 5. Decision Rule

Condition C is claimed superior **only if**:
- ΔQ (C − A) > 0.2, **AND**
- Token cost increase < 5×

## 6. Confidence Intervals

- Bootstrap resampling: n_b = 1000
- CI level: 95%
- Reported as (mean, lower, upper)

## 7. What Was NOT Pre-Specified

The following analyses are **exploratory** (conducted after viewing results) and
are clearly labelled as such in the paper:
- Debate-round ablation (1 vs. 2 vs. 3 rounds)
- Domain breakdown (CS vs. Biomedical)
- Failure mode classification (false consensus, critic hallucination)

## 8. Changes to Protocol

*None. Protocol was not modified after freezing.*
