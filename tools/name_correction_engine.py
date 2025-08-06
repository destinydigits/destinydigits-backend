from tools.numerology_core import extract_full_numerology
from string import ascii_uppercase

def run_name_correction_tool(data):
    name = data.get("name")
    dob = data.get("dob")
    try:
        numerology = extract_full_numerology(name, dob)
        expression = numerology.get("expression_number")
        destiny = numerology.get("destiny_number") or numerology.get("destinyNumber")

        if not expression or not destiny:
            return {
                "tool": "name-correction",
                "name": name,
                "dob": dob,
                "mainNumber": 0,
                "mainPercentage": 0,
                "title": "Name Correction",
                "summary": "Unable to calculate your name or destiny vibration. Please recheck your input.",
                "emoji": "❌"
            }

        # Compatibility logic
        vibe, score, message = get_vibration_compatibility(expression, destiny)

        # Suggestions (currently free)
        suggestions = suggest_letters_to_add(name, expression, destiny)

        return {
            "tool": "name-correction",
            "name": name,
            "dob": dob,
            "mainNumber": score,
            "mainPercentage": score,
            "title": "Name Correction",
            "emoji": "🔤" if score >= 70 else "⚠️",
            "summary": f"{message}\n\nYour name currently vibrates at {expression}, while your destiny is {destiny}. This creates certain energetic blocks in your life path.",
            "vibe": vibe,
            "syncMessage": "Want to enhance your vibration? Try these letter additions for better alignment.",
            "suggestions": suggestions
        }

    except Exception as e:
        return {
            "tool": "name-correction",
            "name": name,
            "dob": dob,
            "mainNumber": 0,
            "mainPercentage": 0,
            "title": "Name Correction",
            "summary": f"Something went wrong: {str(e)}",
            "emoji": "❌"
        }

# Simple compatibility logic
def get_vibration_compatibility(expression, destiny):
    friendly_pairs = {
        1: [1, 5, 7], 2: [2, 4, 8], 3: [3, 6, 9],
        4: [2, 4, 8], 5: [1, 5, 7], 6: [3, 6, 9],
        7: [1, 5, 7], 8: [2, 4, 8], 9: [3, 6, 9]
    }

    if expression == destiny:
        return "Perfect Match", 95, "Your name and destiny are in perfect alignment — a powerful flow of success and clarity."
    elif destiny in friendly_pairs.get(expression, []):
        return "Good Vibration", 80, "Your name supports your destiny well, bringing helpful energy and alignment."
    else:
        return "Misaligned Vibration", 65, "There’s a mismatch between your name and destiny — it may cause emotional or professional friction."

# Letter suggestion logic
def suggest_letters_to_add(name, expression, destiny):
    ideal_letters = []
    formatted_suggestions = []

    for ch in ascii_uppercase:
        new_name = name + ch
        new_expr = get_expression_number(new_name)
        if new_expr == destiny:
            ideal_letters.append(ch)

    # Format output without examples
    for ch in ideal_letters[:5]:
        formatted_suggestions.append(f"Try adding one extra '{ch}' to your name")

    return formatted_suggestions

# Expression Number calculator
def get_expression_number(name):
    letter_map = {
        'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
        'J':1, 'K':2, 'L':3, 'M':4, 'N':5, 'O':6, 'P':7, 'Q':8, 'R':9,
        'S':1, 'T':2, 'U':3, 'V':4, 'W':5, 'X':6, 'Y':7, 'Z':8
    }

    name = name.upper()
    total = sum(letter_map.get(char, 0) for char in name if char.isalpha())

    # Reduce unless master number
    while total not in [11, 22, 33] and total > 9:
        total = sum(int(d) for d in str(total))

    return total
