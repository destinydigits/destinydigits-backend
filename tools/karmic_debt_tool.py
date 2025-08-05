from tools.numerology_core import extract_full_numerology
from datetime import datetime

def run_karmic_debt_tool(name, dob):
    try:
        if not name or not dob:
            raise ValueError("Name and DOB are required")

        numerology = extract_full_numerology(name, dob)

        # Check karmic debt numbers
        birth_day = int(datetime.strptime(dob, "%Y-%m-%d").day)

        karmic_debt_candidates = [
            birth_day,
            numerology.get("life_path"),
            numerology.get("destiny_number"),
            numerology.get("expression_number"),
            numerology.get("heart_number"),
        ]

        karmic_debt_numbers = [13, 14, 16, 19]
        debt_numbers = [n for n in karmic_debt_candidates if n in karmic_debt_numbers]

        # Message definitions
        karmic_meanings = {
            13: "Work through laziness, procrastination, and ego. Success will come only through discipline and hard work.",
            14: "Struggles with freedom, overindulgence, and control. Learn balance, patience, and responsibility.",
            16: "Ego breakdown, shattered illusions. It's about spiritual awakening through letting go of false identities.",
            19: "Learn selflessness and humility. You may feel isolated until you embrace interdependence."
        }

        if debt_numbers:
            summary = f"You carry Karmic Debt Number(s): {', '.join(str(n) for n in debt_numbers)}.\nKarmic Debt Numbers reflect lessons from past lives. If present, they indicate specific challenges you are here to overcome and grow from."
            challenges = [karmic_meanings[n] for n in debt_numbers if n in karmic_meanings]
            summary += "\n\nChallenges linked to your number(s):\n- " + "\n- ".join(challenges)
            main_number = debt_numbers[0]
        else:
            summary = "You do not carry any specific karmic debt number. You are here to build new growth patterns in this lifetime."
            debt_numbers = []
            main_number = 0

        return {
            "tool": "karmic-debt-check",
            "name": name,
            "dob": dob,
            "mainNumber": main_number,
            "mainPercentage": 0,
            "emoji": "🌿",
            "title": "Karmic Debt Check",
            "summary": summary,
            "debtNumbers": debt_numbers
        }

    except Exception as e:
        return {
            "tool": "karmic-debt-check",
            "name": name,
            "dob": dob,
            "mainNumber": 0,
            "mainPercentage": 0,
            "emoji": "❌",
            "title": "Karmic Debt Check",
            "summary": f"Something went wrong: {str(e)}",
            "debtNumbers": []
        }
