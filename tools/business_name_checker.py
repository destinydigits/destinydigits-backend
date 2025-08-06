from datetime import datetime
from tools.numerology_core import numerology_values, extract_full_numerology

def business_name_checker(data):
    name = data.get("businessName")
    dob = data.get("dob")
    try:
        # Expression number from business name
        name_data = numerology_values(name)
        expression_number = name_data["expressionNumber"]

        # Destiny number from user's DOB
        full_data = extract_full_numerology(name, dob)
        destiny_number = full_data["destinyNumber"]

        # Compatibility logic
        diff = abs(expression_number - destiny_number)
        if diff == 0:
            score = 92
            vibe = "Perfect Match"
            emoji = "🌟"
            message = "Your business name is in perfect alignment with your destiny. Full steam ahead!"
        elif diff == 1:
            score = 85
            vibe = "Strong Compatibility"
            emoji = "✅"
            message = "The name strongly supports your path. Success flows with ease."
        elif diff == 2:
            score = 75
            vibe = "Moderately Aligned"
            emoji = "⚖️"
            message = "Good energy overall. You may consider enhancing the name's impact slightly."
        else:
            score = 62
            vibe = "Needs Adjustment"
            emoji = "🔄"
            message = "There may be clashes between your name and core path. Small changes can help."

        return {
            "tool": "business-name-checker",
            "name": name,
            "dob": dob,
            "score": score,
            "emoji": emoji,
            "summary": f"Your business name ‘{name}’ has an expression number {expression_number} which compares to your destiny number {destiny_number}. {message}",
            "title": "Business Name Compatibility",
            "mainNumber": score,
            "mainPercentage": score,
            "vibe": vibe,
            "syncScore": f"{score}/100",
            "syncMessage": message
        }

    except Exception as e:
        return {
            "tool": "business-name-checker",
            "name": name,
            "dob": dob,
            "score": 0,
            "emoji": "❌",
            "summary": f"Something went wrong: {str(e)}",
            "title": "Business Name Compatibility",
            "mainNumber": 0,
            "mainPercentage": 0,
            "vibe": "",
            "syncScore": "0/100",
            "syncMessage": ""
        }
