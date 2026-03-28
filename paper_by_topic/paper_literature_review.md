# Literature Review Papers

Total: 3 papers

- [What's In Your Field? Mapping Scientific Research with Knowledge Graphs and Large Language Models](https://arxiv.org/abs/2503.09894)
    - Abhipsha Das, Nicholas Lourie, Siavash Golkar, Mariel Pettee
    - 🏛️ Institutions: New York University . cm Lawrence Berkeley National Laboratory, Scientific Computing Core at the Flatiron Institute
    - 📅 Date: March 12, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Literature Review]
    - 🔑 Key: [llm], [framework], [survey]
    - 📖 TLDR: The scientific literature's exponential growth makes it increasingly challenging to navigate and synthesize knowledge across disciplines. Large language models (LLMs) are powerful tools for understanding scientific text, but they fail to capture detailed relationships across large bodies of work. Unstructured approaches, like retrieval augmented generation, can sift through such corpora to recall relevant facts; however, when millions of facts influence the answer, unstructured approaches become cost prohibitive. Structured representations offer a natural complement -- enabling systematic analysis across the whole corpus. Recent work enhances LLMs with unstructured or semistructured representations of scientific concepts; to complement this, we try extracting structured representations using LLMs. By combining LLMs' semantic understanding with a schema of scientific concepts, we prototype a system that answers precise questions about the literature as a whole. Our schema applies across scientific fields and we extract concepts from it using only 20 manually annotated abstracts. To demonstrate the system, we extract concepts from 30,000 papers on arXiv spanning astrophysics, fluid dynamics, and evolutionary biology. The resulting database highlights emerging trends and, by visualizing the knowledge graph, offers new ways to explore the ever-growing landscape of scientific knowledge. Demo: abby101/surveyor-0 on HF Spaces. Code: https://github.com/chiral-carbon/kg-for-science.
    - 📄 File: 2503.09894v2.pdf
- [LLM4SR: A Survey on Large Language Models for Scientific Research](https://arxiv.org/abs/2501.04306)
    - Ziming Luo, Zonglin Yang, Zexin Xu, Wei Yang, Xinya Du
    - 🏛️ Institutions: Nanyang Technological University, Cornell University
    - 📅 Date: January 08, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Literature Review]
    - 🔑 Key: [llm], [framework], [benchmark], [survey], [discovery]
    - 📖 TLDR: In recent years, the rapid advancement of Large Language Models (LLMs) has transformed the landscape of scientific research, offering unprecedented support across various stages of the research cycle. This paper presents the first systematic survey dedicated to exploring how LLMs are revolutionizing the scientific research process. We analyze the unique roles LLMs play across four critical stages of research: hypothesis discovery, experiment planning and implementation, scientific writing, and peer reviewing. Our review comprehensively showcases the task-specific methodologies and evaluation benchmarks. By identifying current challenges and proposing future research directions, this survey not only highlights the transformative potential of LLMs, but also aims to inspire and guide researchers and practitioners in leveraging LLMs to advance scientific inquiry. Resources are available at the following repository: https://github.com/du-nlp-lab/LLM4SR
    - 📄 File: 2501.04306v1.pdf
- [Large Language Models for Automated Literature Review: An Evaluation of Reference Generation, Abstract Writing, and Review Composition](http://arxiv.org/abs/2412.13612v5)
    - Xuemei Tang, Xufeng Duan, Zhenguang G. Cai
    - 📅 Date: December 18, 2024
    - 📑 Publisher: arXiv
    - 💻 Topic: [Literature Review]
    - 🔑 Key: [llm], [automation], [framework], [benchmark], [experiment], [survey]
    - 📖 TLDR: Large language models (LLMs) have emerged as a potential solution to automate the complex processes involved in writing literature reviews, such as literature collection, organization, and summarization. However, it is yet unclear how good LLMs are at automating comprehensive and reliable literature reviews. This study introduces a framework to automatically evaluate the performance of LLMs in three key tasks of literature writing: reference generation, literature summary, and literature review composition. We introduce multidimensional evaluation metrics that assess the hallucination rates in generated references and measure the semantic coverage and factual consistency of the literature summaries and compositions against human-written counterparts. The experimental results reveal that even the most advanced models still generate hallucinated references, despite recent progress. Moreover, we observe that the performance of different models varies across disciplines when it comes to writing literature reviews. These findings highlight the need for further research and development to improve the reliability of LLMs in automating academic literature reviews.
