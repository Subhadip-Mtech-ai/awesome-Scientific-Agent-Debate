# AI Assistance Log

**Author:** Subhadip Bag, mra2026005@iiita.ac.in  
**Course:** AI Tools for Research, IIITA  
**Required by:** Assignment Gate G4 — AI usage transparency

---

## Overview

This log records every use of AI tools in this project, including what was
asked, what was used, and what human verification was performed.
All research decisions and interpretations are the author's own.

---

## Tool 1: Antigravity (Google DeepMind)

| Task | AI Contribution | Human Action |
|------|----------------|--------------|
| Literature gap identification | Suggested 5 research gaps from 19 papers | Author cross-checked each gap against source papers; selected Gap 2 (attribution gap) independently |
| Experiment design | Suggested controlled ablation with 3 conditions | Author designed protocol independently; pre-registered before viewing results |
| Repository scaffold | Generated initial file structure | Author reviewed and modified all files; added research-specific content |
| Paper writing | Drafted sections I–III | Author rewrote Methods section; verified all numerical claims |
| Figure design | No AI-generated figures | All figures drawn programmatically by author using fpdf2 |

---

## Tool 2: GitHub Copilot

| Task | AI Contribution | Human Action |
|------|----------------|--------------|
| conditions.py | Autocompleted function signatures | Author wrote all logic from scratch; Copilot only completed variable names |
| evaluate.py | Suggested cosine similarity boilerplate | Author selected appropriate embedding model; verified metric formula |
| run_*.py scripts | Suggested argparse boilerplate | Author designed output format and aggregation logic |

---

## Tool 3: HuggingFace Inference API (Gemma-2-9b-it)

**Role:** Backbone LLM for hypothesis generation (Conditions A, B, C)  
**Human oversight:** Author manually inspected 20 outputs (5 per domain × 2 domains × 2 conditions)
to verify plausibility before accepting full run results.

---

## What AI Did NOT Do

- AI did not design the research question (author identified the attribution gap)
- AI did not select the dataset (author verified HypoBench licence and access)
- AI did not interpret results (all interpretations are the author's own)
- AI did not write the Discussion or Limitations sections without substantial editing
- AI did not set the decision rule or pre-registration threshold

---

## Verification Statement

> I, Subhadip Bag, confirm that:
> 1. All AI-assisted content has been reviewed and verified by me.
> 2. All results, numerical values, and experimental claims are traceable to actual code execution.
> 3. I can explain and demonstrate every component of this work.
> 4. No AI output was accepted without author agreement and verification.

**Signature:** Subhadip Bag  
**Date:** 2026-11-14
