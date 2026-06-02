# devlog  ...for pyquiz June 2026

## Current Status

Working Features
----------------
[x] JSON card storage: quiz_cards.json
[x] Type I cards: multiline display with single line qa's in pairs. Use display for example code and qa's for questions about it. 
[x] Type II cards: multiline display with multiline answer and extra single line Follow-up qa's. Good for making coding exercises. 
[x] Follow-up QA: After multi-line answer, add extra single line questions to answer about the problem
[x] PDF links: Link problem to pdf by popup. Make in googledocs, download as pdf, open with foxit per card to help. 
[x] Directory/Index: Lists types of questions by range. Ex: 1-500: Python, 501-1000: Javascript
[x] Range selector: Select the range to study. App will load and auto shuffle cards in that range. 
[x] QA shuffle toggle: Turn off auto shuffle for certain cards, e.g. cards with non-random QA's. 
[x] Instant grading: Checks answer per problem.
[x] Score tracking: Keep track of score, give final score at end.

--------------------------------------------

## File Structure

PyQuiz
│
├── main.py
│   └── Main Menu
│
├── cards.py
│   ├── Storage System
│   ├── Directory System
│   ├── Card Creation
│   ├── Card Editing
│   └── Validation
│
├── quiz.py
│   ├── Quiz Range Selection
│   └── Quiz Engine
│
└── pdf_viewer.py
    └── PDF Launching

### main.py

Main Menu
├── 1. Quiz Range ➜ quiz.quiz_range()
├── 2. Add Card ➜ cards.add_study_card()
├── 3. Edit Card/View Index ➜ cards.edit_card()
├── 4. Edit Index Directory ➜ cards.edit_directory_note()
└── 5. Exit 

Program startup

### cards.py

cards.py
│
├── Global Data
│   └── study_bank ⇒ Working copy in RAM while the program runs
│
├── Utility
│   ├── normalize()
│   ├── clean_answer()
│   └── multiline_input()
│
├── Directory / Index System
│   │
│   ├── DIRECTORY_FILE
│   │
│   ├── load_directory_note()
│   │   ├── Read directory.txt
│   │   └── Create default if missing
│   │
│   └── edit_directory_note()
│       ├── Display current note
│       ├── Multiline edit
│       └── Save directory.txt
│
├── Card Safety / Validation
│   │
│   └── sanitize_card()
│       ├── Verify card is dict
│       ├── Add missing fields
│       ├── Fix None values
│       ├── Validate followup_qa
│       └── Clean answer text
│
├── File Storage
│   │
│   ├── load_cards()
│   │   ├── Open quiz_cards.json
│   │   ├── Read JSON
│   │   ├── sanitize_card()
│   │   └── Populate study_bank
│   │
│   └── save_all_cards()
│       └── Write study_bank to JSON
│
├── Card Creation System
│   │
│   └── add_study_card()
│       │
│       ├── Select Type
│       │   ├── Type I
│       │   └── Type II
│       │
│       ├── Enter ID
│       ├── Check duplicate ID
│       ├── Enter code
│       │
│       ├── Type I Branch
│       │   ├── Enter QA pairs
│       │   ├── Enter PDF
│       │   ├── Create card
│       │   └── Save
│       │
│       └── Type II Branch
│           ├── Enter answer
│           ├── Enter PDF
│           ├── Enter follow-up QA
│           ├── Create card
│           └── Save
│
├── Card Editing System
│   │
│   └── edit_card()
│       │
│       ├── Verify cards exist
│       ├── Sort cards by ID
│       ├── Display index
│       ├── Select card
│       ├── sanitize_card()
│       │
│       └── Edit Menu
│           ├── Edit code
│           ├── Edit QA
│           ├── Edit pdf link
│           ├── Change ID
│           ├── Delete card
│           ├── Toggle QA shuffle
│           └── Cancel
│
└── Startup
    └── init()
        └── load_cards()

    Card storage: Has all the logic for manipulating cards. Biggest file in app. 
    Add card
    Edit card: 1. Added subroutine to continuously add qa's without exiting mode. 2. Terminate adding new code or qa's by entering "END". 3. Worked on preventing crashes due to bugs by input logic.   
    Save/load JSON: Automatically updates, should never have to be opened. Had connected to sql, gre...but decided best to keep it simple with json for long-term personal use.
    Directory note

