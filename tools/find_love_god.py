from tools.numerology_core import extract_full_numerology

LOVE_GOD_MAP = {
    1: ("Eros (Greek)", "Passionate, direct, and bold in love."),
    2: ("Hathor (Egyptian)", "Nurturing, emotionally intuitive, and values deep bonds."),
    3: ("Freyja (Norse)", "Creative, joyful, and attracts love through charm."),
    4: ("Parvati (Indian)", "Devoted, stable, and builds strong emotional foundations."),
    5: ("Aphrodite (Greek)", "Adventurous, sensual, and thrives on excitement in love."),
    6: ("Lakshmi (Indian)", "Romantic, harmonious, and believes in spiritual connection."),
    7: ("Cupid (Roman)", "Mysterious, idealistic, and seeks soul-level connection."),
    8: ("Ishtar (Babylonian)", "Strong, magnetic, and desires power balance in love."),
    9: ("Radha (Indian)", "Compassionate, selfless, and devoted in love."),
}

def run_find_love_god_tool(name, dob):
    try:
        if not name or not dob:
            raise ValueError("Name and DOB are required")

        numerology = extract_full_numerology(name, dob)
        heart_number = numerology.get("heartNumber")

        if heart_number in LOVE_GOD_MAP:
            deity, message = LOVE_GOD_MAP[heart_number]
            return {
                "tool": "find-love-god",
                "name": name,
                "dob": dob,
                "mainNumber": heart_number,
                "mainPercentage": 0,
                "emoji": "💘",
                "title": "Find Your Love God",
                "summary": f"Your symbolic Love God is **{deity}**.\n\n{message}",
                "loveGod": deity,
                "vibe": message,
                "syncMessage": "Let the divine guide your heart’s journey."
            }
        else:
            return {
                "tool": "find-love-god",
                "name": name,
                "dob": dob,
                "mainNumber": 0,
                "mainPercentage": 0,
                "emoji": "❓",
                "title": "Find Your Love God",
                "summary": "Could not determine your heart number.",
                "loveGod": "Unknown",
                "vibe": "",
                "syncMessage": ""
            }

    except Exception as e:
        return {
            "tool": "find-love-god",
            "name": name,
            "dob": dob,
            "mainNumber": 0,
            "mainPercentage": 0,
            "emoji": "❌",
            "title": "Find Your Love God",
            "summary": f"Something went wrong: {str(e)}",
            "loveGod": "Unknown",
            "vibe": "",
            "syncMessage": ""
        }
