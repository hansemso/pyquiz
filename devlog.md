# Devlog — PyQuiz (June 2026)

---

## Current Status

### Working Features

* [x] JSON card storage (`quiz_cards.json`)
* [x] Type I cards: multiline code + single-line QA pairs
* [x] Type II cards: multiline exercise + multiline answers + follow-up QA
* [x] Follow-up QA after Type II answers
* [x] PDF links per card (open via viewer)
* [x] Directory/Index system (topic ranges like 1–500 Python, 501–1000 JS)
* [x] Range selector for study sessions
* [x] Automatic shuffle for quiz cards
* [x] QA shuffle toggle per card
* [x] Instant grading per question
* [x] Score tracking with final results

---

## File Structure

```
PyQuiz
│
├── main.py
│   └── Main Menu Controller
│
├── cards.py
│   ├── Storage System
│   ├── Directory System
│   ├── Card Creation
│   ├── Card Editing
│   └── Validation Layer
│
├── quiz.py
│   ├── Quiz Range Selector
│   └── Quiz Engine
│
├── pdf_viewer.py
│   └── PDF Launching Utility
│
├── quiz_cards.json
│   └── Study card database
│
└── directory.txt
    └── Index mapping topics to ID ranges
```

---

## Program Flow

```
main.py
│
├── Quiz Range
│   └── run_quiz()
│
├── Add Card
│   └── add_study_card()
│
├── Edit Card
│   └── edit_card()
│
├── Edit Directory Note
│   └── edit_directory_note()
│
└── Exit
```

---

## Data Structures

### Type I Card

```json
{
  "type": "I",
  "id": "1",
  "code": "...",
  "qa": [],
  "pdf": null,
  "no_shuffle_qa": false
}
```

### Type II Card

```json
{
  "type": "II",
  "id": "50",
  "code": "...",
  "answer": "...",
  "followup_qa": [],
  "pdf": null,
  "no_shuffle_qa": false
}
```

---

## Core Modules

### cards.py — Data & Card System

Responsible for all card management.

#### Utility

* normalize()
* clean_answer()
* multiline_input()

#### Storage

* load_cards()
* save_all_cards()

#### Directory System

* load_directory_note()
* edit_directory_note()

#### Validation Layer

* sanitize_card()

  * Prevents missing keys
  * Fixes broken or incomplete cards
  * Ensures safe runtime behavior

#### Card Creation

* add_study_card()

  * Type I creation flow
  * Type II creation flow
  * Follow-up QA builder

#### Card Editing

* edit_card()

  * Select card
  * Modify fields
  * Delete cards
  * Toggle QA shuffle

#### Startup

* init() → load_cards()

---

### quiz.py — Quiz Engine

Handles all quiz execution and grading.

#### Core Engine

* run_quiz(cards_list)

Workflow:

* Filter valid cards
* Loop through cards
* Display code
* Optional PDF viewing
* Branch by card type

#### Type I Flow

* Shuffle QA (optional)
* Ask questions
* Grade answers

#### Type II Flow

* Multiline answer input
* Compare expected answer
* Grade result
* Follow-up QA loop

#### Quiz Range

* quiz_range()

  * Select ID range
  * Shuffle selection
  * Run quiz engine

---

### pdf_viewer.py

* Opens linked PDF files for a card
* Triggered during quiz when available

---

## Current Design Notes

* `study_bank` is the runtime working copy of all cards
* JSON file is only persistent storage
* Program never reads JSON directly except load/save
* All logic operates on in-memory data

---

## Architecture Summary

```
main.py → controls flow

cards.py → data + editing + storage

quiz.py → execution + grading

pdf_viewer.py → external file handling

JSON → persistent storage
```

---

## Future Ideas

* [ ] Search system for cards
* [ ] Tag system
* [ ] Difficulty levels
* [ ] Statistics dashboard
* [ ] Import/export system
* [ ] Backup system
* [ ] Spaced repetition algorithm

---

## Version History

### 2026-06-01

* Added Type II cards
* Added follow-up QA system
* Added answer normalization
* Added QA shuffle toggle
* Improved input safety handling
