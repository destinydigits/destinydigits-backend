
from .numerology_core import extract_full_numerology, reduce_strict, PYTHAGOREAN_VALUES, VOWELS

def process_tool(data):
    tool = data.get("tool")
    name = data.get("name")
    dob = data.get("dob")
    partner = data.get("partnerName")
    partner_dob = data.get("partnerDOB")

    # Extract full numerology once for user
    user_data = extract_full_numerology(name, dob)

    if tool == "life-path":
        lp = user_data.get("life_path")
        return {
            "tool": tool,
            "mainNumber": lp,
            "title": f"Your Life Path Number is {lp}",
            "summary": user_data.get("lifePurpose", ""),
            "extra": {
                "coreTrait": user_data.get("coreTrait"),
                "gift": user_data.get("gift"),
                "lifeDescription": user_data.get("lifeDescription")
            }
        }

    elif tool == "heart-desire":
        if not partner:
            return {"error": "Partner name required"}, 400
        soul_urge_1 = reduce_strict(sum(PYTHAGOREAN_VALUES.get(c, 0) for c in name.upper() if c in VOWELS))
        soul_urge_2 = reduce_strict(sum(PYTHAGOREAN_VALUES.get(c, 0) for c in partner.upper() if c in VOWELS))
        score = max(0, 100 - abs(soul_urge_1 - soul_urge_2) * 10)

        return {
            "tool": tool,
            "mainNumber": f"{soul_urge_1} & {soul_urge_2}",
            "title": f"Your Soul Urge Match Score is {score}%",
            "summary": f"You ({soul_urge_1}) and your partner ({soul_urge_2}) share an emotional alignment of {score}%",
            "score": score
        }

    elif tool == "money-today":
        pdn = user_data.get("personalDay")
        return {
            "tool": tool,
            "mainNumber": pdn,
            "title": f"Your Money Vibration Today is {pdn}",
            "summary": f"Today’s energy is aligned with number {pdn}. Plan financial steps accordingly."
        }

    else:
        return {"error": "Unsupported tool"}, 400
