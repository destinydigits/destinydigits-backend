from tools.numerology_core import reduce_number, get_name_number
from datetime import datetime

def get_birth_number(dob_str):
    try:
        day = int(datetime.strptime(dob_str, "%Y-%m-%d").day)
        return reduce_number(day)
    except:
        return None

def get_life_path_number(dob_str):
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        digits = list(str(dob.day) + str(dob.month) + str(dob.year))
        total = sum(int(d) for d in digits)
        return reduce_number(total)
    except:
        return None

def build_person_profile(name, dob):
    return {
        "name": name,
        "birthNumber": get_birth_number(dob),
        "lifePath": get_life_path_number(dob),
        "nameNumber": get_name_number(name)
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

    p1 = build_person_profile(name1, dob1)
    p2 = build_person_profile(name2, dob2)
    score = calculate_compatibility_score(p1, p2)
    emoji, label = get_emoji_and_label(score)

    summary = f"{p1['name']} and {p2['name']} share a {label.lower()}. Life Path: {p1['lifePath']} vs {p2['lifePath']}, Birth Numbers: {p1['birthNumber']} vs {p2['birthNumber']}."

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
        "syncMessage": summary
    }

