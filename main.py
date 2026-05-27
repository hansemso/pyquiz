# main.py  May 2026 
import sys
import cards
import quiz

# UTF-8 console support
sys.stdout.reconfigure(encoding='utf-8')

cards.load_cards()


def main_menu():

    while True:

        print("\n1. Quiz All Cards")
        print("2. Quiz Range")
        print("3. Add Card")
        print("4. Edit Card")
        print("5. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            quiz.quiz_all()

        elif choice == "2":
            quiz.quiz_range()

        elif choice == "3":
            cards.add_study_card()

        elif choice == "4":
            cards.edit_card()

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("❌ Invalid option.")


# ---------------------------------
# CLEAN CTRL+C EXIT
# ---------------------------------
if __name__ == "__main__":

    try:
        main_menu()

    except KeyboardInterrupt:
        print("\n\nExiting PyQuiz...")