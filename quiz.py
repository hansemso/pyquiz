import random
import cards
import display


# =====================================================
# SAFE GUI DISPLAY
# =====================================================
def safe_show(text, **kwargs):
    try:
        display.show(text, **kwargs)
    except Exception:
        print(text)


# =====================================================
# MAIN ENGINE
# =====================================================
def run_quiz(cards_list):

    score = 0
    total = 0

    cards_list = [
        c for c in cards_list
        if (
            (c.get("type", "I") == "I" and c.get("qa"))
            or c.get("type") == "II"
        )
    ]

    if not cards_list:
        print("No quiz questions.")
        return

    for card in cards_list:

        print("\n" + card.get("code", "<no code>"))

        # =====================================================
        # TYPE II
        # =====================================================
        if card.get("type") == "II":

            total += 1

            ans = cards.multiline_input("\nMain Answer (END to finish): ")
            correct = card.get("answer", "")

            if cards.normalize(ans) == cards.normalize(correct):
                print("✅ Correct")
                score += 1
            else:
                print(f"❌ Expected:\n{correct}")

            for qa in card.get("followup_qa", []):

                total += 1

                q = qa.get("question", "")
                a = qa.get("answer", "")

                gui = qa.get("gui", False)
                file_path = qa.get("file")

                if gui:
                    safe_show(q, image=file_path, font_size=40, width=400, height=200)
                else:
                    print(f"\nQ: {q}")

                user_ans = input("Answer > ").strip()

                if cards.normalize(user_ans) == cards.normalize(a):
                    print("✅ Correct")
                    score += 1
                else:
                    print(f"❌ {a}")

            continue

        # =====================================================
        # TYPE I
        # =====================================================
        qa_list = card.get("qa", [])

        if card.get("shuffle_qa", True):
            random.shuffle(qa_list)

        for qa in qa_list:

            total += 1

            q = qa.get("question", "")
            a = qa.get("answer", "")

            gui = qa.get("gui", False)
            file_path = qa.get("file")

            # SHOW QUESTION (GUI OR TEXT)
            if gui:
                safe_show(q, image=file_path, font_size=40, width=400, height=200)
            else:
                print(f"\nQ: {q}")

            user_ans = input("Answer > ").strip()

            if cards.normalize(user_ans) == cards.normalize(a):
                print("✅ Correct")
                score += 1
            else:
                print(f"❌ {a}")

    print(f"\nFINAL SCORE: {score} / {total}")
    
    
#=====================================================


def quiz_range():
    start, end = parse_range("Select range (e.g. 2-20): ")

    if start > end:
        start, end = end, start

    cards.load_cards("quiz_cards.json")

    filtered = [
        c for c in cards.study_bank
        if start <= int(c.get("id", 0)) <= end
    ]

    if not filtered:
        print("No cards in that range.")
        return

    random.shuffle(filtered)
    run_quiz(filtered)
#------------------------------------
    print("\nDEBUG IDS:")
    