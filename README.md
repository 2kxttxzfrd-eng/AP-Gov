# 🏛️ AP Government Daily Practice

A Streamlit web app for daily AP U.S. Government & Politics exam practice.

## Features
- **20-question mock quizzes** randomly selected from 100+ questions
- **Timed practice** with stopwatch
- **All 5 AP Gov units** covered:
  - Unit 1: Foundations of American Democracy
  - Unit 2: Interactions Among Branches
  - Unit 3: Civil Liberties and Civil Rights
  - Unit 4: American Political Ideologies and Beliefs
  - Unit 5: Political Participation
- **Instant results** with score, unit breakdown, and detailed answer review
- **Concept & explanation** shown for every question (unit, topic, and why the answer is correct)
- **Progress tracking** — daily streak, average/best scores, unit performance, 30-day heatmap
- **Light theme** with clean, modern UI

## Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install streamlit

# Run the app
streamlit run ap_gov_app.py
```

Then open **http://localhost:8501** in your browser.

## Tech Stack
- Python 3.12+
- Streamlit
- JSON file for progress persistence
