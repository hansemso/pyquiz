import tkinter as tk
import re

_root = None
_label = None

_ui_font = "Consolas"
_cjk_font = "Malgun Gothic"


def _has_cjk(text):
    return re.search(r'[\u4e00-\u9fff]', text) is not None


def init(root):
    global _root, _label

    _root = root

    _label = tk.Label(
        _root,
        text="TEST",
        font=(_ui_font, 40),
        bg="white",
        fg="black"
    )

    _label.pack(expand=True, fill="both")
    _label.lift()

    _root.update_idletasks()


def show(text, font_size=40):
    global _root, _label

    if _root is None or _label is None:
        raise RuntimeError("display.init(root) must be called first")

    font = _cjk_font if _has_cjk(text) else _ui_font

    _label.config(text=text, font=(font, font_size))

    _label.lift()
    _root.update_idletasks()
    _root.update()

    print("POPUP:", text)


def close():
    global _root
    if _root:
        _root.destroy()
        _root = None