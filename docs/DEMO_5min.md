# 5-Minute Demo Script

**Talk title:** Does Debate Improve Scientific Hypothesis Quality?
**Speaker:** Subhadip Bag, MRA2026005, IIIT Prayagraj

---

## Slide 1 — Motivation (45 s)

"My literature review found 19 papers on multi-agent systems for hypothesis generation.
Every single one bundles debate, retrieval, role specialisation, and ranking together.
You can't tell which part actually helps. That's the attribution gap I'm addressing."

[Show Table I from paper — prior systems, isolation status]

---

## Slide 2 — Experimental Design (60 s)

"I ran three pipeline variants on 50 HypoBench prompts.
Everything identical: same LLM, same temperature, same seed.
Only the collaboration structure changes."

[Show Fig. 1 — three-condition architecture diagram]

"Condition A: one LLM call, three hypotheses.
Condition B: five independent calls, pick the centroid-nearest one — Self-Consistency.
Condition C: two agents + a critic, two revision rounds — Multi-Agent Debate."

---

## Slide 3 — Results (75 s)

[Show Fig. 4 — grouped bar chart]

"Here are the results. Quality goes from 3.08 to 3.31 to 3.47.
The CIs don't overlap — the differences are real.
But look at the token cost." [Show Fig. 7 — scatter plot]

"MAD costs 3.4× more tokens than a single call.
Self-Consistency alone — just five independent calls — closes 59% of that quality gap
at much lower coordination overhead."

---

## Slide 4 — Key Finding (45 s)

"The practical implication: before you build a multi-agent system,
run Self-Consistency as your baseline.
Debate adds real diversity — 0.52 vs 0.38 — but at 3.4× the cost.
Use it only when diversity is specifically what you need."

[Show Fig. 6 — pie chart of MAD failure modes: 80% success, 12% critic hallucination, 8% false consensus]

"And 20% of MAD runs have failure modes — false consensus or critic hallucination —
consistent with what our review found in the literature."

---

## Slide 5 — Reproduce (15 s)

"Everything is on GitHub. One command:
`bash scripts/reproduce_all.sh` — four minutes, one CPU core, reproduces all results."

[Show repo URL]

---

## Questions to anticipate

- **Why only n=50?** — HypoBench has 50 prompts in the standard split; using all of them is standard.
- **Why not GPT-4o?** — Cost and reproducibility. Gemma-2 on HuggingFace free tier is accessible to anyone.
- **Is this novel?** — No claim of novelty. Du et al. 2024 did MAD; we isolate it on HypoBench with Self-Consistency as a proper intermediate baseline.
