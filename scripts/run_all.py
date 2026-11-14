"""
run_all.py  --  Run all three conditions sequentially and produce combined results table.

Usage:
    python scripts/run_all.py --config configs/experiment.yaml

Calls run_sl.py, run_sc.py, run_mad.py in sequence and prints the combined results table.
"""

import subprocess
import sys
import json
import argparse
import numpy as np


def run_condition(script: str, config: str):
    print(f"\n{'='*60}")
    print(f"Running {script}")
    print('='*60)
    result = subprocess.run(
        [sys.executable, script, "--config", config],
        capture_output=False,
    )
    if result.returncode != 0:
        print(f"WARNING: {script} exited with code {result.returncode}")


def load_summary(path: str) -> dict:
    try:
        with open(path) as f:
            data = json.load(f)
        return data[0] if isinstance(data, list) else data
    except FileNotFoundError:
        return {}


def print_table(summaries: dict):
    print("\n" + "="*70)
    print("COMBINED RESULTS TABLE")
    print("="*70)
    header = f"{'Metric':<25} {'A: SL':>10} {'B: SC':>10} {'C: MAD':>10} {'Delta':>10}"
    print(header)
    print("-"*70)

    for key, label, fmt in [
        ("quality",      "Quality Q (1-5)",    ".3f"),
        ("novelty",      "Novelty N (0-1)",    ".3f"),
        ("diversity",    "Diversity D (0-1)",  ".3f"),
        ("groundedness", "Groundedness G",     ".1%"),
        ("tokens_mean",  "Tokens (mean)",      ".0f"),
    ]:
        vals = {}
        for cond in ["A", "B", "C"]:
            s = summaries.get(cond, {})
            if key == "tokens_mean":
                vals[cond] = s.get(key, 0)
            else:
                nested = s.get(key, {})
                vals[cond] = nested.get("mean", 0) if isinstance(nested, dict) else nested

        delta = vals.get("C", 0) - vals.get("A", 0)
        a_str = format(vals.get("A", 0), fmt)
        b_str = format(vals.get("B", 0), fmt)
        c_str = format(vals.get("C", 0), fmt)
        d_str = ("+" if delta >= 0 else "") + format(delta, fmt)
        print(f"{label:<25} {a_str:>10} {b_str:>10} {c_str:>10} {d_str:>10}")

    print("="*70)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/experiment.yaml")
    args = parser.parse_args()

    scripts = [
        "scripts/run_sl.py",
        "scripts/run_sc.py",
        "scripts/run_mad.py",
    ]
    for script in scripts:
        run_condition(script, args.config)

    summaries = {
        "A": load_summary("results/condition_A_summary.json"),
        "B": load_summary("results/condition_B_summary.json"),
        "C": load_summary("results/condition_C_summary.json"),
    }
    print_table(summaries)


if __name__ == "__main__":
    main()
