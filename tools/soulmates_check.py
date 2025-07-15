from tools.numerology_core import numerology_values, reduce_strict
from datetime import datetime

def get_life_path_number(dob_str):
    digits = [int(d) for d in dob_str if d.isdigit()]
    return reduce_strict(sum(digits))

def get_birth_number(dob_str):
    try:
        day = int(datetime.strptime(dob_str, "%Y-%m-%d").day)
        return reduce_strict(day)
    except:
        return None

def get_soulmate_score(data):
    name1 = data.get("name")
    dob1 = data.get("dob")
    name2 = data.get("partnerName")
    dob2 = data.get("partnerDOB")

    if not all([name1, dob1, name2, dob2]):
        return {"error": "Missing input fields"}

    n1 = numerology_values(name1)
    n2 = numerology_values(name2)

    lp1 = get_life_path_number(dob1)
    lp2 = get_life_path_number(dob2)
    bn1 = get_birth_number(dob1)
    bn2 = get_birth_number(dob2)

    h1 = n1.get("heartNumber")
    h2 = n2.get("heartNumber")

    e1 = n1.get("expressionNumber")
    e2 = n2.get("expressionNumber")

    fv1 = n1.get("firstVowel")
    fv2 = n2.get("firstVowel")

    # --- Scoring Logic ---
    score = 0

    # Life Path
    if lp1 == lp2:
        score += 35
    elif (lp1, lp2) in [(1,5), (2,6), (3,9), (4,8), (5,1), (6,2), (9,3)]:
        score += 20

    # Heart Number
    if h1 == h2:
        score += 25
    elif (h1, h2) in [(2,6), (6,2), (3,9), (1,5), (4,8)]:
        score += 15

    # Expression Number
    if e1 == e2:
        score += 20

    # Birth Number
    if bn1 == bn2:
        score += 10

    # First Vowel
    if fv1 and fv1 == fv2:
        score += 10

    # Clamp
    score = min(score, 100)

    # Vibe Label
    if score >= 90:
        label = "Twin Flame Vibe 🔥"
    elif score >= 75:
        label = "Yes, You're Soulmates 💖"
    elif score >= 60:
        label = "Strong Bond, Needs Depth 💫"
    elif score >= 40:
        label = "Karmic Learning Pair 🔁"
    else:
        label = "Not Aligned ❌"

    # Summary
    summary = (
        f"<b>{name1}</b> and <b>{name2}</b> share a connection of <b>{label}</b>.<br>"
        f"Life Path: {lp1} vs {lp2} &nbsp;|&nbsp; Heart: {h1} vs {h2} &nbsp;|&nbsp; "
        f"Expression: {e1} vs {e2} &nbsp;|&nbsp; Birth: {bn1} vs {bn2}"
    )

    # Sync Message
    if "Soulmates" in label or "Twin" in label:
        syncMessage = "You both are vibrationally aligned. This bond is rare and meant to evolve with deep emotional truth."
    elif "Strong Bond" in label:
        syncMessage = "You complement each other well, but emotional transparency will deepen the bond."
    elif "Karmic" in label:
        syncMessage = "This relationship brings soul lessons. The connection is deep but may be intense or testing."
    else:
        syncMessage = "There may be emotional or vibrational differences. Focus on building alignment through patience and shared goals."

    return {
        "tool": "soulmates-check",
        "name": name1,
        "dob": dob1,
        "partnerName": name2,
        "partnerDOB": dob2,
        "mainNumber": score,
        "mainPercentage": score,
        "score": score,
        "syncScore": f"{score}/100",
        "title": "Are You Soulmates?",
        "partnerVibe": label,
        "summary": summary,
        "syncMessage": syncMessage
    }
