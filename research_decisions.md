# Research Decisions Log

**Author:** Subhadip Bag, mra2026005@iiita.ac.in  
**Last updated:** 2026-11-14

This log records all major technical and research decisions made during the study,
with rationale. Required by assignment Gate G3.

---

## Decision 1: Choice of Backbone LLM

**Decision:** Use `google/gemma-2-9b-it` via HuggingFace Inference API (free tier).  
**Rationale:** Free-tier access; sufficient parameter count for hypothesis generation;
consistent with the assignment's requirement to use AI tools.  
**Alternative considered:** GPT-4o — excluded due to cost; used for 10-prompt pilot only.  
**Risk mitigation:** Pilot run with GPT-4o-mini confirmed rank ordering consistent with Gemma-2.

---

## Decision 2: Dataset Selection

**Decision:** HypoBench [Liu et al., 2025], 50-prompt subset (25 CS + 25 Bio).  
**Rationale:** Only systematic benchmark for hypothesis generation at time of writing;
MIT-licensed; directly cited in our literature review as the evaluation standard.  
**Alternative considered:** Custom prompts — rejected (not reproducible by others).  
**Licence check:** MIT — confirmed 2026-11-01 on GitHub.

---

## Decision 3: MAD Architecture

**Decision:** Minimal Du et al. [3] MAD — 2 agents + 1 critic, 2 rounds.
No retrieval, no ranking, no specialised knowledge roles.  
**Rationale:** Keeps debate as the SOLE independent variable.
Adding retrieval would reintroduce confounders (the attribution gap we are studying).  
**Alternative considered:** 3 agents — excluded (adds another variable; Condition B already
has 5 calls, making call count incomparable).

---

## Decision 4: Self-Consistency Aggregation

**Decision:** Centroid-nearest selection (embedding space, all-MiniLM-L6-v2).  
**Rationale:** Follows Wang et al. [14] original SC formulation.
"Majority vote" is for classification tasks; for open-ended generation,
centroid-nearest is the standard analogue.

---

## Decision 5: LLM-Judge Configuration

**Decision:** Separate judge model (gpt-4o-mini); answer order randomised; fixed seed.  
**Rationale:** Mitigates position bias [Chan et al., 2023]; same model as generator
would have self-preference bias.  
**What we did NOT do:** Human expert evaluation (future work; too time-consuming for n=50).

---

## Decision 6: Primary Metric

**Decision:** Quality (Q) is primary; Diversity (D), Novelty (N), Groundedness (G) are secondary.  
**Pre-registered:** 2026-11-01 in `evaluation_protocol.md`.  
**Rationale:** Quality directly answers the core research question.
Diversity and novelty are secondary contributions of MAD.

---

## Decision 7: Bootstrap CIs Instead of t-test

**Decision:** 95% bootstrap CIs (n_b=1000).  
**Rationale:** Score distribution is non-Gaussian (bounded 1–5 Likert scale).
Bootstrap makes no distributional assumptions.

---

## Decision 8: Compute Budget

**Decision:** Google Colab T4 (free tier), ~2.5 hours.  
**Rationale:** Reproducibility — any reader with a Google account can reproduce.  
**Alternative:** Local GPU or paid API — excluded (limits reproducibility).

---

## Decision 9: Debate Round Ablation

**Decision:** Run 1-round, 2-round, 3-round variants as an EXPLORATORY post-hoc analysis.  
**Status:** Clearly labelled exploratory in paper (Section VI.B).  
**Rationale:** Reviewers of Du et al. noted round count as a hyperparameter;
understanding the saturation point adds practical value.

---

## Decision 10: Failure Mode Analysis

**Decision:** Classify MAD outputs as 'success', 'false_consensus', or 'critic_hallucination'.  
**Method:** Embedding similarity heuristic (cosine > 0.92 = false consensus) + LLM-judge check.  
**Limitation:** Heuristic is imperfect; full human annotation would be more reliable.

---

## AI Tool Usage

See `ai_assistance_log.md`.
