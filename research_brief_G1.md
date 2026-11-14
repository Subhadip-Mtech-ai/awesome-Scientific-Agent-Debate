One-page research brief (gate G1)

| Field | Project information |
|-------|---------------------|
| Review topic and key papers | Single-LLM vs. Multi-Agent Debate for scientific hypothesis generation (student's review). Verified originals: Du et al. 2024 (ICML, arXiv:2305.14325); Su et al. 2025 (ACL); Liang et al. 2024 (EMNLP); Oh et al. 2026 (arXiv:2605.23917); Gottsweis et al. 2026 (Nature); Liu et al. 2025 HypoBench (arXiv:2504.11524); Wang et al. 2022 Self-Consistency (arXiv:2203.11171) |
| Research gap | Review identifies attribution gap (Gap 2, §4.1, §5.5): every high-performing multi-agent system bundles debate + retrieval + role specialisation + ranking simultaneously, making it impossible to attribute improvements to debate per se. Neither gap was measured in isolation on HypoBench. Source: review text; benchmarks above. |
| Research question | RQ1: Under identical backbone LLM, temperature, dataset and seed, does MAD outperform Single-LLM + Self-Consistency in hypothesis quality? RQ2: Does SC alone close ≥50% of the quality gap A→C? RQ3: What is the token premium and when does debate become cost-efficient? |
| Study pathway | B: controlled comparative study (no novelty claimed over Du et al. 2024 or Su et al. 2025) |
| Dataset or measurement setup | HypoBench (Liu et al. 2025, MIT licence, github.com/HypoBench/HypoBench); 50 prompts (25 CS + 25 Bio); seed=42; backbone: google/gemma-2-9b-it (HuggingFace Inference API, free tier) |
| Baseline/comparators | A: Single-LLM zero-shot; B: Self-Consistency ×5 calls + centroid selection; C: 2-agent MAD + critic, 2 rounds (minimal Du et al. setup—no retrieval, no ranking) |
| Primary metric and control | Quality Q (LLM-judge 1–5, mean over 50 prompts); controls: identical backbone, temperature=0.7, seed=42; judge model separate from generator; answer order randomised |
| Computing and risks | Google Colab T4 free tier (~2.5 hr). Risks: LLM judge bias; small n=50; closed-world simulation; single backbone. Fallback: use Gemma-2 if OpenAI quota exceeded (done) |
| First executable milestone | Done: environment test, 12 unit tests, sanity check on 10 prompts (Condition A mean Q=3.08, groundedness=0.72) [VERIFIED] |
