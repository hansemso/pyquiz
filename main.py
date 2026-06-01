# main.py  May 2026 
import sys
import cards
import quiz

# UTF-8 console support
sys.stdout.reconfigure(encoding='utf-8')

cards.load_cards()


def main_menu():

    while True:
        
               
        print("\n1. Quiz Range")
        print("2. Add Card")
        print("3. Edit Card/View Index")
        print("4. Edit Index Directory")
        print("5. Exit")
      
        choice = input("Select option: ").strip()

        print("\n====================================")
        print(cards.load_directory_note())
        print("====================================") 
        
        if choice == "1":
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


# ---------------------------------
# CLEAN CTRL+C EXIT
# ---------------------------------
if __name__ == "__main__":

    try:
        main_menu()

    except KeyboardInterrupt:
        print("\n\nExiting PyQuiz...")