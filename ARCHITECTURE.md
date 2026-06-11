# pyquiz\ARCHITECTURE.md  |  today's date: 6_10_26

# Synopsis: 
- quiz.py and cards.py are the core files. main.py is like a simple breaker box.  
-  


# Recent Development:

6.10.26: Finally got Tkinter to work with pyquiz. Trick was to start over by attaching a relay as it were called "display" then to toggle on/off popup window per question by adding it to Edit Mode as, t = toggle. Defensive development as it were. 
2. 
3.
4.
 

# Architecture (by file):  

## quiz.py [shuffle, 


## cards.py [data, flags

1. Cards are divided into Type I and II: 
	- Type I: one mline(multi) field >> unlimited sline(single) qa-pair fields. Per card.  
	- Type II: one mline question field >> one mline answer field. Per card. 
	- random.shuffle(filtered) card level shuffle. card.get("shuffle_qa",True) = read value of key to on/off qa shuffle of this card(Type I only)   
	qa.get("display", "text").lower() ...means use key="display" to read value="text" and attach to qa object.  
	
	
- Every question in sline qa-pairs has a <gui> on/off switch to which Tkinter is attached. 

- "Directory"=(user's topic ranges menu)  [card(json obj) -> study_bank -> card.get() -> user Index or Directory in Edit Mode]



#================ END ================================

my clipboard:  




- In quiz.py def run_quiz, Type I loop and Type II loop are parallel . 
- Decided to make quiz_gui.py to protect quiz.py and pyquiz in general from bugs caused by gui display logic. 
- print("CALLING DISPLAY:", q)
display.show(q, font_size=60)   ...this is what made tkinter window work for hanja finally said AI. 
🧪 Why HELLO shows but Hanja doesn’t

Because:

HELLO test was forced in main.py ✔
quiz Hanja depends on "display" == "gui" ❌ (likely false or missing)

❌ Tkinter cannot be safely driven from a blocking CLI loop

English question triggers display → works initially
Then input() blocks execution
Tk event queue stalls
next display.show() calls never repaint correctly
window stays on last stable frame (“HELLO 3”)

Tk shows HELLO 3
↓
program enters input() loop
↓
Tk never properly enters stable event cycle
↓
window appears frozen

Finally, ai says not a TK bug but missing data field >> logic never activates gui. 
Your system simply had:

❌ “GUI triggered by metadata that doesn’t exist” ... so I should a have installed a manual switch on each qa pair?  then ai offers "per-card display rules" finally, which I was thinking of doing in the first place to prevent this but this not because it said auto detect english/hanja was good for it. 



## Class A distinctive structural features well developed

- 


## Class B specific/less global features

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
--[x] Bypassed Windows for pdf path to foxit for simplicity.
-[x] How to standardize and apply a protocol throughout a program while avoiding bugs and crashes. Ex: 1. Enter blank to cancel and go back versus enter new text and make a change. new_code = multiline_optional(...) became the choice because : ENTER = cancel and back, END immediately = cancel, text + END is save, whitespace + Enter is what? i.e. input logic/handling became an issue. settled upon:
 After text = input().strip().  input() can't distinguish: Enter, esc, ctrl+c, etc.  -import keyboard is Windows-focused real-time key press. It requires pip install keyboard. It can cause conflicts. Pros avoid esc key. 
- ENTER, SPACE + ENTER, TAB + ENTER, SPACE SPACE SPACE + ENTER == "" ...so, <"" + Enter> = cancel = back =  no change/keep 
- type in DEL + [Enter] = delete/clear
-  type in END + [Enter] -> Finish multiline input for Q or Ans- 
-  other   -> User data

-Removed Ttinter popup for Type II to simplify. Only Type I singline qa's have popups editable in Edit menu option.  The real rule is:

### Design goals:
- Separation of concerns. gui(tkinter) for unicode text display belongs in the display layer, not inside card types.






AI suggests a pre-input engine layer:
keyboard → terminal → input() → string → [[[your parser]]] → meaning
AI says right now "your parser" is scattered:
cards.py
│
├── multiline_required()   → END parser
├── multiline_optional()    → cancel parser
├── edit_qa_loop()          → menu parser
├── add_study_card()        → multi-parser cluster
└── edit_card()             → full state-machine parser

...so decided to keep things the same for now.  
qa's are handled differently though as a rule:

cards.py
│
├── Card field editors
│   ├── code
│   ├── answer
│   ├── pdf
│   └── id
│
└── QA editor
    ├── list view
    ├── add
    ├── edit
    └── return
That is, since qa's are all singleline, just handling them differently and separately may be best, as this app will only be cli-based and simple as possible. So develop extensions and pluggable add ons but keep it simple at its core. 
- a good thing would be to connect with cpymos folder so questions about numpy and such can somehow be connected to exercises. Say for range 2000-3000: ml or numpy problems. So a popup for a pdf or a sci calculator but just another powershell window for py 3. So maybe if q is a problem, can enter solution in cpymos. 
s = solve in CPYMOS
subprocess.run(["cpymos.exe"])
subprocess.Popen(["python", "cpymos.py"])









## File Structure --overall

### Synopsis

```
Triangular design with main.py at top as access. cards.py = data logic(biggest file); quiz.py = runtime logic(selecting, filtering, shuffling).   

foxit is the pdf reader I use:
Test-Path "C:\Program Files\Foxit Software\Foxit PDF Reader\FoxitPDFReader.exe"

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
│   ├── Global Working Memory in RAM ⇆ study_bank ⇆ quiz_cards.json
│   │
│   ├── Utility Functions
│   │   ├── normalize()
│   │   ├── sort_key()   
│   │   ├── multiline_required(...)  
│   │   ├── multiline_optional(...)
│   │   └── multiline_input(...)
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
 │                                      ┌── <Type I>  ➜ <option b> ➜ singline qa pairs  
 ├──<Input: Type I/II> ➜ multiline Q ──│                                      
 │                                      │                                      🡱                                             
 │                                      └── <Type II> ➜ <option b> ➜ MULTILINE ANSWER     *Only Type II has multiline answer, which is in option b not a
 │
 └──➜ shuffle(y/n)     
          │
  ┌───────┴────────┐
  │                │
  ▼                ▼
False             True
(auto)           (exempt)
  │                │
  ▼                ▼
Shuffle QA      Keep QA Order
  │                │
  └───────┬────────┘S
          │
          ▼
       session ➜ grading ➜ next card ➜ final score
```



## LOG (latest date on top)

6_3_26 
- Type 1,2 cards both have multiline question input field and singline qa's. Type 2 has in addition multiline answer. They were separated in edit mode. 
- Also, save work(END), cancel, Enter, back...these are all different loops, easy to tangle in code.  

