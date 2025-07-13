import json
import random
import os

BASE_DIR = os.path.dirname(__file__)
HOROSCOPE_PATH = os.path.join(BASE_DIR, "horoscope_data")

def load_horoscope(number: str, type_: str):
    type_ = type_.lower()
    if type_ not in ["daily", "monthly", "yearly"]:
        return {"error": "Invalid type"}, 400

    file_path = os.path.join(HOROSCOPE_PATH, f"{type_}.json")

    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except Exception:
        return {"error": "Could not load horoscope file"}, 500

    if number not in data:
        return {"error": "Invalid number"}, 400

    entry = data[number]

    # Random message selection
    if type_ == "daily":
        message = random.choice(entry["horoscope"])
        return {
            "number": int(number),
            "type": type_,
            "message": message,
            "luckyColor": entry.get("luckyColor"),
            "todayTip": entry.get("todayTip")
        }

    elif type_ == "monthly" or type_ == "yearly":
        message = random.choice(entry) if isinstance(entry, list) else entry
        return {
            "number": int(number),
            "type": type_,
            "message": message
        }
