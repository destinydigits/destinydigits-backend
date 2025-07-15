from tools.numerology_core import numerology_values

def get_heart_desire_match(data):
    name1 = data.get("name")
    name2 = data.get("partnerName")
    dob1 = data.get("dob", "")
    dob2 = data.get("partnerDOB", "")

    if not name1 or not name2:
        return {"error": "Both names are required"}

    n1 = numerology_values(name1)
    n2 = numerology_values(name2)

    h1 = n1.get("heartNumber")
    h2 = n2.get("heartNumber")

    firstVowelMatch = n1.get("firstVowel") == n2.get("firstVowel")
    nameNumberMatch = n1.get("expressionNumber") == n2.get("expressionNumber")

    # Score logic
    if h1 == h2:
        score = 40
        label = "Emotional Soulmates"
    elif (h1, h2) in [(2,6), (6,2), (4,8), (3,9), (1,5), (5,1)]:
        score = 30
        label = "Harmonious Bond"
    elif (h1 + h2) in [10, 11, 12]:
        score = 20
        label = "Growth Pair"
    else:
        score = 10
        label = "Contrast & Challenge"

    # Bonus
    if firstVowelMatch:
        score += 5
    if nameNumberMatch:
        score += 5

    score = min(score, 50)

    summary = (
        f"<b>{name1}</b> and <b>{name2}</b> have heart numbers {h1} and {h2}.<br>"
        f"This reveals an emotional equation of <b>{label}</b> — driven by your deepest desires and needs."
    )

    if label == "Emotional Soulmates":
        syncMessage = (
            f"Your emotional needs mirror each other. This is a natural, intuitive bond — perfect for love, marriage, or long-term growth."
        )
    elif label == "Harmonious Bond":
        syncMessage = (
            f"Emotionally, you complement each other. One brings care, the other independence — a lovely balance when honored."
        )
    elif label == "Growth Pair":
        syncMessage = (
            f"You may think and feel differently, but together you unlock emotional growth. This bond matures with time and trust."
        )
    else:
        syncMessage = (
            f"Your heart numbers show contrast — expect intense attraction but emotional friction. Communication is your bridge."
        )

    return {
        "tool": "heart-desire",
        "name": name1,
        "dob": dob1,
        "partnerName": name2,
        "partnerDOB": dob2,
        "score": score,
        "mainNumber": score,
        "mainPercentage": int((score / 50) * 100),
        "title": "Heart Desire Match",
        "partnerVibe": label,
        "summary": summary,
        "syncMessage": syncMessage,
        "syncScore": f"{score}/50"
    }
