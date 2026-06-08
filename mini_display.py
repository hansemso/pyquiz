# display.py
import tkinter as tk

def show(text, font_size=48, width=300, height=200, timeout=None):
    root = tk.Tk()
    root.title("Display")
    root.geometry(f"{width}x{height}")
    root.configure(bg="white")

    label = tk.Label(
        root,
        text=text,
        font=("Arial", font_size),
        bg="white"
    )
    label.pack(expand=True)

    # optional auto-close
    if timeout:
        root.after(timeout, root.destroy)

    root.mainloop()