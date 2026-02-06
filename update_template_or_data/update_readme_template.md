# Awesome AI Scientist Papers

A curated collection of research papers on AI scientists, automated scientific discovery, machine learning for science, and related topics. This repository organizes papers by topic, keywords, and authors for easy navigation and discovery.

## 📊 Statistics

![Keyword Word Cloud](update_template_or_data/statistics/keyword_wordcloud.png)

**Total Papers:** See counts below organized by different categories.

## 🎯 What is an AI Scientist?

An **AI Scientist** is an artificial intelligence system capable of conducting scientific research autonomously or semi-autonomously. This includes:
- 🔬 Generating research hypotheses
- 🧪 Designing and conducting experiments
- 📊 Analyzing data and drawing conclusions
- 📝 Writing research papers
- 🔄 Iterating on research directions

This repository tracks the latest research in this rapidly evolving field.

## 🗂️ Browse Papers by Category

### 📚 By Research Topic
{{insert_topic_groups_here}}

### 🔑 By Keywords
{{insert_keyword_groups_here}}

### 👥 By Top Authors
{{insert_author_groups_here}}

## 📚 All Papers (Sorted by Date - Most Recent First)

{{insert_all_papers_here}}

## 🤝 Contributing

We welcome contributions! To add a new paper:

1. Fork this repository
2. Add your paper to `update_template_or_data/update_paper_list.md` following this format:

```markdown
- [Paper Title](https://arxiv.org/abs/XXXX.XXXXX or DOI)
    - Author1, Author2, Author3
    - 🏛️ Institutions: Institution1, Institution2
    - 📅 Date: Month Day, Year
    - 📑 Publisher: Venue (arXiv, Conference, Journal)
    - 💻 Topic: [Choose: AI Scientist, Scientific Discovery, Automated Research, etc.]
    - 🔑 Key: [keyword1], [keyword2], [keyword3]
    - 📖 TLDR: Brief 1-2 sentence summary of the paper.
```

3. Submit a pull request

The repository will automatically regenerate all categorized views when your PR is merged.

### Adding Papers Efficiently

**Option 1: Use AI Assistance**
- Copy the prompt from `update_template_or_data/utils/prompts/auto_prompt_en.txt`
- Paste it to ChatGPT/Claude along with your paper title or arXiv link
- Copy the formatted output into `update_paper_list.md`

**Option 2: Manual Entry**
- Follow the format above
- Ensure all required fields are filled
- Use consistent formatting

## 🛠️ How This Repository Works

This repository uses automation to maintain organization:

1. **Master Database**: All papers are stored in `update_template_or_data/update_paper_list.md`
2. **Automated Processing**: GitHub Actions runs a Python script on every update
3. **Generated Views**: Papers are automatically organized by:
   - Topic (AI Scientist, Scientific Discovery, etc.)
   - Keywords (LLM, agent, framework, etc.)
   - Authors (top 20 most prolific)
4. **Word Cloud**: Keyword frequency visualization is auto-generated
5. **README**: This file is regenerated with updated counts and links

## 📖 Related Resources

- [Awesome AI for Science](https://github.com/yuanqing-wang/awesome-ai-for-science)
- [Awesome Scientific Language Models](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models)
- [Papers with Code - Scientific Discovery](https://paperswithcode.com/task/scientific-discovery)

## 📄 License

This repository is licensed under the MIT License. All papers belong to their respective authors and publishers.

## 🌟 Star History

If you find this repository useful, please consider giving it a star ⭐!

## 📮 Contact

For questions, suggestions, or discussions:
- Open an issue in this repository
- Contribute via pull requests

---

**Last Updated:** Auto-generated on every commit

**Maintained by:** Community contributors
