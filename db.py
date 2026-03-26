import os
import sqlite3
from datetime import datetime

def log_quiz_result(score: int):
    try:
        DB_DIR = os.path.join(os.path.dirname(__file__), "han_data")
        os.makedirs(DB_DIR, exist_ok=True)
        DB_PATH = os.path.join(DB_DIR, "quiz.db")

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS quiz_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER,
                timestamp TEXT
            )
        """)

        cursor.execute(
            "INSERT INTO quiz_results (score, timestamp) VALUES (?, ?)",
            (score, datetime.now())
        )

        conn.commit()
        conn.close()
    except Exception as e:
        print("❌ Error logging quiz result:", e)