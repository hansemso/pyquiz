'''
1.Utility  2.Directory/Index  3.SAFE CARD SANITIZER  4.File Storage  5.Utility Input  6.EDIT MODE  7.ADD CARD  8.EDIT CARD 
RAM: study_bank: List[Dict[str, Any]] = []
L: |1|edit_directory_note(): lines, line, new_text  |4|save_all_cards():path,f |5|multiline_required():prompt,lines,line; multiline_optional():prompt,first,lines,line |6|edit_qa_loop():i,qa,q,a,choice,idx,item,nq,na |7|add_study_card():card_type,card_id,code,answer,pdf,qa_list,q,a |8|edit_card():card,code,first_line,selected_id,action,new_code,sub,new_answer,qa_list,new_pdf,new_id,state,c
E: No indented def's
G: |1|normalize(), sort_key()  |2|DIRECTORY_FILE, load_directory_note(), edit_directory_note() |3|sanitize_card() |4|load_cards(), save_all_cards() |5|multiline_required(), multiline_input(), multiline_optional() |6|edit_qa_loop() |7|add_study_card() |8|edit_card()
B: |1|(none directly used) |2|open,FileNotFoundError |3|dict,list,isinstance |4|open,Exception |5|input,str |6|input,enumerate,int,str |7|input,any,dict,list |8|input,print,next,str,int,dict,enumerate
'''

import json
import os
from typing import List, Dict, Any

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# in-memory data storage loaded from json file. Kept in RAM while program runs. json is the persistent storage:

study_bank: List[Dict[str, Any]] = []  

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# =====================================================
# 1. Utility (generic helpers, no user interaction)
# =====================================================

def normalize(text):
    import unicodedata

    text = (text or "")
    text = unicodedata.normalize("NFKC", text)
    text = text.strip()

    return text
    
    
    

def sort_key(card):  # Used below by sorted()
    cid = str(card.get("id", "")).strip()

    # numeric IDs first
    if cid.isdigit():
        return (0, int(cid))

    # non-numeric IDs go after, sorted alphabetically
    return (1, cid.lower())
    
# =====================================================
# 2. Directory  [card(json obj) -> study_bank -> card.get() -> user Index or Directory in Edit Mode]
# =====================================================


DIRECTORY_FILE = os.path.join(
    os.path.dirname(__file__),
    "directory.txt"
)


def load_directory_note() -> str:
    try:
        with open(DIRECTORY_FILE, "r", encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError:
        default_note = (
            "Cards auto-shuffle by default.\n"
            "Use Edit Card → Toggle QA Shuffle for ordered cards."
        )

        with open(DIRECTORY_FILE, "w", encoding="utf-8") as f:
            f.write(default_note)

        return default_note


def edit_directory_note():
    print("\n===== EDIT DIRECTORY NOTE =====\n")
    print(load_directory_note())

    print("\nType new note.")
    print("Type END to save  |  Press [Enter] to cancel\n")

    lines = []

    while True:
        line = input()

        if line.strip() == "":
            print("\n↩ Returning to menu...")
            return
            
        if line.strip().upper() == "END":
            break

        lines.append(line)
        
    else:
        return

    new_text = "\n".join(lines)  

    with open(DIRECTORY_FILE, "w", encoding="utf-8") as f:
        f.write(new_text)  # Writes to disk

    print("\n✅ Directory updated.")


# =====================================================
# 3. CARD SANITIZER
# =====================================================

def sanitize_card(card: dict) -> dict:  
    if not isinstance(card, dict):
        return {
            "id": "0",
            "code": "",
            "qa": [],
        }

    card["qa"] = [
        q for q in card.get("qa", [])
        if isinstance(q, dict) and "question" in q and "answer" in q
    ]

    for q in card.get("qa", []):
        q.setdefault("display", "text")  # FLAG

    card.setdefault("id", "0")
    card.setdefault("code", "")
    card.setdefault("qa", [])
    card.setdefault("shuffle_qa", True)  #FLAG
    card.setdefault("type", "I")
    card.setdefault("answer", "")
    

    if card["code"] is None:
        card["code"] = ""

    if card["qa"] is None:
        card["qa"] = []

    
    
    if card.get("type") not in ("I", "II"):
        card["type"] = "I"
    
    
    return card


# =====================================================
# 4. File Storage
# =====================================================

def load_cards(filename="quiz_cards.json"):
    global study_bank  # global is a py keyword for go-to-top

    path = os.path.join(os.path.dirname(__file__), filename)

    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)

        study_bank = [sanitize_card(c) for c in raw]
        print(f"✅ Loaded {len(study_bank)} cards")

    except Exception as e:
        study_bank = []
        print("❌ No cards loaded:", e)


