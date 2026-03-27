<<<<<<< HEAD
# 📚 han_data

## 🎯 Overview

# PyQuiz Data Analysis

This folder contains analytics scripts for studying quiz performance data.

The main PyQuiz application records quiz attempts in a SQLite database (`quiz.db`).
These scripts analyze that data to measure learning progress and difficulty.

Scripts included:

• bayes_query.py  
Computes probability of answering a card correctly based on past results.

• prog_over_time.py  
Shows learning progress across quiz sessions.

• quiz_results.py  
Helper functions for recording quiz attempts.

The analytics layer is designed to demonstrate simple data analysis workflows
using Python, JSON data, and SQLite.
=======
# 📚 Pyquiz CLI Study App

## 🎯 Overview

**Pyquiz CLI Study App** is a simple Python command-line flashcard quiz tool that helps you practice programming concepts using JSON-based persistent storage.

Features:

* ✅ Fully modularized structure for easy debugging and modification
* ✅ Add/Edit questions and/or answers in each card
* ✅ Example multi-line code displayed with questions groupable below it
* ✅ Random card shuffle on auto
* ✅ Instant grading feedback per problem, total result at end
* ✅ Card range selector,e.g. 1-1000 for Python, 1001-2000 for biology quiz.
* ✅ Local JSON storage
* ✅ Can connect to sql and add data analysis scripts


---

## 📥 Installation

### 1. Clone the Repository

Open terminal and run:

```bash
git clone https://github.com/hansemso/pyquiz.git
```

Enter project folder:

```bash
cd pyquiz
```

---

### 2. Install Python (If Needed)

Make sure Python 3 is installed.

Check version:

```bash
python --version
```

---

### 3. Run the Application

Start the quiz app with:

```bash
py main.py
```

## 🧠 How to Use
1. py main.py to start app. 

### ⭐ Add/EDIT Study Cards

1. Choose **Add Card** from menu
2. Enter question and answer
3. Choose **Edit Card** from menu. (Select item number first if needed to make change)

---

### ⭐ Start Studying

1. Answer questions
3. Receive instant scoring feedback

---

## 💾 Data Storage

* Study cards are stored locally in JSON format.
* Your progress is saved automatically.

---

## 🛠 Technology Stack

* Python
* CLI Interface
* JSON Persistence

---

## 🌐 Repository

Source code:

👉 https://github.com/hansemso/pyquiz


## 📜 File Structure
```
pyquiz/
├── main.py           # Main menu + program entry point
├── quiz.py           # Quiz logic (run_quiz, quiz_mode, quiz_range)
├── cards.py          # Card storage and JSON read/write
├── db.py             # SQLite logging (log_quiz_result)
├── quiz_cards.json   # Your card database
└── han_data/         # Data analysis apps [[[In Progress]]]
    └── quiz.db       # SQLite DB
```
>>>>>>> 6155ead (Update README and gitignore)
