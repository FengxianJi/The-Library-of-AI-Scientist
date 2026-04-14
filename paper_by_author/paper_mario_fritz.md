# Papers by Mario Fritz

Total: 2 papers

- [Inspectable AI for Science: A Research Object Approach to Generative AI Governance](http://arxiv.org/abs/2604.11261v1)
    - Ruta Binkyte, Sharif Abuaddba, Chamikara Mahawaga, Ming Ding, Natasha Fernandes, Mario Fritz
    - 📅 Date: April 13, 2026
    - 📑 Publisher: arXiv
    - 💻 Topic: [Literature Review]
    - 🔑 Key: [llm], [framework], [survey]
    - 📖 TLDR: This paper introduces AI as a Research Object (AI-RO), a paradigm for governing the use of generative AI in scientific research. Instead of debating whether AI is an author or merely a tool, we propose treating AI interactions as structured, inspectable components of the research process. Under this view, the legitimacy of an AI-assisted scientific paper depends on how model use is integrated into the workflow, documented, and made accountable. Drawing on Research Object theory and FAIR principles, we propose a framework for recording model configuration, prompts, and outputs through interaction logs and metadata packaging. These properties are particularly consequential in security and privacy (S&P) research, where provenance artifacts must satisfy confidentiality constraints, integrity guarantees, and auditability requirements that generic disclosure practices do not address. We implement a lightweight writing pipeline in which a language model synthesizes human-authored structured literature review notes under explicit constraints and produces a verifiable provenance record. We present this work as a position supported by an initial demonstrative workflow, arguing that governance of generative AI in science can be implemented as structured documentation, controlled disclosure, and integrity-preserving provenance capture. Based on this example, we outline and motivate a set of necessary future developments required to make such practices practical and widely adoptable.
- [Context-Aware Reasoning On Parametric Knowledge for Inferring Causal Variables](http://arxiv.org/abs/2409.02604v2)
    - Ivaxi Sheth, Sahar Abdelnabi, Mario Fritz
    - 📅 Date: September 04, 2024
    - 📑 Publisher: arXiv
    - 💻 Topic: [Hypothesis Generation]
    - 🔑 Key: [llm], [benchmark], [discovery], [experiment], [hypothesis], [reasoning]
    - 📖 TLDR: Scientific discovery catalyzes human intellectual advances, driven by the cycle of hypothesis generation, experimental design, evaluation, and assumption refinement. Central to this process is causal inference, uncovering the mechanisms behind observed phenomena. While randomized experiments provide strong inferences, they are often infeasible due to ethical or practical constraints. However, observational studies are prone to confounding or mediating biases. While crucial, identifying such backdoor paths is expensive and heavily depends on scientists' domain knowledge to generate hypotheses. We introduce a novel benchmark where the objective is to complete a partial causal graph. We design a benchmark with varying difficulty levels with over 4000 queries. We show the strong ability of LLMs to hypothesize the backdoor variables between a cause and its effect. Unlike simple knowledge memorization of fixed associations, our task requires the LLM to reason according to the context of the entire graph.
