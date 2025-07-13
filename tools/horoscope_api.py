import json
import random
import os

def load_horoscope(number, type_):
    import os, json, random

    folder = os.path.join(os.path.dirname(__file__), "horoscope_data")
    file_path = os.path.join(folder, f"{type_}.json")

    if not os.path.exists(file_path):
        return {"error": "Could not load horoscope file"}, 500

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if number not in data:
            return {"error": "Invalid number"}, 400

        entry = data[number]

        # DAILY
        if type_ == "daily":
            horoscope_list = entry.get("horoscope", [])
            message = random.choice(horoscope_list) if horoscope_list else "No message available."
            return {
                "message": message,
                "luckyColor": entry.get("luckyColor", ""),
                "todayTip": entry.get("todayTip", "")
            }

        # MONTHLY/YEARLY
        if isinstance(entry, list):
            message = random.choice(entry)
        elif isinstance(entry, str):
            message = entry
        else:
            message = "No message available."

        return {
            "message": message,
            "luckyColor": None,
            "todayTip": None
        }

    except Exception as e:
        return {"error": "Error reading horoscope", "details": str(e)}, 500
