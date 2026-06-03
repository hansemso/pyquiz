import json
import os
from typing import List, Dict, Any

study_bank: List[Dict[str, Any]] = []


# =====================================================
# Utility
# =====================================================

def normalize(text: str | None) -> str:
    return (text or "").strip().lower()

def sort_key(card):
    cid = str(card.get("id", "")).strip()

    # numeric IDs first
    if cid.isdigit():
        return (0, int(cid))

    # non-numeric IDs go after, sorted alphabetically
    return (1, cid.lower())
    
# =====================================================
# Directory/Index
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
    print("Type END on its own line to save.\n")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    new_text = "\n".join(lines)

    with open(DIRECTORY_FILE, "w", encoding="utf-8") as f:
        f.write(new_text)

    print("\n✅ Directory note updated.")


# =====================================================
# SAFE CARD FIXER
# =====================================================

def sanitize_card(card: dict) -> dict:  # *** sanitize_card ***
    if not isinstance(card, dict):
        return {
            "id": "0",
            "code": "",
            "qa": [],
            "pdf": None,
        }

    card.setdefault("id", "0")
    card.setdefault("code", "")
    card.setdefault("qa", [])
    card.setdefault("pdf", None)
    card.setdefault("no_shuffle_qa", False)
    card.setdefault("type", "I")
    card.setdefault("answer", "")
    card.setdefault("followup_qa", [])

    if card["code"] is None:
        card["code"] = ""

    if card["qa"] is None:
        card["qa"] = []

    if not isinstance(card["followup_qa"], list):
        card["followup_qa"] = []

    if not card.get("pdf"):
        card["pdf"] = None
    
    if card.get("type") not in ("I", "II"):
        card["type"] = "I"
    
    return card


# =====================================================
# File Storage
# =====================================================

def load_cards():
    global study_bank

    path = os.path.join(os.path.dirname(__file__), "quiz_cards.json")

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
# Utility Input
# =====================================================

def multiline_input(prompt="Enter text (END to finish):"):
    print(prompt)

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    if not lines:
        return None

    return "\n".join(lines)


# =====================================================
# QA EDITOR 
# =====================================================

def edit_qa_loop(card, qa_list, qa_key):  # ***** edit_qa_loop ****
    
    if not isinstance(qa_list, list):
                return
                
    while True:
        print("\nQA List:\n")

        for i, qa in enumerate(qa_list, start=1):
            q = qa.get("question", "")
            a = qa.get("answer", "")
            print(f"{i}. Q: {q} | A: {a}")
            

        print("\na = add | ENTER = back")
        choice = input("Select: ").strip().lower()

        if choice == "":
            save_all_cards()
            return

        if choice == "a":
            q = input("Q: ").strip()
            a = input("A: ").strip()

            if q and a:
                qa_list.append({"question": q, "answer": a})
                save_all_cards()
            continue

        try:
            idx = int(choice) - 1

            if idx < 0 or idx >= len(qa_list):
                print("❌ Invalid")
                continue

            item = qa_list[idx]
            
            

        except:
            print("❌ Invalid")
            continue

        nq = input("New Q (blank keep): ").strip()
        na = input("New A (blank keep): ").strip()

        if nq:
            item["question"] = nq
        if na:
            item["answer"] = na

        save_all_cards()


# =====================================================
# ADD CARD
# =====================================================

