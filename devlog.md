# devlog  ...for pyquiz June 2026

## Current Status

Working Features
----------------
- [x] Runs on Python 3.xx and terminal for ruggedness, expandability, and easier debugging
- [x] JSON card storage: quiz_cards.json
- [x] Type I cards: multiline display with single line qa's in pairs. Use display for example code and qa's for questions about it.
- [x] Type II cards: multiline display with multiline answer and extra single line Follow-up qa's. Good for making coding exercises.
- [x] Follow-up QA: After multi-line answer, add extra single line questions to answer about the problem
- [x] PDF links: Link problem to pdf by popup. Make in googledocs, download as pdf, open with foxit per card to help.
- [x] Directory/Index: Lists types of questions by range. Ex: 1-500: Python, 501-1000: Javascript
- [x] Range selector: Select the range to study. App will load and auto shuffle cards in that range.
- [x] QA shuffle toggle: Turn off auto shuffle for certain cards, e.g. cards with non-random QA's.
- [x] Instant grading: Checks answer per problem.
- [x] Score tracking: Keep track of score, give final score at end.

---

## File Structure --overall

```
PyQuiz
│
├── main.py
│   │
│   └── Main Menu
│       │
│       ├── 1. Quiz Range
│       │       └── quiz.quiz_range()
│       │
│       ├── 2. Add Card
│       │       └── cards.add_study_card()
│       │
│       ├── 3. Edit Card / View Index
│       │       └── cards.edit_card()
│       │
│       ├── 4. Edit Directory Note
│       │       └── cards.edit_directory_note()
│       │
│       └── 5. Exit
│
├── cards.py
│   │
│   ├── Global Working Memory
│   │   └── study_bank
│   │       └── Active card collection loaded into RAM
│   │
│   ├── Utility Functions
│   │   ├── normalize()
│   │   ├── clean_answer()
│   │   └── multiline_input()
│   │
│   ├── Directory / Index System
│   │   │
│   │   ├── directory.txt
│   │   │
│   │   ├── load_directory_note()
│   │   └── edit_directory_note()
│   │
│   ├── Validation Layer
│   │   │
│   │   └── sanitize_card()
│   │       ├── verify structure
│   │       ├── repair missing fields
│   │       ├── clean answers
│   │       └── validate followup QA
│   │
│   ├── Storage Layer
│   │   │
│   │   ├── load_cards()
│   │   │   └── quiz_cards.json
│   │   │
│   │   └── save_all_cards()
│   │       └── quiz_cards.json
│   │
│   ├── Card Creation
│   │   │
│   │   └── add_study_card()
│   │       ├── Type I
│   │       └── Type II
│   │
│   ├── Card Editing
│   │   │
│   │   └── edit_card()
│   │       ├── Edit Code
│   │       ├── Edit QA
│   │       ├── Edit PDF
│   │       ├── Change ID
│   │       ├── Delete Card
│   │       └── Toggle QA Shuffle
│   │
│   └── Startup
│       └── init()
│
├── quiz.py
│   │
│   ├── quiz_range()
│   │   │
│   │   ├── User enters ID range
│   │   ├── Filter study_bank
│   │   ├── Shuffle card order
│   │   └── run_quiz()
│   │
│   └── Quiz Engine
│       │
│       └── run_quiz()
│           │
│           ├── Display code block
│           ├── Optional PDF launch
│           │
│           ├── Type I Processing
│           │   │
│           │   ├── Read qa list
│           │   ├── Check no_shuffle_qa
│           │   │
│           │   ├── False
│           │   │     └── random.shuffle(qa_list)
│           │   │
│           │   └── True
│           │         └── Preserve order
│           │
│           ├── Ask QA
│           ├── Grade answers
│           └── Track score
│           │
│           ├── Type II Processing
│           │   ├── Multiline answer
│           │   ├── Grade answer
│           │   └── Follow-up QA
│           │
│           └── Final Score
│
├── pdf_viewer.py
│   │
│   └── PDF Launching System
│       └── open_from_card()
│
├── directory.txt
│   │
│   └── User-maintained study/index notes
│
└── quiz_cards.json
    │
    └── Persistent Card Storage
        │
        ├── Type I
        │   ├── id
        │   ├── code
        │   ├── qa
        │   ├── pdf
        │   └── no_shuffle_qa
        │
        └── Type II
            ├── id
            ├── code
            ├── answer
            ├── pdf
            ├── followup_qa
            └── no_shuffle_qa
```

### Shuffle Logic
```
User
 │
 ▼
Main Menu
 │
 ▼
Quiz Range
 │
 ▼
quiz_range()
 │
 ├── Select Start ID
 ├── Select End ID
 │
 ▼
Filter study_bank
 │
 ▼
Selected Cards
 │
 ▼
Shuffle Card Order
(random.shuffle(filtered))
 │
 ▼
run_quiz()
 │
 ▼
Current Card
 │
 ├── Display Code
 ├── Optional PDF
 │
 ▼
Card Type?
 │
 ├───────────────┬────────────────
 │               │
 ▼               ▼
Type I          Type II
 │               │
 ▼               ▼
Read QA      Multiline Answer
 │               │
 ▼               ▼
Check no_shuffle_qa
 │
 ┌───────┴────────┐
 │                │
 ▼                ▼
False            True
(auto)          (exempt)
 │                │
 ▼                ▼
Shuffle QA      Keep QA Order
 │                │
 └───────┬────────┘
         │
         ▼
    Ask Questions
         │
         ▼
      Grade
         │
         ▼
     Next Card
         │
         ▼
    Final Score
```



## Data Structure

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





