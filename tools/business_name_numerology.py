from .numerology_core import extract_full_numerology, numerology_values

# 🔮 Business number suggestions based on user's life path
business_number_map = {
    1: [1, 5, 8],
    2: [2, 6, 9],
    3: [3, 5, 6],
    4: [4, 8],
    5: [1, 3, 5],
    6: [2, 3, 6],
    7: [7, 2, 9],
    8: [1, 4, 8],
    9: [6, 9, 2]
}

# ✍️ Hardcoded example for how number is calculated from business name
def get_example_summary():
    name = "Moon Matrix"
    values = numerology_values(name)
    total = values["expressionNumber"]
    return f"🧾 Example: The business name '{name}' adds up to {total} using the Pythagorean system."

# 🧠 Main runner
def run(name, dob, businessName=None):
    try:
        full = extract_full_numerology(name, dob)
        life_path = full.get("life_path")
        expr = full.get("expression_number")

        if not life_path or not expr:
            return {"error": "Missing user numerology numbers"}

        # Merge both life path and expression suggestions
        user_suggestions = list(set(business_number_map.get(life_path, []) + business_number_map.get(expr, [])))
        user_suggestions.sort()

        summary = (
            f"🔮 Your Life Path: {life_path}\n"
            f"🧠 Your Expression Number: {expr}\n\n"
            f"💼 Based on your personal numbers, the most powerful business name numbers for you are: "
            f"{', '.join(str(n) for n in user_suggestions)}\n\n"
            f"These numbers align with your natural energy and can attract more success, flow, and alignment in business.\n\n"
            + get_example_summary()
        )

        return {
            "tool": "business-name-suggestion",
            "name": name,
            "dob": dob,
            "title": "💼 Business Name Suggestion",
            "mainNumber": life_path,
            "summary": summary
        }

    except Exception as e:
        return {"error": str(e)}
