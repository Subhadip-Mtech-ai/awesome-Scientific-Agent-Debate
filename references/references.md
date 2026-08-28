# Curated Research Papers

This list is intended to contain **verified scholarly resources** relevant to the topic. Do not upload copyrighted paper PDFs unless redistribution is clearly permitted. Prefer arXiv, DOI, publisher, or official project pages.

## Foundational Papers

### 1. AI Safety via Debate
**Authors:** Geoffrey Irving, Paul Christiano, Dario Amodei (2018)

[Paper / arXiv](https://arxiv.org/abs/1805.00899)

Introduces debate between AI systems as a mechanism for scalable oversight and provides an important conceptual foundation for later debate-based LLM systems.

### 2. Improving Factuality and Reasoning in Language Models through Multiagent Debate
**Authors:** Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, Igor Mordatch (2023)

[Paper / arXiv](https://arxiv.org/abs/2305.14325)

Presents multi-agent debate in which multiple LLM instances propose and debate answers over multiple rounds to improve reasoning and factuality.

### 3. Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate
**Authors:** Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Shuming Shi, Zhaopeng Tu (2023)

[Paper / arXiv](https://arxiv.org/abs/2305.19118)

Uses multi-agent debate to address the Degeneration-of-Thought problem and encourage more diverse reasoning.

### 4. ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate
**Authors:** Chi-Min Chan, Weize Chen, Yusheng Su, Jianxuan Yu, Wei Xue, Shanghang Zhang, Jie Fu, Zhiyuan Liu (2023)

[Paper / arXiv](https://arxiv.org/abs/2308.07201)

Applies multi-agent debate to LLM-based evaluation, using role-based agents to compare and judge generated text.

## Single-LLM Reasoning and Ideation

### 5. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
**Authors:** Jason Wei et al. (2022)

[Paper / arXiv](https://arxiv.org/abs/2201.11903)

Foundational prompting method that improves complex reasoning by eliciting intermediate reasoning steps.

### 6. Self-Consistency Improves Chain of Thought Reasoning in Language Models
**Authors:** Xuezhi Wang et al. (2022)

[Paper / arXiv](https://arxiv.org/abs/2203.11171)

Samples multiple reasoning paths and selects a consistent answer, providing a strong single-model baseline for comparison with debate.

### 7. Diversity of Thought Improves Reasoning Abilities of LLMs
**Authors:** Ranjita Naik, Varun Chandrasekaran, Mert Yuksekgonul, Hamid Palangi, Besmira Nushi (2023)

[Paper / arXiv](https://arxiv.org/abs/2310.07088)

Explores prompt diversity and self-ensembling as a way to improve reasoning accuracy and the accuracy-cost trade-off.

### 8. Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers
**Authors:** Chenglei Si, Diyi Yang, Tatsunori Hashimoto (2024)

[Paper / arXiv](https://arxiv.org/abs/2409.04109)

Large-scale study comparing LLM-generated research ideas with expert-generated ideas, with important findings about novelty, feasibility, self-evaluation, and diversity.

### 9. ReAct: Synergizing Reasoning and Acting in Language Models
**Authors:** Shunyu Yao et al. (2023)

[Paper / arXiv](https://arxiv.org/abs/2210.03629)

Combines reasoning traces with actions and external observations, providing background for tool-using research agents.

### 10. Self-Refine: Iterative Refinement with Self-Feedback
**Authors:** Aman Madaan et al. (2023)

[Paper / arXiv](https://arxiv.org/abs/2303.17651)

Shows how a single model can iteratively improve its own output using generated feedback, providing another important baseline to multi-agent critique.

## Multi-Agent Debate, Diversity and Efficiency

### 11. Improving Multi-Agent Debate with Sparse Communication Topology
**Authors:** Yunxuan Li, Yibing Du, Jiageng Zhang, Le Hou, Peter Grabowski, Yeqing Li, Eugene Ie (2024)

[Paper / arXiv](https://arxiv.org/abs/2406.11776)

Studies communication topology and shows that sparse communication can reduce cost while retaining strong debate performance.

### 12. Diversity of Thought Elicits Stronger Reasoning Capabilities in Multi-Agent Debate Frameworks
**Author:** Mahmood Hegazy (2024)

[Paper / arXiv](https://arxiv.org/abs/2410.12853)

Studies heterogeneous model diversity in debate and reports stronger reasoning performance than homogeneous agent groups in several benchmarks.

### 13. Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?
**Authors:** Hyunsoo Kim Choi, Xin Zhu, Shun Li (2025)

[Paper / arXiv](https://arxiv.org/abs/2508.17536)

Separates the effects of majority voting and argument exchange, making it especially relevant to fair single-agent versus debate comparisons.

### 14. iMAD: Intelligent Multi-Agent Debate for Efficient and Accurate LLM Inference
**Authors:** Wei Fan, JinYi Yoon, Bo Ji (2026)

[Paper / arXiv](https://arxiv.org/abs/2511.11306)

Selectively triggers debate only when it is likely to help, targeting the compute cost and possible accuracy degradation of unconditional debate.

### 15. Multi-Agent Debate with Memory Masking
**Authors:** Hongduan Tian, Xiao Feng, Ziyuan Zhao, Xiangyu Zhu, Rolan Yan, Bo Han (2026)

[Paper / arXiv](https://arxiv.org/abs/2603.20215)

Investigates erroneous memories in debate and proposes masking mechanisms to remove misleading context between rounds.

### 16. Hear Both Sides: Efficient Multi-Agent Debate via Diversity-Aware Message Retention
**Authors:** Manh Nguyen, Anh Nguyen, Dung Nguyen, Svetha Venkatesh, Hung Le (2026)

[Paper / arXiv](https://arxiv.org/abs/2603.20640)

Selects diverse and disagreeing messages for propagation between rounds to reduce redundancy and preserve useful disagreement.

### 17. Latent Agents: A Post-Training Procedure for Internalized Multi-Agent Debate
**Authors:** John Seon Keun Yi, Aaron Mueller, Dokyun Lee (2026)

[Paper / arXiv](https://arxiv.org/abs/2604.24881)

Studies distilling debate into a single model, showing why debate-like behavior may sometimes be internalized instead of requiring explicit multi-agent transcripts.

## Scientific Discovery and Hypothesis Generation

### 18. SciAgents: Automating Scientific Discovery through Multi-Agent Intelligent Graph Reasoning
**Authors:** Alireza Ghafarollahi, Markus J. Buehler (2024)

[Paper / arXiv](https://arxiv.org/abs/2409.05556)

Combines ontological knowledge graphs, retrieval tools, LLMs, and multi-agent systems to generate and refine scientific hypotheses.

### 19. Towards an AI co-scientist
**Authors:** Juraj Gottweis et al. (2025)

[Paper / arXiv](https://arxiv.org/abs/2502.18864)

Introduces a multi-agent scientific discovery system using generation, debate, ranking, evolution, and other specialized processes.

### 20. A Multi-Agent System for Automating Scientific Discovery
**Authors:** Ali E. Ghareeb et al. (2026)

[Paper / Nature](https://www.nature.com/articles/s41586-026-10652-y)

Presents Robin, a multi-agent system that combines literature-search and data-analysis agents to automate hypothesis generation and experimental-data analysis.

## Evaluation and Benchmarking

### 21. HeurekaBench: A Benchmarking Framework for AI Co-scientist
**Authors:** Siba Smarak Panigrahi, Jovana Videnović, Maria Brbić (2026)

[Paper / arXiv](https://arxiv.org/abs/2601.01678)

Introduces an open-ended benchmark framework grounded in real scientific studies and code repositories for evaluating scientific agents.

---

## Curation Note

The earlier AI-generated paper contained 24 references. The separate citation audit found that two sampled references had metadata problems, including a misattributed author name and an incomplete citation. Those problematic citations should not be copied blindly into this repository.

The list above intentionally uses a curated set of references with stable scholarly links. Before final submission, re-open each linked source and check the title, authors, year, venue, and identifier one final time.
