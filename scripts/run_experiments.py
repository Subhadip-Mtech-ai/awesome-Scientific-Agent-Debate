"""run_experiments.py — Run all three conditions for all 5 seeds."""

import argparse, json, sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from conditions import generate_sl, generate_sc, generate_mad
from evaluate import evaluate_result
from utils import load_config, save_results, bootstrap_ci
from tqdm import tqdm

def run_one_seed(prompts, seed, cfg):
    results = []
    model_cfg = {**cfg["model"], "seed": seed}
    for entry in tqdm(prompts, desc=f"seed={seed}"):
        row = {"id": entry["id"], "domain": entry.get("domain",""), "seed": seed}
        for cond, fn, kwargs in [
            ("A", generate_sl,  {"n": 3}),
            ("B", generate_sc,  {"n_calls": cfg["conditions"]["B"]["calls_per_prompt"]}),
            ("C", generate_mad, {"rounds": cfg["conditions"]["C"]["n_rounds"]}),
        ]:
            res = fn(prompt=entry["gap"], background=entry["background"], cfg=model_cfg, **kwargs)
            hyps = [res["hypothesis"]] if "hypothesis" in res else res.get("hypotheses", [])
            score = evaluate_result(
                result={**res, "hypotheses": hyps},
                background=entry["background"],
                gap=entry["gap"],
                reference=entry["reference_hypothesis"],
                cfg=model_cfg,
            )
            row[cond] = {**score, "tokens": res.get("tokens", 0)}
        results.append(row)
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/experiment.yaml")
    parser.add_argument("--data",   default="data/HypoBench/hypobench_50.json")
    args = parser.parse_args()
    cfg = load_config(args.config)
    with open(args.data) as f:
        prompts = json.load(f)
    seeds = cfg.get("seeds", [0, 1, 2, 3, 4])
    all_results = []
    for seed in seeds:
        print(f"\n--- Seed {seed} ---")
        all_results.extend(run_one_seed(prompts, seed, cfg))
    os.makedirs("results", exist_ok=True)
    save_results(all_results, "results/results_main.json")
    # Also write CSV
    import csv
    flat = []
    for row in all_results:
        for cond in ["A","B","C"]:
            flat.append({
                "id": row["id"], "domain": row["domain"], "seed": row["seed"],
                "condition": cond,
                **{k: v for k, v in row[cond].items()}
            })
    with open("results/results_main.csv", "w", newline="") as f:
        if flat:
            writer = csv.DictWriter(f, fieldnames=flat[0].keys())
            writer.writeheader(); writer.writerows(flat)
    print("\nDone. Results in results/results_main.csv")

if __name__ == "__main__":
    main()
