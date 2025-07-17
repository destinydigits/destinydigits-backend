from tools.numerology_core import extract_full_numerology

talent_map = {
    1: "Leadership, initiative, and originality. You're naturally bold and independent.",
    2: "Diplomacy, empathy, and emotional intelligence. You're a born peacemaker.",
    3: "Creativity, joy, and expression. You shine in artistic or social roles.",
    4: "Discipline, practicality, and structure. You build things that last.",
    5: "Adaptability, communication, and curiosity. You're a dynamic multitasker.",
    6: "Responsibility, nurturing, and balance. You thrive when helping others.",
    7: "Intuition, depth, and analysis. You uncover hidden truths.",
    8: "Ambition, strategy, and influence. You’re born to manage or lead.",
    9: "Compassion, wisdom, and vision. You uplift others and leave impact."
}

def get_hidden_talents(data):
    name = data.get("name")
    dob = data.get("dob")

    if not name or not dob:
        return {
            "title": "Hidden Talents",
            "summary": "⚠️ Please enter your name and date of birth.",
            "mainNumber": 0,
            "mainPercentage": 0,
            "name": name or "—",
            "dob": dob or "—"
        }

    try:
        numbers = extract_full_numerology(name, dob)
        birth_number = numbers["birthNumber"]
        destiny = numbers["destinyNumber"]
        life_path = numbers["life_path"]

        # Combine the 3 traits
        talents = {
            "Birth Number": talent_map.get(birth_number),
            "Destiny Number": talent_map.get(destiny),
            "Life Path Number": talent_map.get(life_path)
        }

        bullet_points = "\n".join(
            [f"• {k} ({n}): {v}" for k, (n, v) in zip(talents.keys(), [(birth_number, talents['Birth Number']), (destiny, talents['Destiny Number']), (life_path, talents['Life Path Number'])])]
        )

        summary = f"🌟 Your Hidden Talents Revealed:\n\n{bullet_points}"

        return {
            "tool": "hidden-talents",
            "name": name,
            "dob": dob,
            "title": "Hidden Talents",
            "mainNumber": life_path,
            "mainPercentage": 70 + (life_path % 4) * 5,
            "summary": summary
        }

    except Exception as e:
        return {
            "title": "Hidden Talents",
            "summary": f"⚠️ Error decoding talents: {str(e)}",
            "mainNumber": 0,
            "mainPercentage": 0,
            "name": name,
            "dob": dob
        }
