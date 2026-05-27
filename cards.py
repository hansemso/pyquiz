### *** cards.py ***    May 2026

import json
import os
from typing import List, Dict, Any

study_bank: List[Dict[str, Any]] = []


# =====================================================
# Utility
# =====================================================

def normalize(text: str | None) -> str:
    return (text or "").strip().lower()


# =====================================================
# SAFE CARD FIXER
# =====================================================

def sanitize_card(card: dict) -> dict:
    """
    Guarantees every card has a valid structure.
    Prevents runtime crashes from missing keys.
    """

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
    
    if card["code"] is None:
        card["code"] = ""
    
    if card["qa"] is None:
        card["qa"] = []

    if not isinstance(card["qa"], list):
        card["qa"] = []
    
    pdf = card.get("pdf")
    if not pdf:
        card["pdf"] = None
    
    return card


# =====================================================
# File Storage
# =====================================================

def load_cards():
    global study_bank

    path = os.path.join(
        os.path.dirname(__file__),
        "quiz_cards.json"
    )

    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)

        # repair cards on load
        study_bank = [
            sanitize_card(c)
            for c in raw
        ]

        print(f"✅ Loaded {len(study_bank)} cards")

    except Exception as e:
        study_bank = []
        print("❌ No cards loaded:", e)


def save_all_cards():

    path = os.path.join(
        os.path.dirname(__file__),
        "quiz_cards.json"
    )

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            study_bank,
            f,
            indent=2,
            ensure_ascii=False
        )


# =====================================================
# Utility Input
# =====================================================

def multiline_input(prompt="Enter text (END to finish):"):

    print(prompt)

    lines = []
    started = False

    while True:
        line = input()

        # KEEP CURRENT SIGNAL
                   
        if not started and line.strip() == "":
            return None
        started = True

        if line.strip().upper() == "END":
            break

        lines.append(line)

    return "\n".join(lines)


# =====================================================
# Add Card
# =====================================================

def add_study_card():

    print("\n=== Add New Study Card ===")

    card_id = input("Enter card ID: ").strip()

    if any(card.get("id") == card_id for card in study_bank):
        print("❌ Duplicate ID!")
        return

    code = multiline_input(
        "Enter code (END to finish):"
    )

    qa_list = []

    print("\nEnter QA pairs (END as question to stop)")

    while True:

        q = input("Q: ").strip()

        if q.upper() == "END":
            break

        a = input("A: ").strip()

        if q and a:
            qa_list.append({
                "question": q,
                "answer": a
            })

    pdf = input(
        "pdf path (optional, ENTER to skip): "
    ).strip()

    

    pdf = pdf if pdf else None

    

    study_bank.append({
        "id": card_id,
        "code": code,
        "qa": qa_list,
        "pdf": pdf,
        
    })

    save_all_cards()

    print("✅ Card added!")


# =====================================================
# Edit Card
# =====================================================

def edit_card():

    if not study_bank:
        print("❌ No cards available.")
        return

    print()

    for card in study_bank:

        code = card.get("code") or ""

        first_line = (
            code.splitlines()[0]
            if code.strip()
            else "<no code>"
        )

        print(f"{card.get('id')}. {first_line}")

    selected_id = (input(
        "\nSelect card ID: "
    ) or "").strip()

    card = next(
        (
            c for c in study_bank
            if str(c.get("id")) == selected_id
        ),
        None
    )

    if not card:
        print("❌ Card not found.")
        return

    # enforce safe structure
    card = sanitize_card(card)
    
    
    while True:

        print("\n1. Edit code")
        print("2. Edit QA")
        print("3. Edit pdf link")
        print("4. Delete card")
        print("5. Cancel")

        action = input(
            "Select option: "
        ).strip()

        # =================================================
        # EDIT CODE
        # =================================================

        if action == "1":

            print("\nCURRENT CODE:\n")

            print(card.get("code", ""))

            new_code = multiline_input(
                "\nEnter new code "
                "(END to finish, blank = keep current):"
            )

            if new_code is not None and new_code != "":
                card["code"] = new_code
                save_all_cards()
                print("✅ Code updated.")
            else:
                save_all_cards()
                print("↩️ No changes made (kept existing code).")

        # =================================================
        # EDIT QA
        # =================================================

        elif action == "2":  # Option 2: Edit QA

            qa_list = card.setdefault("qa", [])

            # ---------------------------------------------
            # NO QA YET
            # ---------------------------------------------

            if len(qa_list) == 0:

                print("\nNo QA yet. Add some.\n")

                while True:

                    q = input(
                        "Q (END to stop): "
                    ).strip()

                    if q.upper() == "END":
                        break

                    a = input(
                        "A: "
                    ).strip()

                    if q and a:

                        qa_list.append({
                            "question": q,
                            "answer": a
                        })

                        print("✅ QA added.")

                card["qa"] = qa_list

                save_all_cards()

                continue

            # ---------------------------------------------
            # SHOW QA
            # ---------------------------------------------

            print("\nQA List:\n")

            for i, qa in enumerate(qa_list, start=1):

                print(
                    f"{i}. "
                    f"Q: {qa['question']} | "
                    f"A: {qa['answer']}"
                )

            print("\na = add new QA")

            choice = input(
                "\nSelect QA #: "
            ).strip().lower()

            # ---------------------------------------------
            # ADD NEW QA
            # ---------------------------------------------

            if choice == "a":

                print("\nAdding QA pairs (press Enter on Q or A to stop)\n")

                while True:

                    q = input("Q: ").strip()
                    if q == "":
                        print("↩️ Stopped adding QA")
                        break

                    a = input("A: ").strip()
                    if a == "":
                        print("↩️ Stopped adding QA")
                        break

                    qa_list.append({
                        "question": q,
                        "answer": a
                    })

                    
                    print("✅ Added\n")
                
                save_all_cards()
                
                continue

            # ---------------------------------------------
            # EDIT EXISTING QA
            # ---------------------------------------------

            try:
                qa_index = int(choice) - 1

            except:
                print("❌ Invalid selection.")
                continue

            if qa_index < 0 or qa_index >= len(qa_list):
                print("❌ QA not found.")
                continue

            qa_item = qa_list[qa_index]

            print(
                f"\nCurrent Question: "
                f"{qa_item['question']}"
            )

            new_question = input(
                "New Q (blank = keep): "
            ).strip()

            if new_question:
                qa_item["question"] = new_question

            print(
                f"\nCurrent Answer: "
                f"{qa_item['answer']}"
            )

            new_answer = input(
                "New Answer (blank = keep): "
            ).strip()

            if new_answer:
                qa_item["answer"] = new_answer

            save_all_cards()

            print("✅ QA updated.")

#======================================
#     3. Edit Card  (Input pdf path here)
#==============================================
     
        elif action == "3":
            current = card.get("pdf")

            print(f"\nCurrent PDF: {current}")

            new_pdf = input("Enter pdf path (blank = remove): ").strip()

            if new_pdf:
                card["pdf"] = new_pdf
            else:
                card["pdf"] = None

            save_all_cards()
            print("✅ PDF updated.")
    

        # =================================================
        # DELETE
        # =================================================

        elif action == "4":
            confirm = input("Delete card? (y/n): ").strip().lower()

            if confirm == "y":
                study_bank.remove(card)
                save_all_cards()
                print("✅ Card deleted.")
                break

        elif action == "5":
            break

       
        else:
            print("❌ Invalid option.")