"""summarize.py — Aggregate results_main.csv into summary tables."""

import csv, json, os, numpy as np
sys._getframe  # noqa
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from utils import bootstrap_ci

def load_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

def summarize():
    rows = load_csv("results/results_main.csv")
    conditions = ["A", "B", "C"]
    metrics = ["quality", "novelty", "diversity", "groundedness", "tokens"]
    summary = {}
    for cond in conditions:
        cond_rows = [r for r in rows if r["condition"] == cond]
        summary[cond] = {}
        for m in metrics:
            vals = [float(r[m]) for r in cond_rows if m in r and r[m] != ""]
            if vals:
                mean, lo, hi = bootstrap_ci(vals)
                summary[cond][m] = {"mean": round(mean,4),
                                    "ci95_lo": round(lo,4),
                                    "ci95_hi": round(hi,4),
                                    "n": len(vals)}
    # Write summary JSON
    os.makedirs("results", exist_ok=True)
    with open("results/summary_by_condition.json", "w") as f:
        json.dump(summary, f, indent=2)
    # Write table CSV
    with open("results/table_main.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Metric", "A_mean", "A_ci95", "B_mean", "B_ci95",
                          "C_mean", "C_ci95", "Delta_A_C"])
        for m in metrics:
            row = [m]
            vals_by_cond = {}
            for cond in conditions:
                d = summary.get(cond, {}).get(m, {})
                mean = d.get("mean", 0)
                lo   = d.get("ci95_lo", 0)
                hi   = d.get("ci95_hi", 0)
                vals_by_cond[cond] = mean
                row += [f"{mean:.3f}", f"({lo:.2f}-{hi:.2f})"]
            delta = vals_by_cond.get("C",0) - vals_by_cond.get("A",0)
            row.append(f"{delta:+.3f}")
            writer.writerow(row)
    # Print
    print("\n=== Summary by Condition ===")
    print(f"{'Metric':<20} {'A':>8} {'B':>8} {'C':>8} {'Delta':>8}")
    print("-" * 55)
    for m in metrics:
        vals = [summary.get(c, {}).get(m, {}).get("mean", 0) for c in conditions]
        delta = vals[2] - vals[0]
        print(f"{m:<20} {vals[0]:>8.3f} {vals[1]:>8.3f} {vals[2]:>8.3f} {delta:>+8.3f}")

if __name__ == "__main__":
    summarize()
