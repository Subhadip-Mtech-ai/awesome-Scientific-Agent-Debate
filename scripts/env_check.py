"""env_check.py — Verify environment is correctly set up before running experiments."""

import sys
import importlib
import os


REQUIRED = [
    ("numpy",               "numpy"),
    ("pandas",              "pandas"),
    ("scipy",               "scipy"),
    ("sklearn",             "scikit-learn"),
    ("matplotlib",          "matplotlib"),
    ("yaml",                "pyyaml"),
    ("sentence_transformers","sentence-transformers"),
    ("tqdm",                "tqdm"),
    ("requests",            "requests"),
    ("fpdf",                "fpdf2"),
]

REQUIRED_FILES = [
    "configs/experiment.yaml",
    "src/conditions.py",
    "src/evaluate.py",
    "src/utils.py",
    "evaluation_protocol.md",
]

REQUIRED_ENV = ["HF_TOKEN"]

errors = []

print("=" * 50)
print("ENV CHECK — Hypothesis Ablation Study")
print("=" * 50)

# 1. Python version
print(f"\n[1] Python version: {sys.version}")
if sys.version_info < (3, 10):
    errors.append(f"Python >= 3.10 required, got {sys.version}")

# 2. Package imports
print("\n[2] Package imports:")
for mod, pkg in REQUIRED:
    try:
        m = importlib.import_module(mod)
        ver = getattr(m, "__version__", "unknown")
        print(f"    OK  {pkg} ({ver})")
    except ImportError:
        errors.append(f"Missing package: {pkg}")
        print(f"    FAIL  {pkg} — not installed")

# 3. Required files
print("\n[3] Required files:")
for f in REQUIRED_FILES:
    if os.path.exists(f):
        print(f"    OK  {f}")
    else:
        errors.append(f"Missing file: {f}")
        print(f"    FAIL  {f}")

# 4. Environment variables
print("\n[4] Environment variables:")
for var in REQUIRED_ENV:
    val = os.environ.get(var, "")
    if val:
        print(f"    OK  {var} is set (len={len(val)})")
    else:
        print(f"    WARN  {var} not set — HuggingFace API calls will fail")

# 5. Result
print("\n" + "=" * 50)
if errors:
    print("ENV FAIL — fix the issues above before running experiments:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("ENV OK")
print("=" * 50)
