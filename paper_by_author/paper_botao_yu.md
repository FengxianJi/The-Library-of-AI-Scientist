# Papers by Botao Yu

Total: 2 papers

- [Evaluating Large Language Models in Scientific Discovery](https://arxiv.org/abs/2512.15567)
    - Zhangde Song, Jieyu Lu, Yuanqi Du, Botao Yu, Thomas M. Pruyn, Yue Huang, Kehan Guo, Xiuzhe Luo, et al.
    - 🏛️ Institutions: The Ohio State University, Massachusetts Institute of Technology
    - 📅 Date: December 17, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Hypothesis Generation]
    - 🔑 Key: [llm], [framework], [benchmark], [reasoning], [discovery]
    - 📖 TLDR: Large language models (LLMs) are increasingly applied to scientific research, yet prevailing science benchmarks probe decontextualized knowledge and overlook the iterative reasoning, hypothesis generation, and observation interpretation that drive scientific discovery. We introduce a scenario-grounded benchmark that evaluates LLMs across biology, chemistry, materials, and physics, where domain experts define research projects of genuine interest and decompose them into modular research scenarios from which vetted questions are sampled. The framework assesses models at two levels: (i) question-level accuracy on scenario-tied items and (ii) project-level performance, where models must propose testable hypotheses, design simulations or experiments, and interpret results. Applying this two-phase scientific discovery evaluation (SDE) framework to state-of-the-art LLMs reveals a consistent performance gap relative to general science benchmarks, diminishing return of scaling up model sizes and reasoning, and systematic weaknesses shared across top-tier models from different providers. Large performance variation in research scenarios leads to changing choices of the best performing model on scientific discovery projects evaluated, suggesting all current LLMs are distant to general scientific "superintelligence". Nevertheless, LLMs already demonstrate promise in a great variety of scientific discovery projects, including cases where constituent scenario scores are low, highlighting the role of guided exploration and serendipity in discovery. This SDE framework offers a reproducible benchmark for discovery-relevant evaluation of LLMs and charts practical paths to advance their development toward scientific discovery.
    - 📄 File: 2512.15567v1.pdf
- [AutoSDT: Scaling Data-Driven Discovery Tasks Toward Open Co-Scientists](https://arxiv.org/abs/2506.08140)
    - Yifei Li, Hanane Nour Moussa, Ziru Chen, Shijie Chen, Botao Yu, Mingyi Xue, Benjamin Burns, Tzu-Yao Chiu, et al.
    - 🏛️ Institutions: The Ohio State University
    - 📅 Date: June 09, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Scientific Discovery]
    - 🔑 Key: [llm], [agent], [automation], [benchmark], [dataset]
    - 📖 TLDR: Despite long-standing efforts in accelerating scientific discovery with AI, building AI co-scientists remains challenging due to limited high-quality data for training and evaluation. To tackle this data scarcity issue, we present AutoSDT, an automatic pipeline that collects high-quality coding tasks in real-world data-driven discovery workflows. AutoSDT leverages the coding capabilities and parametric knowledge of LLMs to search for diverse sources, select ecologically valid tasks, and synthesize accurate task instructions and code solutions. Using our pipeline, we construct AutoSDT-5K, a dataset of 5,404 coding tasks for data-driven discovery that covers four scientific disciplines and 756 unique Python packages. To the best of our knowledge, AutoSDT-5K is the only automatically collected and the largest open dataset for data-driven scientific discovery. Expert feedback on a subset of 256 tasks shows the effectiveness of AutoSDT: 93% of the collected tasks are ecologically valid, and 92.2% of the synthesized programs are functionally correct. Trained on AutoSDT-5K, the Qwen2.5-Coder-Instruct LLM series, dubbed AutoSDT-Coder, show substantial improvement on two challenging data-driven discovery benchmarks, ScienceAgentBench and DiscoveryBench. Most notably, AutoSDT-Coder-32B reaches the same level of performance as GPT-4o on ScienceAgentBench with a success rate of 7.8%, doubling the performance of its base model. On DiscoveryBench, it lifts the hypothesis matching score to 8.1, bringing a 17.4% relative improvement and closing the gap between open-weight models and GPT-4o.
    - 📄 File: 2506.08140v1.pdf
