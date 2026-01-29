#!/bin/bash
# Quick start script for UIUC Course Sentiment Analyzer

echo "=============================================="
echo "UIUC Course Sentiment Analyzer"
echo "=============================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies if needed
echo "Checking dependencies..."
pip install -r requirements.txt -q

# Run sentiment analysis
echo ""
echo "Running sentiment analysis..."
python src/sentiment_analyzer.py

# Generate visualizations
echo ""
echo "Generating visualizations..."
python src/visualizer.py

echo ""
echo "=============================================="
echo "Analysis complete!"
echo "=============================================="
echo ""
echo "Results saved to:"
echo "  - results/analyzed_reviews.csv"
echo "  - visualizations/*.png"
