# File: tools/vedic_numerology_kundali.py
import datetime
from collections import defaultdict
import json

# ---------------------- PLANET MAPPING ----------------------
PLANET_MAP = {
    1: "Sun (Surya)",
    2: "Moon (Chandra)",
    3: "Jupiter (Guru)",
    4: "Rahu",
    5: "Mercury (Budh)",
    6: "Venus (Shukra)",
    7: "Ketu",
    8: "Saturn (Shani)",
    9: "Mars (Mangal)"
}

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
def get_mahadasha_sequence(birth_number, years=90):
    sequence = []
    current = birth_number
    total = 0
    while total < years:
        years_span = current
        if total + years_span > years:
            years_span = years - total
        sequence.append((current, years_span))
        total += years_span
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
    # Basic calculations
    birth_number = get_birth_number(dob)
    destiny_number = get_destiny_number(dob)
    frequency, available, missing = get_grid_numbers(dob)
    
    today = datetime.date.today()
    dob_date = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
    current_age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))

    # Start from (current_age - 1) for context, go till 90 years of age
    start_year = today.year - 1
    years_remaining = 90 - current_age + 1  # +1 to include current year
    mahadasha_seq = get_mahadasha_sequence(birth_number, years=years_remaining)

    dasha_timeline = []
    year_cursor = start_year

    for m_number, duration in mahadasha_seq:
        for i in range(duration):
            current_year = year_cursor + i
            antar = get_antardasha(m_number, current_year)
            pratyantar = get_pratyantardasha(antar)
            dasha_timeline.append({
                "year": current_year,
                "mahadasha": m_number,
                "mahadasha_planet": PLANET_MAP[m_number],
                "antardasha": antar,
                "antardasha_planet": PLANET_MAP[antar],
                "pratyantardasha": [
                    {"month": m, "number": p, "planet": PLANET_MAP[p]} for m, p in pratyantar
                ]
            })
        year_cursor += duration

    # Current Dasha
    current_dasha = next((item for item in dasha_timeline if item["year"] == today.year), None)

    predictions = load_predictions()

    return {
        "tool": "vedic-numerology-kundali",
        "name": name,
        "dob": dob,
        "birth_number": birth_number,
        "birth_planet": PLANET_MAP[birth_number],
        "destiny_number": destiny_number,
        "destiny_planet": PLANET_MAP[destiny_number],
        "ank_kundali": dict(frequency),
        "available_numbers": available,
        "missing_numbers": missing,
        "current_dasha": current_dasha,
        "mahadasha_chart": dasha_timeline,
        "remedies": predictions.get("remedies", {}),
        "traits": predictions.get("traits", {})
    }

# For local testing
if __name__ == "__main__":
    print(json.dumps(generate_vedic_kundali("Ravi Kumar", "1985-03-31"), indent=2))
