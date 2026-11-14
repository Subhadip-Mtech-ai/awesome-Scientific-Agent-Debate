baseline_validation.md (gate G2)

These are controlled pipeline variants representing different collaboration structures, not reproductions of published tools.
Condition C (MAD) is NOT Du et al.'s full implementation; it is the minimal 2-agent + critic setup with no retrieval, no ranking. No claim is made about equivalence with any published system.

## Checks performed (non-reported smoke seed 999; results in results/baseline_validation.json)

| Item | Result | Status |
|------|--------|--------|
| All 10 sanity-check outputs parseable (3 hypotheses each from Condition A) | 10/10 correct format | VERIFIED |
| Generation deterministic (same seed → same hash) | true | VERIFIED |
| Full pipeline reproducible (sha256 of results_main.csv identical across two complete runs) | hash matches both times | VERIFIED |
| No prompt ID overlap between train/test groups in 5-fold CV | 0 overlapping groups, asserted at runtime and in tests | VERIFIED |
| LLM judge learns nothing from shuffled labels (permutation control) | AUROC 0.509 (0.473–0.527, 5 shuffles) | VERIFIED |
| Condition A baseline quality mean: 3.08 / 5.0 | 3.08 (CI: 2.91–3.26) | VERIFIED |
| Groundedness mean for Condition A ≥ 0.5 | 0.714 | VERIFIED |
| Token count logged per call | avg 487 tokens/prompt (Condition A) | VERIFIED |
| Self-Consistency centroid selection deterministic | unit test passes | VERIFIED |
| MAD sequence: agents revise after critique, not before | verified by reading qualitative outputs | VERIFIED |

## UNCERTAIN

- LLM-judge calibration: a single judge model at temperature=0.0 gives consistent scores but inherits model bias. Not corrected; reported as a limitation (paper Sec. IX).
- SC centroid selection on only 5 calls may not fully represent the output distribution. Reported, not corrected.
- Closed-world n=50: results may not generalise to full HypoBench or other domains.

## CORRECTED (deviations after first smoke run)

- Minor prompt-format inconsistency: the system prompt in conditions.py used a trailing space in the first run. Fixed after reading qualitative outputs; regression test added.
- Effect of fix: largest change in any reported metric < 0.01. See `results/archive_v1_pre_run/`.

## Not done

- No comparison to numbers from any published paper: protocols differ (we isolate debate; published systems bundle multiple components), so no discrepancy analysis is possible.
- No human expert evaluation: future work (paper Sec. X).
