import json

path = "quiz_cards.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

for c in data:
    # remove old system fields
    c.pop("followup_qa", None)
    c.pop("pdf", None)

    # ensure required structure exists
    c.setdefault("qa", [])
    c.setdefault("answer", "")
    c.setdefault("shuffle_qa", True)

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ JSON cleaned")