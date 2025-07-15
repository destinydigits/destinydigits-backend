def get_attraction_insight(data):
    import re
    from collections import Counter

    name = data.get("name", "").upper()

    # ---------------- Pythagorean Mapping ------------------
    pythagorean = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5,
        'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5,
        'X': 6, 'Y': 7, 'Z': 8
    }

    vowels = set("AEIOU")
    consonants = [ch for ch in name if ch in pythagorean and ch not in vowels]
    numbers = [pythagorean[ch] for ch in name if ch in pythagorean]

    # ---------------- Hidden Passion ------------------
    counter = Counter(numbers)
    most_common = counter.most_common(1)
    hidden_passion = most_common[0][0] if most_common else 0

    # ---------------- Personality Number ------------------
    total = sum(pythagorean[ch] for ch in consonants)
    while total > 9 and total not in (11, 22):
        total = sum(int(d) for d in str(total))
    personality = total

    # ---------------- Mappings ------------------
    passion_map = {
        1: {"passion_type": "confident and driven", "passion_energy": "decisive energy"},
        2: {"passion_type": "gentle and caring", "passion_energy": "emotional depth"},
        3: {"passion_type": "fun-loving and witty", "passion_energy": "joy and laughter"},
        4: {"passion_type": "stable and loyal", "passion_energy": "structure and support"},
        5: {"passion_type": "adventurous", "passion_energy": "spontaneity"},
        6: {"passion_type": "nurturing and devoted", "passion_energy": "emotional security"},
        7: {"passion_type": "spiritual and mysterious", "passion_energy": "depth and wisdom"},
        8: {"passion_type": "powerful and ambitious", "passion_energy": "material confidence"},
        9: {"passion_type": "compassionate and artistic", "passion_energy": "romantic sensitivity"}
    }

    personality_map = {
        1: {"personality_style": "bold and assertive", "personality_effect": "motivated and safe"},
        2: {"personality_style": "calm and nurturing", "personality_effect": "emotionally safe"},
        3: {"personality_style": "expressive and fun", "personality_effect": "relaxed and amused"},
        4: {"personality_style": "disciplined and structured", "personality_effect": "secure and organized"},
        5: {"personality_style": "spontaneous and free", "personality_effect": "excited and curious"},
        6: {"personality_style": "caring and family-oriented", "personality_effect": "nurtured and loved"},
        7: {"personality_style": "introspective and deep", "personality_effect": "emotionally intrigued"},
        8: {"personality_style": "confident and ambitious", "personality_effect": "impressed and attracted"},
        9: {"personality_style": "sensitive and poetic", "personality_effect": "emotionally moved"}
    }

    compatibility_map = {
        "1-2": {"compatibility_summary": "creates a powerful balance", "combo_trait_1": "stability", "combo_trait_2": "emotional connection"},
        "5-2": {"compatibility_summary": "blends freedom with empathy", "combo_trait_1": "spontaneity", "combo_trait_2": "understanding"},
        "3-6": {"compatibility_summary": "makes for joyful nurturing bonds", "combo_trait_1": "creativity", "combo_trait_2": "affection"}
    }

    pair_key = f"{hidden_passion}-{personality}"
    reverse_key = f"{personality}-{hidden_passion}"
    compatibility = compatibility_map.get(pair_key) or compatibility_map.get(reverse_key) or {
        "compatibility_summary": "creates a unique attraction dynamic",
        "combo_trait_1": "peace",
        "combo_trait_2": "intensity"
    }

    passion = passion_map.get(hidden_passion, {"passion_type": "interesting", "passion_energy": "energy"})
    persona = personality_map.get(personality, {"personality_style": "balanced", "personality_effect": "comfortable"})

    paragraph = (
        f"You naturally feel attracted to {passion['passion_type']} people who bring {passion['passion_energy']} into life. "
        f"At the same time, you come across as {persona['personality_style']} — making others feel {persona['personality_effect']}. "
        f"This {compatibility['compatibility_summary']}. You attract those who want both {compatibility['combo_trait_1']} and {compatibility['combo_trait_2']} in love."
    )

    return {
    "tool": "attraction-insight",
    "name": name.title(),
    "dob": data.get("dob", ""),
    "mainNumber": personality,
    "mainPercentage": None,
    "title": "Attraction Number Insight",
    "summary": paragraph,
    "paragraph": paragraph,
    "hiddenPassion": hidden_passion,
    "personalityNumber": personality
}
