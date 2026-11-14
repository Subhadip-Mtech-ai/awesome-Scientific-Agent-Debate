#!/usr/bin/env bash
# reproduce_all.sh — Full reproduction pipeline for the hypothesis ablation study.
# Regenerates all results, figures, and paper/preview.pdf from scratch.
# [TESTED] ~2.5 hours on Google Colab T4; ~4 min on CPU for smoke run only.

set -euo pipefail

echo "========================================================"
echo "  Hypothesis Ablation — Full Reproduction Pipeline"
echo "========================================================"

# 0. Environment check
echo "[0] Checking environment..."
python3 scripts/env_check.py

# 1. Validate baselines
echo "[1] Running baseline validation (smoke seed 999)..."
python3 scripts/validate_baselines.py

# 2. Run experiments (all 3 conditions, 5 seeds)
echo "[2] Running experiments (Conditions A, B, C — 5 seeds each)..."
python3 scripts/run_experiments.py --config configs/experiment.yaml

# 3. Summarize
echo "[3] Summarizing results..."
python3 scripts/summarize.py

# 4. Error analysis
echo "[4] Running error analysis (MAD failure modes)..."
python3 scripts/error_analysis.py

# 5. Make figures
echo "[5] Generating figures..."
python3 scripts/make_figures.py

# 6. Make paper numbers (LaTeX macros)
echo "[6] Generating paper numbers (LaTeX macros)..."
python3 scripts/make_paper_numbers.py

# 7. SHA-256 of main results
echo "[7] Computing SHA-256 of results_main.csv..."
sha256sum results/results_main.csv | tee results/logs/results_main.sha256
echo "    Expected: see results/logs/results_main.sha256"

# 8. Unit tests
echo "[8] Running unit tests..."
python3 -m unittest tests.test_pipeline -v

echo ""
echo "========================================================"
echo "  DONE. Check results/ and paper/ directories."
echo "  To compile the paper: cd paper && pdflatex main"
echo "  (requires IEEEtran — use Overleaf if not installed locally)"
echo "========================================================"
