import json
import os
import random

def load_horoscope(number, type_):
    number = str(number)
    try:
        folder_path = os.path.join(os.path.dirname(__file__), "horoscope_data")
        file_path = os.path.join(folder_path, f"{type_}.json")

        if not os.path.exists(file_path):
            return {"error": "Could not load horoscope file"}, 500

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if number not in data:
            return {"error": "Invalid number"}, 400

        entry = data[number]

        # 🟢 DAILY
        if type_ == "daily" and isinstance(entry, dict):
            messages = entry.get("horoscope", [])
            message = random.choice(messages) if messages else "No message available."
            return {
                "message": message,
                "luckyColor": entry.get("luckyColor", ""),
                "todayTip": entry.get("todayTip", "")
            }

        # 🟢 MONTHLY
        if type_ == "monthly" and isinstance(entry, list):
            message = random.choice(entry)
            return {
                "message": message,
                "luckyColor": None,
                "todayTip": None
            }

        # 🟢 YEARLY
        if type_ == "yearly" and isinstance(entry, list):
            message = random.choice(entry)
            return {
                "message": message,
                "luckyColor": None,
                "todayTip": None
            }

        return {"error": "Invalid horoscope format"}

    except Exception as e:
        return {"error": "Internal server error", "details": str(e)}, 500
