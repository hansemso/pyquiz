# main.py  May 2026 
import tkinter as tk
import display
import sys
import cards
import quiz

sys.stdout.reconfigure(encoding='utf-8')

root = tk.Tk()
root.title("PyQuiz")

display.init(root)

display.show("HELLO")

root.update_idletasks()
root.update()


cards.load_cards("quiz_cards.json")




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
            cards.load_cards("quiz_cards.json")
            quiz.quiz_range()
        elif choice == "2":
            cards.add_study_card()
        elif choice == "3":
            cards.edit_card() # Links cards.load_cards() above to edit_card in cards.py
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