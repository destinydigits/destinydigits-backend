from tools.numerology_core import extract_full_numerology

def get_business_partner_compatibility(data):
    name1 = data.get("name")
    dob1 = data.get("dob")
    name2 = data.get("partnerName")
    dob2 = data.get("partnerDOB")

    if not name1 or not dob1 or not name2 or not dob2:
        return {
            "title": "Partner Compatibility in Business",
            "summary": f"⚠️ Missing data.\nname1={name1}, dob1={dob1}, name2={name2}, dob2={dob2}",
            "mainNumber": 0,
            "mainPercentage": 0
        }

    try:
        n1 = extract_full_numerology(name1, dob1)
        n2 = extract_full_numerology(name2, dob2)
    except Exception as e:
        return {
            "title": "Partner Compatibility in Business",
            "summary": f"⚠️ Failed to calculate numerology. Error: {str(e)}",
            "mainNumber": 0,
            "mainPercentage": 0
        }

    lp1 = n1["life_path"]
    lp2 = n2["life_path"]
    hn1 = n1["heartNumber"]
    hn2 = n2["heartNumber"]
    en1 = n1["expression_number"]
    en2 = n2["expression_number"]

    score = 50
    if lp1 == lp2:
        score += 20
    elif abs(lp1 - lp2) == 1:
        score += 10

    if hn1 == hn2:
        score += 10
    elif abs(hn1 - hn2) == 1:
        score += 5

    if en1 == en2:
        score += 10

    score = max(55, min(score, 95))

    # Label + Emoji + Message based on score
    if score >= 85:
        label = "Exceptional Alignment"
        emoji = "🌟"
        summary = "🌟 Excellent compatibility! You both share remarkable alignment in purpose and working style, making you a strong business duo."
        syncMessage = "Your goals and communication sync effortlessly. Make bold moves together."
    elif score >= 70:
        label = "Strong Synergy"
        emoji = "✅"
        summary = "✅ Good compatibility. While there may be a few differences, your core strengths complement each other well for business success."
        syncMessage = "Clarify your roles and collaborate with trust — success awaits."
    else:
        label = "Potential with Patience"
        emoji = "🤝"
        summary = "🤝 Moderate compatibility. With role clarity and clear communication, you can make this partnership work effectively."
        syncMessage = "Plan well and keep communication open to make this work."

    return {
        "tool": "business-partner-check",
        "name": name1,
        "dob": dob1,
        "partnerName": name2,
        "partnerDOB": dob2,
        "score": score,
        "emoji": emoji,
        "summary": summary,
        "title": "Partner Compatibility in Business",
        "mainNumber": score,
        "mainPercentage": score,
        "partnerVibe": label,
        "syncScore": f"{score}/100",
        "syncMessage": syncMessage
    }
