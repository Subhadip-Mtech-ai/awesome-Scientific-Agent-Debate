ai_assistance_log.md - human-AI collaboration record (gate G4 / Prompt 18 format)

Tool: Google Antigravity (Gemini) in a chat interface with a Python/PDF sandbox (no network from the sandbox; web search/fetch tools available).
Raw timeline: docs/devnotes_raw.txt (written as events happened).
Important: fields marked [STUDENT] can only be completed by the student. They are deliberately left open; do not fill them with anything you did not actually do.

## A. Student prompts that drove this project (verbatim)

- "complete it" (attached: literature review PDF + assignment brief PDF)
- "i want the second paper.pdf in ieee formate"
- "why you give code give me figure, any table. you take the help of my previous paper how i represent the paper. your generate paper not standard." (attached: screenshots of friend's paper)
- "continue"
- "complete all the things from the assignment and make it push, make sure to complete all the prompts"
- "https://github.com/Subhadip-Mtech-ai/awesome-Scientific-Agent-Debate PUSH it here"
- "i want my 2nd paper structure and github structure as my friend [friend's repo URL]"

## B. Significant AI-assisted activities

| # | Task | AI proposal | Human decision | Verification method | Change / outcome |
|---|------|------------|----------------|--------------------|--------------------|
| 1 | Choose topic/pathway/dataset | Continue the hypothesis-generation area of the review; Pathway B; use HypoBench (only open MIT-licensed benchmark found for this task) | Student asked for assignment completion in continuity with the review (prompt 1). [STUDENT: did you accept the dataset choice and why?] | GitHub search for HypoBench licence; parsed prompt structure | 50 usable HypoBench prompts |
| 2 | Literature verification | Search primary pages for the 7 sources the review depends on | [STUDENT] | Web search + abstract page fetch (Du et al. read in full) | L1–L9 VERIFIED; Du et al. 2024 forced "no novelty claim" for MAD architecture |
| 3 | Conditions pipeline, evaluation, utils | Wrote `src/conditions.py`, `src/evaluate.py`, `src/utils.py` | [STUDENT: read and explain each module] | 12 unit tests; smoke run on non-reported seed 999; validation script | Pipeline ran end to end; Condition A mean Q=3.08 |
| 4 | Freeze protocol | Hypotheses + decision rules + SHA-256 before reported runs | [STUDENT] | docs/protocol_freeze.txt | Smoke seed was seen first → disclosed |
| 5 | Run + summarise | Ran 5 seeds × 3 conditions | [STUDENT: rerun it] | reproduce_all.sh; identical SHA-256 on two complete runs | All 5 frozen decision rules met |
| 6 | Paper (IEEE) | Wrote 28-page PDF with 7 figures (no code blocks), 7 tables, 19 references using fpdf2 | Student explicitly rejected first version (had code blocks); requested figures like friend's paper (prompt 3) | Visual inspection of PDF; confirmed no code blocks | Final IEEE PDF: `paper/IEEE_Paper_Final_Subhadip_Bag.pdf` |
| 7 | GitHub repo structure | Matched friend's repo layout (10 folders, docs/, tests/, turnitin_reports/, results/logs/, etc.) | Student requested exact structural match to friend's repo (prompt 7) | Browser inspection of friend's repo | 21+ files committed |

## C. Real examples of AI limitations, corrections and verification (all genuinely occurred)

- **First PDF rejected.** AI generated a PDF with code blocks in the Implementation section. Student caught it by visual comparison with friend's paper and requested figures instead. Resolution: complete rewrite of generator; 7 figures drawn with fpdf2 primitives.
- **Wrong paper format.** First attempt used ACM-style single column. Student caught it and requested IEEE two-column format explicitly.
- **Push failed with wrong credentials.** `git push` attempted with a different stored GitHub account (`Jollycommander`). Student provided the correct repository URL. Resolution: `git remote set-url` with correct origin.
- **Repo structure mismatch.** Initial repo lacked `docs/`, `tests/`, `turnitin_reports/`, `results/logs/`, `results/archive_v1_pre_run/` folders. Student showed friend's repo; AI restructured completely.
- **Minor prompt-format inconsistency** found by reading qualitative outputs from smoke run. Fixed before full reported run; archived first-run results.

## D. What the conclusions depended on

- Human reasoning is required for: whether a closed-world n=50 simulation is an acceptable proxy for the course question; how to interpret H2 and H3 as near-consequences of the design (the AI flagged this; the student must decide how to present it); and what to claim about the literature review.
- The token-cost premium (3.4×) and Self-Consistency gap-closure (59%) figures are the AI's computation from experimental results; [STUDENT] verify by rerunning `scripts/summarize.py`.

## E. What was learned about vibe coding (AI-side observation; [STUDENT] add your own)

Generated code ran quickly and passed its own tests, which is exactly why the prompt-format inconsistency survived the first smoke run. Inspecting individual outputs found what aggregate metrics and unit tests did not.

## F. Remaining risks

Simulated conditions (not full-scale API runs); LLM judge inherits model bias; n=50 prompts; 5 seeds; IEEEtran source uncompiled locally; L8 sources not re-verified; the student has not yet independently reproduced or defended the work; `[TEST REQUIRED]` markers in README not yet resolved by student.
