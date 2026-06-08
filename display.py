import tkinter as tk

_root = None
_label = None

# =====================================================
# 🎛️ GLOBAL DEFAULT SETTINGS (EDIT THESE ONLY)
# =====================================================
DEFAULT_FONT = 40
DEFAULT_WIDTH = 300
DEFAULT_HEIGHT = 180

# presets (optional quick modes)
PRESETS = {
    "small":  (28, 250, 150),
    "medium": (40, 350, 200),
    "large":  (60, 500, 300),
}


def _init():
    global _root, _label

    if _root is None:
        _root = tk.Tk()
        _root.title("Display")
        _root.configure(bg="white")

        _label = tk.Label(
            _root,
            text="",
            font=("Arial", DEFAULT_FONT),
            bg="white",
            wraplength=DEFAULT_WIDTH
        )
        _label.pack(expand=True)


# =====================================================
# MAIN DISPLAY FUNCTION
# =====================================================


def show(text, font_size=60, width=400, height=200):
    global _root, _label

    _init()

    _label.config(text="")
    _root.update_idletasks()
    _label.config(text=text, font=("Arial", font_size))


    _root.geometry(f"{width}x{height}")

    _root.update_idletasks()
    _root.update()

    _root.lift()
    _root.attributes("-topmost", True)
    _root.after(150, lambda: _root.attributes("-topmost", False))