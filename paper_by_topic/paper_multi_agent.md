# Multi-Agent Papers

Total: 3 papers

- [InternAgent: When Agent Becomes the Scientist -- Building Closed-Loop System from Hypothesis to Verification](https://arxiv.org/abs/2505.16938)
    - InternAgent Team, Bo Zhang, Shiyang Feng, Xiangchao Yan, Jiakang Yuan, Runmin Ma, Yusong Hu, Zhiyin Yu, et al.
    - 🏛️ Institutions: Shanghai Artificial Intelligence Laboratory
    - 📅 Date: May 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Multi-Agent]
    - 🔑 Key: [agent], [automation], [framework], [hypothesis], [multi-agent]
    - 📖 TLDR: Artificial Intelligence (AI) is accelerating the transformation of scientific research paradigms, not only enhancing research efficiency but also driving innovation. We introduce InternAgent, a unified closed-loop multi-agent framework to conduct Autonomous Scientific Research (ASR) across various scientific research fields, enabling researchers to tackle complicated problems in these fields with unprecedented speed and precision. InternAgent highlights three key advantages: 1) Scalability: InternAgent has demonstrated its versatility across 12 scientific research tasks, capable of generating innovative ideas to enhance the performance of baseline code. 2) Interactivity: InternAgent provides an interface for human expert feedback and multi-agent interaction in automated end-to-end processes, allowing for the seamless integration of domain expert knowledge. 3) Efficiency: InternAgent has achieved promising performance gains in several scientific fields with significantly less time cost compared to human efforts. For instance, in reaction yield prediction, it increased from 27.6% to 35.4% in just 12 hours; in enhancer activity prediction, accuracy rose from 0.65 to 0.79 with only 4 hours of processing; and in 2D semantic segmentation, precision advanced from 78.8% to 81.0% in a mere 30 hours.

- [Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning](https://arxiv.org/abs/2504.17192)
    - Minju Seo, Jinheon Baek, Seongyun Lee, Sung Ju Hwang
    - 🏛️ Institutions: Korea Advanced Institute of Science and Technology (KAIST)
    - 📅 Date: April 24, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Multi-Agent]
    - 🔑 Key: [llm], [agent], [automation], [framework], [benchmark]
    - 📖 TLDR: Despite the rapid growth of machine learning research, corresponding code implementations are often unavailable, making it slow and labor-intensive for researchers to reproduce results and build upon prior work. In the meantime, recent Large Language Models (LLMs) excel at understanding scientific documents and generating high-quality code. Inspired by this, we introduce PaperCoder, a multi-agent LLM framework that transforms machine learning papers into operational code repositories. PaperCoder operates in three stages: planning, where it constructs a high-level roadmap, designs the system architecture with diagrams, identifies file dependencies, and generates configuration files; analysis, which focuses on interpreting implementation-specific details; and generation, where modular, dependency-aware code is produced. Moreover, each phase is instantiated through a set of specialized agents designed to collaborate effectively across the pipeline. We then evaluate PaperCoder on generating code implementations from machine learning papers based on both model-based and human evaluations, particularly from the authors of those papers, with author-released repositories as ground truth if available. Our results demonstrate the effectiveness of PaperCoder in creating high-quality, faithful implementations. Furthermore, it consistently shows strengths in the recently released PaperBench benchmark, surpassing strong baselines by substantial margins. Code is available at: https://github.com/going-doer/Paper2Code.

- [KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment](https://arxiv.org/abs/2502.06472)
    - Yuxing Lu, Wei Wu, Xukai Zhao, Rui Peng, Jinzhuo Wang
    - 🏛️ Institutions: Peking University
    - 📅 Date: February 10, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Multi-Agent]
    - 🔑 Key: [llm], [agent], [automation], [framework], [discovery]
    - 📖 TLDR: Maintaining comprehensive and up-to-date knowledge graphs (KGs) is critical for modern AI systems, but manual curation struggles to scale with the rapid growth of scientific literature. This paper presents KARMA, a novel framework employing multi-agent large language models (LLMs) to automate KG enrichment through structured analysis of unstructured text. Our approach employs nine collaborative agents, spanning entity discovery, relation extraction, schema alignment, and conflict resolution that iteratively parse documents, verify extracted knowledge, and integrate it into existing graph structures while adhering to domain-specific schema. Experiments on 1,200 PubMed articles from three different domains demonstrate the effectiveness of KARMA in knowledge graph enrichment, with the identification of up to 38,230 new entities while achieving 83.1\% LLM-verified correctness and reducing conflict edges by 18.6\% through multi-layer assessments.