def save_all_cards():
    path = os.path.join(os.path.dirname(__file__), "quiz_cards.json")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(study_bank, f, indent=2, ensure_ascii=False)


# =====================================================
# 5. Utility Input [dependent on user input()]
# =====================================================

def multiline_required(prompt="Enter text (END to finish):"):  # inner loop. 
    print(prompt)
    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    return "\n".join(lines)
    

def multiline_input(prompt="Enter text (END to finish):"):
    return multiline_required(prompt)  # i.e. just an extra input method. Good practice for future code change.
    
# optional = can abort and return None to signal “no change”
def multiline_optional(prompt="Enter text (END to save, ENTER to cancel):"):
    print(prompt)

    first = input()

    # KEEP EXISTING VALUE
    if first.strip() == "":
        return None  # Enter 🡪 cancel 🡪 finds new_answer = multiline_optional() in LEGB namespace(declared in EDIT) 🡪 prints message to user by if...None statement

    lines = [first]  # needed bc append() below can only add to an existing list.

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)  # adds new line to existing list. 

    return "\n".join(lines)  # inserts newline for each line in list, stacks vertically

# =====================================================
# 6. EDIT MODE  [edit_qa_loop]
# =====================================================

def edit_qa_loop(card, qa_list):  
    
    if not isinstance(qa_list, list):
                return
                
    while True:
        print("\nQA List:\n")

        for i, qa in enumerate(qa_list, start=1):
            q = qa.get("question", "")
            a = qa.get("answer", "")
            
            mode = qa.get("display", "text")

            g = "GUI" if mode == "gui" else "--"

            print(f"{i}. [{g}] Q: {q} | A: {a}")
            
        print("\na = add | t = toggle gui | g = gui all on/off | e = edit | ENTER = back")
        
        choice = input("Select: ").strip().lower()

        # toggle GUI
        if choice == "t":
            idx = int(input("Toggle which #? ")) - 1

            if 0 <= idx < len(qa_list):
                qa = qa_list[idx]

                mode = qa.get("display", "text")

                qa["display"] = "gui" if mode != "gui" else "text"

                save_all_cards()
                print("🔁 Toggled GUI mode")

            continue
        
        
        
        # add more qa
        if choice == "a":
            q = input("Q: ").strip()
            a = input("A: ").strip()
            if q and a:
                qa_list.append({
                    "question": q,
                    "answer": a,
                    "display": "text"
                })
                save_all_cards()
            continue

    
      
       # edit QA (FIXED VERSION)
        if choice == "e":
            idx = int(input("Edit which #? ")) - 1

            if 0 <= idx < len(qa_list):
                qa = qa_list[idx]

                nq = input("New Q (blank keep): ").strip()
                na = input("New A (blank keep): ").strip()

                if nq:
                    qa["question"] = nq
                if na:
                    qa["answer"] = na

                save_all_cards()
            continue

        # toggle on gui for all in Edit QA
        if choice == "g":

            state = input("on/off? ").strip().lower()

            for qa in qa_list:
                qa["display"] = "gui" if state == "on" else "text"

            save_all_cards()
            print("✅ Updated all questions")
            continue
    
    
    
        # exit if no choice selected
        if choice == "":
            save_all_cards()
            return


# =====================================================
# 7. ADD CARD
# =====================================================

def add_study_card():
    print("\n=== Add New Study Card ===")

    card_type = input("Card type (I / II): ").strip().upper()  # Waits for user input

    if card_type not in ("I", "II"):
        print("❌ Invalid card type.")
        return
        
    card_id = input("Enter card ID: ").strip()    
    
    if not card_id.isdigit():
        print("❌ ID must be numeric for sorting system.")
        return

    if any(card.get("id") == card_id for card in study_bank):
        print("❌ Duplicate ID!")
        return

    #print("DEBUG: before multiline")

    code = multiline_input("Enter code (END to finish):")  # 🔥mline-Q for Type I or II

    if card_type == "II":
        answer = multiline_input("Enter answer (END to finish):")  # 🔥mline-Ans for Type II only as I has none.

        

        

        study_bank.append({
            "type": "II",
            "id": card_id,
            "code": code,
            "answer": answer,
            "shuffle_qa": True,  # FLAG
        })

        save_all_cards()
        
        print("✅ Type II card added!")  
        return

    qa_list = []

    while True:
        q = input("Q: ").strip()
        if q.upper() == "END":
            break

        a = input("A: ").strip()

        if q and a:
            qa_list.append({
                "question": q,
                "answer": a,
                "display": "text"  # FLAG
            })
    

    study_bank.append({
        "type": "I",
        "id": card_id,
        "code": code,
        "qa": qa_list,
        "shuffle_qa": True  # FLAG
    })

    save_all_cards()
    print("✅ Type I card added!")  


