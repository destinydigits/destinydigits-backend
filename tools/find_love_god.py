from tools.numerology_core import extract_full_numerology

LOVE_GODS = {
    1: {
        "god": "Eros",
        "culture": "Greek",
        "vibe": "Bold & Passionate",
        "message": "You lead with fiery intensity and crave direct, passionate love."
    },
    2: {
        "god": "Freyja",
        "culture": "Norse",
        "vibe": "Empathic & Devoted",
        "message": "You seek soulful connection and emotional depth in relationships."
    },
    3: {
        "god": "Aphrodite",
        "culture": "Greek",
        "vibe": "Playful & Artistic",
        "message": "You love with beauty, charm, and a flair for romance."
    },
    4: {
        "god": "Parvati",
        "culture": "Indian",
        "vibe": "Loyal & Grounded",
        "message": "You offer steady love rooted in loyalty, family, and care."
    },
    5: {
        "god": "Rati",
        "culture": "Indian",
        "vibe": "Adventurous & Sensual",
        "message": "You crave exciting and sensual love experiences, always seeking thrill."
    },
    6: {
        "god": "Hathor",
        "culture": "Egyptian",
        "vibe": "Nurturing & Romantic",
        "message": "You express love through kindness, nurturing, and emotional support."
    },
    7: {
        "god": "Ishtar",
        "culture": "Mesopotamian",
        "vibe": "Mysterious & Spiritual",
        "message": "You connect through spiritual bonds and deeper understanding of the soul."
    },
    8: {
        "god": "Venus",
        "culture": "Roman",
        "vibe": "Powerful & Alluring",
        "message": "You love with confidence, magnetism, and emotional authority."
    },
    9: {
        "god": "Lakshmi",
        "culture": "Indian",
        "vibe": "Compassionate & Divine",
        "message": "You radiate love through generosity, grace, and deep compassion."
    }
}

def run_find_love_god(data):
    name = data.get("name")
    dob = data.get("dob")
    try:
        if not name or not dob:
            raise ValueError("Name and DOB required")

        numerology = extract_full_numerology(name, dob)
        heart = numerology.get("heartNumber") or numerology.get("heart_number")

        if not heart or heart not in LOVE_GODS:
            raise ValueError("Heart Number missing or invalid")

        god_info = LOVE_GODS[heart]

        return {
            "tool": "find-love-god",
            "name": name,
            "dob": dob,
            "mainNumber": heart,
            "mainPercentage": heart * 11,  # Optional for visual meter
            "emoji": "💘",
            "title": "Find Your Love God",
            "summary": f"Your Heart Number is {heart}. Based on your romantic vibration, your symbolic love deity is {god_info['god']} ({god_info['culture']}).",
            "loveGod": god_info["god"],
            "vibe": god_info["vibe"],
            "syncMessage": god_info["message"]
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
