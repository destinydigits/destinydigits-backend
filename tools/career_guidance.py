from tools.numerology_core import extract_full_numerology

career_map = {
    1: ("Leadership & Entrepreneurship", "You're born to lead and take charge. Consider roles like CEO, startup founder, or political leader."),
    2: ("Mediation & Support Roles", "You're a natural peacemaker and thrive in cooperative roles. Careers like counselor, HR, or diplomacy suit you."),
    3: ("Creative Fields", "You're expressive and artistic. Explore careers in writing, acting, design, or communication."),
    4: ("Structured Careers", "You’re disciplined and methodical. Ideal roles include engineer, administrator, or analyst."),
    5: ("Communication & Travel", "You thrive on freedom and variety. Careers like sales, media, tourism, or freelancing are great."),
    6: ("Healing & Service", "You're nurturing and responsible. Teaching, therapy, healthcare, or social work are fulfilling."),
    7: ("Research & Spirituality", "You seek truth and knowledge. Explore careers in research, data science, or spirituality."),
    8: ("Business & Authority", "You're ambitious and goal-driven. Finance, law, management, or real estate may suit you."),
    9: ("Service & Impact", "You're compassionate and idealistic. Careers in NGOs, arts, or counseling align well."),
}

def get_career_guidance(data):
    name = data.get("name")
    dob = data.get("dob")

    if not name or not dob:
        return {
            "title": "Career Guidance",
            "summary": "⚠️ Missing name or date of birth. Please try again.",
            "mainNumber": 0,
            "mainPercentage": 0,
            "name": name or "—",
            "dob": dob or "—"
        }

    try:
        numerology = extract_full_numerology(name, dob)
        lp = numerology["life_path"]
    except Exception as e:
        return {
            "title": "Career Guidance",
            "summary": f"⚠️ Error in calculation: {str(e)}",
            "mainNumber": 0,
            "mainPercentage": 0,
            "name": name,
            "dob": dob
        }

    career_title, career_text = career_map.get(lp, ("General Path", "Explore your strengths and passions to find clarity."))

    return {
        "tool": "career-guidance",
        "name": name,
        "dob": dob,
        "mainNumber": lp,
        "mainPercentage": lp * 10 + 50,  # Just for fun display: 60–90%
        "title": "Career Guidance",
        "summary": f"🎯 Based on your Life Path Number {lp}, your ideal career path is: **{career_title}**.\n\n{career_text}"
    }
