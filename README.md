# Awesome Single-LLM vs Multi-Agent Debate for Scientific Hypothesis Generation

A curated collection of research papers, datasets, tools, implementations, and learning resources related to **Single-LLM and Multi-Agent Debate (MAD) systems for scientific hypothesis generation**.

This repository connects an AI-assisted research paper and citation-integrity audit with independently curated resources for understanding how single-LLM generation compares with multi-agent debate, especially for scientific ideation, evaluation, factuality, diversity, and cost.

## Contents

- [Overview](#overview)
- [AI-Assisted Research Paper](#ai-assisted-research-paper)
- [Citation Integrity Audit](#citation-integrity-audit)
- [Survey and Review Papers](#survey-and-review-papers)
- [Foundational Papers](#foundational-papers)
- [Single-LLM Reasoning and Ideation](#single-llm-reasoning-and-ideation)
- [Multi-Agent Debate](#multi-agent-debate)
- [Scientific Discovery and Hypothesis Generation](#scientific-discovery-and-hypothesis-generation)
- [Evaluation, Efficiency and Open Problems](#evaluation-efficiency-and-open-problems)
- [Datasets](#datasets)
- [Tools and Libraries](#tools-and-libraries)
- [GitHub Implementations](#github-implementations)
- [Tutorials and Learning Resources](#tutorials-and-learning-resources)
- [Research Gaps](#research-gaps)
- [License](#license)

## Overview

Large language models are increasingly being studied not only as systems that answer scientific questions, but also as systems that help generate new research ideas and hypotheses. Two important approaches are single-LLM generation and multi-agent debate. A single-LLM system can generate hypotheses using prompting, retrieval, self-consistency, or iterative refinement. A multi-agent debate system instead uses several LLM instances or specialized agents that generate, critique, revise, rank, or judge candidate ideas.

The literature reviewed in the accompanying research paper suggests that multi-agent debate can improve reasoning and factuality in several benchmark settings, but that part of the measured benefit may come from ensembling and majority voting rather than argumentative exchange itself. Debate also introduces risks such as correlated errors, premature consensus, sycophancy, and higher inference cost. For scientific hypothesis generation, the evaluation problem is different because there is usually no single ground-truth answer: novelty, feasibility, mechanistic plausibility, testability, diversity, and downstream experimental success may trade off against each other.

Scientific multi-agent systems such as AI co-scientist, SciAgents, and Robin demonstrate promising research workflows, but the literature still lacks enough controlled, cost-matched comparisons against strong single-LLM baselines. This repository therefore emphasizes both the promise and the limitations of multi-agent approaches and collects resources that help researchers evaluate them critically.

## AI-Assisted Research Paper

**Title:** Single-LLM Versus Multi-Agent Debate Systems for Scientific Hypothesis Generation

**Description:** A comparative review of single-LLM and multi-agent debate architectures, evidence, limitations, cost, scientific discovery applications, and open research questions.

[View the AI-Assisted Research Paper](paper/AI_Assisted_Research_Paper.pdf)

## Citation Integrity Audit

The original AI-generated paper contained 24 references. A systematic sample of 10 references was audited for publication existence, bibliographic metadata, and identifiers. The audit reported 8 references as verified and 2 with metadata problems, producing an authenticity score of 95/100.

The audit is a separate document from this repository's curated literature list. Resources added here should be checked independently before being treated as verified.

[View the Citation Integrity Audit](citation-audit/Citation_Integrity_Audit.pdf)

## Survey and Review Papers

- **HeurekaBench: A Benchmarking Framework for AI Co-scientist** — Introduces an evaluation framework for open-ended scientific analysis and agentic research workflows.
- **Can LLMs Generate Novel Research Ideas?** — Large-scale human evaluation of LLM-generated research ideas and their novelty, feasibility, self-evaluation, and diversity.
- **Towards an AI co-scientist** — Describes a multi-agent scientific discovery system using generation, debate, evolution, ranking, and related specialized roles.

## Foundational Papers

- **AI Safety via Debate** — Early proposal of debate between AI systems as a scalable oversight mechanism.
- **Improving Factuality and Reasoning in Language Models through Multiagent Debate** — Establishes a core multi-agent debate approach for reasoning and factuality.
- **Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate** — Introduces debate as a response to the Degeneration-of-Thought problem.
- **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** — Foundational work on prompting models to produce intermediate reasoning steps.
- **Self-Consistency Improves Chain of Thought Reasoning in Language Models** — Shows how sampling multiple reasoning paths can improve reasoning without inter-agent communication.

## Single-LLM Reasoning and Ideation

See [references/references.md](references/references.md) for the complete curated list.

## Multi-Agent Debate

See [references/references.md](references/references.md) for the complete curated list.

## Scientific Discovery and Hypothesis Generation

The scientific-discovery section includes AI co-scientist, SciAgents, Robin, scientific-ideation datasets, and benchmarks that support evaluation of generated hypotheses.

## Evaluation, Efficiency and Open Problems

Important themes include:
- Debate versus independent voting/ensembling
- Diversity of reasoning
- Correlated errors and groupthink
- Selective triggering of debate
- Memory and message retention
- Compute and token cost
- Novelty versus feasibility
- Claim and citation verification
- Controlled single-agent versus multi-agent ablations

## Datasets

See [datasets/datasets.md](datasets/datasets.md).

## Tools and Libraries

See [tools/tools.md](tools/tools.md).

## GitHub Implementations

See [implementations/github-repositories.md](implementations/github-repositories.md).

## Tutorials and Learning Resources

See [tools/tools.md](tools/tools.md#tutorials-and-learning-resources) for learning resources and official documentation.

## Research Gaps

The accompanying research paper highlights several important gaps:

1. Matched single-LLM versus multi-agent ablations with equal compute budgets.
2. Joint evaluation of novelty, feasibility, testability, and diversity.
3. Debate protocols designed for divergent ideation rather than convergence on one answer.
4. Cost-normalized comparisons using tokens, forward passes, or wall-clock time.
5. Evaluation of correlated errors and agent heterogeneity.
6. Longitudinal tracking from generated hypotheses to real experimental outcomes.

## License

The original research paper and citation-audit document are the student's own course materials. External papers, datasets, tools, and repositories remain subject to their respective licenses and terms. This repository's original curation and documentation are released under the MIT License.
