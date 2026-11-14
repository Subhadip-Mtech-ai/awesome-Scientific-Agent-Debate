evaluation_protocol.md — pre-registered hypotheses and decision rules

**STATUS: FROZEN** — protocol committed before any reported run.
See `docs/protocol_freeze.txt` for SHA-256 hash and UTC timestamp.

## Hypotheses (H) and decision rules (DR)

| ID | Hypothesis | Metric | Decision Rule | Outcome |
|----|-----------|--------|--------------|---------|
| H1 | MAD (C) outperforms Single-LLM (A) in hypothesis quality | ΔQ = Q(C) − Q(A) | DR1: ΔQ > 0.20 | ✅ MET: ΔQ = 0.39 |
| H1b | The quality CI for C does not overlap with CI for A | 95% bootstrap CI | DR2: CIs do not overlap | ✅ MET: A=(2.91–3.26), C=(3.29–3.64) |
| H2 | Self-Consistency (B) closes ≥50% of the quality gap A→C | % gap closed = (Q(B)−Q(A)) / (Q(C)−Q(A)) | DR3: % ≥ 50% | ✅ MET: 59% |
| H3 | MAD uses ≥2× the tokens of Single-LLM | Token ratio = Tokens(C) / Tokens(A) | DR4: ratio ≥ 2.0 | ✅ MET: 3.4× |
| H4 | MAD (C) produces more diverse hypotheses than Single-LLM (A) | ΔD = D(C) − D(A) | DR5: ΔD > 0.05 | ✅ MET: ΔD = 0.14 |

**Note (paper Sec. VII):** H2 and H3 are partly near-consequences of the experimental design (SC uses 5 calls; MAD uses 6 calls). These are disclosed explicitly in the paper.

## Primary metric

**Quality Q**: LLM-judge score 1–5 (plausibility, specificity, relevance), mean over 50 prompts.
- Judge model: gpt-4o-mini (separate from generator backbone)
- Answer order randomised to mitigate position bias [Chan et al. 2023]
- Judge seed = 42; temperature = 0.0

## Test set

- Dataset: HypoBench (Liu et al. 2025, MIT licence)
- N prompts: **50** (25 CS + 25 Bio)
- Random seed: **42**
- 5 independent seeds reported; smoke seed 999 never reported

## Decision rule for claiming C superior

Condition C is claimed superior **only if**:
- ΔQ > 0.20, **AND**
- 95% CI for C does not overlap with 95% CI for A, **AND**
- Token cost increase < 5×

## Confidence intervals

- Bootstrap resampling: n_b = 1000
- CI level: 95%
- Reported as (mean, lower, upper)

## Changes to protocol

*None. Protocol was not modified after freezing (timestamp in docs/protocol_freeze.txt).*

## Exploratory analyses (post-hoc, clearly labelled in paper)

The following analyses were NOT pre-registered and are labelled exploratory:
- Debate-round ablation (1 vs. 2 vs. 3 rounds)
- Domain breakdown (CS vs. Biomedical)
- Failure mode classification (false consensus, critic hallucination)
