#!/usr/bin/env python3
"""
Paper List Processing and Organization Script
Adapted from GUI-Agents-Paper-List for AI Scientist papers
"""

import re
import os
import pandas as pd
from datetime import datetime
from collections import Counter
from dateutil import parser
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import logging

# Set up logging
logging.basicConfig(
    filename='../../logs/error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Topic keywords mapping (changed from environment)
topic_keywords = {
    "AI Scientist": "paper_ai_scientist.md",
    "Scientific Discovery": "paper_scientific_discovery.md",
    "Automated Research": "paper_automated_research.md",
    "Experiment Design": "paper_experiment_design.md",
    "Hypothesis Generation": "paper_hypothesis_generation.md",
    "Literature Review": "paper_literature_review.md",
    "Data Analysis": "paper_data_analysis.md",
    "Machine Learning": "paper_machine_learning.md",
    "Multi-Agent": "paper_multi_agent.md",
    "Misc": "paper_misc.md"
}

# Predefined important keywords
predefined_keywords = {
    "framework", "dataset", "benchmark", "model", "LLM",
    "survey", "evaluation", "agent", "automation", "reasoning"
}

# Configuration
top_num_author = 20
top_num_keywords = 20

def parse_date_with_defaults(date_str):
    """
    Parse date string with multiple fallback strategies.
    Returns datetime object or None.
    """
    if not date_str or date_str.strip() == '':
        return None

    try:
        # Try standard parsing first
        return parser.parse(date_str, default=datetime(1900, 1, 1))
    except:
        pass

    try:
        # Try fuzzy parsing
        return parser.parse(date_str, fuzzy=True, default=datetime(1900, 1, 1))
    except:
        pass

    try:
        # Try to extract year at minimum
        year_match = re.search(r'\b(19|20)\d{2}\b', date_str)
        if year_match:
            year = int(year_match.group())
            return datetime(year, 12, 31)
    except:
        pass

    logging.error(f"Could not parse date: {date_str}")
    return None

def safe_execute(func):
    """Decorator for safe execution with error logging."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {str(e)}", exc_info=True)
            print(f"Error in {func.__name__}: {str(e)}")
            return None
    return wrapper

@safe_execute
def process_markdown(file_path):
    """
    Main processing function - parses markdown file and generates all outputs.
    """
    print("Starting paper list processing...")

    # Read the markdown file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Updated regex pattern for new format (Topic instead of Env)
    new_format_pattern = re.compile(
        r"- \[(.*?)\]\((.*?)\)\s+"          # Title and link
        r"- (.*?)\s+"                       # Authors
        r"- 🏛️ Institutions: (.*?)\s+"      # Institutions
        r"- 📅 Date: (.*?)\s+"              # Date
        r"- 📑 Publisher: (.*?)\s+"         # Publisher
        r"- 💻 Topic: \[(.*?)\]\s+"         # Topic (changed from Env)
        r"- 🔑 Key: (.*?)\s+"               # Keywords
        r"- 📖 TLDR: (.*?)(?:\n- 📄 File:.*?)?\n",  # Summary (with optional file field)
        re.DOTALL
    )

    # Extract all papers
    papers = []
    for match in new_format_pattern.finditer(content):
        paper = {
            'title': match.group(1).strip(),
            'link': match.group(2).strip(),
            'authors': match.group(3).strip(),
            'institutions': match.group(4).strip(),
            'date': match.group(5).strip(),
            'publisher': match.group(6).strip(),
            'topic': match.group(7).strip(),
            'keywords': match.group(8).strip(),
            'tldr': match.group(9).strip()
        }
        papers.append(paper)

    print(f"Found {len(papers)} papers")

    if not papers:
        print("No papers found! Check the format of your update_paper_list.md file.")
        return

    # Create DataFrame
    df = pd.DataFrame(papers)

    # Parse dates
    df['parsed_date'] = df['date'].apply(parse_date_with_defaults)

    # Remove duplicates (keep first occurrence)
    # BUT: Don't deduplicate papers with placeholder titles
    placeholder_mask = df['title'].str.contains('TITLE_NEEDED|NEEDED', case=False, na=False)
    df_placeholder = df[placeholder_mask]
    df_real = df[~placeholder_mask]

    df_real = df_real.drop_duplicates(subset='title', keep='first')
    df = pd.concat([df_real, df_placeholder], ignore_index=True)

    print(f"After deduplication: {len(df)} papers")
    print(f"  - Papers with complete titles: {len(df_real)}")
    print(f"  - Papers with placeholder titles: {len(df_placeholder)}")

    # Sort by date (most recent first)
    df = df.sort_values('parsed_date', ascending=False, na_position='last')

    # Generate all outputs
    generate_topic_files(df)
    generate_keyword_files(df)
    generate_author_files(df)
    generate_wordcloud(df)
    generate_grouping_files(df)
    generate_all_papers_file(df)

    print("Processing complete!")

@safe_execute
def generate_topic_files(df):
    """Generate markdown files for each topic."""
    print("\nGenerating topic-based files...")
    output_dir = '../../../paper_by_topic/'
    os.makedirs(output_dir, exist_ok=True)

    for topic, filename in topic_keywords.items():
        topic_papers = df[df['topic'] == topic]

        if len(topic_papers) > 0:
            output_path = os.path.join(output_dir, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# {topic} Papers\n\n")
                f.write(f"Total: {len(topic_papers)} papers\n\n")

                for _, paper in topic_papers.iterrows():
                    f.write(format_paper_entry(paper))

            print(f"  - {topic}: {len(topic_papers)} papers → {filename}")

@safe_execute
def generate_keyword_files(df):
    """Generate markdown files for top keywords."""
    print("\nGenerating keyword-based files...")
    output_dir = '../../../paper_by_key/'
    os.makedirs(output_dir, exist_ok=True)

    # Extract all keywords
    all_keywords = []
    for keywords_str in df['keywords']:
        # Extract keywords from [keyword1], [keyword2] format
        keywords = re.findall(r'\[(.*?)\]', keywords_str)
        all_keywords.extend([k.strip().lower() for k in keywords])

    # Count keyword frequency
    keyword_counts = Counter(all_keywords)

    # Separate predefined and dynamic keywords
    predefined_with_counts = [(k, keyword_counts.get(k, 0))
                               for k in predefined_keywords
                               if keyword_counts.get(k, 0) > 0]
    predefined_with_counts.sort(key=lambda x: x[1], reverse=True)

    # Get top dynamic keywords (excluding predefined)
    dynamic_keywords = [(k, c) for k, c in keyword_counts.most_common()
                        if k not in predefined_keywords]

    # Combine: predefined first, then top dynamic
    num_dynamic = top_num_keywords - len(predefined_with_counts)
    top_keywords = predefined_with_counts + dynamic_keywords[:num_dynamic]

    print(f"  Processing top {len(top_keywords)} keywords...")

    for keyword, count in top_keywords:
        # Generate filename
        safe_keyword = keyword.replace(' ', '_').replace('/', '_')
        filename = f"paper_{safe_keyword}.md"

        # Find papers with this keyword
        keyword_papers = df[df['keywords'].str.lower().str.contains(
            re.escape(f"[{keyword}]"),
            na=False,
            regex=True
        )]

        if len(keyword_papers) > 0:
            output_path = os.path.join(output_dir, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# Papers on: {keyword.title()}\n\n")
                f.write(f"Total: {len(keyword_papers)} papers\n\n")

                for _, paper in keyword_papers.iterrows():
                    f.write(format_paper_entry(paper))

            print(f"  - {keyword}: {len(keyword_papers)} papers → {filename}")

@safe_execute
def generate_author_files(df):
    """Generate author-based files for top authors."""
    print("\nGenerating author-based files...")
    output_dir = '../../../paper_by_author/'
    os.makedirs(output_dir, exist_ok=True)

    # Extract all authors
    all_authors = []
    for authors_str in df['authors']:
        # Split by comma
        authors = [a.strip() for a in authors_str.split(',')]
        all_authors.extend(authors)

    # Count author frequency
    author_counts = Counter(all_authors)
    top_authors = author_counts.most_common(top_num_author)

    print(f"  Processing top {len(top_authors)} authors...")

    for author, count in top_authors:
        # Generate filename
        safe_author = author.replace(' ', '_').replace('.', '')
        filename = f"paper_{safe_author}.md"

        # Find papers by this author
        author_papers = df[df['authors'].str.contains(
            re.escape(author),
            na=False,
            regex=False
        )]

        if len(author_papers) > 0:
            output_path = os.path.join(output_dir, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# Papers by {author}\n\n")
                f.write(f"Total: {len(author_papers)} papers\n\n")

                for _, paper in author_papers.iterrows():
                    f.write(format_paper_entry(paper))

            print(f"  - {author}: {len(author_papers)} papers → {filename}")

@safe_execute
def generate_wordcloud(df):
    """Generate keyword word cloud visualization."""
    print("\nGenerating word cloud...")

    # Extract all keywords
    all_keywords = []
    for keywords_str in df['keywords']:
        keywords = re.findall(r'\[(.*?)\]', keywords_str)
        all_keywords.extend([k.strip().lower() for k in keywords])

    # Create word frequency dictionary
    keyword_freq = Counter(all_keywords)

    if not keyword_freq:
        print("  No keywords found for word cloud")
        return

    # Generate word cloud
    wordcloud = WordCloud(
        width=2000,
        height=1000,
        background_color='white',
        colormap='viridis',
        relative_scaling=0.5,
        min_font_size=10
    ).generate_from_frequencies(keyword_freq)

    # Plot
    plt.figure(figsize=(20, 10), dpi=400)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)

    # Save
    output_dir = '../../statistics/'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'keyword_wordcloud.png')
    plt.savefig(output_path, dpi=400, bbox_inches='tight')
    plt.close()

    print(f"  Word cloud saved to {output_path}")

@safe_execute
def generate_grouping_files(df):
    """Generate markdown files for topic, keyword, and author groupings."""
    print("\nGenerating grouping files...")

    # Topic grouping
    topic_links = []
    for topic, filename in sorted(topic_keywords.items()):
        count = len(df[df['topic'] == topic])
        if count > 0:
            link = f"- [{topic}](paper_by_topic/{filename}) ({count} papers)"
            topic_links.append(link)

    with open('../../topic_grouping.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(topic_links))
    print(f"  Topic grouping: {len(topic_links)} topics")

    # Keyword grouping
    keyword_files = sorted([f for f in os.listdir('../../../paper_by_key/') if f.endswith('.md')])
    keyword_links = []
    for filename in keyword_files:
        keyword = filename.replace('paper_', '').replace('.md', '').replace('_', ' ').title()
        # Count papers for this keyword
        keyword_lower = keyword.lower().replace(' ', '_')
        keyword_pattern = keyword_lower.replace('_', ' ')
        count = len(df[df['keywords'].str.lower().str.contains(
            re.escape(f"[{keyword_pattern}]"),
            na=False,
            regex=True
        )])
        link = f"- [{keyword}](paper_by_key/{filename}) ({count} papers)"
        keyword_links.append(link)

    with open('../../keyword_grouping.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(keyword_links))
    print(f"  Keyword grouping: {len(keyword_links)} keywords")

    # Author grouping
    author_files = sorted([f for f in os.listdir('../../../paper_by_author/') if f.endswith('.md')])
    author_links = []
    for filename in author_files:
        author = filename.replace('paper_', '').replace('.md', '').replace('_', ' ')
        # Count papers for this author
        count = len(df[df['authors'].str.contains(
            re.escape(author),
            na=False,
            regex=False
        )])
        link = f"- [{author}](paper_by_author/{filename}) ({count} papers)"
        author_links.append(link)

    with open('../../author_grouping.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(author_links))
    print(f"  Author grouping: {len(author_links)} authors")

@safe_execute
def generate_all_papers_file(df):
    """Generate a single file with all papers sorted by date."""
    print("\nGenerating all papers file...")

    with open('../../all_papers.md', 'w', encoding='utf-8') as f:
        for _, paper in df.iterrows():
            f.write(format_paper_entry(paper))

    print(f"  All papers file generated with {len(df)} papers")

def format_paper_entry(paper):
    """Format a single paper entry as markdown."""
    return f"""- [{paper['title']}]({paper['link']})
    - {paper['authors']}
    - 🏛️ Institutions: {paper['institutions']}
    - 📅 Date: {paper['date']}
    - 📑 Publisher: {paper['publisher']}
    - 💻 Topic: [{paper['topic']}]
    - 🔑 Key: {paper['keywords']}
    - 📖 TLDR: {paper['tldr']}

"""

def main():
    """Main entry point."""
    input_file = '../../update_paper_list.md'

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        print("Please create this file first using extract_pdf_metadata.py")
        return

    process_markdown(input_file)

if __name__ == '__main__':
    main()
