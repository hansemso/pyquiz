#display.py  6_8_2026
import tkinter as tk

_root = None
_label = None

# =====================================================
# SETTINGS
# =====================================================
DEFAULT_FONT = 40


PRESETS = {
    "small":  (28, 250, 150),
    "medium": (40, 350, 200),
    "large":  (60, 500, 300),
}


# =====================================================
# INIT WINDOW (CREATE ONCE ONLY)
# =====================================================
def _init():
    global _root, _label

    if _root is None:
        _root = tk.Tk()
        _root.title("Quiz Display")
        _root.configure(bg="white")

        _label = tk.Label(
            _root,
            text="",
            font=("Arial", DEFAULT_FONT),
            bg="white",
            wraplength=400,
            justify="center"
        )
        _label.pack(expand=True, fill="both")

        # keep window alive but non-blocking
        _root.update()


# =====================================================
# CORE DISPLAY FUNCTION
# =====================================================
def show(text, font_size=40, width=400, height=200, image=None, preset=None):

    _init()

    # presets override manual size
    if preset and preset in PRESETS:
        font_size, width, height = PRESETS[preset]

    # image hook (future expansion)
    if image:
        print("IMAGE REQUESTED:", image)

    # update content only (NO reset loop)
    _label.config(text=text, font=("Arial", font_size), wraplength=width)

    _root.geometry(f"{width}x{height}")

    _root.lift()
    _root.attributes("-topmost", True)
    _root.after(100, lambda: _root.attributes("-topmost", False))

    # IMPORTANT: only update IDLE state, not full loop
    _root.update_idletasks()


# =====================================================
# OPTIONAL: CLEAN SHUTDOWN
# =====================================================
def close():
    global _root
    if _root:
        _root.destroy()
        _root = None