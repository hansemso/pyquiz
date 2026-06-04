# quiz.py   May 31, 2026
import random
import cards
import pdf_viewer
from cards import multiline_input






def run_quiz(cards_list):    
    score = 0
    total = 0

    # only cards with QA or Type II
    cards_list = [
        c for c in cards_list
        if (
            (c.get("type", "I") == "I" and c.get("qa"))
            or
            (c.get("type") == "II")
        )
    ]

    if not cards_list:
        print("No quiz questions.")
        return

    for card in cards_list:

        print("\n" + card.get("code", "<no code>"))

        # ==========================
        # PDF (ALL TYPES)
        # ==========================
        
        has_pdf = bool(card.get("pdf"))

        if has_pdf:
            user = input(
                "[p] open PDF / Enter to continue > "
            ).strip().lower()

            if user == "p":
                pdf_viewer.open_from_card(card)

        card_type = card.get("type", "I")

        # ==========================
        # TYPE II
        # ==========================
        if card_type == "II":

            total += 1

            ans = multiline_input(            # User input object
                "\nAnswer (END to finish): "
            )





            # User answer object
            correct = card.get("answer", "")  # card["answer"] from JSON-loaded data, i.e. a json loaded object


# debugging block left in for now  
# repr() returns unformatted string representation of an object, incl hidden characters. debug mode of print(). 

            print("---- USER RAW ----")  # RAW == unformatted str
            print(repr(ans))  # ans is input from user above

            print("---- EXPECTED RAW ----")
            print(repr(correct))  # correct == user object answer from above from json

            print("---- USER LENGTH ----", len(ans))  # len checks for extra spaces, newlines, etc
            print("---- EXPECTED LENGTH ----", len(correct))  # compare discrepancy between user input and json output
#


            if cards.normalize(ans) == cards.normalize(correct):
                print("✅ Correct")
                score += 1
            else:
                print("\n❌ Expected:\n")
                print(correct)

            followup = card.get("followup_qa", [])

            for qa in followup:

                total += 1

                ans = input(
                    f"\nQ: {qa['question']}\nAnswer > "
                ).strip()

                if cards.normalize(ans) == cards.normalize(qa["answer"]):
                    print("✅ Correct")
                    score += 1
                else:
                    print(f"❌ {qa['answer']}")

            continue

        # ==========================
        # TYPE I
        # ==========================
        qa_list = card.get("qa", []).copy()

        if card.get("shuffle_qa", True):
            random.shuffle(qa_list)
    
        for qa in qa_list:

            total += 1

            ans = input(
                f"Q: {qa['question']}\nAnswer > "
            ).strip()

            if cards.normalize(ans) == cards.normalize(qa["answer"]):
                print("✅ Correct")
                score += 1
            else:
                print(f"❌ {qa['answer']}")

    print(f"\nScore: {score} / {total}")



def quiz_range():
    cards.load_cards()

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

    random.shuffle(filtered)

    run_quiz(filtered)
    