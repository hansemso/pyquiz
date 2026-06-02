# devlog  ...for pyquiz June 2026

## Current Status

Working Features
----------------
[x] JSON card storage
[x] Type I cards
[x] Type II cards
[x] Multi-line code display
[x] Multi-line answer input
[x] Follow-up QA
[x] PDF links
[x] Directory note
[x] Range selector
[x] QA shuffle toggle
[x] Instant grading
[x] Score tracking

--------------------------------------------

## File Structure

main.py
    Main menu
    Program startup

cards.py
    Card storage
    Add card
    Edit card
    Save/load JSON
    Directory note

quiz.py
    Quiz engine
    Type I grading
    Type II grading
    Follow-up QA

pdf_viewer.py
    PDF launching

quiz_cards.json
    Study card database

directory.txt
    Index notes

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
    sanitize_card()

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
