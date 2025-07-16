from .numerology_core import extract_full_numerology
from datetime import datetime

def get_essence_number(year, expression_number):
    return (year + expression_number) % 9 or 9

def get_pinnacle_number(year, heart_number):
    return (year + heart_number) % 9 or 9

def run(name, dob):
    try:
        full = extract_full_numerology(name, dob)
        expression = full.get("expression_number") or full.get("expressionNumber")
        heart = full.get("heart_number") or full.get("heartNumber")

        if not expression or not heart:
            return {
                "tool": "venture-timing",
                "name": name,
                "dob": dob,
                "title": "Best Time to Start Venture",
                "summary": "⚠️ Missing core numerology numbers.",
                "mainNumber": 0,
                "score": ""
            }

        current_year = datetime.today().year
        essence = get_essence_number(current_year, expression)
        pinnacle = get_pinnacle_number(current_year, heart)

        summary = (
            f"🧭 Essence Number for {current_year}: {essence}\n"
            f"🏔️ Pinnacle Number for {current_year}: {pinnacle}\n\n"
            "This year reflects your internal and external alignment.\n"
            "- High numbers (7, 8, 9): Strong year to begin.\n"
            "- Medium (4, 5, 6): Plan + slow build.\n"
            "- Low (1, 2, 3): Start groundwork but delay final launch."
        )

        return {
            "tool": "venture-timing",
            "name": name,
            "dob": dob,
            "title": "📈 Best Time to Start Venture",
            "summary": summary,
            "mainNumber": essence,
            "score": ""  # Prevent Compatibility Score from appearing
        }

    except Exception as e:
        return {
            "tool": "venture-timing",
            "name": name,
            "dob": dob,
            "title": "Best Time to Start Venture",
            "summary": f"Error occurred: {str(e)}",
            "mainNumber": 0,
            "score": ""
        }
