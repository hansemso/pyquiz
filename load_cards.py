import os, json, sqlite3

JSON_PATH = os.path.join(os.path.dirname(__file__), '..', 'quiz_cards.json')
DB_PATH = os.path.join(os.path.dirname(__file__), 'quiz.db')

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    cards = json.load(f)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

for card in cards:
    question = card["qa"][0]["question"]
    answer = card["qa"][0]["answer"]
    code = card.get("code", "")
    cursor.execute("INSERT INTO cards (question, answer, code) VALUES (?, ?, ?)",
                   (question, answer, code))

conn.commit()
conn.close()
print("Cards loaded from study_cli_app.")