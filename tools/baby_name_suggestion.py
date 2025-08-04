import json
import random
import os
from tools.numerology_core import extract_full_numerology

# File path
BABY_NAME_PATH = os.path.join(os.path.dirname(__file__), "baby_names.json")

def run_baby_name_suggestion(dob, gender):
    try:
        if not dob or not gender:
            raise ValueError("DOB and gender are required")

        gender = gender.lower()
        if gender not in ["male", "female"]:
            raise ValueError("Invalid gender")

        # Load name data
        with open(BABY_NAME_PATH, "r") as f:
            name_data = json.load(f)

        names = name_data.get(gender, [])
        if not names:
            raise ValueError("No names available for selected gender")

        # Get destiny number from existing numerology engine
        destiny = extract_full_numerology("Baby", dob).get("destinyNumber") or 0

        # Filter names that match destiny number
        matching_names = []
        for name in names:
            expr = extract_full_numerology(name, dob).get("expression_number")
            if expr == destiny:
                matching_names.append(name)

        if not matching_names:
            raise ValueError("No matching names found for destiny number")

        # Pick up to 3 matching names
        final_names = random.sample(matching_names, min(3, len(matching_names)))

        name_blocks = []
        for name in final_names:
            message = f"{name} vibrates with number {destiny}, which aligns beautifully with your baby's life path. It supports their natural growth and soul purpose."
            name_blocks.append({
                "name": name,
                "number": destiny,
                "message": message
            })

        return {
            "tool": "baby-name-suggestion",
            "dob": dob,
            "gender": gender,
            "mainNumber": destiny,
            "mainPercentage": 80 + destiny,
            "title": "Baby Name Suggestion",
            "emoji": "👶",
            "summary": f"Your baby’s Destiny Number is {destiny}. Below are names that align harmoniously with this life path number.",
            "suggestions": name_blocks
        }

    except Exception as e:
        return {
            "tool": "baby-name-suggestion",
            "dob": dob,
            "gender": gender,
            "mainNumber": 0,
            "mainPercentage": 0,
            "title": "Baby Name Suggestion",
            "emoji": "❌",
            "summary": f"Something went wrong: {str(e)}",
            "suggestions": []
        }
