# Papers by Jiaxin Bai

Total: 2 papers

- [Controllable Logical Hypothesis Generation for Abductive Reasoning in Knowledge Graphs](http://arxiv.org/abs/2505.20948v2)
    - Yisen Gao, Jiaxin Bai, Tianshi Zheng, Qingyun Sun, Ziwei Zhang, Xingcheng Fu, et al.
    - 📅 Date: May 27, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Hypothesis Generation]
    - 🔑 Key: [framework], [benchmark], [dataset], [discovery], [experiment], [hypothesis], [reasoning]
    - 📖 TLDR: Abductive reasoning in knowledge graphs aims to generate plausible logical hypotheses from observed entities, with broad applications in areas such as clinical diagnosis and scientific discovery. However, due to a lack of controllability, a single observation may yield numerous plausible but redundant or irrelevant hypotheses on large-scale knowledge graphs. To address this limitation, we introduce the task of controllable hypothesis generation to improve the practical utility of abductive reasoning. This task faces two key challenges when controlling for generating long and complex logical hypotheses: hypothesis space collapse and hypothesis oversensitivity. To address these challenges, we propose CtrlHGen, a Controllable logcial Hypothesis Generation framework for abductive reasoning over knowledge graphs, trained in a two-stage paradigm including supervised learning and subsequent reinforcement learning. To mitigate hypothesis space collapse, we design a dataset augmentation strategy based on sub-logical decomposition, enabling the model to learn complex logical structures by leveraging semantic patterns in simpler components. To address hypothesis oversensitivity, we incorporate smoothed semantic rewards including Dice and Overlap scores, and introduce a condition-adherence reward to guide the generation toward user-specified control constraints. Extensive experiments on three benchmark datasets demonstrate that our model not only better adheres to control conditions but also achieves superior semantic similarity performance compared to baselines. Our code is available at https://github.com/HKUST-KnowComp/CtrlHGen.
- [From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery](https://arxiv.org/abs/2505.13259)
    - Tianshi Zheng, Zheye Deng, Hong Ting Tsang, Weiqi Wang, Jiaxin Bai, Zihao Wang, Yangqiu Song
    - 🏛️ Institutions: The Hong Kong University of Science, F F C Agent Laboratory
    - 📅 Date: May 19, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Scientific Discovery]
    - 🔑 Key: [llm], [agent], [automation], [framework], [survey]
    - 📖 TLDR: Large Language Models (LLMs) are catalyzing a paradigm shift in scientific discovery, evolving from task-specific automation tools into increasingly autonomous agents and fundamentally redefining research processes and human-AI collaboration. This survey systematically charts this burgeoning field, placing a central focus on the changing roles and escalating capabilities of LLMs in science. Through the lens of the scientific method, we introduce a foundational three-level taxonomy-Tool, Analyst, and Scientist-to delineate their escalating autonomy and evolving responsibilities within the research lifecycle. We further identify pivotal challenges and future research trajectories such as robotic automation, self-improvement, and ethical governance. Overall, this survey provides a conceptual architecture and strategic foresight to navigate and shape the future of AI-driven scientific discovery, fostering both rapid innovation and responsible advancement. Github Repository: https://github.com/HKUST-KnowComp/Awesome-LLM-Scientific-Discovery.
    - 📄 File: 2505.13259v3.pdf
