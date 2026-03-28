# Papers by Aniketh Garikaparthi

Total: 2 papers

- [MIR: Methodology Inspiration Retrieval for Scientific Research Problems](http://arxiv.org/abs/2506.00249v1)
    - Aniketh Garikaparthi, Manasi Patwardhan, Aditya Sanjiv Kanade, Aman Hassan, Lovekesh Vig, Arman Cohan
    - 📅 Date: May 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Scientific Discovery]
    - 🔑 Key: [llm], [automation], [benchmark], [dataset], [discovery], [reasoning]
    - 📖 TLDR: There has been a surge of interest in harnessing the reasoning capabilities of Large Language Models (LLMs) to accelerate scientific discovery. While existing approaches rely on grounding the discovery process within the relevant literature, effectiveness varies significantly with the quality and nature of the retrieved literature. We address the challenge of retrieving prior work whose concepts can inspire solutions for a given research problem, a task we define as Methodology Inspiration Retrieval (MIR). We construct a novel dataset tailored for training and evaluating retrievers on MIR, and establish baselines. To address MIR, we build the Methodology Adjacency Graph (MAG); capturing methodological lineage through citation relationships. We leverage MAG to embed an "intuitive prior" into dense retrievers for identifying patterns of methodological inspiration beyond superficial semantic similarity. This achieves significant gains of +5.4 in Recall@3 and +7.8 in Mean Average Precision (mAP) over strong baselines. Further, we adapt LLM-based re-ranking strategies to MIR, yielding additional improvements of +4.5 in Recall@3 and +4.8 in mAP. Through extensive ablation studies and qualitative analyses, we exhibit the promise of MIR in enhancing automated scientific discovery and outline avenues for advancing inspiration-driven retrieval.
- [IRIS: Interactive Research Ideation System for Accelerating Scientific Discovery](http://arxiv.org/abs/2504.16728v2)
    - Aniketh Garikaparthi, Manasi Patwardhan, Lovekesh Vig, Arman Cohan
    - 📅 Date: April 23, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Hypothesis Generation]
    - 🔑 Key: [llm], [agent], [automation], [framework], [discovery], [hypothesis], [multi-agent]
    - 📖 TLDR: The rapid advancement in capabilities of large language models (LLMs) raises a pivotal question: How can LLMs accelerate scientific discovery? This work tackles the crucial first stage of research, generating novel hypotheses. While recent work on automated hypothesis generation focuses on multi-agent frameworks and extending test-time compute, none of the approaches effectively incorporate transparency and steerability through a synergistic Human-in-the-loop (HITL) approach. To address this gap, we introduce IRIS: Interactive Research Ideation System, an open-source platform designed for researchers to leverage LLM-assisted scientific ideation. IRIS incorporates innovative features to enhance ideation, including adaptive test-time compute expansion via Monte Carlo Tree Search (MCTS), fine-grained feedback mechanism, and query-based literature synthesis. Designed to empower researchers with greater control and insight throughout the ideation process. We additionally conduct a user study with researchers across diverse disciplines, validating the effectiveness of our system in enhancing ideation. We open-source our code at https://github.com/Anikethh/IRIS-Interactive-Research-Ideation-System
