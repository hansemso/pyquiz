# quiz.py   May 27, 2026
import random
import cards
import pdf_viewer


def run_quiz(cards_list):

    score = 0
    total = 0

    # only cards with QA
    cards_list = [c for c in cards_list if c.get("qa")]

    if not cards_list:
        print("No quiz questions.")
        return
    
    
    
    for card in cards_list:

        print("\n" + card.get("code", "<no code>"))

        qa_list = card.get("qa", []).copy()

        
        # ======================================
        # QA SHUFFLE (SESSION CONTROLLED)
        # ======================================
        
        if not card.get("no_shuffle_qa", False):
            random.shuffle(qa_list)
        
        
        has_pdf = bool(card.get("pdf"))

        # ======================================
        # PDF (ONCE PER CARD)
        # ======================================
        if has_pdf:
            user = input("[p] open PDF / Enter to continue > ").strip().lower()

            if user == "p":
                pdf_viewer.open_from_card(card)

        # ======================================
        # QUIZ LOOP
        # ======================================
        for qa in qa_list:

            total += 1

            ans = input(f"Q: {qa['question']}\nAnswer > ").strip()

            if cards.normalize(ans) == cards.normalize(qa["answer"]):
                print("✅ Correct")
                score += 1
            else:
                print(f"❌ {qa['answer']}")
    print(f"\nScore: {score} / {total}")



def quiz_range():

    try:
        start = int(input("Start ID: "))
        end = int(input("End ID: "))
    except:
        print("Invalid range")
        return

    

    filtered = [
        c for c in cards.study_bank
        if start <= int(c.get("id", 0)) <= end
    ]

    # keeps card order randomized (optional design choice you already had)
    random.shuffle(filtered)

    run_quiz(filtered)
    