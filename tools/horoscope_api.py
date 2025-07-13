import json
import random
import os

def load_horoscope(number: str, type_: str):
    try:
        file_path = os.path.join(os.path.dirname(__file__), "horoscope_data", f"{type_}.json")

        if not os.path.exists(file_path):
            return {"error": "Could not load horoscope file"}, 500

        with open(file_path, "r", encoding="utf-8") as f:
            all_data = json.load(f)

        number_data = all_data.get(str(number))
        if not number_data:
            return {"error": "No data for this number"}, 404

        selected = random.choice(number_data) if isinstance(number_data, list) else number_data

        # Handle daily format
        if isinstance(selected, dict):
            return {
                "message": selected.get("message", ""),
                "luckyColor": selected.get("luckyColor", ""),
                "todayTip": selected.get("todayTip", "")
            }

        # Handle monthly/yearly format (string list)
        if isinstance(selected, list):
            return {
                "message": "\n\n".join(selected)
            }

        # If selected is already a string
        return {"message": str(selected)}

    except Exception as e:
        return {"error": "Error parsing horoscope", "details": str(e)}, 500
