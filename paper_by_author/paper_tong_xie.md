# Papers by Tong Xie

Total: 2 papers

- [MOOSE-Chem2: Exploring LLM Limits in Fine-Grained Scientific Hypothesis Discovery via Hierarchical Search](https://arxiv.org/abs/2505.19209)
    - Zonglin Yang, Wanhao Liu, Ben Gao, Yujie Liu, Wei Li, Tong Xie, Lidong Bing, Wanli Ouyang, et al.
    - 🏛️ Institutions: University of Science
    - 📅 Date: May 25, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Hypothesis Generation]
    - 🔑 Key: [llm], [automation], [benchmark], [discovery], [hypothesis]
    - 📖 TLDR: Large language models (LLMs) have shown promise in automating scientific hypothesis generation, yet existing approaches primarily yield coarse-grained hypotheses lacking critical methodological and experimental details. We introduce and formally define the new task of fine-grained scientific hypothesis discovery, which entails generating detailed, experimentally actionable hypotheses from coarse initial research directions. We frame this as a combinatorial optimization problem and investigate the upper limits of LLMs' capacity to solve it when maximally leveraged. Specifically, we explore four foundational questions: (1) how to best harness an LLM's internal heuristics to formulate the fine-grained hypothesis it itself would judge as the most promising among all the possible hypotheses it might generate, based on its own internal scoring-thus defining a latent reward landscape over the hypothesis space; (2) whether such LLM-judged better hypotheses exhibit stronger alignment with ground-truth hypotheses; (3) whether shaping the reward landscape using an ensemble of diverse LLMs of similar capacity yields better outcomes than defining it with repeated instances of the strongest LLM among them; and (4) whether an ensemble of identical LLMs provides a more reliable reward landscape than a single LLM. To address these questions, we propose a hierarchical search method that incrementally proposes and integrates details into the hypothesis, progressing from general concepts to specific experimental configurations. We show that this hierarchical process smooths the reward landscape and enables more effective optimization. Empirical evaluations on a new benchmark of expert-annotated fine-grained hypotheses from recent literature show that our method consistently outperforms strong baselines.
    - 📄 File: 2505.19209v2.pdf
- [ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition](https://arxiv.org/abs/2503.21248)
    - Yujie Liu, Zonglin Yang, Tong Xie, Jinjie Ni, Ben Gao, Yuqiang Li, Shixiang Tang, Wanli Ouyang, et al.
    - 🏛️ Institutions: Nanyang Technological University
    - 📅 Date: March 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Scientific Discovery]
    - 🔑 Key: [llm], [automation], [framework], [benchmark], [survey]
    - 📖 TLDR: Large language models (LLMs) have demonstrated potential in assisting scientific research, yet their ability to discover high-quality research hypotheses remains unexamined due to the lack of a dedicated benchmark. To address this gap, we introduce the first large-scale benchmark for evaluating LLMs with a near-sufficient set of sub-tasks of scientific discovery: inspiration retrieval, hypothesis composition, and hypothesis ranking. We develop an automated framework that extracts critical components - research questions, background surveys, inspirations, and hypotheses - from scientific papers across 12 disciplines, with expert validation confirming its accuracy. To prevent data contamination, we focus exclusively on papers published in 2024, ensuring minimal overlap with LLM pretraining data. Our evaluation reveals that LLMs perform well in retrieving inspirations, an out-of-distribution task, suggesting their ability to surface novel knowledge associations. This positions LLMs as "research hypothesis mines", capable of facilitating automated scientific discovery by generating innovative hypotheses at scale with minimal human intervention.
    - 📄 File: 2503.21248v2.pdf
