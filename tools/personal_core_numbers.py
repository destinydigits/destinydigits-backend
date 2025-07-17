from tools.numerology_core import extract_full_numerology, reduce_strict

def get_personal_core_number(data, tool):
    name = data.get("name")
    dob = data.get("dob")

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
        maturity = reduce_strict(life_path + expression)
        birthday = reduce_strict(birth_day)
        hidden = core.get("hiddenPassion")
        personality = core["personality_number"]
        soul_urge = core["heartNumber"]

        # Karmic Lessons: Missing letters from A–Z
        all_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        used_letters = set(name.upper())
        karmic_missing = sorted(all_letters - used_letters)
        karmic_string = ", ".join(karmic_missing)

        result_map = {
            "life-path": {
                "title": "Life Path Number",
                "number": life_path,
                "summary": f"🌟 Your Life Path Number is {life_path}, representing your soul's journey and overall purpose."
            },
            "expression-number": {
                "title": "Expression (Destiny) Number",
                "number": expression,
                "summary": f"🎯 Your Expression Number is {expression}, revealing your natural talents and life potential."
            },
            "soul-urge": {
                "title": "Soul Urge Number",
                "number": soul_urge,
                "summary": f"❤️ Your Soul Urge Number is {soul_urge}. This reflects your inner desires and emotional needs."
            },
            "personality-number": {
                "title": "Personality Number",
                "number": personality,
                "summary": f"🧩 Your Personality Number is {personality}. This is how others perceive you at first glance."
            },
            "birthday-number": {
                "title": "Birthday Number",
                "number": birthday,
                "summary": f"🎁 Your Birthday Number is {birthday}, derived from the day you were born. It reflects a natural strength or talent."
            },
            "maturity-number": {
                "title": "Maturity Number",
                "number": maturity,
                "summary": f"🌱 Your Maturity Number is {maturity}. It reveals your long-term growth and who you're becoming with age."
            },
            "karmic-lessons": {
                "title": "Karmic Lessons",
                "number": 0,
                "summary": f"🧘‍♂️ The letters missing from your name are: {karmic_string}. These indicate your karmic growth areas in this life."
            },
            "hidden-passion": {
                "title": "Hidden Passion Number",
                "number": hidden,
                "summary": f"🔥 Your Hidden Passion Number is {hidden}, showing the force or talent that drives you the most."
            }
        }

        selected = result_map.get(tool)

        return {
            "tool": tool,
            "name": name,
            "dob": dob,
            "title": selected["title"],
            "summary": selected["summary"],
            "mainNumber": selected["number"],
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
