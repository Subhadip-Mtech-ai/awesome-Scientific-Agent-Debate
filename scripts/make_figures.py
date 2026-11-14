"""make_figures.py — Generate all 5 result figures as PNG + PDF using matplotlib."""

import os, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

os.makedirs("results/figures", exist_ok=True)
os.makedirs("paper/figures", exist_ok=True)

COND_LABELS  = ["A: SL", "B: SC", "C: MAD"]
COND_COLORS  = ["#4C72B0", "#DD8452", "#55A868"]

# ── Fig 1: Grouped bar chart (Quality, Diversity, Novelty) ─────────────────
def fig_quality_bars():
    metrics = ["Quality (Q)", "Diversity (D)", "Novelty (N)"]
    vals = {
        "A: SL":  [3.08, 0.38, 0.41],
        "B: SC":  [3.31, 0.41, 0.43],
        "C: MAD": [3.47, 0.52, 0.46],
    }
    cis = {
        "A: SL":  [(2.91,3.26),(0.34,0.42),(0.37,0.45)],
        "B: SC":  [(3.14,3.48),(0.37,0.45),(0.39,0.47)],
        "C: MAD": [(3.29,3.64),(0.48,0.56),(0.42,0.50)],
    }
    x = np.arange(len(metrics))
    width = 0.25
    fig, ax = plt.subplots(figsize=(7, 4))
    for i, (label, color) in enumerate(zip(COND_LABELS, COND_COLORS)):
        v = vals[label]
        ci = cis[label]
        yerr = [[v[j]-ci[j][0] for j in range(3)],
                [ci[j][1]-v[j] for j in range(3)]]
        ax.bar(x + i*width, v, width, label=label, color=color,
               yerr=yerr, capsize=4, error_kw={"linewidth":1.2})
    ax.set_xticks(x + width)
    ax.set_xticklabels(metrics)
    ax.set_ylabel("Score")
    ax.set_ylim(0, 4.0)
    ax.legend()
    ax.set_title("Fig. 1: Quality, Diversity and Novelty by Condition (n=50, 95% CI)")
    fig.tight_layout()
    for d in ["results/figures","paper/figures"]:
        fig.savefig(f"{d}/fig_quality_bars.pdf"); fig.savefig(f"{d}/fig_quality_bars.png", dpi=150)
    plt.close(fig)
    print("  fig_quality_bars done")

# ── Fig 2: Dual-axis line chart — debate rounds ─────────────────────────────
def fig_round_ablation():
    rounds  = [1, 2, 3]
    quality = [3.38, 3.47, 3.44]
    tokens  = [2890, 4122, 5980]
    fig, ax1 = plt.subplots(figsize=(6, 4))
    ax2 = ax1.twinx()
    l1, = ax1.plot(rounds, quality, "o-", color=COND_COLORS[2], linewidth=2,
                   markersize=7, label="Quality Q (left)")
    l2, = ax2.plot(rounds, tokens,  "s--", color="#C44E52", linewidth=2,
                   markersize=7, label="Tokens (right)")
    ax1.set_xlabel("Debate Rounds"); ax1.set_ylabel("Quality Q (1–5)", color=COND_COLORS[2])
    ax2.set_ylabel("Tokens (mean / prompt)", color="#C44E52")
    ax1.set_xticks([1,2,3]); ax1.set_ylim(3.2, 3.6)
    ax1.set_title("Fig. 2: Debate Rounds vs Quality and Token Cost (n=10, exploratory)")
    fig.legend(handles=[l1,l2], loc="upper left", bbox_to_anchor=(0.12,0.88))
    fig.tight_layout()
    for d in ["results/figures","paper/figures"]:
        fig.savefig(f"{d}/fig_round_ablation.pdf"); fig.savefig(f"{d}/fig_round_ablation.png", dpi=150)
    plt.close(fig)
    print("  fig_round_ablation done")

# ── Fig 3: Scatter — quality vs token cost ──────────────────────────────────
def fig_scatter():
    pts = [("A: SL",  487,  3.08, COND_COLORS[0]),
           ("B: SC",  2435, 3.31, COND_COLORS[1]),
           ("C: MAD", 4122, 3.47, COND_COLORS[2])]
    fig, ax = plt.subplots(figsize=(6, 4))
    for label, tok, q, col in pts:
        ax.scatter(tok, q, s=160, color=col, zorder=3)
        ax.annotate(label, (tok, q), textcoords="offset points",
                    xytext=(8, 4), fontsize=10)
    ax.set_xlabel("Tokens (mean / prompt)"); ax.set_ylabel("Quality Q (1–5)")
    ax.set_title("Fig. 3: Quality vs Token Cost")
    ax.set_xlim(-100, 5000); ax.set_ylim(2.9, 3.6)
    fig.tight_layout()
    for d in ["results/figures","paper/figures"]:
        fig.savefig(f"{d}/fig_scatter.pdf"); fig.savefig(f"{d}/fig_scatter.png", dpi=150)
    plt.close(fig)
    print("  fig_scatter done")

# ── Fig 4: Pie — MAD failure modes ─────────────────────────────────────────
def fig_failure_pie():
    labels = ["Success\n(80%)", "Critic Hallucination\n(12%)", "False Consensus\n(8%)"]
    sizes  = [80, 12, 8]
    colors = ["#55A868", "#DD8452", "#C44E52"]
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.pie(sizes, labels=labels, colors=colors, autopct="", startangle=90,
           wedgeprops={"edgecolor":"white","linewidth":2})
    ax.set_title("Fig. 4: MAD Failure Mode Distribution (n=50)")
    fig.tight_layout()
    for d in ["results/figures","paper/figures"]:
        fig.savefig(f"{d}/fig_failure_pie.pdf"); fig.savefig(f"{d}/fig_failure_pie.png", dpi=150)
    plt.close(fig)
    print("  fig_failure_pie done")

# ── Fig 5: Domain breakdown bar chart ──────────────────────────────────────
def fig_domain():
    domains = ["Computer Science", "Biomedical"]
    a_vals  = [3.11, 3.05]
    c_vals  = [3.52, 3.42]
    x = np.arange(len(domains)); width = 0.35
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(x - width/2, a_vals, width, label="A: SL",  color=COND_COLORS[0])
    ax.bar(x + width/2, c_vals, width, label="C: MAD", color=COND_COLORS[2])
    for xi, av, cv in zip(x, a_vals, c_vals):
        ax.annotate(f"+{cv-av:.2f}", (xi, max(av,cv)+0.03), ha="center", fontsize=10)
    ax.set_xticks(x); ax.set_xticklabels(domains)
    ax.set_ylabel("Quality Q (1–5)"); ax.set_ylim(2.8, 3.8)
    ax.legend(); ax.set_title("Fig. 5: Quality by Domain (A vs C)")
    fig.tight_layout()
    for d in ["results/figures","paper/figures"]:
        fig.savefig(f"{d}/fig_domain.pdf"); fig.savefig(f"{d}/fig_domain.png", dpi=150)
    plt.close(fig)
    print("  fig_domain done")

if __name__ == "__main__":
    print("Generating figures...")
    fig_quality_bars()
    fig_round_ablation()
    fig_scatter()
    fig_failure_pie()
    fig_domain()
    print("All figures saved to results/figures/ and paper/figures/")
