# Awesome AI Scientist Papers

A curated collection of research papers on AI scientists, automated scientific discovery, machine learning for science, and related topics. This repository organizes papers by topic, keywords, and authors for easy navigation and discovery.

## 馃搳 Statistics

![Keyword Word Cloud](data/statistics/keyword_wordcloud.png)

**Total Papers:** See counts below organized by different categories.

## 馃幆 What is an AI Scientist?

An **AI Scientist** is an artificial intelligence system capable of conducting scientific research autonomously or semi-autonomously. This includes:
- 馃敩 Generating research hypotheses
- 馃И Designing and conducting experiments
- 馃搳 Analyzing data and drawing conclusions
- 馃摑 Writing research papers
- 馃攧 Iterating on research directions

This repository tracks the latest research in this rapidly evolving field.

## 馃梻锔?Browse Papers by Category

### 馃摎 By Research Topic
{{insert_topic_groups_here}}

### 馃攽 By Keywords
{{insert_keyword_groups_here}}

### 馃懃 By Top Authors
{{insert_author_groups_here}}

## 馃摎 All Papers (Sorted by Date - Most Recent First)

{{insert_all_papers_here}}

## 馃 Contributing

We welcome contributions! To add a new paper:

1. Fork this repository
2. Add your paper to `data/update_paper_list.md` following this format:

```markdown
- [Paper Title](https://arxiv.org/abs/XXXX.XXXXX or DOI)
    - Author1, Author2, Author3
    - 馃彌锔?Institutions: Institution1, Institution2
    - 馃搮 Date: Month Day, Year
    - 馃搼 Publisher: Venue (arXiv, Conference, Journal)
    - 馃捇 Topic: [Choose: AI Scientist, Scientific Discovery, Automated Research, etc.]
    - 馃攽 Key: [keyword1], [keyword2], [keyword3]
    - 馃摉 TLDR: Full abstract of the paper.
```

3. Submit a pull request

The repository will automatically regenerate all categorized views when your PR is merged.

### Adding Papers Efficiently

**Option 1: Use AI Assistance**
- Copy the prompt from `backend/prompts/auto_prompt_en.txt`
- Paste it to ChatGPT/Claude along with your paper title or arXiv link
- Copy the formatted output into `update_paper_list.md`

**Option 2: Manual Entry**
- Follow the format above
- Ensure all required fields are filled
- Use consistent formatting

**Option 3: Auto-fill Institutions**
- Run `python backend/scripts/enrich_institutions.py --pdf-extract --email-map`
- The script uses a 5-tier cascade (Semantic Scholar → OpenAlex → CrossRef → HTML/PDF → Email domain) to fill missing institution data automatically.

## 馃洜锔?How This Repository Works

This repository uses automation to maintain organization:

1. **Master Database**: All papers are stored in `data/update_paper_list.md`
2. **Automated Processing**: GitHub Actions runs a Python script on every update
3. **Generated Views**: Papers are automatically organized by:
   - Topic (AI Scientist, Scientific Discovery, etc.)
   - Keywords (LLM, agent, framework, etc.)
   - Authors (top 20 most prolific)
4. **Word Cloud**: Keyword frequency visualization is auto-generated
5. **README**: This file is regenerated with updated counts and links

## 馃摉 Related Resources

- [Awesome AI for Science](https://github.com/yuanqing-wang/awesome-ai-for-science)
- [Awesome Scientific Language Models](https://github.com/yuzhimanhua/Awesome-Scientific-Language-Models)
- [Papers with Code - Scientific Discovery](https://paperswithcode.com/task/scientific-discovery)

## 馃搫 License

This repository is licensed under the MIT License. All papers belong to their respective authors and publishers.

## 馃専 Star History

If you find this repository useful, please consider giving it a star 猸?

## 馃摦 Contact

For questions, suggestions, or discussions:
- Open an issue in this repository
- Contribute via pull requests

---

**Last Updated:** Auto-generated on every commit

**Maintained by:** Community contributors

