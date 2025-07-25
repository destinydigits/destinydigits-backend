from datetime import datetime
from tools.numerology_core import reduce_strict

def get_life_path(dob):
    try:
        digits = [int(ch) for ch in dob if ch.isdigit()]
        if not digits:
            return None
        return reduce_strict(sum(digits))
    except:
        return None

def get_personal_year(dob, target_year):
    try:
        parts = dob.strip().split("-")
        if len(parts) != 3:
            return None
        y, m, d = map(int, parts)
        return reduce_strict(d + m + target_year)
    except:
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
    name = data.get("name", "").strip()
    dob = data.get("dob", "").strip()

    if not name or not dob or "-" not in dob:
        return {"error": "Name and Date of Birth are required."}

    try:
        life_path = get_life_path(dob)
        if life_path is None:
            return {"error": "Invalid date format or empty DOB"}
        current_year = datetime.now().year
        upcoming_years = []

        for i in range(5):
            year = current_year + i
            py = get_personal_year(dob, year)
            if py is None:
                continue
            tag = tag_for_personal_year(py)
            upcoming_years.append({
                "year": year,
                "personalYear": py,
                "tag": tag
            })

        good_years = [y['year'] for y in upcoming_years if y['personalYear'] in [2, 6, 9]]
        sync_message = (
            f"{', '.join(str(y) for y in good_years)} are highly favorable for long-term commitment. "
            "Align important decisions like engagement or marriage in these years."
            if good_years else
            "The upcoming years carry mixed energies. Focus on inner alignment before choosing a marriage year."
        )

        return {
            "tool": "marriage-year",
            "name": name,
            "dob": dob,
            "title": "Best Year to Marry",
            "summary": f"Based on your birth details, your Life Path Number is {life_path or '—'}, symbolizing your journey and emotional foundation for marriage.",
            "marriageYears": upcoming_years,
            "syncMessage": sync_message
        }

    except Exception as e:
        print(f"[ERROR] get_best_year_to_marry failed: {e}")
        return {"error": f"Unexpected error: {str(e)}"}
