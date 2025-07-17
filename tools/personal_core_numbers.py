from tools.numerology_core import extract_full_numerology, reduce_strict, letter_to_number_pythagorean
from tools.core_number_texts import CORE_NUMBER_TEXT
from collections import Counter

def get_personal_core_number(data, tool):
    name = data.get("name", "").upper()
    dob = data.get("dob", "")

    if not name or not dob:
        return {
            "tool": tool,
            "title": "Core Number",
            "summary": "⚠️ Please enter your name and date of birth.",
            "mainNumber": 0,
            "mainPercentage": 0,
            "name": name or "—",
            "dob": dob or "—"
        }

    try:
        core = extract_full_numerology(name, dob)
        birth_day = int(dob.split("-")[2])
        life_path = core["life_path"]
        expression = core["expression_number"]
        personality = core["personality_number"]
        soul_urge = core["heartNumber"]
        maturity = reduce_strict(life_path + expression)
        birthday = reduce_strict(birth_day)

        # Hidden Passion Number
        digits = [letter_to_number_pythagorean(c) for c in name if c.isalpha()]
        hidden = Counter(digits).most_common(1)[0][0] if digits else None

        # Karmic Lessons – Missing numbers (1–9)
        present_numbers = set(digits)
        all_numbers = set(range(1, 10))
        missing_numbers = sorted(all_numbers - present_numbers)

        # Build result block
        result_map = {
            "life-path": {
                "title": "Life Path Number",
                "number": life_path,
                "description": CORE_NUMBER_TEXT.get("life-path", {}).get(life_path)
            },
            "expression-number": {
                "title": "Expression (Destiny) Number",
                "number": expression,
                "description": CORE_NUMBER_TEXT.get("expression-number", {}).get(expression)
            },
            "soul-urge": {
                "title": "Soul Urge Number",
                "number": soul_urge,
                "description": CORE_NUMBER_TEXT.get("soul-urge", {}).get(soul_urge)
            },
            "personality-number": {
                "title": "Personality Number",
                "number": personality,
                "description": CORE_NUMBER_TEXT.get("personality-number", {}).get(personality)
            },
            "birthday-number": {
                "title": "Birthday Number",
                "number": birthday,
                "description": CORE_NUMBER_TEXT.get("birthday-number", {}).get(birthday)
            },
            "maturity-number": {
                "title": "Maturity Number",
                "number": maturity,
                "description": CORE_NUMBER_TEXT.get("maturity-number", {}).get(maturity)
            },
            "hidden-passion": {
                "title": "Hidden Passion Number",
                "number": hidden,
                "description": CORE_NUMBER_TEXT.get("hidden-passion", {}).get(hidden)
            },
            "karmic-lessons": {
                "title": "Karmic Lessons",
                "number": len(missing_numbers),
                "description": (
                    "🧠 Your Karmic Lessons:\n\n" + "\n".join([
                        f"{n} → {CORE_NUMBER_TEXT.get('karmic-lessons', {}).get(n, '...')}"
                        for n in missing_numbers
                    ]) if missing_numbers else
                    "🌟 No Karmic Lessons — You carry all primary strengths from birth."
                )
            }
        }

        selected = result_map.get(tool)

        return {
            "tool": tool,
            "name": name,
            "dob": dob,
            "title": selected["title"],
            "summary": selected["description"] or "🔍 Insight not found.",
            "mainNumber": selected["number"] or 0,
            "mainPercentage": selected["number"] * 11 if isinstance(selected["number"], int) else 0
        }

    except Exception as e:
        return {
            "tool": tool,
            "title": "Core Number",
            "summary": f"⚠️ Error while processing: {str(e)}",
            "mainNumber": 0,
            "mainPercentage": 0,
            "name": name,
            "dob": dob
        }
