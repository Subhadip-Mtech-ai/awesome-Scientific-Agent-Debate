"""
run_mad.py  --  Run Condition C: Multi-Agent Debate on all 50 HypoBench prompts.

Usage:
    python scripts/run_mad.py --config configs/experiment.yaml

Output:
    results/condition_C_outputs.json
    results/condition_C_scores.json
    results/condition_C_error_analysis.json
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from conditions import generate_mad
from evaluate import evaluate_result
from utils import load_config, save_results, save_token_log, bootstrap_ci

import numpy as np
from tqdm import tqdm


# Failure mode classification
def classify_failure(h1: str, h2: str, background: str) -> str:
    """
    Classify MAD failure mode:
      - 'false_consensus'   : agents converged on the same (possibly incorrect) claim
      - 'critic_hallucination': critic introduced a claim absent from both outputs
      - 'success'           : debate improved or maintained quality
    """
    h1_lower = h1.lower()
    h2_lower = h2.lower()
    # Simple heuristic: high similarity after debate = possible false consensus
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity
    emb = SentenceTransformer("all-MiniLM-L6-v2")
    vecs = emb.encode([h1, h2])
    sim = cosine_similarity([vecs[0]], [vecs[1]])[0][0]
    if sim > 0.92:
        return "false_consensus"
    # If final hypothesis contains terms absent from background + both original outputs, flag
    # (simplified heuristic -- replace with LLM-judge in full implementation)
    return "success"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/experiment.yaml")
    parser.add_argument("--data",   default="data/HypoBench/hypobench_50.json")
    args = parser.parse_args()

    cfg = load_config(args.config)
    model_cfg = cfg["model"]
    rounds = cfg["conditions"]["C"]["n_rounds"]

    with open(args.data) as f:
        prompts = json.load(f)

    outputs, scores, error_records = [], [], []

    for entry in tqdm(prompts, desc="Condition C (MAD)"):
        result = generate_mad(
            prompt=entry["gap"],
            background=entry["background"],
            rounds=rounds,
            cfg=model_cfg,
        )
        result_wrapped = {**result, "hypotheses": [result["hypothesis"]]}
        score = evaluate_result(
            result=result_wrapped,
            background=entry["background"],
            gap=entry["gap"],
            reference=entry["reference_hypothesis"],
            cfg=model_cfg,
        )
        failure = classify_failure(
            result["hypothesis"],
            result.get("agent2_hypothesis", result["hypothesis"]),
            entry["background"],
        )
        error_records.append({"id": entry["id"], "failure_mode": failure})
        outputs.append({**result, "id": entry["id"], "failure_mode": failure})
        scores.append({**score, "id": entry["id"]})

    # Failure mode summary
    from collections import Counter
    failure_counts = Counter(r["failure_mode"] for r in error_records)
    total = len(error_records)
    failure_summary = {k: {"count": v, "pct": v / total} for k, v in failure_counts.items()}

    q_vals = [s["quality"] for s in scores]
    n_vals = [s["novelty"] for s in scores]
    d_vals = [s["diversity"] for s in scores]
    g_vals = [s["groundedness"] for s in scores]
    t_vals = [s["tokens"] for s in scores]

    summary = {
        "condition": "C",
        "quality":        {"mean": np.mean(q_vals), "ci95": bootstrap_ci(q_vals)},
        "novelty":        {"mean": np.mean(n_vals), "ci95": bootstrap_ci(n_vals)},
        "diversity":      {"mean": np.mean(d_vals), "ci95": bootstrap_ci(d_vals)},
        "groundedness":   {"mean": np.mean(g_vals)},
        "tokens_mean":    np.mean(t_vals),
        "n_prompts":      len(prompts),
        "failure_modes":  failure_summary,
    }

    save_results(outputs, "results/condition_C_outputs.json")
    save_results(scores,  "results/condition_C_scores.json")
    save_results([summary], "results/condition_C_summary.json")
    save_results(error_records, "results/condition_C_error_analysis.json")
    save_token_log("results/token_log_C.json")

    print(f"\n=== Condition C Summary ===")
    print(f"Quality  : {summary['quality']['mean']:.3f} {summary['quality']['ci95']}")
    print(f"Novelty  : {summary['novelty']['mean']:.3f}")
    print(f"Diversity: {summary['diversity']['mean']:.3f}")
    print(f"Grounded : {summary['groundedness']['mean']:.1%}")
    print(f"Tokens   : {summary['tokens_mean']:.0f} mean/prompt")
    print(f"Failure modes: {failure_summary}")


if __name__ == "__main__":
    main()
