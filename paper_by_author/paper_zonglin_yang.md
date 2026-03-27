# Papers by Zonglin Yang

Total: 4 papers

- [Harnessing Large Language Models for Scientific Novelty Detection](https://arxiv.org/abs/2505.24615)
    - Yan Liu, Zonglin Yang, Soujanya Poria, Thanh-Son Nguyen, Erik Cambria
    - 🏛️ Institutions: Nanyang Technological University
    - 📅 Date: May 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Misc]
    - 🔑 Key: [llm], [benchmark], [dataset], [experiment]
    - 📖 TLDR: In an era of exponential scientific growth, identifying novel research ideas is crucial and challenging in academia. Despite potential, the lack of an appropriate benchmark dataset hinders the research of novelty detection. More importantly, simply adopting existing NLP technologies, e.g., retrieving and then cross-checking, is not a one-size-fits-all solution due to the gap between textual similarity and idea conception. In this paper, we propose to harness large language models (LLMs) for scientific novelty detection (ND), associated with two new datasets in marketing and NLP domains. To construct the considerate datasets for ND, we propose to extract closure sets of papers based on their relationship, and then summarize their main ideas based on LLMs. To capture idea conception, we propose to train a lightweight retriever by distilling the idea-level knowledge from LLMs to align ideas with similar conception, enabling efficient and accurate idea retrieval for LLM novelty detection. Experiments show our method consistently outperforms others on the proposed benchmark datasets for idea retrieval and ND tasks. Codes and data are available at https://anonymous.4open.science/r/NoveltyDetection-10FB/.
    - 📄 File: 2505.24615v1.pdf
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
- [LLM4SR: A Survey on Large Language Models for Scientific Research](https://arxiv.org/abs/2501.04306)
    - Ziming Luo, Zonglin Yang, Zexin Xu, Wei Yang, Xinya Du
    - 🏛️ Institutions: Nanyang Technological University, Cornell University
    - 📅 Date: January 08, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Literature Review]
    - 🔑 Key: [llm], [framework], [benchmark], [survey], [discovery]
    - 📖 TLDR: In recent years, the rapid advancement of Large Language Models (LLMs) has transformed the landscape of scientific research, offering unprecedented support across various stages of the research cycle. This paper presents the first systematic survey dedicated to exploring how LLMs are revolutionizing the scientific research process. We analyze the unique roles LLMs play across four critical stages of research: hypothesis discovery, experiment planning and implementation, scientific writing, and peer reviewing. Our review comprehensively showcases the task-specific methodologies and evaluation benchmarks. By identifying current challenges and proposing future research directions, this survey not only highlights the transformative potential of LLMs, but also aims to inspire and guide researchers and practitioners in leveraging LLMs to advance scientific inquiry. Resources are available at the following repository: https://github.com/du-nlp-lab/LLM4SR
    - 📄 File: 2501.04306v1.pdf
