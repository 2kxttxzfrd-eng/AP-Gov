"""
AP U.S. Government & Politics – Daily Practice App (Streamlit)
"""

import streamlit as st
import random
import json
import os
from datetime import datetime, timedelta
from question_bank import QUESTION_BANK

# ──────────────────────────────────────────────
#  Configuration
# ──────────────────────────────────────────────
QUESTIONS_PER_QUIZ = 25
LETTERS = ["A", "B", "C", "D"]
PROGRESS_FILE = "progress.json"
UNIT_NAMES = {
    "All Units": "All Units",
    "Unit 1": "Foundations of American Democracy",
    "Unit 2": "Interactions Among Branches",
    "Unit 3": "Civil Liberties and Civil Rights",
    "Unit 4": "American Political Ideologies and Beliefs",
    "Unit 5": "Political Participation",
}
UNIT_OPTIONS = list(UNIT_NAMES.keys())


# ──────────────────────────────────────────────
#  Persistence helpers  (JSON file on disk)
# ──────────────────────────────────────────────
def _progress_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), PROGRESS_FILE)

def load_progress():
    path = _progress_path()
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {"history": []}

def save_progress(data):
    with open(_progress_path(), "w") as f:
        json.dump(data, f, indent=2)

def today_key():
    return datetime.now().strftime("%Y-%m-%d")

def get_streak(history):
    if not history:
        return 0
    dates = sorted(set(h["date"] for h in history), reverse=True)
    streak = 0
    check = datetime.now().date()
    if today_key() not in dates:
        check -= timedelta(days=1)
    for _ in range(365):
        if check.strftime("%Y-%m-%d") in dates:
            streak += 1
            check -= timedelta(days=1)
        else:
            break
    return streak


