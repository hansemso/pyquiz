import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE quiz_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    card_id INTEGER,
    correct INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
conn.close()

print("quiz_results table created.")