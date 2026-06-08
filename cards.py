# cards.py  (CLEAN STABLE CORE MODULE)

import json
import os
from typing import List, Dict, Any

# =====================================================
# GLOBAL STORAGE (RAM)
# =====================================================

study_bank: List[Dict[str, Any]] = []

# =====================================================
# 1] Utility
# =====================================================

def normalize(text: str | None) -> str:
    return (text or "").strip().lower()


def sort_key(card):
    cid = str(card.get("id", "")).strip()
    if cid.isdigit():
        return (0, int(cid))
    return (1, cid.lower())

# =====================================================
# 2] FILE STORAGE
# =====================================================

def load_cards(filename="quiz_cards.json"):
    global study_bank

    path = os.path.join(os.path.dirname(__file__), filename)

    try:
        with open(path, "r", encoding="utf-8") as f:
            study_bank = json.load(f)
        print(f"✅ Loaded {len(study_bank)} cards from {filename}")

    except FileNotFoundError:
        study_bank = []
        print("⚠️ No card file found, starting empty.")

    except Exception as e:
        study_bank = []
        print("❌ Failed to load cards:", e)


def save_all_cards(filename="quiz_cards.json"):
    path = os.path.join(os.path.dirname(__file__), filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(study_bank, f, indent=2, ensure_ascii=False)

# =====================================================
# 3] DIRECTORY NOTE
# =====================================================

DIRECTORY_FILE = os.path.join(os.path.dirname(__file__), "directory.txt")


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

    print("\nType new note. END to save.\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    with open(DIRECTORY_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("✅ Directory updated.")

# =====================================================
# 4] INPUT HELPERS
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


def multiline_optional(prompt="Enter text (END to finish):"):
    print(prompt)
    first = input()

    if first.strip() == "" or first.strip().upper() == "END":
        return None

    lines = [first]

    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    return "\n".join(lines)