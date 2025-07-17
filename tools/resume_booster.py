from tools.numerology_core import extract_full_numerology

vibration_strength = {
    1: ("Strong", "Leadership, initiative, and solo success."),
    2: ("Weak", "Can cause hesitation or over-dependence."),
    3: ("Strong", "Charisma and charm — great for creative resumes."),
    4: ("Moderate", "Disciplined but rigid — try softening with initials."),
    5: ("Strong", "Versatile and dynamic — excellent career vibration."),
    6: ("Stable", "Reliable and responsible — safe for job roles."),
    7: ("Weak", "Too introspective — consider tweaking name energy."),
    8: ("Very Strong", "Authoritative and business-aligned — excellent for success."),
    9: ("Strong", "Visionary and service-driven — works best in impact careers.")
}

def get_resume_booster(data):
    name = data.get("name")
    dob = data.get("dob")

    if not name or not dob:
        return {
            "title": "Resume Booster",
            "summary": "⚠️ Please enter both your name and date of birth.",
            "mainNumber": 0,
            "mainPercentage": 0,
            "name": name or "—",
            "dob": dob or "—"
        }

    try:
        numbers = extract_full_numerology(name, dob)
        expression = numbers["expression_number"]
        status, feedback = vibration_strength.get(expression, ("Neutral", "Balanced but unremarkable vibration."))

        tweak = ""
        if status in ["Weak", "Moderate"]:
            tweak = (
                "\n\n💡 *Tip:* Consider modifying your name slightly for a stronger first impression — "
                "e.g., adding a middle initial, full middle name, or slight spelling variation."
            )

        summary = f"🔠 Your Name Number is {expression} → {status} Career Vibration\n\n{feedback}{tweak}"

        return {
            "tool": "resume-booster",
            "name": name,
            "dob": dob,
            "mainNumber": expression,
            "mainPercentage": 60 + (expression % 5) * 7,
            "title": "Resume Booster",
            "summary": summary
        }

    except Exception as e:
        return {
            "title": "Resume Booster",
            "summary": f"⚠️ Could not process your details: {str(e)}",
            "mainNumber": 0,
            "mainPercentage": 0,
            "name": name,
            "dob": dob
        }
