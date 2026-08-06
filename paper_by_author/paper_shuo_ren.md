# Papers by Shuo Ren

Total: 2 papers

- [EviGraph: Evidence-Guided Autonomous Research Agents](http://arxiv.org/abs/2608.04738v1)
    - Zhenjiang Ren, Ruiji Li, Xujing Zhang, Ziliang Pang, Shuo Ren, Jiajun Zhang
    - 📅 Date: August 05, 2026
    - 📑 Publisher: arXiv
    - 💻 Topic: [Misc]
    - 🔑 Key: [agent], [automation], [framework], [experiment], [hypothesis]
    - 📖 TLDR: Autonomous research agents can generate hypotheses, execute experiments, and draft manuscripts, yet their outputs often contain unsupported claims and inconsistencies between research questions, experiments, results, and conclusions. We argue that this problem is partly architectural: existing systems organize research as sequential pipelines but do not explicitly maintain or validate the evolving claim-evidence structure across stages.In this paper, we introduce EviGraph, an autonomous research framework that represents the research process as a typed evidence graph containing Problem, Gap, Hypothesis, Experiment, Finding, and Claim nodes. The graph serves as the operational state of the agent rather than a post-hoc record. EviGraph inspects evidence chains for missing dependencies, semantic misalignment, and result-claim inconsistencies, localizes the earliest weak node, and regenerates its affected downstream subgraph. Graph checkpointing prevents unsuccessful repairs from corrupting previously validated evidence. Manuscripts are generated only after every retained claim is grounded in a validated evidence chain.Experiments on ARC-Bench-ML and NanoResearch-20 show that EviGraph outperforms the compared end-to-end research-agent baselines in overall research performance, improves Claim Support Rate by 40.19% over the strongest baseline, and achieves 87.73% Experimental Data Consistency. These results demonstrate the value of explicit evidence-state maintenance for reliable autonomous research.
- [Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents](https://arxiv.org/abs/2503.24047)
    - Shuo Ren, Can Xie, Pu Jian, Zhenjiang Ren, Chunlin Leng, Jiajun Zhang
    - 🏛️ Institutions: State Key Laboratory of Multimodal Artificial Intelligence Systems, Foundation Model Research Center
    - 📅 Date: March 31, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Hypothesis Generation]
    - 🔑 Key: [llm], [agent], [automation], [benchmark], [survey]
    - 📖 TLDR: As scientific research becomes increasingly complex, innovative tools are needed to manage vast data, facilitate interdisciplinary collaboration, and accelerate discovery. Large language models (LLMs) are now evolving into LLM-based scientific agents that automate critical tasks ranging from hypothesis generation and experiment design to data analysis and simulation. Unlike general-purpose LLMs, these specialized agents integrate domain-specific knowledge, advanced tool sets, and robust validation mechanisms, enabling them to handle complex data types, ensure reproducibility, and drive scientific breakthroughs. This survey provides a focused review of the architectures, design, benchmarks, applications, and ethical considerations surrounding LLM-based scientific agents. We highlight why they differ from general agents and the ways in which they advance research across various scientific fields. By examining their development and challenges, this survey offers a comprehensive roadmap for researchers and practitioners to harness these agents for more efficient, reliable, and ethically sound scientific discovery.
    - 📄 File: 2503.24047v2.pdf
