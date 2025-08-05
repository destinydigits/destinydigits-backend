from tools.numerology_core import extract_full_numerology

LOVE_GOD_MAP = {
    1: {
        "god": "Eros",
        "vibe": "Passionate Initiator",
        "summary": "You are bold and unafraid in love. Your heart is ruled by Eros, the Greek god of passion. You bring spark and desire into relationships, lighting fires that can’t be ignored.",
        "syncMessage": "Trust your passion — let Eros guide you to pursue love with courage and intensity."
    },
    2: {
        "god": "Radha",
        "vibe": "Devoted Companion",
        "summary": "Your heart resonates with Radha, symbol of divine devotion and soul connection in Indian mythology. You seek emotional closeness and spiritual bonding.",
        "syncMessage": "Let your love flow with devotion — Radha's energy helps you create soulful bonds that last."
    },
    3: {
        "god": "Freyja",
        "vibe": "Creative Charmer",
        "summary": "Your heart dances with Freyja, the Norse goddess of love and beauty. You express love through joy, charm, and emotional creativity.",
        "syncMessage": "Let Freyja inspire your heart — charm, express, and celebrate the joy of connection."
    },
    4: {
        "god": "Hathor",
        "vibe": "Loyal Protector",
        "summary": "You embody Hathor’s spirit, the Egyptian goddess of love, protection, and motherhood. Your love is stable, loyal, and deeply nurturing.",
        "syncMessage": "Let Hathor remind you — love grows through care, loyalty, and shared structure."
    },
    5: {
        "god": "Cupid",
        "vibe": "Magnetic Explorer",
        "summary": "With Cupid’s essence, you seek excitement and variety in love. Your heart craves freedom, but also delights in the playful pursuit of connection.",
        "syncMessage": "Let Cupid's arrows lead you — explore love with curiosity, but stay true to your core."
    },
    6: {
        "god": "Aphrodite",
        "vibe": "Romantic Dreamer",
        "summary": "Your heart number is 6 – full of love, harmony, and beauty. Your guiding Love God is Aphrodite, the Greek goddess of love and desire. Her divine influence helps you form deep, beautiful connections that celebrate emotional truth and romance.",
        "syncMessage": "Let your love life be guided by Aphrodite's grace — express beauty, care, and soul-deep connection."
    },
    7: {
        "god": "Parvati",
        "vibe": "Spiritual Lover",
        "summary": "Your love path aligns with Parvati, the goddess of devotion and inner connection. You seek depth and meaning beyond physical attraction.",
        "syncMessage": "Let Parvati's calm devotion lead you — seek the soul behind the smile."
    },
    8: {
        "god": "Venus",
        "vibe": "Sensual Power",
        "summary": "Venus blesses you with the power to love with intensity and stability. You offer your partner emotional strength, sensuality, and loyalty.",
        "syncMessage": "Let Venus shine through you — love boldly and protect what matters."
    },
    9: {
        "god": "Lakshmi",
        "vibe": "Compassionate Healer",
        "summary": "Your love is generous and healing. Guided by Lakshmi, you bring compassion, support, and grace to every connection.",
        "syncMessage": "Let Lakshmi guide your relationships — serve with love and uplift others through care."
    }
}


def run_find_love_god(name, dob):
    try:
        if not name or not dob:
            raise ValueError("Name and DOB required")

        numerology = extract_full_numerology(name, dob)
        heart_number = numerology.get("heartNumber") or numerology.get("heart_number")

        if heart_number not in LOVE_GOD_MAP:
            raise ValueError("Unable to map heart number")

        god_data = LOVE_GOD_MAP[heart_number]

        return {
            "tool": "find-love-god",
            "name": name,
            "dob": dob,
            "mainNumber": heart_number,
            "mainPercentage": 0,
            "title": "Find Your Love God",
            "emoji": "💘",
            "summary": god_data["summary"],
            "loveGod": god_data["god"],
            "vibe": god_data["vibe"],
            "syncMessage": god_data["syncMessage"]
        }

    except Exception as e:
        return {
            "tool": "find-love-god",
            "name": name,
            "dob": dob,
            "mainNumber": 0,
            "mainPercentage": 0,
            "title": "Find Your Love God",
            "emoji": "❌",
            "summary": f"Something went wrong: {str(e)}",
            "loveGod": "",
            "vibe": "",
            "syncMessage": ""
        }
