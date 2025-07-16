from tools.numerology_core import extract_full_numerology

def get_business_partner_compatibility(data):
    name1 = data.get("name")
    dob1 = data.get("dob")
    name2 = data.get("partnerName")
    dob2 = data.get("partnerDOB")

    if not name1 or not dob1 or not name2 or not dob2:
        return {
            "title": "Partner Compatibility in Business",
            "summary": f"DEBUG: name1={name1}, dob1={dob1}, name2={name2}, dob2={dob2}",
            "compatibilityScore": 0
        }
    try:
        n1 = extract_full_numerology(name1, dob1)
        n2 = extract_full_numerology(name2, dob2)
    except Exception as e:
        return {
            "title": "Partner Compatibility in Business",
            "summary": f"⚠️ Failed to calculate numerology. Error: {str(e)}",
            "compatibilityScore": 0
        }

    lp1 = n1["life_path"]
    lp2 = n2["life_path"]
    hn1 = n1["heartNumber"]
    hn2 = n2["heartNumber"]
    en1 = n1["expression_number"]
    en2 = n2["expression_number"]

    # Scoring Logic
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

    if score >= 85:
        msg = "🌟 Excellent compatibility! You both share remarkable alignment in purpose and working style, making you a strong business duo."
    elif score >= 70:
        msg = "✅ Good compatibility. While there may be a few differences, your core strengths complement each other well for business success."
    else:
        msg = "🤝 Moderate compatibility. With role clarity and clear communication, you can make this partnership work effectively."

    return {
        "title": "Partner Compatibility in Business",
        "summary": msg,
        "compatibilityScore": score
    }
