"""test_pipeline.py — 12 unit and regression tests for the hypothesis ablation pipeline."""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


class TestConditionA(unittest.TestCase):
    """Unit tests for Single-LLM baseline (Condition A)."""

    def test_parse_hypotheses_numbered(self):
        from conditions import _parse_hypotheses
        text = "1. Hypothesis one.\n2. Hypothesis two.\n3. Hypothesis three."
        result = _parse_hypotheses(text, 3)
        self.assertEqual(len(result), 3)
        self.assertIn("Hypothesis one", result[0])

    def test_parse_hypotheses_fallback(self):
        from conditions import _parse_hypotheses
        text = "No numbering here, just a hypothesis."
        result = _parse_hypotheses(text, 1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], text)

    def test_parse_hypotheses_limit(self):
        from conditions import _parse_hypotheses
        text = "1. A.\n2. B.\n3. C.\n4. D."
        result = _parse_hypotheses(text, 3)
        self.assertEqual(len(result), 3)


class TestEvaluationMetrics(unittest.TestCase):
    """Unit tests for evaluation metrics."""

    def test_novelty_identical(self):
        from evaluate import score_novelty
        # Same text should have novelty near 0
        h = "Increasing training data size improves model accuracy."
        novelty = score_novelty(h, h)
        self.assertLess(novelty, 0.1)

    def test_novelty_different(self):
        from evaluate import score_novelty
        h = "Quantum entanglement enables faster-than-light communication."
        r = "Photosynthesis efficiency depends on chlorophyll concentration."
        novelty = score_novelty(h, r)
        self.assertGreater(novelty, 0.3)

    def test_diversity_single(self):
        from evaluate import score_diversity
        result = score_diversity(["Only one hypothesis."])
        self.assertEqual(result, 0.0)

    def test_diversity_identical(self):
        from evaluate import score_diversity
        h = "Deep learning improves image classification accuracy."
        result = score_diversity([h, h, h])
        self.assertLess(result, 0.05)

    def test_diversity_different(self):
        from evaluate import score_diversity
        hyps = [
            "Temperature affects enzyme activity through protein denaturation.",
            "Quantum tunnelling enables faster chemical reactions at low temperatures.",
            "Neural plasticity in the hippocampus underlies spatial memory formation.",
        ]
        result = score_diversity(hyps)
        self.assertGreater(result, 0.3)

    def test_groundedness_match(self):
        from evaluate import score_groundedness
        background = "The transformer model uses self-attention mechanisms for sequence modelling."
        hypothesis = "Self-attention mechanisms enable transformers to capture long-range dependencies."
        self.assertTrue(score_groundedness(hypothesis, background))

    def test_groundedness_no_match(self):
        from evaluate import score_groundedness
        background = "The transformer model uses self-attention mechanisms for sequence modelling."
        hypothesis = "Quantum computing will replace classical hardware by 2035."
        self.assertFalse(score_groundedness(hypothesis, background))

    def test_groundedness_rate(self):
        from evaluate import groundedness_rate
        background = "Neural networks learn hierarchical representations of input data."
        hyps = [
            "Hierarchical representations improve generalisation in neural networks.",
            "Quantum tunnelling has no relevance to machine learning.",
        ]
        rate = groundedness_rate(hyps, background)
        self.assertAlmostEqual(rate, 0.5)


class TestUtils(unittest.TestCase):
    """Unit tests for utility functions."""

    def test_count_tokens(self):
        from utils import count_tokens
        text = "This is a simple test sentence with eight words."
        tokens = count_tokens(text)
        # Should be roughly 8 * 1.3 ≈ 10
        self.assertGreater(tokens, 5)
        self.assertLess(tokens, 20)

    def test_bootstrap_ci_coverage(self):
        from utils import bootstrap_ci
        import numpy as np
        values = list(np.random.normal(3.0, 0.5, 50))
        mean, lower, upper = bootstrap_ci(values)
        self.assertAlmostEqual(mean, np.mean(values), places=5)
        self.assertLess(lower, mean)
        self.assertGreater(upper, mean)

    def test_bootstrap_ci_constant(self):
        from utils import bootstrap_ci
        values = [3.0] * 20
        mean, lower, upper = bootstrap_ci(values)
        self.assertAlmostEqual(mean, 3.0, places=5)
        self.assertAlmostEqual(lower, 3.0, places=5)
        self.assertAlmostEqual(upper, 3.0, places=5)


if __name__ == "__main__":
    unittest.main()
