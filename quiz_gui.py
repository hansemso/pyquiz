import tkinter as tk
from cards import load_cards
import display

cards = load_cards()
i = 0

root = tk.Tk()
root.title("PyQuiz GUI")

display.init(root)   # ONLY ONCE

entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)

status = tk.Label(root, text="", font=("Arial", 12))
status.pack()


# ----------------------------
# SHOW CARD
# ----------------------------


def show_card():
    global i

    if i >= len(cards):
        display.show("DONE", font_size=60)
        status.config(text="Finished")
        return

    card = cards[i]

    print("CALLING DISPLAY:", card["q"])

    display.show(card["q"], font_size=60)

    status.config(text=f"Card {i+1}/{len(cards)}")
    
    
    
    
# ----------------------------
# SUBMIT ANSWER
# ----------------------------



def submit():
    global i

    ans = entry.get().strip()
    card = cards[i]

    if ans.lower() == "q":
        root.destroy()
        return

    if ans == card["a"]:
        status.config(text="✔ Correct")
    else:
        status.config(text=f"❌ {card['a']}")

    i += 1
    entry.delete(0, tk.END)
    show_card()


# ----------------------------
# BUTTONS
# ----------------------------
tk.Button(root, text="Submit", command=submit).pack()

tk.Button(root, text="Quit", command=root.destroy).pack()


# ----------------------------
# START
# ----------------------------
show_card()
root.mainloop()