from .numerology_core import numerology_values
import random

# 🔢 Multiple insights per number (expandable)
business_insights = {
    1: [
        "Excellent for leadership-oriented ventures and personal brands.",
        "Number 1 attracts authority, courage, and pioneering success.",
        "Ideal for startups where innovation and boldness matter."
    ],
    2: [
        "Best for partnerships, healing, and wellness brands.",
        "Brings balance, diplomacy, and harmony in business.",
        "Works well for feminine brands, counselors, or coaches."
    ],
    3: [
        "A magnet for creative success — great for media, art, and entertainment.",
        "Brings joy, communication, and social popularity.",
        "Perfect for influencers, marketing firms, and creative startups."
    ],
    4: [
        "Good for structure-based businesses like finance, education, or real estate.",
        "Number 4 brings order, trust, and reliability.",
        "Ideal for traditional setups that value discipline and consistency."
    ],
    5: [
        "Dynamic and bold — attracts trendsetters, marketers, and travelers.",
        "Favors businesses in communication, media, or tech.",
        "Excellent for freedom-driven ventures with global reach."
    ],
    6: [
        "Works well for healing, family, and creative lifestyle brands.",
        "6 brings nurturing energy — good for design, wellness, or education.",
        "Ideal for brands that care, serve, and beautify."
    ],
    7: [
        "Spiritual and analytical — great for research, psychology, or niche tech.",
        "Number 7 favors thinkers, healers, and high-vibration entrepreneurs.",
        "Perfect for consulting, soul-led coaching, or deep niche brands."
    ],
    8: [
        "Powerful for money, success, and legacy-building businesses.",
        "Ideal for finance, real estate, and leadership ventures.",
        "Number 8 brings power, status, and high-level authority."
    ],
    9: [
        "The global helper — good for humanitarian or social impact ventures.",
        "Brings emotional intelligence, vision, and universal appeal.",
        "Perfect for coaching, NGOs, spiritual brands, and causes."
    ]
}

def run(name, dob, businessName=None):
    try:
        if not businessName:
            return {"error": "Missing business name"}

        values = numerology_values(businessName)
        total = values["expressionNumber"]

        summary_list = business_insights.get(total, ["No insights available for this number."])
        summary = random.choice(summary_list)

        return {
            "tool": "business-name-check",  # ✅ match with frontend ID
            "name": businessName,
            "title": "🔢 Business Name Numerology",
            "mainNumber": total,
            "summary": f"The name '{businessName}' resonates with the number {total}, which means: {summary}"
        }

    except Exception as e:
        return {"error": str(e)}
