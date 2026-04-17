# Deployment Checklist

## Before Pushing To GitHub

- Verify project opens locally using a static server (index.html)
- Verify Streamlit app starts with app.py
- Confirm these files exist:
  - app.py
  - requirements.txt
  - runtime.txt
  - index.html
  - styles/main.css
  - scripts/main.js
  - assets/logo.jpeg

## Git Commands

Use these commands from the project root:

```bash
git init
git add .
git commit -m "Initial commit: Internship Project 1"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

## Streamlit Cloud Settings

- Repository: your GitHub repo
- Branch: main
- Main file path: app.py
- Python version: from runtime.txt

## If Build Fails On Streamlit

- Check streamlit cloud logs for missing package name
- Confirm requirements.txt is in root folder
- Confirm app.py is in root folder
- Redeploy after pushing fixes to main
