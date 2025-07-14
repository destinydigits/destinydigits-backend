def get_karmic_lesson_marriage(data):
    import re

    name = data.get("name", "").upper()
    dob = data.get("dob", "")

    # ---------------------- Life Path Calculation ----------------------
    digits = [int(ch) for ch in re.sub(r"[^0-9]", "", dob)]
    life_path = sum(digits)
    while life_path > 9:
        life_path = sum(int(d) for d in str(life_path))

    life_path_meanings = {
        1: "Leader, independent, takes initiative",
        2: "Peacemaker, patient, nurturing",
        3: "Creative, expressive, joyful",
        4: "Practical, grounded, responsible",
        5: "Freedom seeker, adaptable, energetic",
        6: "Loving, loyal, family-oriented",
        7: "Spiritual, introspective, deep thinker",
        8: "Ambitious, powerful, material mastery",
        9: "Compassionate, old soul, forgiving"
    }

    life_path_description = life_path_meanings.get(life_path, "")

    # ---------------------- Karmic Lessons ----------------------
    pythagorean = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5,
        'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5,
        'X': 6, 'Y': 7, 'Z': 8
    }

    vowels = set("AEIOU")
    consonant_nums = []
    vowel_nums = []

    for ch in name:
        if ch in pythagorean:
            val = pythagorean[ch]
            if ch in vowels:
                vowel_nums.append(val)
            else:
                consonant_nums.append(val)

    karmic_missing = sorted(set(range(1, 10)) - set(consonant_nums))
    karmic_lesson_map = {
        1: "Self-confidence, taking initiative",
        2: "Cooperation, patience",
        3: "Expressing emotions, joy",
        4: "Stability, responsibility",
        5: "Adaptability, letting go",
        6: "Commitment, love",
        7: "Trust, spiritual faith",
        8: "Power, money karma",
        9: "Forgiveness, letting go of past"
    }
    karmic_lessons = [karmic_lesson_map[num] for num in karmic_missing]

    # ---------------------- Soul Urge ----------------------
    soul_urge = sum(vowel_nums)
    while soul_urge > 9:
        soul_urge = sum(int(d) for d in str(soul_urge))

    soul_urge_meanings = {
        1: "You seek recognition, respect and leadership in love.",
        2: "You crave emotional bonding and harmony.",
        3: "You long for fun, creativity and expressive love.",
        4: "You need stable, dependable love rooted in loyalty.",
        5: "You want freedom in love and a partner who gives space.",
        6: "You deeply desire family, nurturing and true companionship.",
        7: "You seek soulful, spiritual connection.",
        8: "You desire ambition, power and loyalty in love.",
        9: "You want a divine, karmic bond – with compassion and depth."
    }
    soul_description = soul_urge_meanings.get(soul_urge, "")

    # ---------------------- Final Summary ----------------------
    summary = f"Life Path: {life_path} → {life_path_description}\n"
    summary += f"Karmic Lessons (missing): {', '.join(map(str, karmic_missing))}\n"
    summary += "\n" + "\n".join([f"- {lesson}" for lesson in karmic_lessons]) + "\n\n"
    summary += f"Soul Urge: {soul_urge} → {soul_description}"

    return {
        "tool": "karmic-marriage",
        "name": name.title(),
        "dob": dob,
        "mainNumber": life_path,
        "title": f"Karmic Lesson in Marriage",
        "summary": summary,
        "extraTip": "Marriage is your spiritual classroom – embrace the lessons with love."
    }
