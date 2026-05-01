# quiz.py
import random
import cards


def run_quiz(cards_list):
    score = 0
    total = 0
    print("\n=== Quiz Mode ===\n")
    try:
        for card in cards_list:
            for line in card.get("code", "").splitlines():
                print(line.encode().decode("unicode_escape"))

            qa_list = card.get("qa", [])
            total += len(qa_list)

            for qa in qa_list:
                print(qa.get("question", ""))
                ans = input("> ").strip()
                if cards.normalize(ans) == cards.normalize(qa.get("answer", "")):
                    print("✔ Correct\n")
                    score += 1
                else:
                    print(f"✘ Wrong (Answer: {qa.get('answer','')})\n")

        print(f"\nScore: {score} / {total}")
        
    except KeyboardInterrupt:
        print(f"\nQuiz terminated. Score: {score} / {total}")

def quiz_all():
    if not cards.study_bank:
        print("❌ No cards available.")
        return
    run_quiz(cards.study_bank)

def quiz_range():
    if not cards.study_bank:
        print("❌ No cards available.")
        return
    try:
        start = int(input("Start ID: "))
        end = int(input("End ID: "))
    except:
        print("❌ Invalid range.")
        return

    filtered = [c for c in cards.study_bank if start <= int(c.get("id", 0)) <= end]
    if not filtered:
        print("❌ No cards in that range.")
        return

    random.shuffle(filtered)
    run_quiz(filtered)
    
    