from tools.numerology_core import extract_full_numerology

def run_find_love_god_tool(name, dob):
    try:
        if not name or not dob:
            raise ValueError("Name and DOB are required")

        numerology = extract_full_numerology(name, dob)
        heart_number = numerology.get("heartNumber") or numerology.get("heart_number")

        if not heart_number or not isinstance(heart_number, int):
            raise ValueError("Unable to calculate Heart Number")

        love_god_map = {
            1: ("Eros", "💘", "Passionate Initiator", "You channel deep desire and fearless romantic energy."),
            2: ("Hathor", "🌺", "Romantic Harmonizer", "You seek emotional connection and nurturing in love."),
            3: ("Aphrodite", "🌸", "Playful Charmer", "You enchant others with charm, wit, and beauty."),
            4: ("Parvati", "🪷", "Steadfast Devotee", "You value loyalty, tradition, and deep spiritual love."),
            5: ("Freyja", "🔥", "Adventurous Lover", "You seek freedom, passion, and unforgettable experiences."),
            6: ("Kamadeva", "🌿", "Nurturing Guardian", "You protect love and family with a graceful heart."),
            7: ("Venus", "✨", "Spiritual Lover", "You crave soul connection and metaphysical romance."),
            8: ("Inanna", "👑", "Empowered Romantic", "You balance power and passion in your relationships."),
            9: ("Radha", "🎶", "Transcendent Devotee", "Your love reflects divine surrender and emotional wisdom."),
        }

        deity_info = love_god_map.get(heart_number)
        if not deity_info:
            raise ValueError("No matching deity for Heart Number")

        deity, emoji, vibe, message = deity_info

        return {
            "tool": "find-love-god",
            "name": name,
            "dob": dob,
            "mainNumber": heart_number,
            "mainPercentage": 80 + heart_number,
            "title": "Find Your Love God",
            "emoji": emoji,
            "loveGod": deity,
            "vibe": vibe,
            "syncMessage": message,
            "summary": f"Based on your Heart Number {heart_number}, your romantic energy aligns with {deity}, the deity of {vibe.lower()}."
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
            "loveGod": "Unknown",
            "vibe": "",
            "syncMessage": "",
            "summary": f"Something went wrong: {str(e)}"
        }
