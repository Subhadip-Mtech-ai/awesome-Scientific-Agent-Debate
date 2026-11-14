"""validate_baselines.py — Run baseline sanity checks on smoke seed 999 (not reported)."""

import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from utils import load_config, bootstrap_ci
import numpy as np

cfg = load_config("configs/experiment.yaml")

print("=" * 55)
print("BASELINE VALIDATION (smoke seed 999 — not reported)")
print("=" * 55)

checks = []

# Check 1: Config loads correctly
try:
    assert cfg["model"]["seed"] == 42
    assert cfg["model"]["temperature"] == 0.7
    checks.append(("Config values match frozen protocol", True))
except AssertionError as e:
    checks.append(("Config values match frozen protocol", False))

# Check 2: bootstrap CI works
try:
    vals = list(np.random.default_rng(999).normal(3.0, 0.5, 50))
    mean, lo, hi = bootstrap_ci(vals, n_resamples=1000)
    assert lo < mean < hi
    checks.append(("Bootstrap CI: lo < mean < hi", True))
except Exception as e:
    checks.append(("Bootstrap CI: lo < mean < hi", False))

# Check 3: Evaluation protocol file exists
checks.append(("evaluation_protocol.md exists",
                os.path.exists("evaluation_protocol.md")))

# Check 4: Protocol freeze file exists
checks.append(("docs/protocol_freeze.txt exists",
                os.path.exists("docs/protocol_freeze.txt")))

# Check 5: src files exist
for f in ["src/conditions.py", "src/evaluate.py", "src/utils.py"]:
    checks.append((f"{f} exists", os.path.exists(f)))

# Report
all_pass = True
for label, ok in checks:
    status = "OK  " if ok else "FAIL"
    print(f"  [{status}] {label}")
    if not ok:
        all_pass = False

# Save validation record
os.makedirs("results", exist_ok=True)
record = {"checks": [{"label": l, "passed": p} for l, p in checks],
          "all_passed": all_pass, "smoke_seed": 999}
with open("results/baseline_validation.json", "w") as f:
    json.dump(record, f, indent=2)

print()
if all_pass:
    print("BASELINE VALIDATION PASSED — full run approved")
else:
    print("BASELINE VALIDATION FAILED — fix issues before running experiments")
    sys.exit(1)
