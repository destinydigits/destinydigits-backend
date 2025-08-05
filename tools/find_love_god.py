from tools.numerology_core import extract_full_numerology

LOVE_GOD_LOOKUP = {
    1: {
        "god": "Eros (Greek)",
        "vibe": "Bold & Passionate",
        "summary": "You are driven by desire and courage, much like Eros, the Greek god of primal love. Your love style is intense, fearless, and magnetic.",
    },
    2: {
        "god": "Freya (Norse)",
        "vibe": "Devoted & Intuitive",
        "summary": "Your heart mirrors Freya, the Norse goddess of love and magic. You're emotionally deep, nurturing, and value soulful bonds.",
    },
    3: {
        "god": "Aphrodite (Greek)",
        "vibe": "Joyful & Alluring",
        "summary": "You embody Aphrodite’s radiant beauty and charm. Your love style is expressive, romantic, and full of playful energy.",
    },
    4: {
        "god": "Kamadeva (Indian)",
        "vibe": "Loyal & Grounded",
        "summary": "Your devotion echoes Kamadeva, the Indian god of desire. You offer stability and sensual warmth to your relationships.",
    },
    5: {
        "god": "Hathor (Egyptian)",
        "vibe": "Adventurous & Magnetic",
        "summary": "Like Hathor, you bring joy and sensual adventure. Your love path is exciting, and you thrive on variety and connection.",
    },
    6: {
        "god": "Parvati (Indian)",
        "vibe": "Compassionate & Romantic",
        "summary": "Your energy resonates with Parvati — a symbol of unconditional love and dedication. You're caring, artistic, and value emotional harmony.",
    },
    7: {
        "god": "Cupid (Roman)",
        "vibe": "Mystic & Soulful",
        "summary": "Cupid’s mystical presence aligns with your spiritual heart. You long for deep, soul-to-soul connections that transcend the ordinary.",
    },
    8: {
        "god": "Inanna (Mesopotamian)",
        "vibe": "Powerful & Sensual",
        "summary": "Inanna’s fierce love energy mirrors yours — powerful, transformative, and bold. You're not afraid to lead with passion.",
    },
    9: {
        "god": "Rati (Indian)",
        "vibe": "Universal & Healing",
        "summary": "Your soul reflects Rati, goddess of longing and divine love. You offer selfless affection, healing energy, and emotional wisdom.",
    }
}

def run_find_love_god(name, dob):
    try:
        if not name or not dob:
            raise ValueError("Missing name or dob")

        numerology = extract_full_numerology(name, dob)
        heart = numerology.get("heartNumber") or numerology.get("heart_desire")
        expr = numerology.get("expression_number")

        number = heart if heart else expr
        if not number or number not in LOVE_GOD_LOOKUP:
            raise ValueError("Unable to determine vibration number")

        deity = LOVE_GOD_LOOKUP[number]

        return {
            "tool": "find-love-god",
            "name": name,
            "dob": dob,
            "mainNumber": number,
            "mainPercentage": 90,
            "emoji": "💘",
            "title": "Find Your Love God",
            "loveGod": deity["god"],
            "vibe": deity["vibe"],
            "summary": deity["summary"],
            "syncMessage": f"{deity['god']} is your symbolic guide in love — let this divine energy inspire your heart's journey."
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
            "loveGod": "",
            "vibe": "",
            "syncMessage": ""
        }
