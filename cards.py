import json
import os
from typing import List, Dict, Any

study_bank: List[Dict[str, Any]] = []

# -------------------------
# Utility
# -------------------------
def normalize(text: str | None) -> str:
    return (text or "").strip().lower()

# -------------------------
# File Storage
# -------------------------
def load_cards():
    global study_bank
    path = os.path.join(os.path.dirname(__file__), "quiz_cards.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            study_bank = json.load(f)
        print(f"✅ Loaded {len(study_bank)} cards")
    except Exception:
        study_bank = []
        print("❌ No cards loaded")

def save_all_cards():
    path = os.path.join(os.path.dirname(__file__), "quiz_cards.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(study_bank, f, indent=2, ensure_ascii=False)

# -------------------------
# Add / Edit cards
# -------------------------
def multiline_input(prompt="Enter text (END to finish):"):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def add_study_card():
    print("\n=== Add New Study Card ===")
    card_id = input("Enter card ID: ").strip()
    if any(card.get("id") == card_id for card in study_bank):
        print("❌ Duplicate ID!")
        return

    code = multiline_input("Enter code (you can paste ANSI codes, END to finish):")

    qa_list = []
    print("\nEnter QA pairs (END as question to stop)")
    while True:
        q = input("Question: ").strip()
        if q.upper() == "END":
            break
        a = input("Answer: ").strip()
        if q and a:
            qa_list.append({"question": q, "answer": a})

    study_bank.append({"id": card_id, "code": code, "qa": qa_list})
    save_all_cards()
    print("✅ Card added!")

def edit_card():
    if not study_bank:
        print("❌ No cards available.")
        return

    print("\n=== Edit Card ===\n")
    for i, card in enumerate(study_bank, start=1):
        first_line = card.get('code', '').splitlines()[0] if card.get('code') else "<no code>"
        print(f"{i}. {first_line}")

    try:
        choice = int(input("\nSelect card number: ").strip()) - 1
    except:
        print("❌ Invalid input.")
        return

    if choice < 0 or choice >= len(study_bank):
        print("❌ Card not found.")
        return

    card = study_bank[choice]

    print("\n1. Edit Code\n2. Edit QA\n3. Delete Card\n4. Cancel")
    action = input("Select option: ").strip()

    if action == "1":
        new_code = multiline_input("Enter new code (END to finish):")
        if new_code.strip():
            card["code"] = new_code.strip()
            save_all_cards()
            print("✅ Code updated.")

    elif action == "2":
        qa_list = card.get("qa", [])
        if not qa_list:
            print("❌ No QA list.")
            return

        print("\nQA List:")
        for i, qa in enumerate(qa_list, start=1):
            print(f"{i}. Q: {qa.get('question','')} | A: {qa.get('answer','')}")

        try:
            qa_index = int(input("Select QA number to edit: ").strip()) - 1
        except:
            print("❌ Invalid QA selection.")
            return

        if qa_index < 0 or qa_index >= len(qa_list):
            print("❌ QA not found.")
            return

        # Edit question
        current_question = qa_list[qa_index].get("question", "")
        print(f"Current Question: {current_question}")
        new_question = input("New Question (leave blank to keep): ").strip()
        if new_question:
            qa_list[qa_index]["question"] = new_question

        # Edit answer
        current_answer = qa_list[qa_index].get("answer", "")
        print(f"Current Answer: {current_answer}")
        new_answer = input("New Answer (leave blank to keep): ").strip()
        if new_answer:
            qa_list[qa_index]["answer"] = new_answer

        card["qa"] = qa_list
        save_all_cards()
        print("✅ QA updated.")

    elif action == "3":
        if input("Delete card? (y/n): ").lower() == "y":
            study_bank.pop(choice)
            save_all_cards()
            print("✅ Card deleted.")

    else:
        print("❌ Cancelled.")