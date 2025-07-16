from numerology_core import extract_full_numerology

def business_partner_check(data):
    name1 = data.get("name")
    dob1 = data.get("dob")
    name2 = data.get("partnerName")
    dob2 = data.get("partnerDOB")

    if not name1 or not dob1 or not name2 or not dob2:
        return {
            "title": "Partner Compatibility in Business",
            "summary": "⚠️ Missing or invalid data. Please go back and try again.",
            "compatibilityScore": 0
        }

    n1 = extract_full_numerology(name1, dob1)
    n2 = extract_full_numerology(name2, dob2)

    lp1 = n1["life_path"]
    lp2 = n2["life_path"]
    hn1 = n1["heartNumber"]
    hn2 = n2["heartNumber"]

    # Compatibility logic (custom ranges)
    compatibility = 50  # base score

    if lp1 == lp2:
        compatibility += 20
    elif abs(lp1 - lp2) in [1, 2]:
        compatibility += 10

    if hn1 == hn2:
        compatibility += 15
    elif abs(hn1 - hn2) == 1:
        compatibility += 5

    # Normalize score
    compatibility = min(compatibility, 95)
    compatibility = max(compatibility, 55)

    # Compatibility message
    if compatibility >= 85:
        message = "🌟 Excellent compatibility! This partnership has high potential for long-term success with mutual understanding and complementary strengths."
    elif compatibility >= 70:
        message = "👍 Good compatibility! You both bring complementary skills and shared values to the table—great for collaboration."
    else:
        message = "🤝 Moderate compatibility. With clear communication and role clarity, this partnership can still thrive."

    return {
        "title": "Partner Compatibility in Business",
        "summary": message,
        "compatibilityScore": compatibility
    }
