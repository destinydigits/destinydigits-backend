from datetime import datetime
from tools.numerology_core import reduce_strict

def get_life_path(dob):
    digits = [int(ch) for ch in dob if ch.isdigit()]
    return reduce_strict(sum(digits))

def get_personal_year(dob, target_year):
    try:
        parts = dob.strip().split("-")
        if len(parts) != 3:
            return None
        y, m, d = map(int, parts)
        return reduce_strict(d + m + target_year)
    except Exception:
        return None

def tag_for_personal_year(py):
    if py == 2:
        return "💖 Ideal Year for Marriage"
    elif py == 6:
        return "💍 Strong Vibes for Commitment"
    elif py == 9:
        return "🌈 Karmic Completion – Good for Long-term Union"
    elif py == 3:
        return "😐 Joyful but not stable for marriage"
    elif py == 7:
        return "⚠️ Emotionally Detached – not recommended"
    elif py == 5:
        return "⚠️ Unstable year – avoid major commitments"
    elif py == 8:
        return "💼 Career Focused Year"
    else:
        return "🔄 Neutral Influence"

def get_best_year_to_marry(data):
    name = data.get("name")
    dob = data.get("dob")

    if not name or not dob:
        return {"error": "Name and Date of Birth are required."}

    life_path = get_life_path(dob)
    current_year = datetime.now().year
    upcoming_years = []

    for i in range(5):
        year = current_year + i
        py = get_personal_year(dob, year)
        tag = tag_for_personal_year(py)
        upcoming_years.append({
            "year": year,
            "personalYear": py,
            "tag": tag
        })

    # Select strong years for summary
    good_years = [y['year'] for y in upcoming_years if y['personalYear'] in [2, 6, 9]]
    sync_message = (
        f"{', '.join(str(y) for y in good_years)} "
        "are highly favorable for long-term commitment. "
        "Align important decisions like engagement or marriage in these years."
        if good_years else
        "The upcoming years carry mixed energies. Focus on inner alignment before choosing a marriage year."
    )

    return {
        "tool": "best-year-to-marry",
        "name": name,
        "dob": dob,
        "mainNumber": life_path,
        "title": "Best Year to Marry",
        "summary": f"Based on your birth details, your Life Path Number is {life_path}, symbolizing your journey and emotional foundation for marriage.",
        "marriageYears": upcoming_years,
        "syncMessage": sync_message
    }
