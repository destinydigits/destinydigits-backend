# File: tools/vedic_numerology_kundali.py
import datetime
from collections import defaultdict
import json

# ---------------------- CORE REDUCTION ----------------------
def reduce_strict(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

# ---------------------- BASIC NUMBERS ----------------------
def get_birth_number(dob):
    return reduce_strict(int(dob.split("-")[2]))

def get_destiny_number(dob):
    return reduce_strict(sum(int(d) for d in dob.replace("-", "")))

# ---------------------- GRID NUMBERS ----------------------
def get_grid_numbers(dob):
    digits = [int(d) for d in dob.replace("-", "")]
    frequency = defaultdict(int)
    for d in digits:
        frequency[d] += 1
    available = sorted(set(frequency.keys()))
    missing = [i for i in range(1, 10) if i not in available]
    return frequency, available, missing

# ---------------------- MAHADASHA ----------------------
def get_mahadasha_sequence(birth_number):
    sequence = []
    current = birth_number
    total = 0
    while total < 45:
        years = current
        if total + years > 45:
            years = 45 - total
        sequence.append((current, years))
        total += years
        current = 1 if current == 9 else current + 1
    return sequence

# ---------------------- ANTARDASHA ----------------------
def get_year_number(year):
    return reduce_strict(sum(int(d) for d in str(year)))

def get_antardasha(mahadasha, year):
    num = (mahadasha + get_year_number(year)) % 9
    return 9 if num == 0 else num

# ---------------------- PRATYANTARDASHA ----------------------
def get_pratyantardasha(antardasha):
    return [(month, (antardasha + month) % 9 or 9) for month in range(1, 13)]

# ---------------------- PREDICTION TEXT LOADER ----------------------
def load_predictions():
    try:
        with open("prediction_texts.json", "r") as f:
            return json.load(f)
    except:
        return {"remedies": {}, "traits": {}}

# ---------------------- MAIN FUNCTION ----------------------
def generate_vedic_kundali(name, dob):
    birth_number = get_birth_number(dob)
    destiny_number = get_destiny_number(dob)
    frequency, available, missing = get_grid_numbers(dob)
    mahadasha_seq = get_mahadasha_sequence(birth_number)

    start_year = datetime.datetime.strptime(dob, "%Y-%m-%d").year
    year_cursor = start_year
    dasha_timeline = []

    for m_number, duration in mahadasha_seq:
        for i in range(duration):
            current_year = year_cursor + i
            antar = get_antardasha(m_number, current_year)
            pratyantar = get_pratyantardasha(antar)
            dasha_timeline.append({
                "year": current_year,
                "mahadasha": m_number,
                "antardasha": antar,
                "pratyantardasha": [
                    {"month": m, "number": p} for m, p in pratyantar
                ]
            })
        year_cursor += duration

    predictions = load_predictions()

    return {
        "tool": "vedic-numerology-kundali",
        "name": name,
        "dob": dob,
        "birth_number": birth_number,
        "destiny_number": destiny_number,
        "ank_kundali": dict(frequency),
        "available_numbers": available,
        "missing_numbers": missing,
        "mahadasha_chart": dasha_timeline,
        "remedies": predictions.get("remedies", {}),
        "traits": predictions.get("traits", {})
    }

# For local testing only
if __name__ == "__main__":
    print(json.dumps(generate_vedic_kundali("Ravi Kumar", "1985-03-31"), indent=2))
