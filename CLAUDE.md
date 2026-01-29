# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

UIUC Course Sentiment Analyzer - A Python NLP tool that analyzes student course reviews to help UIUC students make informed course selection decisions. Uses dual sentiment analysis (VADER + TextBlob) with topic extraction and visualization generation.

## Commands

```bash
# Setup virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Download required NLTK data (one-time)
python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('punkt'); nltk.download('stopwords')"

# Run sentiment analysis pipeline
python src/sentiment_analyzer.py   # Outputs: results/analyzed_reviews.csv

# Generate visualizations
python src/visualizer.py           # Outputs: visualizations/*.png

# Run both steps (macOS/Linux)
./run_analysis.sh
```

## Architecture

### Data Flow
1. Input: `data/sample_reviews.csv` (columns: course_code, course_name, review, rating, semester)
2. Processing: `src/sentiment_analyzer.py` → `results/analyzed_reviews.csv`
3. Visualization: `src/visualizer.py` → `visualizations/*.png`

### Key Components

**`src/sentiment_analyzer.py`** - `CourseReviewAnalyzer` class
- `clean_text()` - Text preprocessing (lowercase, remove special chars)
- `analyze_sentiment_vader()` - VADER sentiment (compound threshold: ±0.05)
- `analyze_sentiment_textblob()` - TextBlob sentiment (polarity threshold: ±0.1)
- `extract_topics()` - Keyword-based topic detection (difficulty, workload, teaching, exams, helpful)
- `analyze_all()` - Full pipeline execution
- `get_course_summary()` - Per-course statistics

**`src/visualizer.py`** - `ReviewVisualizer` class
- Generates 7 visualizations: sentiment distribution, course comparison, rating vs sentiment, course ratings, positive/negative word clouds, topic distribution
- Color scheme: Positive=#2ecc71 (green), Neutral=#95a5a6 (gray), Negative=#e74c3c (red)
- Output: 300 DPI PNG files

**`src/scraper.py`** - Optional Reddit scraper using PRAW (requires API credentials)

### Dependencies
Core: pandas, numpy, nltk (VADER), textblob, matplotlib, seaborn, wordcloud

## Development Notes

- No automated tests or linting configured
- Topic keywords are hardcoded in `extract_topics()` - extend regex patterns for new categories
- CSV column names are case-sensitive and must match exactly
- In-memory pandas processing - not optimized for datasets >100K reviews
