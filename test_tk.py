import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="START", font=("Consolas", 40))
label.pack()

def step(i=0):
    label.config(text=str(i))
    print("set:", i)

    if i < 4:
        root.after(1000, lambda: step(i+1))

step()
root.mainloop()