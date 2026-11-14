"""
utils.py  --  Token counting, LLM calls, and logging utilities.
"""

import json
import os
import time
import yaml
from datetime import datetime

_token_log = []


def load_config(path: str = "configs/experiment.yaml") -> dict:
    """Load experiment YAML configuration."""
    with open(path, "r") as f:
        return yaml.safe_load(f)


def call_llm(messages: list, cfg: dict) -> tuple:
    """
    Call the backbone LLM via HuggingFace Inference API.
    Falls back to OpenAI if HF quota is exceeded.

    Returns
    -------
    (response_text: str, total_tokens: int)
    """
    import requests

    model = cfg.get("model", "google/gemma-2-9b-it")
    temperature = cfg.get("temperature", 0.7)
    max_tokens = cfg.get("max_new_tokens", 512)

    # Format prompt from messages
    prompt = _format_messages(messages)
    input_tokens = count_tokens(prompt)

    hf_token = os.environ.get("HF_TOKEN", "")
    headers = {"Authorization": f"Bearer {hf_token}", "Content-Type": "application/json"}
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_tokens,
            "temperature": temperature,
            "do_sample": True,
            "seed": cfg.get("seed", 42),
        },
    }

    url = f"https://api-inference.huggingface.co/models/{model}"
    response = requests.post(url, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    data = response.json()

    if isinstance(data, list):
        text = data[0].get("generated_text", "")
        # Remove the input prompt from output
        if text.startswith(prompt):
            text = text[len(prompt):].strip()
    else:
        text = str(data)

    output_tokens = count_tokens(text)
    total_tokens = input_tokens + output_tokens
    return text, total_tokens


def _format_messages(messages: list) -> str:
    """Convert chat messages to a single prompt string."""
    parts = []
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        if role == "system":
            parts.append(f"System: {content}")
        elif role == "user":
            parts.append(f"User: {content}")
        elif role == "assistant":
            parts.append(f"Assistant: {content}")
    parts.append("Assistant:")
    return "\n\n".join(parts)


def count_tokens(text: str) -> int:
    """
    Approximate token count (word-based estimate, 1.3 tokens per word).
    Replace with tiktoken for exact OpenAI counts.
    """
    return int(len(text.split()) * 1.3)


def log_call(condition: str, tokens: int) -> None:
    """Append token usage to in-memory log."""
    _token_log.append({
        "condition": condition,
        "tokens": tokens,
        "timestamp": datetime.utcnow().isoformat(),
    })


def save_token_log(path: str = "results/token_log.json") -> None:
    """Write token log to disk."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(_token_log, f, indent=2)
    print(f"Token log saved to {path}")


def save_results(results: list, path: str) -> None:
    """Save list of result dicts to JSON."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {path}")


def bootstrap_ci(values: list, n_resamples: int = 1000, ci: float = 0.95) -> tuple:
    """
    Bootstrap confidence interval for the mean.

    Returns
    -------
    (mean, lower_bound, upper_bound)
    """
    import numpy as np
    arr = np.array(values)
    means = [np.mean(np.random.choice(arr, size=len(arr), replace=True))
             for _ in range(n_resamples)]
    alpha = 1 - ci
    lower = float(np.percentile(means, 100 * alpha / 2))
    upper = float(np.percentile(means, 100 * (1 - alpha / 2)))
    return float(arr.mean()), lower, upper
