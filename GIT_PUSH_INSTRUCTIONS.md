# Step-by-Step: Push to Your GitHub Repository

## Prerequisites
- ✅ You've created a GitHub repository named `SentimentAnalyzer`
- ✅ You have Git installed on your computer
- ✅ You have the project folder on your computer

---

## Step 1: Open Terminal/Command Prompt

**macOS/Linux:**
- Open Terminal application
- Or right-click the project folder → "New Terminal at Folder"

**Windows:**
- Open Command Prompt or PowerShell
- Or right-click the project folder → "Git Bash Here" (if you have Git Bash)

---

## Step 2: Navigate to Project Folder

```bash
# If you're not already in the project folder
cd path/to/SentimentAnalyzer

# For example:
# cd ~/Desktop/SentimentAnalyzer
# or
# cd C:\Users\Sara\Desktop\SentimentAnalyzer
```

Verify you're in the right place:
```bash
ls  # macOS/Linux
dir # Windows

# You should see: data/, src/, README.md, etc.
```

---

## Step 3: Configure Git (First Time Only)

```bash
# Set your name
git config --global user.name "Sara Kulkarni"

# Set your email (use your UIUC email)
git config --global user.email "saradk2@illinois.edu"

# Verify it worked
git config --global --list
```

---

## Step 4: Initialize Git Repository

```bash
# Initialize git in this folder
git init

# Verify it worked - you should see "Initialized empty Git repository"
```

---

## Step 5: Connect to GitHub

```bash
# Add your GitHub repository as the remote
git remote add origin https://github.com/saradkul829/SentimentAnalyzer.git

# Verify the connection
git remote -v

# You should see:
# origin  https://github.com/saradkul829/SentimentAnalyzer.git (fetch)
# origin  https://github.com/saradkul829/SentimentAnalyzer.git (push)
```

---

## Step 6: Stage All Files

```bash
# Add all files to staging
git add .

# Check what will be committed
git status

# You should see a long list of files in green
```

---

## Step 7: Create Your First Commit

```bash
# Commit with a descriptive message
git commit -m "Initial commit: UIUC Course Sentiment Analyzer with NLP analysis and visualizations"

# You should see a summary like:
# [main (root-commit) abc1234] Initial commit...
# XX files changed, XXXX insertions(+)
```

---

## Step 8: Push to GitHub

```bash
# Set the branch name to 'main' and push
git branch -M main
git push -u origin main
```

**If this is your first time pushing:**

You'll be asked to authenticate. You have two options:

### Option A: Use Personal Access Token (Recommended)

1. Go to GitHub.com
2. Click your profile picture → Settings
3. Scroll down → Developer settings
4. Personal access tokens → Tokens (classic)
5. "Generate new token (classic)"
6. Give it a name: "UIUC Project"
7. Select scopes: Check "repo" (all sub-items)
8. Click "Generate token"
9. **COPY THE TOKEN** (you won't see it again!)
10. When prompted for password, paste the token

### Option B: Use GitHub CLI

```bash
# Install GitHub CLI if you don't have it
# Visit: https://cli.github.com/

# Authenticate
gh auth login

# Follow the prompts
```

---

## Step 9: Verify on GitHub

1. Go to `https://github.com/saradkul829/SentimentAnalyzer`
2. You should see all your files! 🎉
3. The README.md should display beautifully
4. Check that you have:
   - ✅ data/sample_reviews.csv
   - ✅ src/sentiment_analyzer.py
   - ✅ src/visualizer.py
   - ✅ README.md
   - ✅ All other files

---

## Step 10: Make Your Repository Look Professional

### Add Topics
1. On your GitHub repo page, click the gear icon next to "About"
2. Add topics: `python` `nlp` `sentiment-analysis` `data-science` `uiuc` `machine-learning`
3. Click "Save changes"

### Update Repository Description
1. Click the gear icon next to "About"
2. Description: "NLP-powered sentiment analysis tool helping UIUC students make informed course decisions"
3. Website: Your LinkedIn or portfolio (optional)
4. Click "Save changes"

### Pin the Repository
1. Go to your GitHub profile page
2. Click "Customize your pins"
3. Select this repository
4. Click "Save pins"

---

## Making Future Updates

Whenever you change files:

```bash
# 1. Check what changed
git status

# 2. Stage the changes
git add .
# Or stage specific files:
# git add README.md
# git add src/sentiment_analyzer.py

# 3. Commit with a message
git commit -m "Add more sample data and improve analysis"

# 4. Push to GitHub
git push
```

---

## Troubleshooting

### Problem: "fatal: not a git repository"
**Solution:** You're not in the project folder. Navigate there first:
```bash
cd path/to/SentimentAnalyzer
```

### Problem: "remote origin already exists"
**Solution:** Remove and re-add:
```bash
git remote remove origin
git remote add origin https://github.com/saradkul829/SentimentAnalyzer.git
```

### Problem: "authentication failed"
**Solution:** Use a Personal Access Token instead of your password (see Step 8, Option A)

### Problem: "rejected because the remote contains work"
**Solution:** Your GitHub repo isn't empty. Either:
1. Delete the repo and create a new empty one, OR
2. Force push (⚠️ this will overwrite GitHub):
```bash
git push -f origin main
```

### Problem: "Permission denied (publickey)"
**Solution:** You need to set up SSH keys or use HTTPS with token (Option A in Step 8)

---

## Common Git Commands Reference

```bash
# Check status
git status

# See commit history
git log --oneline

# See what changed
git diff

# Undo last commit (keeps changes)
git reset --soft HEAD~1

# Discard all local changes (⚠️ careful!)
git reset --hard HEAD

# Pull latest from GitHub
git pull

# Create a new branch
git checkout -b feature-name

# Switch branches
git checkout main
```

---

## Checklist: Is Everything Pushed?

- [ ] All files visible on GitHub
- [ ] README.md displays correctly
- [ ] data/sample_reviews.csv is there
- [ ] src/ folder has both Python files
- [ ] requirements.txt is present
- [ ] .gitignore is working (no __pycache__ or venv/)
- [ ] Repository has topics/tags
- [ ] Repository description is set
- [ ] Repository is pinned on your profile

---

## What's Next?

1. **Test Your Repository**
   - Clone it to a different location to make sure it works:
   ```bash
   cd ~/Desktop
   git clone https://github.com/saradkul829/SentimentAnalyzer.git test-clone
   cd test-clone
   ```

2. **Update Your Resume**
   - Add the GitHub link to your resume
   - Mention it in your Product Space application

3. **Share It**
   - Post about it on LinkedIn
   - Add to your portfolio
   - Show it to friends for feedback

4. **Keep Building**
   - Work on Project 2 or 3
   - Add more features to this project
   - Keep your GitHub active!

---

## Need More Help?

- **Git Documentation:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com/
- **Visual Git Tutorial:** https://learngitbranching.js.org/

**You've got this!** 🚀

Once you push, you'll have a professional project on your GitHub that showcases your skills. That's a huge accomplishment!
