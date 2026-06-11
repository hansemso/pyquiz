import sys
import cards
import quiz

sys.stdout.reconfigure(encoding='utf-8')

# ------------------------
# LOAD DATA
# ------------------------
cards.load_cards("quiz_cards.json")


# ------------------------
# MENU (CLI LOOP)
# ------------------------
def main_menu():
    while True:

        print("\n1. Quiz Range")
        print("2. Add Card")
        print("3. Edit Mode/Index")
        print("4. Edit Directory")
        print("5. Exit")

        choice = input("Select option: ").strip()

        print("\n====================================")
        print(cards.load_directory_note())
        print("====================================")

        if choice == "1":
            cards.load_cards("quiz_cards.json")
            quiz.quiz_range()

        elif choice == "2":
            cards.add_study_card()

        elif choice == "3":
            cards.edit_card()

        elif choice == "4":
            cards.edit_directory_note()

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("❌ Invalid option.")


# ------------------------
# START APP
# ------------------------
if __name__ == "__main__":
    main_menu()