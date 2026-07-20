import random
import cards
import display

DEBUG = False


# =====================================================
# RANGE PARSER
# =====================================================

def parse_range(prompt):
    raw = input(prompt).strip()

    if "-" not in raw:
        n = int(raw)
        return n, n

    start, end = raw.split("-")
    return int(start), int(end)


# =====================================================
# ANSWER HANDLER
# =====================================================
def get_answer(prompt, multiline=False):
    if multiline:
        return cards.multiline_input(prompt)

    ans = input(prompt).strip()

    if ans.lower() in ("q", "quit", "exit"):
        return "__EXIT__"

    return ans


# =====================================================
# AUTO FONT RULES
# =====================================================
def font_for(text):
    if not text:
        return 28

    # Hanja
    if any('\u4e00' <= c <= '\u9fff' for c in text):
        return 60

    # Diagram
    if "\n" in text:
        return 22

    return 28


# =====================================================
# MAIN QUIZ ENGINE
# =====================================================
def run_quiz(cards_list):

    score = 0
    total = 0

    # filter valid cards
    cards_list = [
        c for c in cards_list
        if isinstance(c.get("qa"), list) and len(c.get("qa")) > 0
    ]

    if not cards_list:
        print("No quiz questions.")
        return

    for card in cards_list:

        # =====================================================
        # TYPE II (MULTILINE)
        # =====================================================
        if card.get("type") == "II":
            print("\n" + card.get("code", "<no code>"))

            user_ans = get_answer(
                "Answer (END to finish, or q to quit):",
                multiline=True
            )

            if user_ans == "__EXIT__":
                print("\n↩ Returning to menu...")
                return

            total += 1
            correct = card.get("answer", "")

            if cards.normalize(user_ans) == cards.normalize(correct):
                print("✅ Correct")
                score += 1
            else:
                print("❌ Incorrect")
                print(correct)

            continue

        # =====================================================
        # TYPE I
        # =====================================================
        code = card.get("code", "")
        if code:
            print("\n" + code)

        qa_list = card.get("qa") or []

        if card.get("shuffle_qa", True):
            random.shuffle(qa_list)

        # =====================================================
        # CARD-LEVEL POPUP (diagram / stored popup)
        # =====================================================
        popup = card.get("popup", "")

        if popup.strip():
            display.show(popup, font_size=font_for(popup))

        for qa in qa_list:

            q = qa.get("question", "")
            a = qa.get("answer", "")

            print(f"\nQ: {q}")

            # =================================================
            # AUTO HANJA FALLBACK (IMPORTANT FIX)
            # =================================================
            if any('\u4e00' <= c <= '\u9fff' for c in q):
                display.show(q, font_size=60)

            user_ans = get_answer("Answer > ", multiline=False)

            if user_ans == "__EXIT__":
                print("\n↩ Returning to menu...")
                return

            total += 1

            if cards.normalize(user_ans) == cards.normalize(a):
                print("✅ Correct")
                score += 1
            else:
                print(f"❌ {a}")

    print(f"\nFINAL SCORE: {score} / {total}")


# =====================================================
# QUIZ RANGE
# =====================================================
def quiz_range():

    def safe_int(x):
        try:
            return int(x)
        except:
            return -1

    start, end = parse_range("Select range (e.g. 2-20): ")

    if start > end:
        start, end = end, start

    filtered = []

    for c in cards.study_bank:
        cid = safe_int(c.get("id"))
        if start <= cid <= end:
            filtered.append(c)

    if not filtered:
        print("No cards in that range.")
        return

    random.shuffle(filtered)
    run_quiz(filtered)