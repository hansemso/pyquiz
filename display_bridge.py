import tkinter as tk
import display

_root = tk.Tk()
_root.title("PyQuiz Overlay")
_root.geometry("500x300")

display.init(_root)

def pump():
    _root.update()
    _root.after(30, pump)

pump()