# =====================================================
# 8] EDIT CARD 
# =====================================================

def edit_card():         # 🡨 elif choice == "3": from main.py 
    if not study_bank:
        print("❌ No cards available.")
        return

    print()  # print blank line. cosmetic. no other purpose.
    
### from global list in study_bank, creates temporary sorted list in ram only Python knows 
    for card in sorted(study_bank, key=sort_key):  # from def sort_key() in 1]Utility above. 
        code = card.get("code") or ""
        first_line = code.splitlines()[0] if code.strip() else "<no code>"
        print(f"{card.get('id')}. {first_line}")  # 1st line of multiline question(type I/II in 7]ADD CARD)

    selected_id = input("\nSelect card ID: ").strip()  # a) user inputs card id

    card = next(
        (c for c in study_bank if str(c.get("id")) == selected_id), 
        None
    )  

    if not card:
        print("❌ Card not found.")
        return

    print(f"\nCard loaded: {card.get('id')} ({card.get('type')})")
    
    
    
    
    if not card:
        print("❌ Card not found.")
        return

    # 🔥 sanitize BEFORE ANY TYPE CHECKS ARE USED
    card = sanitize_card(card)  # take 'card' to 3] def sanitize_card, assign back to 'card'

   # print("card type:", card.get("type"))  # 3.Edit prints I or II after card id input. Serves as 🐞DEBUG🐞 for 'type' = variable for type I or II loop defined in 2] add card.

#  main.py → 3. Edit Card/View Index →  ***** EDIT MENU *****
    while True:  # outer loop
        print("\n1. Edit mline Q")  # For both type I and II, multiline question only
        print("2. Edit qa, mline Ans")  # qa edit(type I,II) + multiline answer(type I only)
        print("3. Change card id")
        print("4. Delete card")
        print("5. Auto shuffle_qa on/off")  # FLAG 
        print("6. Cancel")

        action = input("Select option: ").strip()  # action is the variable for user input string for elif list below

        

        # 1: Edit multiline-Question(mline-Q)  
        if action == "1":  # 🔥 Input mline-Q for Type I and II
            print("\nCURRENT CODE:\n")
            print(card.get("code", ""))  # If no saved code/Q, print empty str instead

            new_code = multiline_optional(
                "Enter new code (END to finish, ENTER to cancel):"
            )

            if new_code is not None:
                card["code"] = new_code
                
                save_all_cards()
                
                print("✅ Code updated.")
            else:
                print("↩️ No changes made.")  # Program "backs out" bc nothing was done. It feels like it backs out to user when all it did actually was do nothing, cancelled action. 
                
           

        # 2: EDIT QA.  🔥Type II multiline answer goes here
        
        elif action == "2":
            if card.get("type") == "II":

                while True:
                    print("\n1. Edit mline-Ans")
                    print("2. Back")

                    sub = input("Select option: ").strip()

                    if sub == "1":
                        print("\nCURRENT ANSWER:\n")
                        print(card.get("answer", ""))

                        new_answer = multiline_optional("New answer (END to save, ENTER to cancel):")

                        if new_answer is None:
                            print("↩️ No changes made.")
                        else:
                            card["answer"] = new_answer
                            save_all_cards()
                            
                            print("✅ Answer updated.")

                    
                    elif sub == "2":
                        break

                    else:
                        print("❌ Invalid option.")

            else:
                qa_list = card.setdefault("qa", [])
                edit_qa_loop(card, qa_list)
                
                save_all_cards()

      
    
        elif action == "3":
            new_id = input("New ID: ").strip()
            if new_id:
                card["id"] = new_id
                save_all_cards()
                
        elif action == "4":
            if input("Delete? (y/n): ").lower() == "y":
                study_bank.remove(card)
                save_all_cards()
                break

        elif action == "5":
            card["shuffle_qa"] = not card.get("shuffle_qa", True)
            save_all_cards()

            if card["shuffle_qa"]:
                shuffle_status = "ON (shuffle allowed)"  #FLAG
            else:
                shuffle_status = "OFF (no shuffle)"
            
            
            print(f"🔁 Auto shuffle toggled: {shuffle_status}")
    
            
            
#        elif action == "debug":
#            print("=== DEBUG CARDS ===")
#            for c in study_bank:
#                print("ID:", c.get("id"),
#                  "| shuffle:", c.get("shuffle_qa"),
#                  "| type:", c.get("type"))
    
        elif action == "6":
            break

        else:
            print("❌ Invalid option.")
            
            save_all_cards()
            
            
            
            
