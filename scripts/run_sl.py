"""
run_sl.py  --  Run Condition A: Single-LLM Baseline on all 50 HypoBench prompts.

Usage:
    python scripts/run_sl.py --config configs/experiment.yaml

Output:
    results/condition_A_outputs.json
    results/condition_A_scores.json
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from conditions import generate_sl
from evaluate import evaluate_result
from utils import load_config, save_results, save_token_log, bootstrap_ci

import numpy as np
from tqdm import tqdm


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/experiment.yaml")
    parser.add_argument("--data",   default="data/HypoBench/hypobench_50.json")
    args = parser.parse_args()

    cfg = load_config(args.config)
    model_cfg = cfg["model"]

    with open(args.data) as f:
        prompts = json.load(f)

    outputs, scores = [], []
    for entry in tqdm(prompts, desc="Condition A (SL)"):
        result = generate_sl(
            prompt=entry["gap"],
            background=entry["background"],
            n=3,
            cfg=model_cfg,
        )
        score = evaluate_result(
            result=result,
            background=entry["background"],
            gap=entry["gap"],
            reference=entry["reference_hypothesis"],
            cfg=model_cfg,
        )
        outputs.append({**result, "id": entry["id"]})
        scores.append({**score, "id": entry["id"]})

    # Aggregate
    q_vals = [s["quality"] for s in scores]
    n_vals = [s["novelty"] for s in scores]
    d_vals = [s["diversity"] for s in scores]
    g_vals = [s["groundedness"] for s in scores]
    t_vals = [s["tokens"] for s in scores]

    summary = {
        "condition": "A",
        "quality":      {"mean": np.mean(q_vals), "ci95": bootstrap_ci(q_vals)},
        "novelty":      {"mean": np.mean(n_vals), "ci95": bootstrap_ci(n_vals)},
        "diversity":    {"mean": np.mean(d_vals), "ci95": bootstrap_ci(d_vals)},
        "groundedness": {"mean": np.mean(g_vals)},
        "tokens_mean":  np.mean(t_vals),
        "n_prompts":    len(prompts),
    }

    save_results(outputs, "results/condition_A_outputs.json")
    save_results(scores,  "results/condition_A_scores.json")
    save_results([summary], "results/condition_A_summary.json")
    save_token_log("results/token_log_A.json")

    print(f"\n=== Condition A Summary ===")
    print(f"Quality  : {summary['quality']['mean']:.3f} {summary['quality']['ci95']}")
    print(f"Novelty  : {summary['novelty']['mean']:.3f}")
    print(f"Diversity: {summary['diversity']['mean']:.3f}")
    print(f"Grounded : {summary['groundedness']['mean']:.1%}")
    print(f"Tokens   : {summary['tokens_mean']:.0f} mean/prompt")


if __name__ == "__main__":
    main()
