# tools/birthday_year_tool.py

import json
import os
from datetime import datetime
from tools.numerology_core import extract_full_numerology

# Load JSON from correct file
with open(os.path.join("tools", "annual_vibration.json"), "r") as f:
    INSIGHT_PARAGRAPHS = json.load(f)

def reduce_number(n):
    while n > 9 and n not in (11, 22, 33):
        n = sum(int(d) for d in str(n))
    return n

def get_annual_vibration_number(dob_str: str, today: datetime = None) -> int:
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    today = today or datetime.today()
    day, month = dob.day, dob.month
    year = today.year
    return reduce_number(day + month + year)

def run_birthday_year_prediction(name: str, dob: str) -> dict:
    try:
        numerology = extract_full_numerology(name, dob)
        life_path = numerology.get("life_path")
        heart_number = numerology.get("heartNumber")
        vibration = get_annual_vibration_number(dob)

        # Birthday range generation
        today = datetime.today()
        birth = datetime.strptime(dob, "%Y-%m-%d")
        this_year = today.year

        start = datetime(this_year, birth.month, birth.day)
        if today >= start:
            end = datetime(this_year + 1, birth.month, birth.day)
        else:
            start = datetime(this_year - 1, birth.month, birth.day)
            end = datetime(this_year, birth.month, birth.day)

        period_str = f"{start.strftime('%d %B %Y')} to {end.strftime('%d %B %Y')}"

        return {
            "tool": "birthday-year-prediction",
            "title": "🎉 Personalized Birthday Year Report",
            "name": name,
            "dob": dob,
            "lifePath": life_path,
            "heartNumber": heart_number,
            "annualVibration": vibration,
            "mainNumber": vibration,
            "mainPercentage": 100,
            "period": period_str,
            "paragraphs": {
                "intro": f"🎉 Happy Birthday {name}! This new cycle brings a fresh opportunity to step into your true nature.",
                "lifePathInsight": INSIGHT_PARAGRAPHS["life_path"].get(str(life_path), "No Life Path insight found."),
                "heartInsight": INSIGHT_PARAGRAPHS["heart_number"].get(str(heart_number), "No Heart Number insight found."),
                "birthdayYearInsight": INSIGHT_PARAGRAPHS["annual_vibration"].get(str(vibration), "No Annual Vibration message found."),
                "quote": INSIGHT_PARAGRAPHS.get("quote", "")
            }
        }

    except Exception as e:
        return {
            "tool": "birthday-year-prediction",
            "error": "Something went wrong while generating the report.",
            "details": str(e)
        }
