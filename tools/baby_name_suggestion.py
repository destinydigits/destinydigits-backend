import json
import random
import os
from tools.numerology_core import extract_full_numerology

# Path to baby_names.json
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

        # Calculate destiny number
        destiny = get_destiny_number(dob)

        # Match names with same vibration
        matching_names = []
        for name in names:
            number = get_expression_number(name)
            if number == destiny:
                matching_names.append(name)

        if not matching_names:
            raise ValueError("No matching names found for this destiny number")

def get_expression_number(name):
    letter_map = {
        'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
        'J':1, 'K':2, 'L':3, 'M':4, 'N':5, 'O':6, 'P':7, 'Q':8, 'R':9,
        'S':1, 'T':2, 'U':3, 'V':4, 'W':5, 'X':6, 'Y':7, 'Z':8
    }

    name = name.upper()
    total = sum(letter_map.get(ch, 0) for ch in name if ch.isalpha())

    while total not in [11, 22, 33] and total > 9:
        total = sum(int(d) for d in str(total))

    return total

        # Pick 3 random names
        final_names = random.sample(matching_names, min(3, len(matching_names)))

        # Prepare response
        name_blocks = []
        for name in final_names:
            message = f"{name} vibrates with number {destiny}, which aligns beautifully with your baby's life path. It supports natural growth and soul expression."
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