# ──────────────────────────────────────────────
#  Page config
# ──────────────────────────────────────────────
st.set_page_config(page_title="AP Gov Daily Practice", page_icon="🏛️", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #f0f4ff, #e8ecf8, #f5f7ff); }
    div[data-testid="stMainBlockContainer"] { max-width: 780px; }
    .big-score { text-align:center; font-size:3.5rem; font-weight:800; color:#059669; margin:0; }
    .score-sub { text-align:center; font-size:1.2rem; color:#4f46e5; }
    .unit-tag { display:inline-block; padding:2px 10px; border-radius:12px; font-size:0.78rem;
                background:rgba(99,102,241,0.12); color:#4f46e5; margin-bottom:6px; }
    .correct-box { border-left:4px solid #22c55e; padding:12px; border-radius:8px;
                   background:rgba(34,197,94,0.08); margin-bottom:10px; color:#1e293b; }
    .wrong-box  { border-left:4px solid #ef4444; padding:12px; border-radius:8px;
                   background:rgba(239,68,68,0.06); margin-bottom:10px; color:#1e293b; }
    .concept-tag { font-size:0.82rem; padding:4px 8px; border-radius:6px;
                   background:rgba(99,102,241,0.1); color:#4338ca; display:inline-block; margin-top:6px; }
    h1, h2, h3 { color: #1e293b !important; }
    p, span, label, div { color: #334155; }
    div[data-testid="stMetricValue"] { color: #4f46e5 !important; }
    div[data-testid="stMetricLabel"] { color: #64748b !important; }
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
#  Session state init
# ──────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"
if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = []
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "selected_unit" not in st.session_state:
    st.session_state.selected_unit = "All Units"


# ──────────────────────────────────────────────
#  Navigation helpers
# ──────────────────────────────────────────────
def go_home():
    st.session_state.page = "home"
    st.session_state.quiz_submitted = False
    st.session_state.answers = {}

def start_quiz():
    unit = st.session_state.selected_unit
    if unit == "All Units":
        pool = QUESTION_BANK
    else:
        pool = [q for q in QUESTION_BANK if q["unit"] == unit]
    count = min(QUESTIONS_PER_QUIZ, len(pool))
    questions = random.sample(pool, count)
    st.session_state.quiz_questions = questions
    st.session_state.answers = {}
    st.session_state.quiz_submitted = False
    st.session_state.start_time = datetime.now()
    st.session_state.page = "quiz"

def go_progress():
    st.session_state.page = "progress"


# ──────────────────────────────────────────────
#  HOME PAGE
# ──────────────────────────────────────────────
def render_home():
    prog = load_progress()
    streak = get_streak(prog["history"])

    st.markdown("<div style='text-align:center;font-size:64px;margin-top:20px;'>🏛️</div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;margin:0;color:#1e293b;'>AP Government<br><span style='background:linear-gradient(90deg,#059669,#3b82f6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;'>Daily Practice</span></h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;color:#64748b;'>{QUESTIONS_PER_QUIZ} questions from a bank of {len(QUESTION_BANK)} · Timed · Track your progress</p>", unsafe_allow_html=True)

    if streak > 0:
        st.success(f"🔥 **{streak}-day streak!** Keep it going!")

    today_done = [h for h in prog["history"] if h["date"] == today_key()]
    if today_done:
        best = max(today_done, key=lambda h: h["score"])
        pct = round(best["score"] / best["total"] * 100)
        st.info(f"✅ Today's practice complete! Best score: **{best['score']}/{best['total']}** ({pct}%)")

    st.markdown("")
    # Unit selector
    st.markdown("#### 📚 Choose Your Practice")
    unit_labels = [f"🌐 {k}" if k == "All Units" else f"📖 {k}: {UNIT_NAMES[k]}" for k in UNIT_OPTIONS]
    selected_idx = UNIT_OPTIONS.index(st.session_state.selected_unit)
    chosen = st.radio(
        "Select a unit to practice:",
        UNIT_OPTIONS,
        index=selected_idx,
        format_func=lambda k: f"🌐 {k}" if k == "All Units" else f"📖 {k}: {UNIT_NAMES[k]}",
        key="unit_selector",
        label_visibility="collapsed",
    )
    st.session_state.selected_unit = chosen

    # Show pool size for selected unit
    if chosen == "All Units":
        pool_size = len(QUESTION_BANK)
    else:
        pool_size = sum(1 for q in QUESTION_BANK if q["unit"] == chosen)
    quiz_count = min(QUESTIONS_PER_QUIZ, pool_size)
    st.caption(f"📝 {quiz_count} questions will be drawn from {pool_size} available")

    st.markdown("")
    col1, col2 = st.columns(2)
    with col1:
        label = "Practice Again" if today_done else "🚀 Start Today's Practice"
        st.button(label, on_click=start_quiz, use_container_width=True, type="primary")
    with col2:
        st.button("📊 View Progress", on_click=go_progress, use_container_width=True)


# ──────────────────────────────────────────────
#  QUIZ PAGE
# ──────────────────────────────────────────────
def render_quiz():
    questions = st.session_state.quiz_questions
    total_q = len(questions)

    if st.session_state.quiz_submitted:
        render_results()
        return

    # Unit label
    unit = st.session_state.selected_unit
    unit_label = "All Units" if unit == "All Units" else f"{unit}: {UNIT_NAMES[unit]}"
    st.markdown(f"**📚 Practicing: {unit_label}**")

    # Timer display
    if st.session_state.start_time:
        elapsed = (datetime.now() - st.session_state.start_time).seconds
        mins, secs = divmod(elapsed, 60)
        st.markdown(f"⏱ Time elapsed: **{mins:02d}:{secs:02d}**")

    # Progress
    answered = sum(1 for q in questions if q["id"] in st.session_state.answers)
    st.progress(answered / total_q, text=f"Answered {answered} / {total_q}")

    # Render each question
    for i, q in enumerate(questions):
        with st.container():
            st.markdown(f"<span class='unit-tag'>{q['unit']}: {q['unitName']}</span>", unsafe_allow_html=True)
            st.markdown(f"**Q{i+1}.** {q['question']}")
            key = f"q_{q['id']}"
            options_with_letters = [f"{LETTERS[j]}) {opt}" for j, opt in enumerate(q["options"])]

            prev = st.session_state.answers.get(q["id"])
            prev_index = LETTERS.index(prev) if prev else None

            choice = st.radio(
                "Select your answer:",
                options_with_letters,
                index=prev_index,
                key=key,
                label_visibility="collapsed",
            )
            if choice:
                letter = choice[0]
                st.session_state.answers[q["id"]] = letter
            st.divider()

    # Submit
    unanswered = total_q - len(st.session_state.answers)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("🏠 Back to Home", on_click=go_home, use_container_width=True)
    with col2:
        if unanswered > 0:
            st.warning(f"{unanswered} question(s) unanswered")
        if st.button("✅ Submit Answers", use_container_width=True, type="primary"):
            st.session_state.quiz_submitted = True
            st.rerun()


# ──────────────────────────────────────────────
#  RESULTS PAGE
# ──────────────────────────────────────────────
def render_results():
    questions = st.session_state.quiz_questions
    total_q = len(questions)
    answers = st.session_state.answers
    elapsed = (datetime.now() - st.session_state.start_time).seconds if st.session_state.start_time else 0

    # Calculate score
    score = 0
    unit_stats = {}
    for q in questions:
        correct = answers.get(q["id"]) == q["answer"]
        if correct:
            score += 1
        u = q["unit"]
        if u not in unit_stats:
            unit_stats[u] = {"name": q["unitName"], "correct": 0, "total": 0}
        unit_stats[u]["total"] += 1
        if correct:
            unit_stats[u]["correct"] += 1

    # Save progress
    prog = load_progress()
    prog["history"].append({
        "date": today_key(),
        "score": score,
        "total": total_q,
        "time": elapsed,
        "unitStats": unit_stats,
    })
    save_progress(prog)

    # Display score
    pct = round(score / total_q * 100)
    mins, secs = divmod(elapsed, 60)

    st.markdown("## 🎉 Practice Complete!")
    st.markdown(f"<p class='big-score'>{score} / {total_q}</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='score-sub'>{pct}% · Time: {mins:02d}:{secs:02d}</p>", unsafe_allow_html=True)
    st.markdown("")

    # AP Score estimate
    if pct >= 80:
        st.success("🏆 Excellent! You're on track for a 5!")
    elif pct >= 65:
        st.info("👍 Good job! Aim for a 4 or 5.")
    elif pct >= 50:
        st.warning("📚 Keep studying — you can improve!")
    else:
        st.error("💪 Don't give up! Review the concepts below.")

    # Unit breakdown
    st.markdown("### 📊 Unit Breakdown")
    for unit_key in sorted(unit_stats.keys()):
        us = unit_stats[unit_key]
        upct = round(us["correct"] / us["total"] * 100) if us["total"] else 0
        label = f"{unit_key}: {us['name']}  —  {us['correct']}/{us['total']} ({upct}%)"
        st.progress(upct / 100, text=label)

    # Review answers
    st.markdown("### 📝 Review Answers")
    for i, q in enumerate(questions):
        user_ans = answers.get(q["id"])
        correct = user_ans == q["answer"]
        correct_letter = q["answer"]
        correct_idx = LETTERS.index(correct_letter)
        user_idx = LETTERS.index(user_ans) if user_ans else None

        css_class = "correct-box" if correct else "wrong-box"
        icon = "✅" if correct else "❌"

        user_text = f"{user_ans}) {q['options'][user_idx]}" if user_ans else "No answer"
        correct_text = f"{correct_letter}) {q['options'][correct_idx]}"

        html = f"<div class='{css_class}'>"
        html += f"<strong>{icon} Q{i+1}.</strong> {q['question']}<br>"
        if correct:
            html += f"<span style='color:#16a34a;'>Your answer: {user_text}</span><br>"
        else:
            html += f"<span style='color:#dc2626;text-decoration:line-through;'>Your answer: {user_text}</span><br>"
            html += f"<span style='color:#16a34a;'>Correct: {correct_text}</span><br>"
        html += f"<span class='concept-tag'>📘 {q['unit']} · {q['concept']} — {q['explanation']}</span>"
        html += "</div>"
        st.markdown(html, unsafe_allow_html=True)

    st.markdown("")
    col1, col2 = st.columns(2)
    with col1:
        st.button("🏠 Back to Home", on_click=go_home, use_container_width=True)
    with col2:
        st.button("🔄 Practice Again", on_click=start_quiz, use_container_width=True, type="primary")


# ──────────────────────────────────────────────
#  PROGRESS PAGE
# ──────────────────────────────────────────────
def render_progress():
    prog = load_progress()
    hist = prog["history"]

    st.button("← Back to Home", on_click=go_home)
    st.markdown("## 📊 Your Progress")

    if not hist:
        st.info("No practice history yet. Complete a quiz to see your progress!")
        return

    # Stats
    unique_days = len(set(h["date"] for h in hist))
    avg_pct = round(sum(h["score"] / h["total"] * 100 for h in hist) / len(hist))
    best_pct = round(max(h["score"] / h["total"] * 100 for h in hist))
    streak = get_streak(hist)
    bonus_points = sum(1 for h in hist if round(h["score"] / h["total"] * 100) >= 90)

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Days Practiced", unique_days)
    col2.metric("Average Score", f"{avg_pct}%")
    col3.metric("Best Score", f"{best_pct}%")
    col4.metric("Day Streak 🔥", streak)
    col5.metric("Bonus Points ⭐", bonus_points)

    # Unit Performance (aggregate)
    st.markdown("### 📈 Unit Performance (All Time)")
    all_units = {}
    for h in hist:
        if "unitStats" in h:
            for unit_key, us in h["unitStats"].items():
                if unit_key not in all_units:
                    all_units[unit_key] = {"name": us["name"], "correct": 0, "total": 0}
                all_units[unit_key]["correct"] += us["correct"]
                all_units[unit_key]["total"] += us["total"]

    if all_units:
        for unit_key in sorted(all_units.keys()):
            us = all_units[unit_key]
            upct = round(us["correct"] / us["total"] * 100) if us["total"] else 0
            label = f"{unit_key}: {us['name']}  —  {us['correct']}/{us['total']} ({upct}%)"
            st.progress(upct / 100, text=label)

    # Heatmap (last 30 days)
    st.markdown("### 🗓️ Last 30 Days")
    today = datetime.now().date()
    dates_scores = {}
    for h in hist:
        d = h["date"]
        pct = round(h["score"] / h["total"] * 100)
        if d not in dates_scores or pct > dates_scores[d]:
            dates_scores[d] = pct

    cols = st.columns(15)
    for i in range(30):
        d = (today - timedelta(days=29 - i)).strftime("%Y-%m-%d")
        col = cols[i % 15]
        if d in dates_scores:
            p = dates_scores[d]
            if p >= 90:
                color = "#22c55e"
            elif p >= 70:
                color = "#4ade80"
            elif p >= 50:
                color = "#fbbf24"
            else:
                color = "#f87171"
            col.markdown(
                f"<div title='{d}: {p}%' style='width:28px;height:28px;border-radius:5px;background:{color};margin:2px auto;'></div>",
                unsafe_allow_html=True,
            )
        else:
            col.markdown(
                f"<div title='{d}: No practice' style='width:28px;height:28px;border-radius:5px;background:rgba(0,0,0,0.06);margin:2px auto;'></div>",
                unsafe_allow_html=True,
            )

    # History list
    st.markdown("### 📋 Recent Sessions")
    for h in reversed(hist[-15:]):
        pct = round(h["score"] / h["total"] * 100)
        mins, secs = divmod(h.get("time", 0), 60)
        if pct >= 70:
            icon = "🟢"
        elif pct >= 50:
            icon = "🟡"
        else:
            icon = "🔴"
        bonus = " ⭐ +1 bonus" if pct >= 90 else ""
        st.markdown(f"{icon} **{h['date']}** — {h['score']}/{h['total']} ({pct}%)  ⏱ {mins}m {secs}s{bonus}")

    # Clear data
    st.markdown("---")
    if st.button("🗑️ Clear All Data", type="secondary"):
        save_progress({"history": []})
        st.rerun()


# ──────────────────────────────────────────────
#  Router
# ──────────────────────────────────────────────
page = st.session_state.page
if page == "home":
    render_home()
elif page == "quiz":
    render_quiz()
elif page == "progress":
    render_progress()
