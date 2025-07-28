import datetime
from .lookup_tables import (
    number_profile,
    heart_profile,
    challenge_profile,
    expression_profile,
    personality_profile
)

PYTHAGOREAN_VALUES = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
    'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
}

VOWELS = set('AEIOU')


def reduce_number(n):
    while n > 9 and n not in (11, 22, 33):
        n = sum(int(d) for d in str(n))
    return n

def reduce_strict(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n
    
def reduce_to_single_digit(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def numerology_values(name):
    name = name.upper()
    all_letters = [PYTHAGOREAN_VALUES[c] for c in name if c in PYTHAGOREAN_VALUES]
    vowels = [PYTHAGOREAN_VALUES[c] for c in name if c in VOWELS]
    consonants = [PYTHAGOREAN_VALUES[c] for c in name if c not in VOWELS and c in PYTHAGOREAN_VALUES]
    return {
        'expressionNumber': reduce_strict(sum(all_letters)),
        'heartNumber': reduce_strict(sum(vowels)),
        'personalityNumber': reduce_strict(sum(consonants)),
        'habitNumber': reduce_strict(sum(PYTHAGOREAN_VALUES[c] for c in name.split()[0] if c in PYTHAGOREAN_VALUES)),
        'firstLetter': name[0],
        'firstVowel': next((c for c in name if c in VOWELS), None),
        'hiddenPassion': max(set(all_letters), key=all_letters.count) if all_letters else None
    }

def get_challenge_numbers(day, month, year):
    c1 = abs(month - day)
    c2 = abs(day - year)
    c3 = abs(c2 - c1)
    c4 = abs(year - month)
    reduced = [reduce_strict(c) for c in (c1, c2, c3, c4)]
    return reduced

def get_primary_challenge_number(challenge_list):
    for c in challenge_list:
        if c != 0:
            return c
    return None

def get_pinnacle_numbers(day, month, year):
    p1 = reduce_strict(day + month)
    p2 = reduce_strict(day + year)
    p3 = reduce_strict(p1 + p2)
    p4 = reduce_strict(month + year)
    return [p1, p2, p3, p4]

def enrich_report(numbers):
    lp = numbers["life_path"]
    enriched = number_profile.get(lp, {})
    numbers.update(enriched)

    # Get expression profile safely
    expr = expression_profile.get(numbers.get("expression_number"), {})
    numbers["talents"] = expr.get("talents", "")
    numbers["expressionTrait"] = expr.get("expressionTrait", "")
    numbers["problemSolvingStyle"] = expr.get("problemSolvingStyle", "")

    # Get heart profile safely
    heart = heart_profile.get(numbers.get("heartNumber"), "")
    numbers["emotionalNeed"] = heart if isinstance(heart, str) else heart.get("emotionalNeed", "")

    # Get personality profile safely
    mask = personality_profile.get(numbers.get("personality_number"), "")
    numbers["outerMask"] = mask if isinstance(mask, str) else mask.get("outerMask", "")

    # For JS compatibility (optional duplicates)
    numbers["heartDescription"] = numbers["emotionalNeed"]
    numbers["expressionDescription"] = numbers["expressionTrait"]
    numbers["maskDescription"] = numbers["outerMask"]

    # Challenge info
    challenge = challenge_profile.get(numbers.get("challenge_number"), {})
    numbers["struggle"] = challenge.get("struggle", "")
    numbers["resolutionTip"] = challenge.get("resolutionTip", "")

    return numbers


def get_pinnacle_phase_texts(birth_year, pinnacles):
    descriptions = {
        1: "Independence, ambition, leadership",
        2: "Emotional sensitivity, building deep bonds",
        3: "Creativity, self-expression, joy",
        4: "Discipline, creating structure",
        5: "Change, adventure, freedom",
        6: "Love, family, and responsibility",
        7: "Spiritual growth, introspection, study",
        8: "Material success, power, management",
        9: "Compassion, service, humanitarian focus"
    }
    return {
        "pinnacle_phase_1": f"Age 0–27: {pinnacles[0]} – {descriptions.get(pinnacles[0], '')}",
        "pinnacle_phase_2": f"Age 28–36: {pinnacles[1]} – {descriptions.get(pinnacles[1], '')}",
        "pinnacle_phase_3": f"Age 37–45: {pinnacles[2]} – {descriptions.get(pinnacles[2], '')}",
        "pinnacle_phase_4": f"Age 46+: {pinnacles[3]} – {descriptions.get(pinnacles[3], '')}",
    }


def extract_full_numerology(name, dob_str):
    dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d")
    day, month, year = dob.day, dob.month, dob.year

    numbers = numerology_values(name)
    master_numbers = {}

    raw_birth = day
    birth_number = reduce_strict(day)
    if raw_birth in (11, 22, 33):
        master_numbers['birthNumber'] = raw_birth

    raw_destiny = sum(int(d) for d in dob_str if d.isdigit())
    destiny_number = reduce_strict(raw_destiny)
    life_path = destiny_number
    if raw_destiny in (11, 22, 33):
        master_numbers['destinyNumber'] = raw_destiny

    talent_number = [int(d) for d in str(destiny_number)] if destiny_number > 9 else [destiny_number]
    ultimate_number = reduce_strict(numbers['expressionNumber'] + destiny_number)
    challenge_list = get_challenge_numbers(day, month, reduce_strict(year))
    challenge_number = get_primary_challenge_number(challenge_list)
    today = datetime.datetime.today()
    personal_year = reduce_to_single_digit(day + month + today.year)
    personal_month = reduce_to_single_digit(personal_year + today.month)
    personal_day = reduce_to_single_digit(personal_month + today.day)

    pinnacles = get_pinnacle_numbers(day, month, reduce_strict(year))
    challenge_list = get_challenge_numbers(day, month, reduce_strict(year))
    challenge_number = get_primary_challenge_number(challenge_list)

    result = {
        'nameNumber': numbers['expressionNumber'],
        'birthNumber': birth_number,
        'life_path': life_path,
        'destinyNumber': destiny_number,
        'heartNumber': numbers['heartNumber'],
        'personalityNumber': numbers['personalityNumber'],
        'ultimateNumber': ultimate_number,
        'talentNumber': talent_number,
        'habitNumber': numbers['habitNumber'],
        'firstLetter': numbers['firstLetter'],
        'firstVowel': numbers['firstVowel'],
        'challengeNumbers': challenge_list,
        'challenge_number': challenge_number,
        'p1': pinnacles[0],
        'p2': pinnacles[1],
        'p3': pinnacles[2],
        'p4': pinnacles[3],
        'c1': challenge_list[0],
        'c2': challenge_list[1],
        'c3': challenge_list[2],
        'c4': challenge_list[3],
        'personalYear': personal_year,
        'personalMonth': personal_month,
        'personalDay': personal_day,
        'heart_desire': numbers['heartNumber'],
        'expression_number': numbers['expressionNumber'],
        'personality_number': numbers['personalityNumber']
    }

    pinnacle_texts = get_pinnacle_phase_texts(year, pinnacles)
    result.update(pinnacle_texts)

    if master_numbers:
        result['masterNumbers'] = master_numbers

    return enrich_report(result)

# ➡ NEW FUNCTION FOR FULL REPORT
def generate_full_report(name, dob_str):
    data = extract_full_numerology(name, dob_str)
    sections = []

    # 1. Life Path Section
    lp = data.get('life_path')
    if lp in number_profile:
        profile = number_profile[lp]
        sections.append(f"""
        <div class='report-box'>
            <h3>✨ 1. Life Path – Your Soul’s Journey</h3>
            <p>{profile.get('lifeDescription', '')}</p>
            <p><strong>Core Trait:</strong> {profile.get('coreTrait', '')}</p>
            <p><strong>Life Purpose:</strong> {profile.get('lifePurpose', '')}</p>
            <p><strong>Gift:</strong> {profile.get('gift', '')}</p>
        </div>
        """)

    # 2. Heart’s Desire Section
    heart = data.get('heartNumber')
    if heart in heart_profile:
        heart_data = heart_profile[heart]
        sections.append(f"""
        <div class='report-box'>
            <h3>💖 2. Heart's Desire – Your Emotional Core</h3>
            <p>{heart_data.get('emotionalMessage', '')}</p>
        </div>
        """)

    # 3. Personality Section
    pers = data.get('personality_number')
    if pers in personality_profile:
        pers_data = personality_profile[pers]
        sections.append(f"""
        <div class='report-box'>
            <h3>👥 3. Your Personality – Your Social Mask</h3>
            <p>{pers_data.get('maskMessage', '')}</p>
        </div>
        """)

    # 4. Challenge Section
    ch = data.get('challenge_number')
    if ch in challenge_profile:
        sections.append(f"""
        <div class='report-box'>
            <h3>⚔️ 4. Challenge – Your Inner Work</h3>
            <p><strong>Challenge {ch}:</strong> {challenge_profile[ch].get('struggle', '')}</p>
            <p>💎 <strong>Healing Tip:</strong> {challenge_profile[ch].get('resolutionTip', '')}</p>
        </div>
        """)

    # 5. Expression Section
    exp = data.get('expression_number')
    if exp in expression_profile:
        exp_data = expression_profile[exp]
        sections.append(f"""
        <div class='report-box'>
            <h3>🌈 5. How You Express – Your Gift & Style</h3>
            <p>🔧 <strong>Natural Talents:</strong> {exp_data.get('talents', '')}</p>
            <p>🚀 <strong>How You Shine:</strong> {exp_data.get('expressionTrait', '')}</p>
            <p>🎯 <strong>Your Power Style:</strong> {exp_data.get('problemSolvingStyle', '')}</p>
        </div>
        """)

    # 6. Pinnacle & Personal Numbers
    sections.append(f"""
    <div class='report-box'>
        <h3>🧭 6. Numerology Identity Card</h3>
        <ul>
            <li><strong>Life Path:</strong> {lp} – {number_profile.get(lp, {}).get('coreTrait', '')}</li>
            <li><strong>Heart's Desire:</strong> {data.get('heartNumber', '')}</li>
            <li><strong>Personality:</strong> {data.get('personalityNumber', '')}</li>
            <li><strong>Expression:</strong> {data.get('expression_number', '')}</li>
            <li><strong>Challenge:</strong> {data.get('challenge_number', '')}</li>
            <li><strong>Pinnacle 1:</strong> {data.get('pinnacle_phase_1', '')}</li>
            <li><strong>Pinnacle 2:</strong> {data.get('pinnacle_phase_2', '')}</li>
            <li><strong>Pinnacle 3:</strong> {data.get('pinnacle_phase_3', '')}</li>
            <li><strong>Pinnacle 4:</strong> {data.get('pinnacle_phase_4', '')}</li>
        </ul>
    </div>
    """)

    return "\n".join(sections)



def letter_to_number_pythagorean(letter):
    return PYTHAGOREAN_VALUES.get(letter.upper(), 0)
