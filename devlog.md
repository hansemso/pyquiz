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

### Synopsis

```
Triangular design with main.py at top as access. cards.py = data logic(biggest file); quiz.py = runtime logic(selecting, filtering, shuffling).   

```

PyQuiz
│
├── main.py
│   │
│   └── Main Menu
│       │
│       ├── 1. Quiz Range
│       │       └── quiz.quiz_range()  # Listed in directory which user can modify. Groups cards into topics.
│       │
│       ├── 2. Add Card
│       │       └── cards.add_study_card()
│       │
│       ├── 3. Edit Card / View Index
│       │       └── cards.edit_card()  # Select by ID num ➜ cards.py below ➜ edit mode
│       │
│       ├── 4. Edit Directory Note
│       │       └── cards.edit_directory_note()  # Stores directory in txt file. Just for user to view.
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
│   │       ├── Type I  #multiline problem, single-line qa's
│   │       └── Type II  #multiline problem and answer with extra single-line qa's
│   │
│   ├── Card Editing
│   │   │
│   │   └── edit_card()
│   │       ├── Edit Code  # multiline
│   │       ├── Edit QA  #edit qa in pairs, type 'a' to keep adding
│   │       ├── Edit PDF  # Link to pdf. View with foxit. Store in \notes
│   │       ├── Change ID  # In case need to shuffle across ranges
│   │       ├── Delete Card
│   │       └── Toggle QA Shuffle  # y/n exempts select cards from auto shuffle
│   │
│   └── Startup
│       └── init()  #loads from json into study_bank
│
├── quiz.py
│   │
│   ├── quiz_range()
│   │   │
│   │   ├── User enters ID range ➜ Filter study_bank ➜ Shuffle
│   │   └── run_quiz()
│   │
│   └── Quiz Engine
│       │
│       └── run_quiz()
│           │
│           ├── Display multiline problem(sample code or other)
│           ├── Optional PDF launch(User enters [p])
│           │
│           ├── Type I Processing
│           │   │
│           │   ├── Read qa list
│           │   └── Check no_shuffle_qa ➜ If True, cancel auto shuffle, preserve order
│           │
│           ├── Ask QA ➜ Grade answers ➜ Track score
│           │
│           ├── Type II Processing
│           │   └── Multiline answer ➜ Grade answer ➜ Follow-up QA
│           │
│           └── Final Score
│
├── pdf_viewer.py ➜ PDF Launching System ➜ open_from_card()
│
├── directory.txt ➜ User-maintained study/index notes
│                                                   ┌──  Type I
└── quiz_cards.json ➜ Persistent Card Storage  ────┤
                                                    └──  Type II
        
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
quiz_range() ➜ Select Start ID ➜ Select End ID ➜ Filter study_bank ➜ Selected Cards ⏎
 │
 ▼
(random.shuffle(filtered))  # runs on auto for all cards, shutoff per card in Edit
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
 ├───────────────────────┬
 │                       │
 ▼                       ▼
Type I                Type II
 │                       │
 ▼                       ▼
Singleline QA's    Multiline Answer
 │                       │
 ▼                       ▼
 └──  shuffle(y/n)     ──┘
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
      session ➜ grading ➜ next card ➜ final score
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





