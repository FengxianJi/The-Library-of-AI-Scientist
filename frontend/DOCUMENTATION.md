# AI Scientist Paper Collection

A curated collection of research papers on **AI Scientists** and **Automated Scientific Discovery**, featuring fully automated daily arXiv paper search with intelligent filtering and categorization.

## Features

- **Automated Daily Discovery**: Searches arXiv every day at 2:00 AM UTC
- **Intelligent Filtering**: 3-tier keyword system with relevance scoring
- **Auto-Categorization**: Papers sorted by topic, keyword, and author
- **README Generation**: Automatically updated with new papers

## Project Structure

```
├── paper_by_topic/          # Papers categorized by research topic
├── paper_by_key/            # Papers categorized by keyword
├── paper_by_author/         # Papers categorized by author (in development)
├── update_template_or_data/ # Data files and processing scripts
│   ├── utils/scripts/       # Automation scripts
│   └── arxiv_search_config.yaml  # Search configuration
└── .github/workflows/       # GitHub Actions automation
```

## Usage

### Browse Papers

- **Main README**: Browse all papers in chronological order
- **By Topic**: See `paper_by_topic/` directory
- **By Keyword**: See `paper_by_key/` directory
- **By Author**: See `paper_by_author/` directory (in development)

### Add Papers Manually

1. Add paper entries to `update_template_or_data/update_paper_list.md`
2. Follow this format:

```markdown
- [Paper Title](https://arxiv.org/abs/XXXX.XXXXX)
    - Author1, Author2, et al.
    - 🏛️ Institutions: University1, Company1
    - 📅 Date: Month Day, Year
    - 📑 Publisher: arXiv
    - 💻 Topic: [AI Scientist]
    - 🔑 Key: [llm], [agent], [automation]
    - 📖 TLDR: Paper summary...
```

3. Commit and push - automation will regenerate all files

## Automation

### Daily Workflow

The system automatically:
1. Searches arXiv for new AI Scientist papers
2. Filters papers using relevance scoring
3. Auto-accepts highly relevant papers (score ≥ 0.8)
4. Flags papers for manual review (score 0.5-0.8)
5. Categorizes papers by topic and keyword
6. Regenerates README and category files
7. Commits and pushes changes

### Search Queries

The automation uses 9 targeted queries:
- AI scientist / autonomous scientist
- Scientific discovery with LLM/agents
- Hypothesis generation
- Automated research
- Experiment design
- Literature review automation
- Data analysis automation
- Multi-agent scientific systems
- LLM for scientific research

### Filtering

Papers are scored based on keyword matches:
- **High-Priority**: AI scientist, automated research, autonomous research
- **Medium-Priority**: Hypothesis generation, experiment design, research agents
- **Supporting**: LLM, multi-agent, research workflow

## Configuration

### Search Settings

Edit `update_template_or_data/arxiv_search_config.yaml`:

```yaml
filtering:
  min_auto_accept_score: 0.8
  min_review_score: 0.5
  min_score_threshold: 0.4

search_params:
  max_results_per_query: 50
  initial_lookback_days: 7
```

### Schedule

Edit `.github/workflows/arxiv_daily_search.yml`:

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # 2:00 AM UTC daily
```

## Paper Categories

### Topics
- **AI Scientist**: Autonomous AI scientists
- **Scientific Discovery**: AI-driven discovery systems
- **Hypothesis Generation**: Automated hypothesis generation
- **Literature Review**: Automated literature review
- **Data Analysis**: Automated data analysis
- **Machine Learning**: ML for scientific research
- **Multi-Agent**: Multi-agent research systems
- **Misc**: Other related papers

### Keywords
- **agent**: Agent-based systems
- **automation**: Automation frameworks
- **benchmark**: Benchmarks and evaluation
- **dataset**: Research datasets
- **discovery**: Discovery systems
- **experiment**: Experiment design
- **framework**: Software frameworks
- **hypothesis**: Hypothesis generation
- **llm**: Large language models
- **reasoning**: Reasoning capabilities
- **survey**: Survey papers

## Development

### Prerequisites

```bash
pip install -r requirements.txt
```

### Local Testing

```bash
# Test arXiv search
python update_template_or_data/utils/scripts/arxiv_auto_search.py

# Test paper processing
cd update_template_or_data/utils/scripts
python sort_by_date.py
python generate_readme.py
```

## Contributing

1. Fork the repository
2. Add papers to `update_template_or_data/update_paper_list.md`
3. Follow the paper format guidelines
4. Create a pull request

## Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for complete deployment instructions.

## License

This project is open source. Papers are property of their respective authors.

## Acknowledgments

- Papers sourced from [arXiv.org](https://arxiv.org)
- Automated using GitHub Actions
