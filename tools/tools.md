# Tools and Frameworks

Frameworks, platforms, and libraries relevant to multi-agent debate and LLM-based scientific hypothesis generation, as discussed in the paper.

## Multi-Agent Orchestration Frameworks

| Tool | Purpose | Relevance |
|---|---|---|
| **AutoGen** (Microsoft) | General-purpose framework for building multi-agent LLM conversations | Common substrate for implementing debate-style architectures |
| **CAMEL** | Role-playing multi-agent communication framework | Used in several MAD reproduction studies |
| **LangGraph** | Graph-based orchestration for multi-step / multi-agent LLM workflows | Useful for implementing sparse-topology debate (Li et al., 2024) |
| **ChatEval codebase** | Reference implementation of multi-agent debate for LLM-based evaluation | Chan et al. (2023), arXiv:2308.07201 |
| **Multi-Agent Debate (Du et al.) reference code** | Original MAD implementation for factuality/reasoning tasks | Du et al. (2023), arXiv:2305.14325 |

## Scientific Discovery / Hypothesis-Generation Systems

| System | Organization | Description |
|---|---|---|
| **AI co-scientist** | Google DeepMind / Google Research | Multi-agent system (Generation, Reflection, Ranking, Evolution, Proximity, Meta-review agents) for hypothesis generation, using simulated scientific debate as one generation strategy |
| **SciAgents** | MIT (Buehler Lab) | Multi-agent system combining LLM conversation with a materials-science ontological knowledge graph for hypothesis generation |
| **Robin** | FutureHouse | Multi-agent "lab-in-the-loop" system integrating literature search and data-analysis agents for end-to-end scientific discovery |
| **Coated-LLM** | — | Researcher/Reviewer/Moderator multi-agent framework for biomedical (drug-combination) hypothesis generation |
| **HeurekaBench harness** | — | Benchmarking infrastructure for evaluating agentic scientific-analysis systems, including critic/debate modules |

## Underlying LLM Reasoning Techniques (single-agent baselines)

| Technique | Description | Key Reference |
|---|---|---|
| **Chain-of-Thought (CoT) prompting** | Elicits intermediate reasoning steps from a single model | Wei et al. (2022), arXiv:2201.11903 |
| **Self-Consistency** | Samples multiple independent CoT reasoning paths and majority-votes over final answers, without inter-agent communication | Wang et al. (2022), arXiv:2203.11171 |
| **Retrieval-Augmented Generation (RAG)** | Grounds single-LLM idea generation in retrieved literature | Standard technique referenced across hypothesis-generation systems |

## Efficiency / Cost-Reduction Tools for Multi-Agent Debate

| Tool / Method | Purpose |
|---|---|
| **Sparse Communication Topology** | Restricts which agents can see which peers' messages to reduce token cost | Li et al. (2024), arXiv:2406.11776 |
| **Memory Masking** | Filters stale/erroneous context from debate transcripts across rounds | Tian et al. (2026), arXiv:2603.20215 |
| **Diversity-Aware Message Retention** | Retains only non-redundant messages across debate rounds | Nguyen et al. (2026), arXiv:2603.20640 |
| **iMAD (Intelligent Multi-Agent Debate)** | Learns when to trigger debate vs. rely on a single agent, to save compute | Fan, Yoon & Ji (2026), arXiv:2511.11306 |
| **Latent Agents (debate distillation)** | Internalizes debate-style reasoning into a single fine-tuned model | Yi, Mueller & Lee (2026), arXiv:2604.24881 |

## Notes

This list is a curated pointer index for further exploration; it is not exhaustive and does not constitute an endorsement of any specific tool. Consult each project's own repository or paper for installation instructions, licensing, and current maintenance status.
