# Misc Papers

Total: 7 papers

- [Scientific Algorithm Discovery by Augmenting AlphaEvolve with Deep Research](https://arxiv.org/abs/2510.06056)
    - Gang Liu, Yihan Zhu, Jie Chen, Meng Jiang
    - 🏛️ Institutions: IBM Watson AI Lab, IBM Research
    - 📅 Date: October 07, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Misc]
    - 🔑 Key: [llm], [agent], [framework], [benchmark], [discovery]
    - 📖 TLDR: Large language models hold promise as scientific assistants, yet existing agents either rely solely on algorithm evolution or on deep research in isolation, both of which face critical limitations. Pure algorithm evolution, as in AlphaEvolve, depends only on the internal knowledge of LLMs and quickly plateaus in complex domains, while pure deep research proposes ideas without validation, resulting in unrealistic or unimplementable solutions. We present DeepEvolve, an agent that integrates deep research with algorithm evolution, uniting external knowledge retrieval, cross-file code editing, and systematic debugging under a feedback-driven iterative loop. Each iteration not only proposes new hypotheses but also refines, implements, and tests them, avoiding both shallow improvements and unproductive over-refinements. Across nine benchmarks in chemistry, mathematics, biology, materials, and patents, DeepEvolve consistently improves the initial algorithm, producing executable new algorithms with sustained gains. By bridging the gap between unguided evolution and research without grounding, DeepEvolve provides a reliable framework for advancing scientific algorithm discovery. Our code is available at https://github.com/liugangcode/deepevolve.

- [Context-Aware Scientific Knowledge Extraction on Linked Open Data using Large Language Models](https://arxiv.org/abs/2506.17580)
    - Sajratul Y. Rubaiat, Hasan M. Jamil
    - 🏛️ Institutions: Hasso Plattner Institute
    - 📅 Date: June 21, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Misc]
    - 🔑 Key: [llm], [framework], [discovery], [experiment]
    - 📖 TLDR: The exponential growth of scientific literature challenges researchers extracting and synthesizing knowledge. Traditional search engines return many sources without direct, detailed answers, while general-purpose LLMs may offer concise responses that lack depth or omit current information. LLMs with search capabilities are also limited by context window, yielding short, incomplete answers. This paper introduces WISE (Workflow for Intelligent Scientific Knowledge Extraction), a system addressing these limits by using a structured workflow to extract, refine, and rank query-specific knowledge. WISE uses an LLM-powered, tree-based architecture to refine data, focusing on query-aligned, context-aware, and non-redundant information. Dynamic scoring and ranking prioritize unique contributions from each source, and adaptive stopping criteria minimize processing overhead. WISE delivers detailed, organized answers by systematically exploring and synthesizing knowledge from diverse sources. Experiments on HBB gene-associated diseases demonstrate WISE reduces processed text by over 80% while achieving significantly higher recall over baselines like search engines and other LLM-based approaches. ROUGE and BLEU metrics reveal WISE's output is more unique than other systems, and a novel level-based metric shows it provides more in-depth information. We also explore how the WISE workflow can be adapted for diverse domains like drug discovery, material science, and social science, enabling efficient knowledge extraction and synthesis from unstructured scientific papers and web sources.

- [AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131)
    - Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, et al.
    - 🏛️ Institutions: Google. 2
    - 📅 Date: June 16, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Misc]
    - 🔑 Key: [llm], [agent], [automation], [discovery]
    - 📖 TLDR: In this white paper, we present AlphaEvolve, an evolutionary coding agent that substantially enhances capabilities of state-of-the-art LLMs on highly challenging tasks such as tackling open scientific problems or optimizing critical pieces of computational infrastructure. AlphaEvolve orchestrates an autonomous pipeline of LLMs, whose task is to improve an algorithm by making direct changes to the code. Using an evolutionary approach, continuously receiving feedback from one or more evaluators, AlphaEvolve iteratively improves the algorithm, potentially leading to new scientific and practical discoveries. We demonstrate the broad applicability of this approach by applying it to a number of important computational problems. When applied to optimizing critical components of large-scale computational stacks at Google, AlphaEvolve developed a more efficient scheduling algorithm for data centers, found a functionally equivalent simplification in the circuit design of hardware accelerators, and accelerated the training of the LLM underpinning AlphaEvolve itself. Furthermore, AlphaEvolve discovered novel, provably correct algorithms that surpass state-of-the-art solutions on a spectrum of problems in mathematics and computer science, significantly expanding the scope of prior automated discovery methods (Romera-Paredes et al., 2023). Notably, AlphaEvolve developed a search algorithm that found a procedure to multiply two $4 \times 4$ complex-valued matrices using $48$ scalar multiplications; offering the first improvement, after 56 years, over Strassen's algorithm in this setting. We believe AlphaEvolve and coding agents like it can have a significant impact in improving solutions of problems across many areas of science and computation.

- [Harnessing Large Language Models for Scientific Novelty Detection](https://arxiv.org/abs/2505.24615)
    - Yan Liu, Zonglin Yang, Soujanya Poria, Thanh-Son Nguyen, Erik Cambria
    - 🏛️ Institutions: Nanyang Technological University
    - 📅 Date: May 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Misc]
    - 🔑 Key: [llm], [benchmark], [dataset], [experiment]
    - 📖 TLDR: In an era of exponential scientific growth, identifying novel research ideas is crucial and challenging in academia. Despite potential, the lack of an appropriate benchmark dataset hinders the research of novelty detection. More importantly, simply adopting existing NLP technologies, e.g., retrieving and then cross-checking, is not a one-size-fits-all solution due to the gap between textual similarity and idea conception. In this paper, we propose to harness large language models (LLMs) for scientific novelty detection (ND), associated with two new datasets in marketing and NLP domains. To construct the considerate datasets for ND, we propose to extract closure sets of papers based on their relationship, and then summarize their main ideas based on LLMs. To capture idea conception, we propose to train a lightweight retriever by distilling the idea-level knowledge from LLMs to align ideas with similar conception, enabling efficient and accurate idea retrieval for LLM novelty detection. Experiments show our method consistently outperforms others on the proposed benchmark datasets for idea retrieval and ND tasks. Codes and data are available at https://anonymous.4open.science/r/NoveltyDetection-10FB/.

