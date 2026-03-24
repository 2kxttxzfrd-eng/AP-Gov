// ============================================================
//  AP Government Daily Practice – Application Logic
// ============================================================

(function () {
  "use strict";

  // ── Constants ──
  const QUESTIONS_PER_QUIZ = 20;
  const STORAGE_KEY = "apgov_progress";

  // ── DOM refs ──
  const screens = {
    home: document.getElementById("home-screen"),
    quiz: document.getElementById("quiz-screen"),
    results: document.getElementById("results-screen"),
    progress: document.getElementById("progress-screen"),
  };

  // Home
  const startBtn = document.getElementById("start-btn");
  const progressBtn = document.getElementById("progress-btn");
  const streakBanner = document.getElementById("streak-banner");
  const todayStatus = document.getElementById("today-status");

  // Quiz
  const questionCounter = document.getElementById("question-counter");
  const timerEl = document.getElementById("timer");
  const quizProgressBar = document.getElementById("quiz-progress-bar");
  const unitBadge = document.getElementById("unit-badge");
  const questionText = document.getElementById("question-text");
  const optionsContainer = document.getElementById("options");
  const prevBtn = document.getElementById("prev-btn");
  const nextBtn = document.getElementById("next-btn");
  const submitBtn = document.getElementById("submit-btn");

  // Results
  const scoreNumber = document.getElementById("score-number");
  const scorePercent = document.getElementById("score-percent");
  const scoreTime = document.getElementById("score-time");
  const unitBreakdown = document.getElementById("unit-breakdown");
  const reviewList = document.getElementById("review-list");
  const homeBtn = document.getElementById("home-btn");
  const retryBtn = document.getElementById("retry-btn");

  // Progress
  const backHomeBtn = document.getElementById("back-home-btn");
  const statTotalDays = document.getElementById("stat-total-days");
  const statAvgScore = document.getElementById("stat-avg-score");
  const statBestScore = document.getElementById("stat-best-score");
  const statStreak = document.getElementById("stat-streak");
  const unitPerformance = document.getElementById("unit-performance");
  const calendarHeatmap = document.getElementById("calendar-heatmap");
  const historyList = document.getElementById("history-list");
  const clearDataBtn = document.getElementById("clear-data-btn");

  // ── State ──
  let currentQuiz = []; // 20 question objects
  let userAnswers = []; // user selections (A/B/C/D or null)
  let currentIndex = 0;
  let timerInterval = null;
  let elapsedSeconds = 0;

  // ── Helpers ──
  function todayKey() {
    const d = new Date();
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
  }

  function showScreen(name) {
    Object.values(screens).forEach((s) => s.classList.remove("active"));
    screens[name].classList.add("active");
    window.scrollTo(0, 0);
  }

  function shuffle(arr) {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function loadProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY)) || { history: [] };
    } catch {
      return { history: [] };
    }
  }

  function saveProgress(data) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  }

  function getStreak(history) {
    if (!history.length) return 0;
    const sorted = [...history].sort((a, b) => b.date.localeCompare(a.date));
    let streak = 0;
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    let checkDate = new Date(today);

    // If today hasn't been done yet, start checking from yesterday
    if (!sorted.find(h => h.date === todayKey())) {
      checkDate.setDate(checkDate.getDate() - 1);
    }

    for (let i = 0; i < 365; i++) {
      const key = `${checkDate.getFullYear()}-${String(checkDate.getMonth() + 1).padStart(2, "0")}-${String(checkDate.getDate()).padStart(2, "0")}`;
      if (sorted.find(h => h.date === key)) {
        streak++;
        checkDate.setDate(checkDate.getDate() - 1);
      } else {
        break;
      }
    }
    return streak;
  }

  // ── Home Screen ──
  function renderHome() {
    const prog = loadProgress();
    const streak = getStreak(prog.history);

    if (streak > 0) {
      streakBanner.textContent = `🔥 ${streak}-day streak! Keep it going!`;
      streakBanner.classList.add("show");
    } else {
      streakBanner.classList.remove("show");
    }

    const todayDone = prog.history.find((h) => h.date === todayKey());
    if (todayDone) {
      todayStatus.innerHTML = `✅ Today's practice complete! Score: <strong>${todayDone.score}/${QUESTIONS_PER_QUIZ}</strong> (${Math.round((todayDone.score / QUESTIONS_PER_QUIZ) * 100)}%)`;
      todayStatus.classList.add("show");
      startBtn.textContent = "Practice Again";
    } else {
      todayStatus.classList.remove("show");
      startBtn.textContent = "Start Today's Practice";
    }
    showScreen("home");
  }

  // ── Quiz Logic ──
  function startQuiz() {
    currentQuiz = shuffle(QUESTION_BANK).slice(0, QUESTIONS_PER_QUIZ);
    userAnswers = new Array(QUESTIONS_PER_QUIZ).fill(null);
    currentIndex = 0;
    elapsedSeconds = 0;
    startTimer();
    renderQuestion();
    showScreen("quiz");
  }

  function startTimer() {
    clearInterval(timerInterval);
    timerInterval = setInterval(() => {
      elapsedSeconds++;
      const m = String(Math.floor(elapsedSeconds / 60)).padStart(2, "0");
      const s = String(elapsedSeconds % 60).padStart(2, "0");
      timerEl.textContent = `⏱ ${m}:${s}`;
    }, 1000);
  }

  function renderQuestion() {
    const q = currentQuiz[currentIndex];
    questionCounter.textContent = `Question ${currentIndex + 1} / ${QUESTIONS_PER_QUIZ}`;
    quizProgressBar.style.width = `${((currentIndex + 1) / QUESTIONS_PER_QUIZ) * 100}%`;
    unitBadge.textContent = `${q.unit}: ${q.unitName}`;
    questionText.textContent = q.question;

    const letters = ["A", "B", "C", "D"];
    optionsContainer.innerHTML = q.options
      .map(
        (opt, i) => `
      <button class="option-btn ${userAnswers[currentIndex] === letters[i] ? "selected" : ""}" data-letter="${letters[i]}">
        <span class="option-letter">${letters[i]}</span>
        <span>${opt}</span>
      </button>`
      )
      .join("");

    optionsContainer.querySelectorAll(".option-btn").forEach((btn) => {
      btn.addEventListener("click", () => selectOption(btn.dataset.letter));
    });

    prevBtn.disabled = currentIndex === 0;
    if (currentIndex === QUESTIONS_PER_QUIZ - 1) {
      nextBtn.style.display = "none";
      submitBtn.style.display = "";
    } else {
      nextBtn.style.display = "";
      submitBtn.style.display = "none";
    }
  }

  function selectOption(letter) {
    userAnswers[currentIndex] = letter;
    renderQuestion();
  }

  function submitQuiz() {
    clearInterval(timerInterval);
    let score = 0;
    const unitStats = {};

    currentQuiz.forEach((q, i) => {
      const correct = userAnswers[i] === q.answer;
      if (correct) score++;

      const key = q.unit;
      if (!unitStats[key]) unitStats[key] = { name: q.unitName, correct: 0, total: 0 };
      unitStats[key].total++;
      if (correct) unitStats[key].correct++;
    });

    // Save to progress
    const prog = loadProgress();
    prog.history.push({
      date: todayKey(),
      score,
      total: QUESTIONS_PER_QUIZ,
      time: elapsedSeconds,
      unitStats,
    });
    saveProgress(prog);

    renderResults(score, unitStats);
  }

  // ── Results ──
  function renderResults(score, unitStats) {
    scoreNumber.textContent = score;
    const pct = Math.round((score / QUESTIONS_PER_QUIZ) * 100);
    scorePercent.textContent = `${pct}%`;
    scorePercent.style.color = pct >= 70 ? "#4ade80" : pct >= 50 ? "#fbbf24" : "#f87171";

    const m = String(Math.floor(elapsedSeconds / 60)).padStart(2, "0");
    const s = String(elapsedSeconds % 60).padStart(2, "0");
    scoreTime.textContent = `Time: ${m}:${s}`;

    // Unit breakdown bars
    unitBreakdown.innerHTML = Object.entries(unitStats)
      .sort((a, b) => a[0].localeCompare(b[0]))
      .map(([unit, st]) => {
        const p = Math.round((st.correct / st.total) * 100);
        const cls = p >= 70 ? "green" : p >= 50 ? "yellow" : "red";
        return `<div class="unit-bar">
        <div class="unit-bar-label"><span>${unit}: ${st.name}</span><span>${st.correct}/${st.total}</span></div>
        <div class="unit-bar-track"><div class="unit-bar-fill ${cls}" style="width:${p}%"></div></div>
      </div>`;
      })
      .join("");

    // Review list
    const letters = ["A", "B", "C", "D"];
    reviewList.innerHTML = currentQuiz
      .map((q, i) => {
        const correct = userAnswers[i] === q.answer;
        const userAns = userAnswers[i] ? `${userAnswers[i]}) ${q.options[letters.indexOf(userAnswers[i])]}` : "No answer";
        const correctAns = `${q.answer}) ${q.options[letters.indexOf(q.answer)]}`;
        return `<div class="review-item ${correct ? "correct" : "wrong"}">
        <div class="review-q">${i + 1}. ${q.question}</div>
        <div class="review-answer">
          ${correct
            ? `<span class="label">Your answer: </span><span class="correct-text">${userAns} ✓</span>`
            : `<span class="label">Your answer: </span><span class="wrong-text">${userAns}</span><br/>
               <span class="label">Correct answer: </span><span class="correct-text">${correctAns}</span>`
          }
        </div>
        <div class="review-concept">📘 ${q.unit} · ${q.concept} — ${q.explanation}</div>
      </div>`;
      })
      .join("");

    showScreen("results");
  }

  // ── Progress Screen ──
  function renderProgress() {
    const prog = loadProgress();
    const hist = prog.history;

    // Stats
    const uniqueDays = [...new Set(hist.map((h) => h.date))].length;
    statTotalDays.textContent = uniqueDays;

    if (hist.length) {
      const avg = Math.round(hist.reduce((s, h) => s + (h.score / h.total) * 100, 0) / hist.length);
      statAvgScore.textContent = avg + "%";
      const best = Math.round(Math.max(...hist.map((h) => (h.score / h.total) * 100)));
      statBestScore.textContent = best + "%";
    } else {
      statAvgScore.textContent = "—";
      statBestScore.textContent = "—";
    }

    statStreak.textContent = getStreak(hist);

    // Unit performance (aggregate)
    const allUnits = {};
    hist.forEach((h) => {
      if (h.unitStats) {
        Object.entries(h.unitStats).forEach(([unit, st]) => {
          if (!allUnits[unit]) allUnits[unit] = { name: st.name, correct: 0, total: 0 };
          allUnits[unit].correct += st.correct;
          allUnits[unit].total += st.total;
        });
      }
    });
    unitPerformance.innerHTML = Object.entries(allUnits)
      .sort((a, b) => a[0].localeCompare(b[0]))
      .map(([unit, st]) => {
        const p = Math.round((st.correct / st.total) * 100);
        const cls = p >= 70 ? "green" : p >= 50 ? "yellow" : "red";
        return `<div class="unit-bar">
        <div class="unit-bar-label"><span>${unit}: ${st.name}</span><span>${p}% (${st.correct}/${st.total})</span></div>
        <div class="unit-bar-track"><div class="unit-bar-fill ${cls}" style="width:${p}%"></div></div>
      </div>`;
      })
      .join("") || '<p style="color:#9ca3af;">No data yet. Complete a practice to see results!</p>';

    // Calendar heatmap – last 30 days
    calendarHeatmap.innerHTML = "";
    const today = new Date();
    for (let i = 29; i >= 0; i--) {
      const d = new Date(today);
      d.setDate(d.getDate() - i);
      const key = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
      const dayEntries = hist.filter((h) => h.date === key);
      let level = 0;
      if (dayEntries.length) {
        const bestPct = Math.max(...dayEntries.map((e) => (e.score / e.total) * 100));
        if (bestPct >= 90) level = 4;
        else if (bestPct >= 70) level = 3;
        else if (bestPct >= 50) level = 2;
        else level = 1;
      }
      const dayEl = document.createElement("div");
      dayEl.className = `heatmap-day level-${level}`;
      dayEl.title = `${key}${dayEntries.length ? ` — Best: ${Math.round(Math.max(...dayEntries.map((e) => (e.score / e.total) * 100)))}%` : " — No practice"}`;
      calendarHeatmap.appendChild(dayEl);
    }

    // History list (last 15)
    const recent = [...hist].reverse().slice(0, 15);
    historyList.innerHTML = recent
      .map((h) => {
        const pct = Math.round((h.score / h.total) * 100);
        const cls = pct >= 70 ? "good" : pct >= 50 ? "ok" : "bad";
        const m = h.time ? `${Math.floor(h.time / 60)}m ${h.time % 60}s` : "";
        return `<div class="history-item">
        <span>${h.date}</span>
        <span class="history-score ${cls}">${h.score}/${h.total} (${pct}%) ${m ? "· " + m : ""}</span>
      </div>`;
      })
      .join("") || '<p style="color:#9ca3af;">No history yet.</p>';

    showScreen("progress");
  }

  // ── Event Listeners ──
  startBtn.addEventListener("click", startQuiz);
  retryBtn.addEventListener("click", startQuiz);
  progressBtn.addEventListener("click", renderProgress);

  prevBtn.addEventListener("click", () => {
    if (currentIndex > 0) { currentIndex--; renderQuestion(); }
  });
  nextBtn.addEventListener("click", () => {
    if (currentIndex < QUESTIONS_PER_QUIZ - 1) { currentIndex++; renderQuestion(); }
  });
  submitBtn.addEventListener("click", () => {
    const unanswered = userAnswers.filter((a) => a === null).length;
    if (unanswered > 0) {
      if (!confirm(`You have ${unanswered} unanswered question${unanswered > 1 ? "s" : ""}. Submit anyway?`)) return;
    }
    submitQuiz();
  });

  homeBtn.addEventListener("click", renderHome);
  backHomeBtn.addEventListener("click", renderHome);

  clearDataBtn.addEventListener("click", () => {
    if (confirm("Are you sure you want to clear all progress data? This cannot be undone.")) {
      localStorage.removeItem(STORAGE_KEY);
      renderProgress();
    }
  });

  // ── Keyboard navigation ──
  document.addEventListener("keydown", (e) => {
    if (!screens.quiz.classList.contains("active")) return;
    if (e.key === "ArrowRight" || e.key === "d") {
      if (currentIndex < QUESTIONS_PER_QUIZ - 1) { currentIndex++; renderQuestion(); }
    } else if (e.key === "ArrowLeft" || e.key === "a") {
      if (currentIndex > 0) { currentIndex--; renderQuestion(); }
    } else if (["1", "2", "3", "4"].includes(e.key)) {
      selectOption(["A", "B", "C", "D"][parseInt(e.key) - 1]);
    }
  });

  // ── Init ──
  renderHome();
})();
