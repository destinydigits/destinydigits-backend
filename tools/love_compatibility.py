from datetime import datetime
from tools.numerology_core import numerology_values, reduce_strict

def get_birth_number(dob_str):
    try:
        day = int(datetime.strptime(dob_str, "%Y-%m-%d").day)
        return reduce_strict(day)
    except:
        return None

def get_life_path_number(dob_str):
    try:
        digits = [int(d) for d in dob_str if d.isdigit()]
        return reduce_strict(sum(digits))
    except:
        return None

def build_person_profile(name, dob):
    name_data = numerology_values(name)
    return {
        "name": name,
        "birthNumber": get_birth_number(dob),
        "lifePath": get_life_path_number(dob),
        "nameNumber": name_data.get("expressionNumber")
    }

def score_match(n1, n2):
    if n1 is None or n2 is None:
        return 0
    if n1 == n2:
        return 1
    if (n1, n2) in [(1,5),(2,6),(3,9),(4,8),(5,1),(6,2),(9,3)]:
        return 0.5
    return 0

def calculate_compatibility_score(p1, p2):
    score = 0
    score += score_match(p1["lifePath"], p2["lifePath"]) * 40
    score += score_match(p1["birthNumber"], p2["birthNumber"]) * 20
    score += score_match(p1["nameNumber"], p2["nameNumber"]) * 30

    matches = sum([
        p1["lifePath"] == p2["lifePath"],
        p1["birthNumber"] == p2["birthNumber"],
        p1["nameNumber"] == p2["nameNumber"]
    ])
    if matches >= 2:
        score += 10

    return round(score)

def get_emoji_and_label(score):
    if score >= 90:
        return "🥰", "Soulmate Energy"
    elif score >= 75:
        return "😊", "Strong Bond"
    elif score >= 60:
        return "🙂", "Balanced Match"
    elif score >= 40:
        return "😐", "Needs Effort"
    else:
        return "😢", "Challenging Match"

def get_love_compatibility(data):
    name1 = data.get("name")
    dob1 = data.get("dob")
    name2 = data.get("partnerName")
    dob2 = data.get("partnerDOB")

    if not all([name1, dob1, name2, dob2]):
        return {"error": "Missing required fields"}

    p1 = build_person_profile(name1, dob1)
    p2 = build_person_profile(name2, dob2)
    score = calculate_compatibility_score(p1, p2)
    emoji, label = get_emoji_and_label(score)

    # 🌟 Emotional Market-Friendly Summary
    summary = (
        f"<b>{p1['name']}</b> and <b>{p2['name']}</b> share a "
        f"<span style='color:#d32f2f;'>{label}</span>.<br>"
        f"<b>Life Path:</b> {p1['lifePath']} vs {p2['lifePath']} &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"<b>Birth Numbers:</b> {p1['birthNumber']} vs {p2['birthNumber']}"
    )

    # 💬 Insight based on label
    if label == "Soulmate Energy":
        syncMessage = (
            f"Your bond feels karmic and effortless. "
            f"<b>{p1['name']}</b> and <b>{p2['name']}</b> were destined to cross paths — a connection that goes beyond this lifetime."
        )
    elif label == "Strong Bond":
        syncMessage = (
            f"There is real emotional chemistry here. "
            f"You both support each other’s growth and find joy in shared values and vision."
        )
    elif label == "Balanced Match":
        syncMessage = (
            f"This relationship has great potential. "
            f"With communication and a little adjustment, <b>{p1['name']}</b> and <b>{p2['name']}</b> can evolve beautifully together."
        )
    elif label == "Needs Effort":
        syncMessage = (
            f"There are fundamental differences, but not walls. "
            f"Honest effort and emotional awareness can help <b>{p1['name']}</b> and <b>{p2['name']}</b> build understanding."
        )
    else:
        syncMessage = (
            f"This is a karmic connection — possibly intense or testing. "
            f"<b>{p1['name']}</b> and <b>{p2['name']}</b> must choose patience, maturity, and mutual respect to make it thrive."
        )

    return {
        "tool": "love-compatibility",
        "name": name1,
        "dob": dob1,
        "partnerName": name2,
        "partnerDOB": dob2,
        "score": score,
        "emoji": emoji,
        "summary": summary,
        "title": "Love Compatibility",
        "mainNumber": score,
        "partnerVibe": label,
        "syncScore": f"{score}/100",
        "syncMessage": syncMessage
    }