def add_study_card():
    print("\n=== Add New Study Card ===")

    card_type = input("Card type (I / II): ").strip().upper()

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

    print("DEBUG: before multiline")

    code = multiline_input("Enter code (END to finish):")

    if card_type == "II":
        answer = multiline_input("Enter answer (END to finish):")

        pdf = input("pdf path (optional): ").strip() or None

        followup_qa = []
        print("\nOptional follow-up QA (END to stop)\n")

        while True:
            q = input("Q: ").strip()
            if q.upper() == "END":
                break

            a = input("A: ").strip()
            if a.upper() == "END" or a == "":
                break

            followup_qa.append({"question": q, "answer": a})

        study_bank.append({
            "type": "II",
            "id": card_id,
            "code": code,
            "answer": answer,
            "pdf": pdf,
            "no_shuffle_qa": False,
            "followup_qa": followup_qa
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
            qa_list.append({"question": q, "answer": a})

    pdf = input("pdf path (optional): ").strip() or None

    study_bank.append({
        "type": "I",
        "id": card_id,
        "code": code,
        "qa": qa_list,
        "pdf": pdf,
        "no_shuffle_qa": False
    })

    save_all_cards()
    print("✅ Card added!")


# =====================================================
# EDIT CARD (FIXED)
# =====================================================

def edit_card():                    # ***** edit_card ******
    if not study_bank:
        print("❌ No cards available.")
        return

    print()
    
# *************** for card in sorted *********
    for card in sorted(study_bank, key=sort_key):
        code = card.get("code") or ""
        first_line = code.splitlines()[0] if code.strip() else "<no code>"
        print(f"{card.get('id')}. {first_line}")

    selected_id = input("\nSelect card ID: ").strip()

    card = next((c for c in study_bank if str(c.get("id")) == selected_id), None)

    if not card:
        print("❌ Card not found.")
        return

    # 🔥 sanitize BEFORE ANY TYPE CHECKS ARE USED
    card = sanitize_card(card)

    print("DEBUG TYPE:", card.get("type"))


    while True:
        print("\n1. Edit Type I/II Question")
        print("2. Edit Type II Multiline Answer, Type I/II qa's")
        print("3. Edit pdf link")
        print("4. Change ID")
        print("5. Delete card")
        print("6. Toggle QA shuffle")
        print("7. Cancel")

        action = input("Select option: ").strip()

        

        # 1. EDIT CODE  *** action 1. Code only, not type 2 multiline answer ****
        if action == "1":
            print("\nCURRENT CODE:\n")
            print(card.get("code", ""))

            new_code = multiline_input("Enter new code (END to finish):")

            if new_code is not None:
                card["code"] = new_code
                
                save_all_cards()
                
                print("✅ Code updated.")
            else:
                print("↩️ No changes made.")
                
           

        # 2. EDIT QA.  Type 2 multiline answer goes here ***
        
        elif action == "2":
            if card.get("type", "I") == "II":  
                while True:
                    print("\n1. Edit Type II multiline answer")  # multiline ANSWER
                    print("2. Edit follow-up QA")  
                    print("3. Back")

                    sub = input("Select option: ").strip()

                    if sub == "1":
                        print("\nCURRENT ANSWER:\n")
                        print(card.get("answer", ""))

                        new_answer = multiline_input("New answer (END to finish):")

                        if new_answer is not None:
                            card["answer"] = new_answer
                            save_all_cards()
                            print("✅ Answer updated.")
                        else:
                            print("↩️ No changes made.")
                            
                        #continue  ...this makes it break. Can't enter new answer

                    elif sub == "2":
                        qa_list = card.setdefault("followup_qa", [])
                        edit_qa_loop(card, qa_list, "followup_qa")

                    elif sub == "3":
                        break

            else:
                qa_list = card.setdefault("qa", [])
                edit_qa_loop(card, qa_list, "qa")
                save_all_cards()

        elif action == "3":
            card["pdf"] = input("PDF (blank remove): ").strip() or None
            save_all_cards()

        elif action == "4":
            new_id = input("New ID: ").strip()
            if new_id:
                card["id"] = new_id
                save_all_cards()
                
        elif action == "5":
            if input("Delete? (y/n): ").lower() == "y":
                study_bank.remove(card)
                save_all_cards()
                break

        elif action == "6":
            card["no_shuffle_qa"] = not card.get("no_shuffle_qa", False)
            save_all_cards()
            
        elif action == "7":
            break

        else:
            print("❌ Invalid option.")
            
            save_all_cards()