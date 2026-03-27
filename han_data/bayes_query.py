import sqlite3
import os
import json

# Paths
BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "quiz.db")


# ----------------------------
# Load cards
# ----------------------------

def load_cards():
    base = os.path.dirname(__file__)      # han_data
    root = os.path.dirname(base)          # pyquiz
    path = os.path.join(root, "quiz_cards.json")

    print("Loading cards from:", path)    # debugging line

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# ----------------------------
# Flatten cards into questions
# ----------------------------

def flatten_cards(cards):
    items = []

    for card in cards:
        card_id = card.get("id")
        code = card.get("code", "")
        qa_list = card.get("qa", [])

        for qa in qa_list:
            items.append({
                "card_id": card_id,
                "code": code,
                "question": qa.get("question"),
                "answer": qa.get("answer")
            })

    return items


# ----------------------------
# Connect to database
# ----------------------------
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


# ----------------------------
# Build probability lookup
# ----------------------------
cursor.execute("""
SELECT card_id, COUNT(*) as attempts, SUM(correct) as correct_count
FROM quiz_results
GROUP BY card_id
""")

prob_lookup = {}

for card_id, attempts, correct_count in cursor.fetchall():
    if attempts > 0:
        prob_lookup[card_id] = correct_count / attempts
    else:
        prob_lookup[card_id] = 0


# ----------------------------
# Load and flatten cards
# ----------------------------
cards = load_cards()
items = flatten_cards(cards)


# ----------------------------
# Print probabilities
# ----------------------------
print("\nBayes-style probability per question:\n")

for item in items:
    card_id = item["card_id"]
    question = item["question"]

    prob = prob_lookup.get(card_id, 0)

    print(f"[Card {card_id}] {question}")
    print(f"P(correct) ≈ {prob:.2f}\n")


conn.close()