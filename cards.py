### *** cards.py ***    6_1_2026

import json
import os
from typing import List, Dict, Any

study_bank: List[Dict[str, Any]] = []


# =====================================================
# Utility
# =====================================================

def normalize(text: str | None) -> str:
    return (text or "").strip().lower()


def clean_answer(text: str) -> str:
    if not isinstance(text, str):
        return ""
    return text.replace("----------------------", "").rstrip()


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
            "type": "I",
            "no_shuffle_qa": False,
            "answer": "",
            "followup_qa": []
        }

    card.setdefault("id", "0")
    card.setdefault("code", "")
    card.setdefault("qa", [])
    card.setdefault("pdf", None)
    card.setdefault("no_shuffle_qa", False)
    card.setdefault("type", "I")
    card.setdefault("answer", "")
    card.setdefault("followup_qa", [])

    # normalize fields
    if card["code"] is None:
        card["code"] = ""

    if card["qa"] is None:
        card["qa"] = []

    if not isinstance(card["followup_qa"], list):
        card["followup_qa"] = []

    # ensure QA structure safety
    card["followup_qa"] = [
        qa for qa in card["followup_qa"]
        if isinstance(qa, dict) and "question" in qa and "answer" in qa
    ]

    card["answer"] = clean_answer(card.get("answer", ""))

    if not card.get("pdf"):
        card["pdf"] = None

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

    return "\n".join(lines)


# =====================================================
# Add Card
# =====================================================

def add_study_card():

    print("\n=== Add New Study Card ===")

    card_type = input("Card type (I / II): ").strip().upper()

    if card_type not in ("I", "II"):
        print("❌ Invalid card type.")
        return

    card_id = input("Enter card ID: ").strip()

    if any(str(card.get("id")) == card_id for card in study_bank):
        print("❌ Duplicate ID!")
        return

    code = multiline_input("Enter code (END to finish):")

    # TYPE II
    if card_type == "II":

        answer = multiline_input("Enter answer (END to finish):")

        pdf = input("pdf path (optional): ").strip() or None

        followup_qa = []

        print("\nOptional follow-up QA (ENTER Q = stop)\n")

        while True:
            q = input("Q: ").strip()
            if q.upper() == "END":
                break

            a = input("A: ").strip()
            if a == "" or a.upper() == "END":
                break

            followup_qa.append({"question": q, "answer": a})

        study_bank.append({
            "type": "II",
            "id": card_id,
            "code": code,
            "answer": clean_answer(answer),
            "pdf": pdf,
            "no_shuffle_qa": False,
            "followup_qa": followup_qa
        })

        save_all_cards()
        print("✅ Type II card added!")
        return

    # TYPE I
    qa_list = []

    print("\nEnter QA pairs (END as question to stop)")

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
# Edit Card
# =====================================================

def edit_card():

    if not study_bank:
        print("❌ No cards available.")
        return

    print()

    def safe_id_key(c):
        try:
            return int(c.get("id", 0))
        except:
            return 0

    for card in sorted(study_bank, key=safe_id_key):

        code = card.get("code") or ""
        first_line = code.splitlines()[0] if code.strip() else "<no code>"

        print(f"{card.get('id')}. {first_line}")

    selected_id = (input("\nSelect card ID: ") or "").strip()

    card = next(
        (c for c in study_bank if str(c.get("id")) == selected_id),
        None
    )

    if not card:
        print("❌ Card not found.")
        return

    card = sanitize_card(card)

    while True:

        print("\n1. Edit code")
        print("2. Edit QA")
        print("3. Edit pdf link")
        print("4. Change ID")
        print("5. Delete card")
        print("6. Toggle QA shuffle")
        print("7. Cancel")

        action = input("Select option: ").strip()

        if action == "7":
            break

        elif action == "5":
            confirm = input("Delete card? (y/n): ").strip().lower()
            if confirm == "y":
                study_bank.remove(card)
                save_all_cards()
                print("✅ Card deleted.")
                break


def init():
    load_cards()