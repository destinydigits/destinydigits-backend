from string import digits as digit_chars

def run_mobile_number_checker(mobile_number, name=None, dob=None):
    try:
        # Extract digits only
        digits = [int(d) for d in str(mobile_number) if d in digit_chars]
        if len(digits) < 10:
            raise ValueError("Invalid mobile number")

        total = sum(digits)

        # Reduce total to a vibration number
        while total not in [11, 22, 33] and total > 9:
            total = sum(int(d) for d in str(total))

        vibration = total
        traits = vibration_traits.get(vibration, default_traits)

        # Optional: Destiny comparison
        feeling = ""
        if name and dob:
            try:
                from tools.numerology_core import extract_full_numerology
                profile = extract_full_numerology(name, dob)
                destiny = profile.get("destiny_number") or profile.get("destinyNumber")
                if destiny:
                    diff = abs(vibration - destiny)
                    if destiny == vibration:
                        feeling = "This number is in perfect harmony with your destiny path."
                    elif diff in [1, 2]:
                        feeling = "This number gently supports your destiny path with a unique influence."
                    else:
                        feeling = "This number carries a different energy than your life path — use it with awareness."
            except Exception as e:
                feeling = ""

        return {
            "tool": "mobile-number-checker",
            "mobileNumber": str(mobile_number),
            "mainNumber": vibration,
            "mainPercentage": traits["score"],
            "title": "Mobile Number Vibration Checker",
            "emoji": "📲",
            "summary": traits["summary"],
            "vibrationMeaning": traits["meaning"],
            "energyMessage": traits["message"],
            "remedy": traits["remedy"],
            "feeling": feeling
        }

    except Exception as e:
        return {
            "tool": "mobile-number-checker",
            "mobileNumber": str(mobile_number),
            "mainNumber": 0,
            "mainPercentage": 0,
            "title": "Mobile Number Vibration Checker",
            "emoji": "❌",
            "summary": f"Something went wrong: {str(e)}",
            "vibrationMeaning": "",
            "energyMessage": "",
            "remedy": "",
            "feeling": ""
        }


# 🌟 Lookup Table
vibration_traits = {
    1: {
        "score": 85,
        "meaning": "Leadership, Initiative, Confidence",
        "summary": "Your number vibrates with 1 — ideal for those who lead, build, and take charge. It's great for entrepreneurs and go-getters.",
        "message": "This is a bold and pioneering number. Use it to stand out but stay grounded.",
        "remedy": "Keep a copper coin in your wallet for balance."
    },
    2: {
        "score": 75,
        "meaning": "Partnership, Peace, Sensitivity",
        "summary": "Your mobile number has a soft energy — perfect for consultants, healers, or team players. You build trust easily.",
        "message": "You’re guided by intuition and empathy. Don’t let others overpower your calm.",
        "remedy": "Use a silver case or moonstone accessory to protect emotional energy."
    },
    3: {
        "score": 80,
        "meaning": "Joy, Creativity, Expression",
        "summary": "This number promotes joy, creativity, and strong social influence. Great for artists, influencers, and communicators.",
        "message": "Let your voice be heard — your number supports visibility.",
        "remedy": "Chant 'Om' 3 times before calls for better clarity."
    },
    4: {
        "score": 70,
        "meaning": "Stability, Discipline, Planning",
        "summary": "This number brings structure — great for professionals in law, admin, or engineering. It creates loyalty and trust.",
        "message": "Embrace order, but don’t resist flexibility.",
        "remedy": "Touch your phone to soil or natural surface weekly for grounding."
    },
    5: {
        "score": 78,
        "meaning": "Freedom, Change, Adventure",
        "summary": "Perfect for marketers, travellers, or salespeople — this number attracts opportunities and movement.",
        "message": "Use this vibration to inspire others, but avoid burnout from overcommitment.",
        "remedy": "Use a green accessory to anchor your energy."
    },
    6: {
        "score": 82,
        "meaning": "Love, Family, Responsibility",
        "summary": "Excellent for family people, coaches, and caregivers. You attract harmony — and people come to you for advice.",
        "message": "Balance giving with self-care. Your energy is nurturing.",
        "remedy": "Keep a rose quartz crystal or use soft pink visuals."
    },
    7: {
        "score": 77,
        "meaning": "Wisdom, Mystery, Inner Growth",
        "summary": "Your mobile number connects you to introspection and deep learning. Great for teachers, writers, spiritual seekers.",
        "message": "Don’t isolate too much — stay open to connection too.",
        "remedy": "Use calming sounds or binaural tones when on call."
    },
    8: {
        "score": 88,
        "meaning": "Power, Wealth, Legacy",
        "summary": "A strong number for success-minded people — CEOs, managers, or those in finance. It draws authority.",
        "message": "Respect power and stay humble. Karma responds fast to 8 energy.",
        "remedy": "Donate or give regularly to keep energy flowing."
    },
    9: {
        "score": 83,
        "meaning": "Spirituality, Endings, Influence",
        "summary": "This number carries humanitarian energy. Ideal for speakers, healers, or social workers.",
        "message": "Use your charisma wisely — many people listen when you speak.",
        "remedy": "Light a diya or candle on Thursdays to clear energy."
    },
    11: {
        "score": 91,
        "meaning": "Master Intuition, Vision, Illumination",
        "summary": "Your number has a master frequency — rare and intuitive. You may sense things before others do.",
        "message": "Use this insight to guide, but avoid anxiety from overthinking.",
        "remedy": "Meditate for 11 minutes daily to tune in."
    },
    22: {
        "score": 92,
        "meaning": "Master Builder, Execution, Visionary",
        "summary": "This is a powerful manifestation number. You’re meant to build big things that help the world.",
        "message": "Stay focused and act with clarity — distractions dilute your gift.",
        "remedy": "Keep a to-do list on your phone to stay aligned."
    },
    33: {
        "score": 94,
        "meaning": "Master Teacher, Love in Action",
        "summary": "Your mobile number vibrates with pure compassion. Ideal for spiritual guides, therapists, or mentors.",
        "message": "Stay rooted — others will naturally look to you.",
        "remedy": "Avoid harsh tones or anger on calls; stay calm."
    }
}

default_traits = {
    "score": 70,
    "meaning": "Neutral Energy",
    "summary": "This number carries a neutral vibration. Stay aware of your thoughts and tone during communication.",
    "message": "Numbers don’t define you — your intent does.",
    "remedy": "Speak with kindness and clarity."
}
