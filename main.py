import sys
import cards
import quiz

cards.load_cards()

def main_menu():
    while True:
        print("\n1. Quiz All Cards\n2. Quiz Range\n3. Add Card\n4. Edit Card\n5. Exit")
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
            sys.exit(0)

if __name__ == "__main__":
    main_menu()