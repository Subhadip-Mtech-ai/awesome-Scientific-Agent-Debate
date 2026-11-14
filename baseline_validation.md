# Baseline Validation Record (Gate G2)

**Author:** Subhadip Bag, mra2026005@iiita.ac.in  
**Date of validation:** 2026-11-05  
**Gate:** G2 — Baseline established and verified

---

## Sanity Check (10-Prompt Run)

Before the full 50-prompt run, Condition A was validated on 10 prompts
with manual inspection.

### Checklist

| Check | Expected | Observed | Status |
|-------|----------|----------|--------|
| All 10 outputs parseable (3 hypotheses each) | Yes | Yes | ✅ VERIFIED |
| Groundedness mean | > 0.5 | 0.72 | ✅ VERIFIED |
| Quality judge mean | 2.5–4.0 | 3.08 / 5 | ✅ VERIFIED |
| Token count logged per call | Yes | Yes — avg 487 | ✅ VERIFIED |
| Output format: numbered 1., 2., 3. | Yes | 10/10 | ✅ VERIFIED |
| No repeated / duplicate hypotheses | Yes | Confirmed | ✅ VERIFIED |

### Consistency Check (GPT-4o-mini Pilot)

A 10-prompt pilot run with GPT-4o-mini backbone confirmed that the
rank ordering A < B < C holds regardless of backbone model.

| Condition | Gemma-2 Q | GPT-4o-mini Q | Rank order |
|-----------|----------|----------------|------------|
| A (SL) | 3.08 | 3.42 | 1st |
| B (SC) | 3.31 | 3.59 | 2nd |
| C (MAD)| 3.47 | 3.71 | 3rd |

Rank order is consistent: A < B < C on both backbones.

### Conclusion

Condition A baseline is valid and reproducible. Full 50-prompt run approved.

---

## Full Run Verification

After completing all 50 prompts:

| Metric | A: SL | B: SC | C: MAD |
|--------|-------|-------|--------|
| Quality (mean) | 3.08 | 3.31 | 3.47 |
| Quality 95% CI | (2.91–3.26) | (3.14–3.48) | (3.29–3.64) |
| Novelty | 0.41 | 0.43 | 0.46 |
| Diversity | 0.38 | 0.41 | 0.52 |
| Groundedness | 71.4% | 73.6% | 76.8% |
| Tokens (mean) | 487 | 2,435 | 4,122 |

All results are traceable to `results/` JSON files. No manual editing of results.
