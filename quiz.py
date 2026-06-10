# quiz.py  6_8_2026

DEBUG = False

import random
import cards
import display


# =====================================================
# PARSE RANGE
# =====================================================

def parse_range(prompt):
    raw = input(prompt).strip()

    if "-" not in raw:
        n = int(raw)
        return n, n

    start, end = raw.split("-")
    return int(start), int(end)


# =====================================================
# SAFE DISPLAY WRAPPER (ONLY INTERFACE USED BY ENGINE)
# =====================================================


def render_question(q, qa):

    mode = qa.get("display", "text").lower()

    # ALWAYS CLI
    print(f"\nQ: {q}")

    # GUI ONLY if explicitly asked
    if mode == "gui":
        display.show(q, font_size=35, width=400, height=200)


# =====================================================
# ASK INPUT (UNIFIED)
# =====================================================
def get_answer(prompt, multiline=False):
    if multiline:
        return cards.multiline_input(prompt)
    return input(prompt).strip()


# =====================================================
# MAIN QUIZ ENGINE
# =====================================================




def run_quiz(cards_list):  # For both Type I AND II
    if DEBUG:
        for card in cards_list:
            print("CARD CHECK QA:", card.get("id"), card.get("qa"))
        
        

    score = 0
    total = 0

    # FILTER valid cards
    cards_list = [
        c for c in cards_list
        if isinstance(c.get("qa"), list) and len(c.get("qa")) > 0
    ]




    if not cards_list:
        print("No quiz questions.")
        return


    for card in cards_list:

        if DEBUG:
            print("CARD ID:", card.get("id"))
            print("QA COUNT:", len(card.get("qa", [])))

        # --------------------- 
        # TYPE II part of def run_quiz above
        # ---------------------
        
        if card.get("type") == "II":
            print("\n" + card.get("code", "<no code>"))

            user_ans = get_answer(
                "mline Answer (END to finish):",
                multiline=True
            )

            total += 1

            correct = card.get("answer", "")  # correct defined

            if cards.normalize(user_ans) == cards.normalize(correct):  # def normalize in cards.py 1.Utility
                print("✅ Correct")
                score += 1
            else:
                print("❌ Incorrect")
                print("\nCorrect answer:")
                print(correct)

            continue


        
        
# =========================
# TYPE I MODE
# =========================

        

        # ALWAYS show code/context first

        code = card.get("code", "")  #       ***code = card.get***



        if code:
            print("\n" + code)

        qa_list = card.get("qa") or []

        if DEBUG:
            print("TYPE I QA LENGTH:", len(qa_list))
            if qa_list:
                print("FIRST QA ITEM:", qa_list[0])
            else:
                print("⚠️ EMPTY QA LIST")
        
        
        

        if card.get("shuffle_qa", True):
            random.shuffle(qa_list)

        for qa in qa_list:

            q = qa.get("question", "")
            a = qa.get("answer", "")

            print(f"\nQ: {q}")

            user_ans = get_answer("Answer > ", multiline=False)

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

    try:
        start, end = parse_range("Select range (e.g. 2-20): ")
    except ValueError:
        print("Invalid input format. Use like 10-20")
        return

    if start > end:
        start, end = end, start
    
    
    
    if DEBUG:
        print("DEBUG RANGE:", start, end)

    filtered = []

    for c in cards.study_bank:
        cid = safe_int(c.get("id"))

        if DEBUG:
            print("RAW CARD:", c.get("id"), "->", cid)

        if start <= cid <= end:
            filtered.append(c)
            
    if DEBUG:
        print("FILTERED COUNT:", len(filtered))

    if not filtered:
        print("No cards in that range.")
        return

    random.shuffle(filtered)
    run_quiz(filtered)

    
    if DEBUG:
        print("\nDEBUG IDS COMPLETE")