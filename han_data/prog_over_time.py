import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'quiz.db')

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Simple query: show number of correct answers per day
query = """
SELECT DATE(timestamp) as day, SUM(correct) as correct_answers
FROM quiz_results
GROUP BY day
ORDER BY day DESC
LIMIT 10
"""

rows = cursor.execute(query).fetchall()
conn.close()

print("Recent Quiz Performance:\n")
for day, correct in rows:
    print(f"{day}: {correct} correct answers")