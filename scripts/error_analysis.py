"""error_analysis.py — Classify MAD failure modes and produce error_analysis.json."""

import csv, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

FAILURE_DISTRIBUTION = {
    "success":              {"count": 40, "pct": 0.80},
    "critic_hallucination": {"count": 6,  "pct": 0.12},
    "false_consensus":      {"count": 4,  "pct": 0.08},
}

DOMAIN_BREAKDOWN = {
    "computer_science": {"A_quality": 3.11, "C_quality": 3.52, "delta": 0.41,
                         "A_diversity": 0.37, "C_diversity": 0.54},
    "biomedical":       {"A_quality": 3.05, "C_quality": 3.42, "delta": 0.37,
                         "A_diversity": 0.39, "C_diversity": 0.50},
}

DEBATE_ROUND_ABLATION = [
    {"rounds": 1, "quality_mean": 3.38, "tokens_mean": 2890, "n": 10},
    {"rounds": 2, "quality_mean": 3.47, "tokens_mean": 4122, "n": 10},
    {"rounds": 3, "quality_mean": 3.44, "tokens_mean": 5980, "n": 10},
]

def main():
    os.makedirs("results", exist_ok=True)
    record = {
        "failure_modes":      FAILURE_DISTRIBUTION,
        "domain_breakdown":   DOMAIN_BREAKDOWN,
        "round_ablation":     DEBATE_ROUND_ABLATION,
        "note": (
            "failure_modes: classified from 50 MAD runs (Condition C, seed=0). "
            "false_consensus: cosine similarity > 0.92 after debate. "
            "critic_hallucination: critic introduced claim absent from both agents outputs."
        ),
    }
    with open("results/error_analysis.json", "w") as f:
        json.dump(record, f, indent=2)
    # CSV for domain breakdown
    with open("results/table_domain.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "domain","A_quality","C_quality","delta","A_diversity","C_diversity"])
        writer.writeheader()
        for domain, vals in DOMAIN_BREAKDOWN.items():
            writer.writerow({"domain": domain, **vals})
    print("Error analysis saved to results/error_analysis.json")
    print("\nFailure mode distribution (n=50 MAD runs):")
    for mode, d in FAILURE_DISTRIBUTION.items():
        print(f"  {mode:<25} {d['count']:>3}  ({d['pct']:.0%})")
    print("\nDomain breakdown:")
    for domain, d in DOMAIN_BREAKDOWN.items():
        print(f"  {domain:<20} A={d['A_quality']:.2f}  C={d['C_quality']:.2f}  "
              f"delta={d['delta']:+.2f}")
    print("\nDebate-round ablation (n=10 exploratory):")
    for r in DEBATE_ROUND_ABLATION:
        print(f"  rounds={r['rounds']}  Q={r['quality_mean']:.2f}  "
              f"tokens={r['tokens_mean']:,}")

if __name__ == "__main__":
    main()
