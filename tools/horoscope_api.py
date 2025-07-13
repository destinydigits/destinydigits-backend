import os
import json
import random

def load_horoscope(number, type_):
    try:
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "horoscope_data", f"{type_}.json")

        if not os.path.exists(file_path):
            return {"error": "Horoscope file not found"}, 500

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if number not in data:
            return {"error": "No data for this number"}, 400

        entry = data[number]

        # For DAILY format
        if type_ == "daily" and isinstance(entry, dict):
            messages = entry.get("horoscope", [])
            message = random.choice(messages) if messages else "No message available."
            return {
                "message": message,
                "luckyColor": entry.get("luckyColor", ""),
                "todayTip": entry.get("todayTip", "")
            }

        # For MONTHLY/YEARLY: entry is list of strings
        if isinstance(entry, list):
            message = random.choice(entry)
            return {
                "message": message,
                "luckyColor": None,
                "todayTip": None
            }

        # If entry is a plain string (rare case)
        if isinstance(entry, str):
            return {
                "message": entry,
                "luckyColor": None,
                "todayTip": None
            }

        return {"message": "No horoscope found."}

    except Exception as e:
        return {"error": "Error reading horoscope", "details": str(e)}, 500
