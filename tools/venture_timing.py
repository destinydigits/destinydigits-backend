from .numerology_core import extract_full_numerology
from datetime import datetime

def get_essence_number(year, expression_number):
    return (year + expression_number) % 9 or 9

def get_pinnacle_number(year, heart_number):
    return (year + heart_number) % 9 or 9

def run(name, dob):
    try:
        full = extract_full_numerology(name, dob)
        expression = full.get("expression_number")
        heart = full.get("heart_number")

        if not expression or not heart:
            return {"error": "Missing core numerology numbers"}

        current_year = datetime.today().year
        current_essence = get_essence_number(current_year, expression)
        current_pinnacle = get_pinnacle_number(current_year, heart)

        summary = (
            f"Essence Number for {current_year}: {current_essence}\n"
            f"Pinnacle Number for {current_year}: {current_pinnacle}\n\n"
            "This year aligns your spiritual and external energies. "
            "If both numbers are high (like 8 or 9), it's a strong year to launch your venture. "
            "If they're lower, it may be a time for planning and groundwork."
        )

        return {
            "tool": "venture-timing",
            "name": name,
            "dob": dob,
            "title": "📈 Best Time to Start Venture",
            "summary": summary,
            "mainNumber": current_essence,
            "score": ""  # Prevent Compatibility Score from appearing
        }

    except Exception as e:
        return {"error": str(e)}
