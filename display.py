import tkinter as tk

_root = None
_text = None
_initialized = False


def init():
    global _root, _text, _initialized

    if _initialized:
        return

    _root = tk.Tk()
    _root.title("PyQuiz")

    _root.geometry("900x600")
    _root.minsize(400, 300)

    # IMPORTANT FIX:
    # wrap="none" prevents diagram scrambling
    _text = tk.Text(
        _root,
        font=("Consolas", 24),
        wrap="none",
        padx=20,
        pady=20
    )

    _text.pack(expand=True, fill="both")

    _initialized = True


def show(text, font_size=28):
    global _text, _root, _initialized

    if not _initialized:
        init()

    _text.config(state="normal")
    _text.delete("1.0", tk.END)

    _text.insert(tk.END, text)

    _text.config(font=("Consolas", font_size))
    _text.config(state="disabled")

    _root.update()