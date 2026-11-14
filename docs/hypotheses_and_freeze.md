# hypotheses_and_freeze.md — pre-registered hypotheses, decision rules, and freeze record

**Frozen:** 2026-11-01T10:45:00Z (UTC)
**Hash:** see docs/protocol_freeze.txt
**Important disclosure:** Smoke seed 999 was run BEFORE the decision rules below were written. The smoke results were inspected; this is disclosed here and in the paper (Sec. VII). Seeds 0–4 were NOT seen before freezing.

---

## Hypotheses

| ID | Statement | Metric | Threshold |
|----|-----------|--------|-----------|
| H1 | MAD (C) outperforms Single-LLM (A) in hypothesis quality | ΔQ = Q(C)−Q(A) | > 0.20 |
| H1b | Quality CI for C does not overlap with CI for A | 95% bootstrap CI | non-overlapping |
| H2 | Self-Consistency (B) closes ≥50% of quality gap A→C | (Q(B)−Q(A))/(Q(C)−Q(A)) | ≥ 0.50 |
| H3 | MAD uses ≥2× tokens of Single-LLM | Tokens(C)/Tokens(A) | ≥ 2.0 |
| H4 | MAD (C) produces more diverse hypotheses than Single-LLM (A) | ΔD = D(C)−D(A) | > 0.05 |

## Decision rules (DR)

DR1: Claim H1 supported if ΔQ > 0.20 on the full 50-prompt test set.
DR2: Claim H1b supported if 95% bootstrap CIs for Q(A) and Q(C) do not overlap.
DR3: Claim H2 supported if % gap closed ≥ 50%.
DR4: Claim H3 supported if token ratio ≥ 2.0.
DR5: Claim H4 supported if ΔD > 0.05.

**Note:** H2 and H3 are partly near-consequences of the experimental design (SC uses 5 calls; MAD uses 6 calls per prompt). This is disclosed in paper Sec. VII and does not invalidate the measurement — it limits the causal interpretation.

## Outcomes (filled after reported runs)

| ID | Supported? | Value |
|----|-----------|-------|
| H1 | YES | ΔQ = 0.39 |
| H1b | YES | A=(2.91–3.26), C=(3.29–3.64), no overlap |
| H2 | YES | 59% gap closed |
| H3 | YES | 3.4× tokens |
| H4 | YES | ΔD = 0.14 |
