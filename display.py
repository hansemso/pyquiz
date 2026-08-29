import tkinter as tk
import tkinter.font as tkfont

_root = None
_text = None
_initialized = False


def init():
    global _root, _text, _initialized

    if _initialized:
        return

    _root = tk.Tk()
    _root.title("PyQuiz")

    # Small popup
    _root.geometry("500x350")
    _root.minsize(350, 250)

    _text = tk.Text(
        _root,
        font=("Consolas", 12),
        wrap="none",
        padx=10,
        pady=10,
        borderwidth=0
    )

    _text.pack(
        expand=True,
        fill="both"
    )

    _initialized = True


def show(text, font_size=28):
    global _text, _root

    if not _initialized:
        init()

    _text.config(state="normal")
    _text.delete("1.0", tk.END)
    _text.insert("1.0", text)

    # Force Tkinter to calculate the actual widget size
    _root.update_idletasks()

    available_width = _text.winfo_width() - 25

    # Use the actual Consolas font metrics
    size = font_size

    while size > 8:

        test_font = tkfont.Font(
            family="Consolas",
            size=size
        )

        longest_line = max(
            text.splitlines(),
            key=len,
            default=""
        )

        text_width = test_font.measure(longest_line)

        if text_width <= available_width:
            break

        size -= 1

    _text.config(
        font=("Consolas", size)
    )

    _text.config(state="disabled")

    _root.update_idletasks()