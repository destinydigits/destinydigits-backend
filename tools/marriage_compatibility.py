from tools.numerology_core import numerology_values, reduce_strict
from datetime import datetime

def get_life_path(dob):
    digits = [int(d) for d in dob if d.isdigit()]
    return reduce_strict(sum(digits))

def get_birth_number(dob):
    try:
        day = int(datetime.strptime(dob, "%Y-%m-%d").day)
        return reduce_strict(day)
    except:
        return None

def get_personal_year(dob, year=None):
    if not dob:
        return None
    if year is None:
        year = datetime.now().year
    try:
        day = int(dob[-2:])
        month = int(dob[5:7])
        return reduce_strict(day + month + year)
    except:
        return None

def get_marriage_compatibility(data):
    name1 = data.get("name")
    dob1 = data.get("dob")
    name2 = data.get("partnerName")
    dob2 = data.get("partnerDOB")

    if not all([name1, dob1, name2, dob2]):
        return {"error": "All fields are required"}

    n1 = numerology_values(name1)
    n2 = numerology_values(name2)

    # Numbers
    lp1 = get_life_path(dob1)
    lp2 = get_life_path(dob2)

    h1 = n1.get("heartNumber")
    h2 = n2.get("heartNumber")

    e1 = n1.get("expressionNumber")
    e2 = n2.get("expressionNumber")

    bn1 = get_birth_number(dob1)
    bn2 = get_birth_number(dob2)

    fv1 = n1.get("firstVowel")
    fv2 = n2.get("firstVowel")

    py1 = get_personal_year(dob1)
    py2 = get_personal_year(dob2)

    # Scoring
    total = 0
    breakdown = {}

    # Life Path Match
    if lp1 == lp2:
        score = 30
    elif (lp1, lp2) in [(1,5), (2,6), (3,9), (4,8), (6,3), (9,3), (5,1)]:
        score = 20
    else:
        score = 10
    total += score
    breakdown['Life Path Match'] = (score, f"{lp1} vs {lp2}")

    # Heart Number
    if h1 == h2:
        score = 25
    elif (h1, h2) in [(2,6), (6,2), (4,8), (3,9), (1,5), (5,1)]:
        score = 15
    else:
        score = 5
    total += score
    breakdown['Heart Desire Match'] = (score, f"{h1} vs {h2}")

    # Expression Number
    if e1 == e2:
        score = 15
    else:
        score = 5
    total += score
    breakdown['Expression Number Match'] = (score, f"{e1} vs {e2}")

    # Birth Number
    if bn1 == bn2:
        score = 10
    else:
        score = 5
    total += score
    breakdown['Birth Number Match'] = (score, f"{bn1} vs {bn2}")

    # First Vowel
    if fv1 and fv1 == fv2:
        score = 10
    else:
        score = 0
    total += score
    breakdown['First Vowel Match'] = (score, f"{fv1 or '-'} vs {fv2 or '-'}")

    # Personal Year
    if py1 == py2:
        score = 10
    elif abs(py1 - py2) == 1:
        score = 5
    else:
        score = 0
    total += score
    breakdown['Personal Year Sync'] = (score, f"{py1} vs {py2}")

    # Final Label
    if total >= 90:
        label = "Marriage of Souls 💍"
        quote = "Your bond reflects divine alignment — a sacred union of mind, body, and soul."
    elif total >= 75:
        label = "High Compatibility 🌹"
        quote = "With mutual understanding, your love story can become timeless."
    elif total >= 60:
        label = "Strong Bond, Needs Nurturing 🌱"
        quote = "A marriage with potential — if both are ready to grow and adapt."
    elif total >= 40:
        label = "Challenging Yet Possible 💫"
        quote = "This connection demands patience, compromise, and emotional intelligence."
    else:
        label = "Caution: Karmic or Unstable Path ⚠️"
        quote = "Marriage is possible, but deep inner work and healing are key to sustaining it."

    # Summary
    summary_lines = [
        f"<b>Life Path:</b> {breakdown['Life Path Match'][1]} — Score: {breakdown['Life Path Match'][0]}/30",
        f"<b>Heart Desire:</b> {breakdown['Heart Desire Match'][1]} — Score: {breakdown['Heart Desire Match'][0]}/25",
        f"<b>Expression Number:</b> {breakdown['Expression Number Match'][1]} — Score: {breakdown['Expression Number Match'][0]}/15",
        f"<b>Birth Number:</b> {breakdown['Birth Number Match'][1]} — Score: {breakdown['Birth Number Match'][0]}/10",
        f"<b>First Vowel:</b> {breakdown['First Vowel Match'][1]} — Score: {breakdown['First Vowel Match'][0]}/10",
        f"<b>Personal Year:</b> {breakdown['Personal Year Sync'][1]} — Score: {breakdown['Personal Year Sync'][0]}/10",
        "<br><b>Total Compatibility:</b> {}%".format(total)
    ]

    syncMessage = f"{quote}"

    return {
        "tool": "marriage-compatibility",
        "name": name1,
        "dob": dob1,
        "partnerName": name2,
        "partnerDOB": dob2,
        "mainNumber": total,
        "mainPercentage": total,
        "score": total,
        "syncScore": f"{total}/100",
        "title": "Marriage Compatibility",
        "partnerVibe": label,
        "summary": "<br>".join(summary_lines),
        "syncMessage": syncMessage
    }
