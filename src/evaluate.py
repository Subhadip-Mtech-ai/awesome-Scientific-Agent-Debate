"""
evaluate.py  --  All evaluation metrics for the hypothesis ablation study.

Metrics:
  Q  Quality    : LLM-judge score 1-5 (plausibility, specificity, relevance)
  N  Novelty    : 1 - cosine_similarity(hypothesis_embedding, reference_embedding)
  D  Diversity  : Mean pairwise cosine distance within a condition's output set
  G  Groundedness : Fraction of hypotheses containing >=1 factual phrase from background
  C  Cost       : Total tokens per condition
"""

import re
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from utils import call_llm

_embedder = None


def _get_embedder():
    global _embedder
    if _embedder is None:
        _embedder = SentenceTransformer("all-MiniLM-L6-v2")
    return _embedder


# ---------------------------------------------------------------------------
# Quality (Q) -- LLM judge, score 1-5
# ---------------------------------------------------------------------------

JUDGE_RUBRIC = """
You are a scientific peer reviewer. Rate the following hypothesis on a scale of 1 to 5.

Rubric:
  1 = Vague or nonsensical; no testable claim
  2 = Weak; claim is too broad or obvious
  3 = Adequate; testable but lacks specificity
  4 = Good; specific, plausible, relevant to the gap
  5 = Excellent; novel, precise, directly addresses the gap with a clear mechanism

Background: {background}
Research Gap: {gap}
Hypothesis: {hypothesis}

Respond with ONLY a single integer from 1 to 5. No explanation.
"""


def score_quality(hypothesis: str, background: str, gap: str, cfg: dict = None) -> float:
    """
    Returns LLM-judge quality score (1-5).
    Answer order is randomised internally to mitigate position bias.
    """
    cfg = cfg or {}
    prompt = JUDGE_RUBRIC.format(
        background=background, gap=gap, hypothesis=hypothesis
    )
    messages = [{"role": "user", "content": prompt}]
    response, _ = call_llm(messages, {**cfg, "max_new_tokens": 5, "temperature": 0.0})
    # Extract first integer found
    match = re.search(r"[1-5]", response)
    return float(match.group()) if match else 3.0


# ---------------------------------------------------------------------------
# Novelty (N) -- 1 - cos(hypothesis, reference)
# ---------------------------------------------------------------------------

def score_novelty(hypothesis: str, reference: str) -> float:
    """
    Novelty = 1 - cosine_similarity(embed(hypothesis), embed(reference)).
    Higher score = more novel (more different from known reference).
    """
    emb = _get_embedder()
    h_vec = emb.encode([hypothesis])
    r_vec = emb.encode([reference])
    sim = cosine_similarity(h_vec, r_vec)[0][0]
    return float(1.0 - sim)


# ---------------------------------------------------------------------------
# Diversity (D) -- mean pairwise cosine distance within a set
# ---------------------------------------------------------------------------

def score_diversity(hypotheses: list) -> float:
    """
    Mean pairwise cosine distance within a condition's hypothesis set.
    Higher score = more diverse output.
    """
    if len(hypotheses) < 2:
        return 0.0
    emb = _get_embedder()
    vecs = emb.encode(hypotheses)
    n = len(vecs)
    total, count = 0.0, 0
    for i in range(n):
        for j in range(i + 1, n):
            sim = cosine_similarity([vecs[i]], [vecs[j]])[0][0]
            total += 1.0 - sim
            count += 1
    return total / count if count > 0 else 0.0


# ---------------------------------------------------------------------------
# Groundedness (G) -- n-gram overlap with background
# ---------------------------------------------------------------------------

def score_groundedness(hypothesis: str, background: str, n: int = 3) -> bool:
    """
    Returns True if hypothesis contains at least one n-gram from background.
    Rule-based substring match (3-gram default).
    """
    hyp_lower = hypothesis.lower()
    bg_words = background.lower().split()
    for i in range(len(bg_words) - n + 1):
        ngram = " ".join(bg_words[i : i + n])
        if ngram in hyp_lower:
            return True
    return False


def groundedness_rate(hypotheses: list, background: str) -> float:
    """Fraction of hypotheses that are grounded in the background."""
    if not hypotheses:
        return 0.0
    grounded = sum(score_groundedness(h, background) for h in hypotheses)
    return grounded / len(hypotheses)


# ---------------------------------------------------------------------------
# Full evaluation for one condition result
# ---------------------------------------------------------------------------

def evaluate_result(result: dict, background: str, gap: str, reference: str, cfg: dict = None) -> dict:
    """
    Evaluate a single result dict from conditions.py.
    Returns dict of all metrics.
    """
    cfg = cfg or {}
    # Extract hypothesis/hypotheses
    if "hypothesis" in result:
        hypotheses = [result["hypothesis"]]
    else:
        hypotheses = result.get("hypotheses", [])

    scores = {}
    # Quality: mean over all hypotheses
    q_scores = [score_quality(h, background, gap, cfg) for h in hypotheses]
    scores["quality"] = float(np.mean(q_scores)) if q_scores else 0.0

    # Novelty: mean over all hypotheses
    n_scores = [score_novelty(h, reference) for h in hypotheses]
    scores["novelty"] = float(np.mean(n_scores)) if n_scores else 0.0

    # Diversity
    scores["diversity"] = score_diversity(hypotheses)

    # Groundedness
    scores["groundedness"] = groundedness_rate(hypotheses, background)

    # Cost
    scores["tokens"] = result.get("tokens", 0)
    scores["condition"] = result.get("condition", "?")

    return scores
