# Papers by Haizhao Yang

Total: 3 papers

- [AutoSR: Automatic Symbolic Regression by Searching Research States](https://arxiv.org/abs/2608.16876)
    - Kejia Zhang, Youran Sun, Xingyu Ren, Chugang Yi, Haizhao Yang
    - 🏛️ Institutions: University of Maryland, The Chinese University of Hong Kong
    - 📅 Date: August 17, 2026
    - 📑 Publisher: arXiv
    - 💻 Topic: [Scientific Discovery]
    - 🔑 Key: [llm], [agent], [discovery], [reasoning], [framework]
    - 📖 TLDR: We introduce Automatic Symbolic Regression (AutoSR), a fully automated system that instantiates Research-Space Symbolic Regression by searching persistent scientific investigations rather than isolated equations. Finite, noisy data often yield numerically competitive expressions that imply very different behavior outside the observed regime, making numerical fit and syntactic complexity insufficient measures of scientific credibility. Existing approaches largely focus on improving expressions, yet the search typically retains little beyond the resulting formula and score, losing the scientific record, such as motivations and probes, that inform what to try next. AutoSR preserves this record in a Research State, coupling each candidate equation with the reasoning, computational evidence, and independent review developed along its branch. Proposer--reviewer agents develop these states under progressive-widening Monte Carlo tree search (PW-MCTS), which allocates computation across competing investigations, while the accumulated research record is ultimately synthesized into a final report that explains the leading relation and the basis for its selection. Across nine selected challenges from two benchmark suites, AutoSR recovers algebraically equivalent relations in every case, including three cp3-bench problems that no published system recovers and six structurally diverse LSR-Transform problems. Overall, AutoSR extends symbolic regression from equation-level search toward automated scientific investigation, allowing scientific knowledge and accumulated evidence to shape both what is explored and how the resulting equation is justified.
- [AgonAlpha: Autonomous Alpha Discovery via Prompt Economy and Scalable Agentic Search](https://arxiv.org/abs/2608.11250)
    - Weicheng Ye, Youran Sun, Xingyu Ren, Shunyao Yu, Chugang Yi, Haizhao Yang
    - 🏛️ Institutions: The Chinese University of Hong Kong, University of Maryland
    - 📅 Date: August 04, 2026
    - 📑 Publisher: arXiv
    - 💻 Topic: [Scientific Discovery]
    - 🔑 Key: [llm], [agent], [automation], [discovery], [framework]
    - 📖 TLDR: Language models can propose many plausible trading factors, but an autonomous research system must also allocate its evaluation budget, verify its own evidence, and preserve how each candidate was produced. We present AgonAlpha, an architecture that searches over frozen research artifacts---hypotheses, executable expressions, platform evidence, rationales, and review status---rather than formulas alone. To our knowledge, AgonAlpha is the first alpha-mining system to combine verified artifact search, a fresh-context adversarial reviewer with re-execution and veto authority, and pending-aware parallel budget allocation, together with a complete public evidence trail. Independent deployments on WorldQuant BRAIN produced SPECTACULAR-grade alphas across five users and six model backends, with Fitness reaching 9.50 and Sharpe reaching 3.48, while retaining prompt-to-expression provenance for every submission.
- [AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing](https://arxiv.org/abs/2602.17607)
    - Jianda Du, Youran Sun, Haizhao Yang
    - 🏛️ Institutions: University of Maryland
    - 📅 Date: February 19, 2026
    - 📑 Publisher: arXiv
    - 💻 Topic: [Scientific Discovery]
    - 🔑 Key: [llm], [multi-agent], [automation], [framework], [experiment]
    - 📖 TLDR: PDEs are central to scientific and engineering modeling, yet designing accurate numerical solvers typically requires substantial mathematical expertise and manual tuning. Recent neural network-based approaches improve flexibility but often demand high computational cost and suffer from limited interpretability. We introduce AutoNumerics, a multi-agent framework that autonomously designs, implements, debugs, and verifies numerical solvers for general PDEs directly from natural language descriptions. Unlike black-box neural solvers, our framework generates transparent solvers grounded in classical numerical analysis. We introduce a coarse-to-fine execution strategy and a residual-based self-verification mechanism. Experiments on 24 canonical and real-world PDE problems demonstrate that AutoNumerics achieves competitive or superior accuracy compared to existing neural and LLM-based baselines, and correctly selects numerical schemes based on PDE structural properties, suggesting its viability as an accessible paradigm for automated PDE solving.
