from numerology_core import extract_full_numerology
from utils import get_expression_number, get_destiny_number, get_vibration_compatibility

def run_name_correction_tool(name, dob):
    try:
        # Extract numbers
        numerology = extract_full_numerology(name, dob)
        expression = numerology.get("expression_number")
        destiny = numerology.get("destiny_number")

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

        # Optional suggestions (currently free)
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
            "suggestions": suggestions  # Example: ['T', 'R', 'A']
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


# Helper function
def suggest_letters_to_add(name, expression, destiny):
    # Dummy logic: try appending letters A-Z, recalc expression, return those matching destiny
    from string import ascii_uppercase
    from numerology_core import get_expression_number

    ideal_letters = []
    for ch in ascii_uppercase:
        new_name = name + ch
        new_expr = get_expression_number(new_name)
        if new_expr == destiny:
            ideal_letters.append(ch)

    return ideal_letters[:5]  # limit to top 5
