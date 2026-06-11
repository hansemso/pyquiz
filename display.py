import tkinter as tk

_root = None
_label = None
_initialized = False


def init():
    global _root, _label, _initialized

    if _initialized:
        return

    _root = tk.Tk()
    _root.title("PyQuiz")

    _label = tk.Label(_root, text="", font=("Consolas", 40), bg="white")
    _label.pack(expand=True, fill="both")

    _initialized = True


def show(text, font_size=40):
    global _root, _label, _initialized

    if not _initialized:
        init()

    _label.config(
        text=text,
        font=("Malgun Gothic", font_size)
    )
    _root.update_idletasks()
    _root.update()