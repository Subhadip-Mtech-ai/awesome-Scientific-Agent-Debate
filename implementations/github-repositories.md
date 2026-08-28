# Open-Source Implementations

GitHub repositories implementing the systems and techniques discussed in the paper. Links point to the repositories most commonly cited by each paper's authors or community at the time of writing; **verify current availability and licensing directly before use**, as repository locations and maintenance status can change after this list was compiled.

## Multi-Agent Debate (General Reasoning)

| Project | Paper | Notes |
|---|---|---|
| **Multiagent-Debate** | Du, Li, Torralba, Tenenbaum & Mordatch (2023) — arXiv:2305.14325 | Original reference implementation of multi-agent debate for factuality and reasoning tasks |
| **ChatEval** | Chan et al. (2023) — arXiv:2308.07201 | Reference implementation of multi-agent-debate-based LLM evaluation |
| **Multi-Agent Debate (Divergent Thinking / DoT)** | Liang et al. (2024) — arXiv:2305.19118 | Tit-for-tat debate framework addressing the Degeneration-of-Thought problem |

## Efficiency-Oriented Multi-Agent Debate

| Project | Paper | Notes |
|---|---|---|
| **Sparse Communication Topology for MAD** | Li et al. (2024) — arXiv:2406.11776 | Reduced-connectivity debate graphs |
| **Talk Isn't Always Cheap (failure-mode analysis)** | Wynn, Satija & Hadfield (2025) — arXiv:2509.05396 | Code released at `github.com/TheNormativityLab/talk-aint-cheap` (per paper's stated code-availability section) |

## Scientific Discovery Systems

| Project | Paper | Notes |
|---|---|---|
| **SciAgents** | Ghafarollahi & Buehler (2025) — DOI:10.1002/adma.202413523 | Multi-agent + knowledge-graph hypothesis generation for materials science (MIT Buehler Lab) |
| **Robin** | Ghareeb et al. (2025) — DOI:10.1038/s41586-026-10652-y | End-to-end multi-agent scientific-discovery system (FutureHouse) |
| **AI co-scientist** | Gottweis et al. (2025) — arXiv:2502.18864 | Not fully open-sourced at time of writing; described in detail in the paper and companion Google Research blog materials |

## Related / Adjacent Multi-Agent Biomedical Systems

| Project | Paper | Notes |
|---|---|---|
| **Coated-LLM** | *iScience* (2025) | Researcher/Reviewer/Moderator multi-agent framework for Alzheimer's drug-combination hypothesis generation |
| **CARE-AD** | Li, Wang, Berlowitz et al., *npj Digital Medicine* (2025) | Multi-agent LLM framework for Alzheimer's disease risk prediction from longitudinal clinical notes (adjacent application, not hypothesis generation per se) |

## How to Contribute

If you know of an actively maintained, canonical implementation for any system listed here — or in the paper's reference list — please open a pull request adding it, with a link to the specific commit or release you verified.

## Disclaimer

Inclusion in this list is not an endorsement of code quality, security, or fitness for any particular purpose. Several of these systems (AI co-scientist, Robin) are primarily described in their papers without a fully public reference implementation; treat listed repository names as pointers to verify independently, not as guaranteed live links.
