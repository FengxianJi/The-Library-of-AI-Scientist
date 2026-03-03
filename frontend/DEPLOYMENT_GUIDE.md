# Deployment Guide

## Quick Start

### 1. Push to GitHub

```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin master
```

### 2. Enable GitHub Actions

1. Go to your repository on GitHub
2. Click the **Actions** tab
3. If prompted, click **"I understand my workflows, go ahead and enable them"**
4. The automation will run daily at 2:00 AM UTC

### 3. Test the Automation (Optional)

**Manual trigger on GitHub:**
1. Go to **Actions** → **"Daily arXiv Paper Search"**
2. Click **"Run workflow"**
3. Select branch and click **"Run workflow"**

**Local testing:**
```bash
python update_template_or_data/utils/scripts/arxiv_auto_search.py
```

## Configuration

### Repository Settings (Optional)

**For automatic issue creation:**
1. Go to **Settings** → **Actions** → **General**
2. Under "Workflow permissions", ensure:
   - ✅ "Read and write permissions" is selected
   - ✅ "Allow GitHub Actions to create and approve pull requests" is checked

**Add labels for issues:**
1. Go to **Issues** → **Labels**
2. Create labels:
   - `paper-review` (color: #0075ca)
   - `automated` (color: #7057ff)

### Customize Search Settings

Edit `update_template_or_data/arxiv_search_config.yaml`:

```yaml
# Adjust filtering thresholds
filtering:
  min_auto_accept_score: 0.8    # Auto-accept threshold
  min_review_score: 0.5          # Manual review threshold
  min_score_threshold: 0.4       # Exclusion threshold

# Modify search parameters
search_params:
  max_results_per_query: 50
  initial_lookback_days: 7
```

### Change Schedule

Edit `.github/workflows/arxiv_daily_search.yml`:

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # 2:00 AM UTC daily
```

Cron format: `minute hour day month weekday`
- `0 2 * * *` = 2:00 AM UTC daily
- `0 */6 * * *` = Every 6 hours
- `0 2 * * 1` = 2:00 AM UTC every Monday

## How It Works

### Daily Automation

```
2:00 AM UTC Daily
    ↓
Search arXiv API
    ↓
Apply filtering
    ↓
├─ Auto-accepted (score ≥ 0.8)
│  ├─ Append to paper list
│  ├─ Categorize papers
│  ├─ Regenerate README
│  └─ Commit & push
│
├─ Pending review (0.5 ≤ score < 0.8)
│  ├─ Save to arxiv_pending_review.md
│  └─ Create GitHub issue
│
└─ Excluded (score < 0.4)
   └─ Save to arxiv_excluded.md
```

### Manual Paper Addition

1. Add papers to `update_template_or_data/update_paper_list.md`
2. Follow the format:
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
3. Commit and push
4. GitHub Actions will regenerate all files

## Troubleshooting

### Workflow Fails
- Check **Actions** tab for error logs
- Common issues:
  - API timeout (normal, will retry next run)
  - No papers found (normal, no action needed)
  - Permission denied (check repository settings)

### Papers Not Being Added
- Check `arxiv_pending_review.md` - may need manual review
- Check `arxiv_excluded.md` - may be filtered out
- Adjust filtering thresholds if too strict

### Duplicate Papers
- System tracks seen papers automatically
- Check `.arxiv_search_state.json` if duplicates appear

## Support

For issues:
1. Check GitHub Actions logs
2. Review `update_template_or_data/logs/error.log`
3. Open a GitHub issue

## Quick Links

- **Configuration**: `update_template_or_data/arxiv_search_config.yaml`
- **Daily Workflow**: `.github/workflows/arxiv_daily_search.yml`
- **Main Script**: `update_template_or_data/utils/scripts/arxiv_auto_search.py`
