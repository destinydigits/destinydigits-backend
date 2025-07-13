import json
import random
import os

def load_horoscope(number: str, type_: str):
    file_path = f"horoscope_data/{type_}.json"
    if not os.path.exists(file_path):
        return {"error": "Could not load horoscope file"}, 500

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        options = data.get(str(number))
        if not options:
            return {"error": "Invalid number or content missing"}, 400

        selected = random.choice(options) if isinstance(options, list) else options

        if type_ == "daily":
            return {
                "message": selected.get("message", ""),
                "luckyColor": selected.get("luckyColor", ""),
                "todayTip": selected.get("todayTip", "")
            }

        # for monthly/yearly: join list into string
        return {
            "message": "\n\n".join(selected) if isinstance(selected, list) else str(selected)
        }

    except Exception as e:
        return {"error": "Error parsing horoscope file", "details": str(e)}, 500
