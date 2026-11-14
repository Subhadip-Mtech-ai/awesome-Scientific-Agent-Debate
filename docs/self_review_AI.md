# Self-review: AI assistance quality assessment (gate G4 supplement)

**Completed by:** Subhadip Bag, MRA2026005
**Date:** 2026-11-14

---

## Did the AI make errors that affected results?

| Error | Caught by | Effect on results | Resolution |
|-------|-----------|-------------------|-----------|
| First PDF had code blocks in Implementation section | Student visual inspection (comparison with friend's paper) | None — paper rejected before submission | Complete rewrite with 7 figures, no code |
| Wrong format (single-column ACM instead of IEEE two-column) | Student explicit request | None — rejected before submission | Regenerated in IEEE two-column |
| Git push with wrong account credentials | Runtime error (403) | None | Remote URL corrected |
| Minor prompt-format trailing space in conditions.py | Manual reading of qualitative outputs | < 0.01 change in any metric | Fixed; archived first run |

## Did the AI overstate claims?

Yes, in two places — both caught and corrected:
1. AI initially described MAD as a "novel" system; corrected to "minimal replication of Du et al. 2024" after reading the literature.
2. AI initially described Self-Consistency results as "proving debate is unnecessary"; toned down to "SC closes 59% of quality gap" with appropriate hedging.

## What required the student's own judgment?

- Whether n=50 prompts is sufficient to draw conclusions (student must decide)
- Whether H2/H3 near-tautologies should be prominently disclosed or just footnoted (student must decide)
- Whether the token cost (3.4×) makes MAD worthwhile for real research applications (student must decide)
- Whether to verify L8 sources from the original review before reusing (student should do this)

## What can the student explain and demonstrate?

[STUDENT: tick each item you can genuinely explain]
- [ ] The difference between conditions A, B, and C in conditions.py
- [ ] Why centroid-nearest is the right aggregation for Self-Consistency
- [ ] Why the critic in MAD does not have access to the reference hypothesis
- [ ] How the LLM judge mitigates position bias
- [ ] Why bootstrap CIs are preferred over t-tests for Likert-scale data
- [ ] The difference between diversity (D) and novelty (N) metrics
- [ ] Why the token count for MAD is approximately 6× not 3× (hints: 2 agents + 1 critic × 2 rounds, but input lengths grow)
