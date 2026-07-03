# Papers by Haonan Huang

Total: 2 papers

- [Grounded autonomous research: a fault-tolerant LLM pipeline from corpus to manuscript in frontier computational physics](http://arxiv.org/abs/2607.02329v1)
    - Haonan Huang
    - 📅 Date: July 02, 2026
    - 📑 Publisher: arXiv
    - 💻 Topic: [Misc]
    - 🔑 Key: [llm], [agent], [automation], [framework], [dataset], [reasoning], [survey]
    - 📖 TLDR: Autonomous-research agents have demonstrated end-to-end LLM automation in machine-learning sandboxes where execution provides calibration. Frontier physical science differs categorically: physical reasoning underlies every methodology choice, toolchains are often underdocumented, and calibration must come from external literature anchors - which unscaffolded agents cite but do not confront, hallucinating plausible, unverifiable results from internal priors. We present a pipeline that runs end-to-end from a corpus of 11,083 recent condensed-matter physics arXiv papers to a publication-grade manuscript with three substantive physics findings (here on altermagnetic piezomagnetism): the agent autonomously conceives a research direction by mapping the corpus, calibrates methodology by reproducing published references, conducts novel first-principles computations, and writes the manuscript - grounded in literature throughout, across 47 fresh-context sessions in six phases sharing only on-disk state, with 2,162 literature-consultation events. Fault tolerance emerges from redundancy: fresh-context isolation, distributed grounding, and adversarial review catch what any single session misses; pre- and post-pilot stages are fully autonomous, and pilot requires bounded human intervention only at reproduction failures - operational knowledge curation, not scientific direction. Two paired failure modes - a pre-architecture baseline and a no-pilot ablation - isolate structurally enforced numerical confrontation at calibration checkpoints as the operative grounding mechanism. The primitives, characterized failure modes, and quantified intervention pattern lay a foundation for autonomous research in high-stakes scientific domains beyond computational physics.
- [Towards grounded autonomous research: an end-to-end LLM mini research loop on published computational physics](http://arxiv.org/abs/2604.12198v1)
    - Haonan Huang
    - 📅 Date: April 14, 2026
    - 📑 Publisher: arXiv
    - 💻 Topic: [Misc]
    - 🔑 Key: [llm], [agent], [automation], [framework], [reasoning]
    - 📖 TLDR: Recent autonomous LLM agents have demonstrated end-to-end automation of machine-learning research. Real-world physical science is intrinsically harder, requiring deep reasoning bounded by physical truth and, because real systems are too complex to study in isolation, almost always built on existing literature. We focus on the smallest meaningful unit of such research, a mini research loop in which an agent reads a paper, reproduces it, critiques it, and extends it. We test this loop in two complementary regimes: scale and depth. At scale, across 111 open-access computational physics papers, an agent autonomously runs the read-plan-compute-compare loop and, without being asked to critique, raises substantive concerns on ~42% of papers - 97.7% of which require execution to surface. In depth, for one Nature Communications paper on multiscale simulation of a 2D-material MOSFET, the agent runs new calculations missing from the original and produces, unsupervised, a publishable Comment -- composed, figured, typeset, and PDF-iterated -- that revises the paper's headline conclusion.
