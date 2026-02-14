import json
import os
import urllib.parse

# EDIT THESE:
CARDS_FOLDER = r"./Front"
BASE_URL = "https://raw.githubusercontent.com/bmartingame/cards/main/Front/"   # must end with /
DEFAULT_BACK_URL = "https://raw.githubusercontent.com/bmartingame/cards/main/Magic_card_back.jpg"

def is_image(fn: str) -> bool:
    return fn.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))

db = {}

for fn in sorted(os.listdir(CARDS_FOLDER)):
    if not is_image(fn):
        continue
    name = os.path.splitext(fn)[0]
    # URL-encode filename for safe URLs
    url_fn = urllib.parse.quote(fn)
    db[name] = {
        "face": BASE_URL + url_fn,
        "back": DEFAULT_BACK_URL
    }

with open("cards_db.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"Wrote cards_db.json with {len(db)} cards")