- [ScienceMeter: Tracking Scientific Knowledge Updates in Language Models](https://arxiv.org/abs/2505.24302)
    - Yike Wang, Shangbin Feng, Yulia Tsvetkov, Hannaneh Hajishirzi
    - 🏛️ Institutions: Hannaneh Hajishirzi University of Washington Allen Institute, Microsoft Accelerate Foundation Models Research. neurips
    - 📅 Date: May 30, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Misc]
    - 🔑 Key: [llm], [framework], [dataset], [reasoning], [experiment]
    - 📖 TLDR: Large Language Models (LLMs) are increasingly used to support scientific research, but their knowledge of scientific advancements can quickly become outdated. We introduce ScienceMeter, a new framework for evaluating scientific knowledge update methods over scientific knowledge spanning the past, present, and future. ScienceMeter defines three metrics: knowledge preservation, the extent to which models' understanding of previously learned papers are preserved; knowledge acquisition, how well scientific claims from newly introduced papers are acquired; and knowledge projection, the ability of the updated model to anticipate or generalize to related scientific claims that may emerge in the future. Using ScienceMeter, we examine the scientific knowledge of LLMs on claim judgment and generation tasks across a curated dataset of 15,444 scientific papers and 30,888 scientific claims from ten domains including medicine, biology, materials science, and computer science. We evaluate five representative knowledge update approaches including training- and inference-time methods. With extensive experiments, we find that the best-performing knowledge update methods can preserve only 85.9% of existing knowledge, acquire 71.7% of new knowledge, and project 37.7% of future knowledge. Inference-based methods work for larger models, whereas smaller models require training to achieve comparable performance. Cross-domain analysis reveals that performance on these objectives is correlated. Even when applying on specialized scientific LLMs, existing knowledge update methods fail to achieve these objectives collectively, underscoring that developing robust scientific knowledge update mechanisms is both crucial and challenging.

- [Exploiting Edited Large Language Models as General Scientific Optimizers](https://arxiv.org/abs/2503.09620)
    - Qitan Lv, Tianyu Liu, Hong Wang
    - 🏛️ Institutions: University of Science and Technology of China
    - 📅 Date: March 08, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Misc]
    - 🔑 Key: [llm], [reasoning], [experiment]
    - 📖 TLDR: Large language models (LLMs) have been widely adopted in mathematical optimization in scientific scenarios for their extensive knowledge and advanced reasoning capabilities. Existing methods mainly focus on utilizing LLMs to solve optimization problems in a prompt-based manner, which takes observational feedback as additional textual descriptions. However, due to LLM's \textbf{high sensitivity to the prompts} and \textbf{tendency to get lost in lengthy prompts}, these methods struggle to effectively utilize the {observational} feedback from each optimization step, which severely hinders the applications for real-world scenarios. To address these challenges, we propose a conceptually simple and general {bi-level} optimization method, namely \textbf{G}eneral \textbf{S}cientific \textbf{O}ptimizers (GSO). Specifically, GSO first utilizes inner-level simulators as experimental platforms to evaluate the current solution and provide observational feedback. Then, LLMs serve as knowledgeable and versatile scientists, generating new solutions by refining potential errors from the feedback as the outer-level optimization. Finally, simulations together with the expert knowledge in LLMs are jointly updated with bi-level interactions via model editing. Extensive experiments show that GSO consistently outperforms existing state-of-the-art methods using \textit{six} different LLM backbones on \textit{seven} different tasks, demonstrating the effectiveness and a wide range of applications.

- [Curie: Toward Rigorous and Automated Scientific Experimentation with AI Agents](https://arxiv.org/abs/2502.16069)
    - Patrick Tser Jern Kon, Jiachen Liu, Qiuyi Ding, Yiming Qiu, Zhenning Yang, Yibo Huang, Jayanth Srinivasa, Myungjin Lee, et al.
    - 🏛️ Institutions: University of Michigan
    - 📅 Date: February 22, 2025
    - 📑 Publisher: arXiv
    - 💻 Topic: [Misc]
    - 🔑 Key: [llm], [agent], [automation], [framework], [benchmark]
    - 📖 TLDR: Scientific experimentation, a cornerstone of human progress, demands rigor in reliability, methodical control, and interpretability to yield meaningful results. Despite the growing capabilities of large language models (LLMs) in automating different aspects of the scientific process, automating rigorous experimentation remains a significant challenge. To address this gap, we propose Curie, an AI agent framework designed to embed rigor into the experimentation process through three key components: an intra-agent rigor module to enhance reliability, an inter-agent rigor module to maintain methodical control, and an experiment knowledge module to enhance interpretability. To evaluate Curie, we design a novel experimental benchmark composed of 46 questions across four computer science domains, derived from influential research papers, and widely adopted open-source projects. Compared to the strongest baseline tested, we achieve a 3.4$\times$ improvement in correctly answering experimental questions. Curie is open-sourced at https://github.com/Just-Curieous/Curie.

