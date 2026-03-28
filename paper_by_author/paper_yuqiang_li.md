# Papers by Yuqiang Li

Total: 2 papers

- [Unleashing LLMs in Bayesian Optimization: Preference-Guided Framework for Scientific Discovery](https://papers.cool/venue/LktUOZayG9@OpenReview)
    - Xinzhe Yuan, Zhuo Chen, Jianshu Zhang, Huan Xiong, Nanyang Ye, Yuqiang Li, et al.
    - 📅 Date: March 28, 2026
    - 📑 Publisher: arXiv
    - 💻 Topic: [Scientific Discovery]
    - 🔑 Key: [llm], [framework], [benchmark], [discovery], [experiment], [reasoning]
    - 📖 TLDR: Scientific discovery is increasingly constrained by costly experiments and limited budgets, making efficient optimization essential for AI for science. Bayesian Optimization (BO), while widely adopted for balancing exploration and exploitation, suffers from slow cold-start performance and poor scalability in high-dimensional settings, limiting its effectiveness in real-world scientific applications. To address these challenges, we propose LLM-Guided Bayesian Optimization (LGBO), the first LLM preference-guided BO framework that continuously integrates the semantic reasoning of large language models (LLMs) into the optimization loop. Unlike prior works that use LLMs only for warm-start initialization or candidate generation, LGBO introduces a region-lifted preference mechanism that embeds LLM-driven preferences into every iteration, shifting the surrogate mean in a stable and controllable way. Theoretically, we prove that LGBO is not perform significantly worse than standard BO in the worst case, while achieving significantly faster convergence when preferences align with the objective. Empirically, LGBO achieves consistent improvements across diverse dry benchmarks in physics, chemistry, biology, and materials science. Most notably, in a new wet-lab optimization of Fe–Cr battery electrolytes, LGBO reaches \textbf{90\% of the best observed value within 6 iterations}, whereas standard BO and existing LLM-augmented baselines require more than 10 iterations. Together, the results suggest that LGBO offers a promising direction for integrating LLMs into scientific optimization workflows.
- [ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition](https://arxiv.org/abs/2503.21248)
    - Yujie Liu, Zonglin Yang, Tong Xie, Jinjie Ni, Ben Gao, Yuqiang Li, Shixiang Tang, Wanli Ouyang, et al.
    - 🏛️ Institutions: Nanyang Technological University
    - 📅 Date: March 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Scientific Discovery]
    - 🔑 Key: [llm], [automation], [framework], [benchmark], [survey]
    - 📖 TLDR: Large language models (LLMs) have demonstrated potential in assisting scientific research, yet their ability to discover high-quality research hypotheses remains unexamined due to the lack of a dedicated benchmark. To address this gap, we introduce the first large-scale benchmark for evaluating LLMs with a near-sufficient set of sub-tasks of scientific discovery: inspiration retrieval, hypothesis composition, and hypothesis ranking. We develop an automated framework that extracts critical components - research questions, background surveys, inspirations, and hypotheses - from scientific papers across 12 disciplines, with expert validation confirming its accuracy. To prevent data contamination, we focus exclusively on papers published in 2024, ensuring minimal overlap with LLM pretraining data. Our evaluation reveals that LLMs perform well in retrieving inspirations, an out-of-distribution task, suggesting their ability to surface novel knowledge associations. This positions LLMs as "research hypothesis mines", capable of facilitating automated scientific discovery by generating innovative hypotheses at scale with minimal human intervention.
    - 📄 File: 2503.21248v2.pdf