### quiz.py

quiz.py
│
├── Imports
│   ├── random
│   ├── cards
│   ├── pdf_viewer
│   └── multiline_input
│
├── Quiz Engine
│   │
│   └── run_quiz(cards_list)
│       │
│       ├── Initialize score
│       │   ├── score = 0
│       │   └── total = 0
│       │
│       ├── Filter valid cards
│       │   ├── Type I with QA
│       │   └── Type II
│       │
│       ├── Empty quiz check
│       │
│       └── For each card
│           │
│           ├── Display code
│           │
│           ├── PDF System
│           │   ├── Check pdf exists
│           │   ├── Ask user
│           │   └── Open PDF
│           │
│           ├── Determine card type
│           │
│           ├── Type II Branch
│           │   │
│           │   ├── Multiline answer input
│           │   ├── Compare answer
│           │   ├── Grade answer
│           │   ├── Display expected answer
│           │   │
│           │   └── Follow-up QA Loop
│           │       ├── Ask question
│           │       ├── Grade answer
│           │       └── Update score
│           │
│           └── Type I Branch
│               │
│               ├── Copy QA list
│               ├── Shuffle QA (optional)
│               │
│               └── QA Loop
│                   ├── Ask question
│                   ├── Grade answer
│                   └── Update score
│
│       └── Print Final Score
│
└── Quiz Range Selector
    │
    └── quiz_range()
        │
        ├── Input start ID
        ├── Input end ID
        ├── Validate range
        │
        ├── Filter cards
        │   └── ID between start/end
        │
        ├── Shuffle cards
        │
        └── run_quiz(filtered)


    Quiz engine
    Type I grading
    Type II grading
    Follow-up QA

### pdf_viewer.py
    PDF launching

### quiz_cards.json
    Study card database

### directory.txt
    Index: Contains file for updating directory from within app.

--------------------------------------------

## Data Structure

Type I Card

{
    "type": "I",
    "id": "1",
    "code": "...",
    "qa": [],
    "pdf": null,
    "no_shuffle_qa": false
}

Type II Card

{
    "type": "II",
    "id": "50",
    "code": "...",
    "answer": "...",
    "followup_qa": [],
    "pdf": null,
    "no_shuffle_qa": false
}

--------------------------------------------

## Current Program Flow

main.py

Menu
 ├─ Quiz Range
 │   └─ run_quiz()
 │
 ├─ Add Card
 │   └─ add_study_card()
 │
 ├─ Edit Card
 │   └─ edit_card()
 │
 ├─ Edit Directory Note
 │
 └─ Exit

--------------------------------------------

## cards.py Structure

Utility
    normalize()
    multiline_input()
    clean_answer()

Storage
    load_cards()
    save_all_cards()

Directory
    load_directory_note()
    edit_directory_note()

Card Validation
    sanitize_card(): Crucial for preventing bugs. Decided user should type in exactly what is required. Problems answers have cues to direct user on how, e.g. (commas, spaces, keyword, etc)

Card Creation
    add_study_card()

Card Editing
    edit_card()

Initialization
    init()

--------------------------------------------

## quiz.py Structure

run_quiz()

    Build card list

    For each card

        Type I
            display code
            ask QA
            grade

        Type II
            display exercise
            multiline answer
            compare answer
            follow-up QA

    show score

--------------------------------------------

## Future Ideas

Search System
[ ]

Card Tags
[ ]

Difficulty Levels
[ ]

Statistics
[ ]

Import / Export
[ ]

Backup System
[ ]

Spaced Repetition
[ ]

--------------------------------------------

## Known Issues

None currently

--------------------------------------------

## Version History

2026-06-01
    Added Type II cards
    Added follow-up QA
    Added answer cleaning
    Added QA shuffle toggle
