"""
conditions.py  --  Three pipeline variants for hypothesis generation.

Condition A: Single-LLM Baseline (SL)
Condition B: Self-Consistency (SC)
Condition C: Multi-Agent Debate (MAD)

All three share the same backbone LLM, temperature, and seed.
Only the collaboration structure differs.
"""

import random
import numpy as np
from utils import call_llm, count_tokens, log_call


SYSTEM_PROMPT = (
    "You are an expert scientific researcher. "
    "Generate clear, specific, testable hypotheses based on the provided background."
)


# ---------------------------------------------------------------------------
# Condition A: Single-LLM Baseline
# ---------------------------------------------------------------------------

def generate_sl(prompt: str, background: str, n: int = 3, cfg: dict = None) -> dict:
    """
    One zero-shot call. Returns n distinct hypotheses.

    Parameters
    ----------
    prompt : str
        The research gap / question.
    background : str
        Background paragraph from HypoBench.
    n : int
        Number of hypotheses to generate.
    cfg : dict
        Config dict (temperature, seed, model).

    Returns
    -------
    dict with keys: hypotheses (list[str]), tokens (int), condition ('A')
    """
    cfg = cfg or {}
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                f"Background: {background}\n\n"
                f"Gap: {prompt}\n\n"
                f"Generate {n} distinct scientific hypotheses. "
                "Number them 1., 2., 3."
            ),
        },
    ]
    response, tokens = call_llm(messages, cfg)
    hypotheses = _parse_hypotheses(response, n)
    log_call("A", tokens)
    return {"hypotheses": hypotheses, "tokens": tokens, "condition": "A"}


# ---------------------------------------------------------------------------
# Condition B: Self-Consistency
# ---------------------------------------------------------------------------

def generate_sc(prompt: str, background: str, n_calls: int = 5, cfg: dict = None) -> dict:
    """
    5 independent single-LLM calls. Selects the hypothesis closest to the
    centroid of all outputs using sentence embeddings.

    Returns
    -------
    dict with keys: hypothesis (str), all_hypotheses (list), tokens (int), condition ('B')
    """
    from sentence_transformers import SentenceTransformer
    cfg = cfg or {}
    model_emb = SentenceTransformer("all-MiniLM-L6-v2")

    all_hyps = []
    total_tokens = 0
    for i in range(n_calls):
        result = generate_sl(prompt, background, n=1, cfg=cfg)
        all_hyps.extend(result["hypotheses"])
        total_tokens += result["tokens"]

    # Select centroid-nearest hypothesis
    embeddings = model_emb.encode(all_hyps)
    centroid = embeddings.mean(axis=0)
    distances = np.linalg.norm(embeddings - centroid, axis=1)
    best_idx = int(np.argmin(distances))

    log_call("B", total_tokens)
    return {
        "hypothesis": all_hyps[best_idx],
        "all_hypotheses": all_hyps,
        "tokens": total_tokens,
        "condition": "B",
    }


# ---------------------------------------------------------------------------
# Condition C: Multi-Agent Debate (MAD)
# ---------------------------------------------------------------------------

def _agent_generate(prompt: str, background: str, persona: str, cfg: dict) -> tuple:
    """Single agent generates one hypothesis."""
    messages = [
        {
            "role": "system",
            "content": (
                f"{SYSTEM_PROMPT} "
                f"You are {persona}. Be critical of obvious answers."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Background: {background}\n\n"
                f"Gap: {prompt}\n\n"
                "Generate one specific, testable scientific hypothesis."
            ),
        },
    ]
    return call_llm(messages, cfg)


def _critic_evaluate(h1: str, h2: str, background: str, cfg: dict) -> tuple:
    """Critic identifies inconsistencies and factual errors between two hypotheses."""
    messages = [
        {
            "role": "system",
            "content": (
                "You are a critical scientific reviewer. "
                "Identify factual inconsistencies, unsupported claims, "
                "and areas for improvement in the submitted hypotheses."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Background: {background}\n\n"
                f"Hypothesis 1: {h1}\n\n"
                f"Hypothesis 2: {h2}\n\n"
                "Critique both hypotheses. Point out specific factual errors "
                "or inconsistencies. Be specific and constructive."
            ),
        },
    ]
    return call_llm(messages, cfg)


def _agent_revise(hypothesis: str, critique: str, background: str, persona: str, cfg: dict) -> tuple:
    """Agent revises its hypothesis based on critic feedback."""
    messages = [
        {
            "role": "system",
            "content": (
                f"{SYSTEM_PROMPT} You are {persona}. "
                "Revise your hypothesis based on the critique provided."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Background: {background}\n\n"
                f"Your original hypothesis: {hypothesis}\n\n"
                f"Critique received: {critique}\n\n"
                "Revise your hypothesis to address the critique. "
                "Return only the revised hypothesis."
            ),
        },
    ]
    return call_llm(messages, cfg)


def generate_mad(prompt: str, background: str, rounds: int = 2, cfg: dict = None) -> dict:
    """
    Multi-Agent Debate: 2 generator agents + 1 critic, with `rounds` revision rounds.

    Replicates the minimal Du et al. [3] MAD setup.
    No retrieval, ranking, or specialised knowledge roles.

    Returns
    -------
    dict: hypothesis (str, Agent 1 post-revision consensus), tokens (int), condition ('C')
    """
    cfg = cfg or {}
    total_tokens = 0

    # Round 0: Independent generation
    h1, t1 = _agent_generate(prompt, background, "Agent 1 (perspective: mechanistic)", cfg)
    h2, t2 = _agent_generate(prompt, background, "Agent 2 (perspective: empirical)", cfg)
    total_tokens += t1 + t2

    # Debate rounds
    for round_num in range(rounds):
        critique, tc = _critic_evaluate(h1, h2, background, cfg)
        total_tokens += tc
        h1, tr1 = _agent_revise(h1, critique, background, "Agent 1", cfg)
        h2, tr2 = _agent_revise(h2, critique, background, "Agent 2", cfg)
        total_tokens += tr1 + tr2

    # Final output: Agent 1 revised hypothesis (post-debate consensus)
    log_call("C", total_tokens)
    return {
        "hypothesis": h1,
        "agent2_hypothesis": h2,
        "tokens": total_tokens,
        "condition": "C",
    }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _parse_hypotheses(text: str, n: int) -> list:
    """Extract numbered hypotheses from LLM output."""
    lines = text.strip().split("\n")
    hypotheses = []
    for line in lines:
        line = line.strip()
        if line and line[0].isdigit() and "." in line[:3]:
            hypotheses.append(line.split(".", 1)[1].strip())
    # Fallback: return full text as single hypothesis
    if not hypotheses:
        hypotheses = [text.strip()]
    return hypotheses[:n]
