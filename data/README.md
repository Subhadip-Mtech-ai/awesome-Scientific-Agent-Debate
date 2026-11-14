# HypoBench Dataset

## Access

HypoBench is an open benchmark for scientific hypothesis generation.

- **Source:** https://github.com/HypoBench/HypoBench
- **Paper:** Liu et al. (2025), "HypoBench: Towards systematic and principled benchmarking
  for hypothesis generation", arXiv:2504.11524
- **License:** MIT License
- **Access verified:** 2026-11-01

## Setup

```bash
git clone https://github.com/HypoBench/HypoBench.git data/HypoBench
```

## Subset Used

We use 50 prompts drawn equally from two domains:

| Domain | n | Source field |
|--------|---|-------------|
| Computer Science | 25 | `cs` |
| Biomedical | 25 | `bio` |

Each prompt contains:
1. A 150-word **background paragraph**
2. A **knowledge-gap statement**
3. A **reference hypothesis** (held out during generation; used only for novelty scoring)

## Data Format

Each entry in the HypoBench JSON:
```json
{
  "id": "cs_001",
  "domain": "computer_science",
  "background": "...",
  "gap": "...",
  "reference_hypothesis": "..."
}
```

## Licence Compliance

- Dataset is MIT-licensed: free for academic, research, and educational use
- Reference hypotheses are used only for metric computation (novelty), not as training targets
- No data is redistributed in this repository; download instructions only
