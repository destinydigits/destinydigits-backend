from datetime import datetime
from tools.numerology_core import get_challenge_numbers, get_primary_challenge_number, challenge_profile

def run_current_challenge(data):
    try:
        name = data.get("name")
        dob = data.get("dob")

        if not name or not dob:
            raise ValueError("Name and DOB are required")

        dob_obj = datetime.strptime(dob, "%Y-%m-%d")
        day, month, year = dob_obj.day, dob_obj.month, dob_obj.year

        # Calculate challenge numbers
        challenge_list = get_challenge_numbers(day, month, year)
        current_challenge = get_primary_challenge_number(challenge_list)

        if not current_challenge or current_challenge not in challenge_profile:
            raise ValueError("Challenge number could not be determined")

        profile = challenge_profile[current_challenge]
        struggle = profile.get("struggle", "No struggle info available.")
        tip = profile.get("resolutionTip", "No tip available.")

        return {
            "tool": "current-challenge",
            "name": name,
            "dob": dob,
            "mainNumber": current_challenge,
            "mainPercentage": current_challenge * 10,
            "emoji": "⚔️",
            "title": "Your Current Life Challenge",
            "summary": f"You are currently facing Challenge Number {current_challenge}. This reflects your key personal struggle or growth phase.",
            "challengeMeaning": struggle,
            "healingTip": tip
        }

    except Exception as e:
        return {
            "tool": "current-challenge",
            "name": data.get("name"),
            "dob": data.get("dob"),
            "mainNumber": 0,
            "mainPercentage": 0,
            "emoji": "❌",
            "title": "Your Current Life Challenge",
            "summary": f"Something went wrong: {str(e)}",
            "challengeMeaning": "",
            "healingTip": ""
        }
