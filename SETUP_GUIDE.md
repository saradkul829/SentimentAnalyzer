# Setup and Git Push Guide

## Quick Setup (5 Minutes)

### Step 1: Initial Setup on Your Computer

```bash
# Navigate to where you want to store the project
cd ~/Desktop  # or wherever you prefer

# Copy the project folder from Claude to your computer
# (You'll download the ZIP and extract it)

# Navigate into the project
cd SentimentAnalyzer

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Test the Project

```bash
# Run the analysis
python src/sentiment_analyzer.py

# Generate visualizations
python src/visualizer.py

# OR use the quick start script (macOS/Linux):
./run_analysis.sh
```

If everything works, you should see:
- `results/analyzed_reviews.csv` created
- Multiple PNG files in `visualizations/` folder

### Step 3: Connect to Your GitHub Repository

```bash
# Initialize git (if not already done)
git init

# Add your GitHub repository as remote
git remote add origin https://github.com/saradkul829/SentimentAnalyzer.git

# Check the connection
git remote -v
```

### Step 4: Make Your First Commit

```bash
# Check what files will be added
git status

# Add all files
git add .

# Create your first commit
git commit -m "Initial commit: UIUC Course Sentiment Analyzer with NLP analysis"

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 5: Verify on GitHub

1. Go to `https://github.com/saradkul829/SentimentAnalyzer`
2. You should see all your files
3. The README.md should display nicely
4. Check that visualizations folder has the PNG files

---

## Troubleshooting

### Problem: "Permission denied" when pushing

**Solution:**
```bash
# You may need to authenticate with GitHub
# Option 1: Use Personal Access Token
# Go to GitHub Settings → Developer settings → Personal access tokens
# Generate a token and use it as your password

# Option 2: Set up SSH key
# Follow: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
```

### Problem: "pip install fails"

**Solution:**
```bash
# Try upgrading pip first
pip install --upgrade pip

# Then install requirements again
pip install -r requirements.txt

# If specific packages fail, install them one by one:
pip install pandas numpy matplotlib seaborn nltk textblob wordcloud
```

### Problem: "ModuleNotFoundError" when running scripts

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Reinstall requirements
pip install -r requirements.txt
```

### Problem: "NLTK data not found"

**Solution:**
Run this Python script once:
```python
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
```

---

## Customization Tips

### Adding Your Own Data

1. Edit `data/sample_reviews.csv`
2. Add more rows following the same format:
   ```
   course_code,course_name,review,rating,semester
   ```
3. Run the analysis again

### Changing the README

1. Edit `README.md`
2. Update your GitHub username and LinkedIn URL
3. Commit and push:
   ```bash
   git add README.md
   git commit -m "Update README with personal information"
   git push
   ```

### Adding Screenshots to README

1. Run the analysis to generate visualizations
2. Take screenshots or use the PNG files directly
3. Create an `images/` folder:
   ```bash
   mkdir images
   cp visualizations/*.png images/
   ```
4. Update README.md to reference images:
   ```markdown
   ![Sentiment Distribution](images/sentiment_distribution.png)
   ```
5. Commit and push:
   ```bash
   git add images/ README.md
   git commit -m "Add visualization screenshots to README"
   git push
   ```

---

## Making Updates Later

Whenever you make changes:

```bash
# Check what changed
git status

# Add all changes
git add .

# Commit with a descriptive message
git commit -m "Description of what you changed"

# Push to GitHub
git push
```

### Good Commit Message Examples:
- ✅ "Add more sample data for CS courses"
- ✅ "Improve sentiment analysis accuracy"
- ✅ "Fix bug in topic extraction"
- ✅ "Update README with setup instructions"
- ❌ "Update" (too vague)
- ❌ "Fix stuff" (not descriptive)

---

## What's Already Configured

✅ `.gitignore` - Prevents committing unnecessary files  
✅ `requirements.txt` - All dependencies listed  
✅ `README.md` - Professional documentation  
✅ Project structure - Organized and clean  
✅ Sample data - Ready to run immediately  
✅ Working code - Tested and functional  

---

## Next Steps After Pushing

1. **Add Topics to Repository**
   - Go to your repo on GitHub
   - Click "About" (gear icon)
   - Add topics: `python`, `nlp`, `sentiment-analysis`, `data-science`, `uiuc`

2. **Pin the Repository**
   - Go to your GitHub profile
   - Click "Customize your pins"
   - Select this repository

3. **Share It**
   - Add the link to your resume
   - Include in Product Space application
   - Share with friends for feedback

---

## Need Help?

If you get stuck:
1. Read error messages carefully
2. Google the error
3. Check Stack Overflow
4. Ask ChatGPT/Claude for help with specific errors
5. Review this guide again

You've got this! 🚀
