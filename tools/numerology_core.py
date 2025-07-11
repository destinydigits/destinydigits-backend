
import datetime

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

def numerology_values(name):
    name = name.upper()
    all_letters = [PYTHAGOREAN_VALUES[c] for c in name if c in PYTHAGOREAN_VALUES]
    vowels = [PYTHAGOREAN_VALUES[c] for c in name if c in VOWELS]
    consonants = [PYTHAGOREAN_VALUES[c] for c in name if c not in VOWELS and c in PYTHAGOREAN_VALUES]
    return {
        'expressionNumber': reduce_number(sum(all_letters)),
        'heartNumber': reduce_number(sum(vowels)),
        'personalityNumber': reduce_number(sum(consonants)),
        'habitNumber': reduce_number(sum(PYTHAGOREAN_VALUES[c] for c in name.split()[0] if c in PYTHAGOREAN_VALUES)),
        'firstLetter': name[0],
        'firstVowel': next((c for c in name if c in VOWELS), None),
        'hiddenPassion': max(set(all_letters), key=all_letters.count) if all_letters else None
    }

def get_challenge_numbers(day, month, year):
    c1 = abs(month - day)
    c2 = abs(day - year)
    c3 = abs(c2 - c1)
    c4 = abs(year - month)
    return [reduce_number(c) for c in (c1, c2, c3, c4)]

def get_pinnacle_numbers(day, month, year):
    p1 = reduce_number(day + month)
    p2 = reduce_number(day + year)
    p3 = reduce_number(p1 + p2)
    p4 = reduce_number(month + year)
    return [p1, p2, p3, p4]

def extract_full_numerology(name, dob_str):
    dob = datetime.datetime.strptime(dob_str, "%d-%m-%Y")
    day, month, year = dob.day, dob.month, dob.year

    numbers = numerology_values(name)

    birth_number = reduce_number(day)
    destiny_number = reduce_number(sum(int(d) for d in dob_str if d.isdigit()))
    talent_number = [int(d) for d in str(destiny_number)] if destiny_number > 9 else [destiny_number]
    ultimate_number = reduce_number(numbers['expressionNumber'] + destiny_number)

    today = datetime.datetime.today()
    personal_year = reduce_number(day + month + today.year)
    personal_month = reduce_number(personal_year + today.month)
    personal_day = reduce_number(personal_month + today.day)

    return {
        'nameNumber': numbers['expressionNumber'],
        'birthNumber': birth_number,
        'destinyNumber': destiny_number,
        'heartNumber': numbers['heartNumber'],
        'personalityNumber': numbers['personalityNumber'],
        'ultimateNumber': ultimate_number,
        'talentNumber': talent_number,
        'habitNumber': numbers['habitNumber'],
        'firstLetter': numbers['firstLetter'],
        'firstVowel': numbers['firstVowel'],
        'challengeNumbers': get_challenge_numbers(day, month, reduce_number(year)),
        'pinnacleNumbers': get_pinnacle_numbers(day, month, reduce_number(year)),
        'personalYear': personal_year,
        'personalMonth': personal_month,
        'personalDay': personal_day
    }
