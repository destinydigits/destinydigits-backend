import datetime
from .lookup_tables import (
    number_profile,
    heart_profile,
    challenge_profile,
    expression_profile,
    personality_profile
)

PYTHAGOREAN_VALUES = {
    'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
    'J':1, 'K':2, 'L':3, 'M':4, 'N':5, 'O':6, 'P':7, 'Q':8, 'R':9,
    'S':1, 'T':2, 'U':3, 'V':4, 'W':5, 'X':6, 'Y':7, 'Z':8
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
    return [reduce_strict(c) for c in (c1, c2, c3, c4)]

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
    numbers["heartDescription"] = heart_profile.get(numbers.get("heartNumber"), "")
    numbers["struggle"] = challenge_profile.get(numbers.get("challenge_number"), {}).get("struggle", "")
    numbers["resolutionTip"] = challenge_profile.get(numbers.get("challenge_number"), {}).get("resolutionTip", "")
    numbers["expressionDescription"] = expression_profile.get(numbers.get("expression_number"), "")
    numbers["maskDescription"] = personality_profile.get(numbers.get("personality_number"), "")
    return numbers
    
def extract_full_numerology(name, dob_str):
    dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d")
    day, month, year = dob.day, dob.month, dob.year

    numbers = numerology_values(name)
    master_numbers = {}

    # Master check but reduce anyway
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

    today = datetime.datetime.today()
    personal_year = reduce_strict(day + month + today.year)
    personal_month = reduce_strict(personal_year + today.month)
    personal_day = reduce_strict(personal_month + today.day)

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
        'challengeNumbers': get_challenge_numbers(day, month, reduce_strict(year)),
        'pinnacleNumbers': get_pinnacle_numbers(day, month, reduce_strict(year)),
        'personalYear': personal_year,
        'personalMonth': personal_month,
        'personalDay': personal_day,  # ✅ COMMA FIXED HERE
        'heart_desire': numbers['heartNumber'],
        'expression_number': numbers['expressionNumber'],
        'personality_number': numbers['personalityNumber'],
        'challenge_number': get_challenge_numbers(day, month, reduce_strict(year))[0],
        'p1': get_pinnacle_numbers(day, month, reduce_strict(year))[0],
        'p2': get_pinnacle_numbers(day, month, reduce_strict(year))[1],
        'p3': get_pinnacle_numbers(day, month, reduce_strict(year))[2],
        'p4': get_pinnacle_numbers(day, month, reduce_strict(year))[3],
    }
    if master_numbers:
        result['masterNumbers'] = master_numbers

    return enrich_report(result)  


