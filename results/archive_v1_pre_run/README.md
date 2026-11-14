# Archive: v1 Pre-Fix Results

This directory contains results from the **first run** before the prompt-format inconsistency was corrected.

## What was fixed

A trailing space in the system prompt in `src/conditions.py` caused minor tokenisation differences across conditions in the first run. Found by manually reading qualitative outputs after the smoke run.

## Effect on results

Largest change in any metric: < 0.01 (negligible). See `results/pre_post_fix_comparison.csv`.

## Files

Same structure as the main `results/` directory. All files are archived for transparency and reproducibility.
