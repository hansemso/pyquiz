import os
import subprocess


def find_foxit():
    possible_paths = [
        r"C:\Program Files\Foxit Software\Foxit PDF Reader\FoxitPDFReader.exe",
        r"C:\Program Files (x86)\Foxit Software\Foxit PDF Reader\FoxitPDFReader.exe",
        r"C:\Program Files\Foxit Software\Foxit PDF Reader\FoxitPDFEditor.exe",
    ]

    for p in possible_paths:
        if os.path.exists(p):
            return p

    return None


def open_from_card(card):

    pdf = card.get("pdf")

    if not pdf:
        print("❌ No PDF attached.")
        return

    base_dir = os.path.dirname(__file__)
    pdf_path = os.path.join(base_dir, pdf)

    if not os.path.exists(pdf_path):
        print("❌ PDF not found:", pdf_path)
        return

    foxit = find_foxit()

    if not foxit:
        print("❌ Foxit not found on system.")
        return

    try:
        subprocess.Popen([foxit, pdf_path])
        print("✅ Opened in Foxit")

    except Exception as e:
        print("❌ Failed to open Foxit:", e)