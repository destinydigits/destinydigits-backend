# File: tools/vedic_numerology_kundali.py (Pro-Level Vedic Numerology Engine)
import datetime
import json
from collections import defaultdict
with open("tools/ank_kundali_traits.json", "r", encoding="utf-8") as f:
    ANK_TRAITS = json.load(f)

with open("tools/birth_destiny_interpretations.json", "r", encoding="utf-8") as f:
    BIRTH_DESTINY_TEXT = json.load(f)

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

# ---------------------- CORE UTILS ---------------------
def reduce_strict(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def get_day_lord_number(date):
    weekday = date.weekday()  # Monday=0, Sunday=6
    mapping = {6: 1, 0: 2, 1: 9, 2: 5, 3: 3, 4: 6, 5: 8}  # Sun=1, Mon=2, Tue=9...
    return mapping.get(weekday, 1)

# ---------------------- BASIC NUMBERS ----------------------
def get_birth_number(dob):
    return reduce_strict(int(dob.split("-")[2]))

def get_destiny_number(dob):
    return reduce_strict(sum(int(d) for d in dob.replace("-", "")))

# ---------------------- PRIMARY ANK KUNDALI ----------------------
def build_primary_ank_kundali(dob, birth_number, destiny_number):
    parts = dob.split("-")
    day, month, year_last2 = parts[2], parts[1], parts[0][2:]
    digits = []
    for val in day + month + year_last2:
        if val != "0":
            digits.append(int(val))
    digits.append(birth_number)
    digits.append(destiny_number)
    grid_map = {n: [] for n in range(1, 10)}
    for d in digits:
        grid_map[d].append(str(d))
    grid = [
        [" ".join(grid_map[3]), " ".join(grid_map[1]), " ".join(grid_map[9])],
        [" ".join(grid_map[6]), " ".join(grid_map[7]), " ".join(grid_map[5])],
        [" ".join(grid_map[2]), " ".join(grid_map[8]), " ".join(grid_map[4])]
    ]
    missing = [num for num, vals in grid_map.items() if not vals]
    return grid, missing

# ---------------------- YOG DETECTION ----------------------
def detect_yogs(digits):
    yogs = []
    sets = [set([1,4,7]), set([2,5,8]), set([3,6,9])]
    for s in sets:
        if s.issubset(digits):
            if s == {1,4,7}:
                yogs.append("1-4-7 Yog: Leadership + Hard Work = Growth")
            if s == {2,5,8}:
                yogs.append("2-5-8 Yog: Financial Stability and Balance")
            if s == {3,6,9}:
                yogs.append("3-6-9 Yog: Creativity and Fame")
    return yogs


# ---------------------- ANK INTERPRETATION ----------------------
def generate_ank_interpretation(grid, missing_numbers):
    count_map = {n: 0 for n in range(1, 10)}
    for row in grid:
        for cell in row:
            for num in cell.split():
                if num.isdigit():
                    count_map[int(num)] += 1

    # Personality & Nature
    present_personality = [n for n in [1, 3, 5, 9] if count_map[n] > 0]
    missing_personality = [n for n in [1, 3, 5, 9] if n not in present_personality]

    personality_text = [ANK_TRAITS["personality"][str(n)]["positive"] for n in present_personality]
    for n in present_personality:
        if count_map[n] > 1:
            personality_text.append(ANK_TRAITS["personality"][str(n)]["negative"])
    missing_personality_text = [ANK_TRAITS["personality"][str(n)]["negative"] for n in missing_personality]

    personality_paragraph = (
        f"Your personality is shaped by {', '.join(f'{n} ({PLANET_MAP[n]})' for n in present_personality)}, "
        + f"bringing traits like {', '.join([ANK_TRAITS['personality'][str(n)]['positive'].split(' ',1)[1] for n in present_personality])}. "
        + (" ".join(personality_text) if personality_text else "")
        + (f" However, missing {', '.join(f'{n} ({PLANET_MAP[n]})' for n in missing_personality)} "
           f"can lead to {', '.join(missing_personality_text)}." if missing_personality else "")
    )

    # Career & Finance
    present_career = [n for n in [4, 5, 8] if count_map[n] > 0]
    missing_career = [n for n in [4, 5, 8] if n not in present_career]

    career_text = [ANK_TRAITS["career"][str(n)]["positive"] for n in present_career]
    for n in present_career:
        if count_map[n] > 1:
            career_text.append(ANK_TRAITS["career"][str(n)]["negative"])
    missing_career_text = [ANK_TRAITS["career"][str(n)]["negative"] for n in missing_career]

    career_paragraph = (
        f"Career and finances are influenced by {', '.join(f'{n} ({PLANET_MAP[n]})' for n in present_career)}. "
        + " ".join(career_text)
        + (f" Missing {', '.join(f'{n} ({PLANET_MAP[n]})' for n in missing_career)} "
           f"may cause {', '.join(missing_career_text)}." if missing_career else "")
    )

    # Love & Relationships
    present_love = [n for n in [2, 6] if count_map[n] > 0]
    missing_love = [n for n in [2, 6] if n not in present_love]

    love_text = [ANK_TRAITS["love"][str(n)]["positive"] for n in present_love]
    for n in present_love:
        if count_map[n] > 1:
            love_text.append(ANK_TRAITS["love"][str(n)]["negative"])
    missing_love_text = [ANK_TRAITS["love"][str(n)]["negative"] for n in missing_love]

    love_paragraph = (
        f"In love and relationships, {', '.join(f'{n} ({PLANET_MAP[n]})' for n in present_love)} "
        + (" ".join(love_text) if love_text else "")
        + (f" Missing {', '.join(f'{n} ({PLANET_MAP[n]})' for n in missing_love)} "
           f"may bring {', '.join(missing_love_text)}." if missing_love else "")
    )

    # Health & Mindset
    present_health = [n for n in [1, 9, 7, 8] if count_map[n] > 0]
    missing_health = [n for n in [1, 9, 7, 8] if n not in present_health]

    health_text = [ANK_TRAITS["health"][str(n)]["positive"] for n in present_health]
    for n in present_health:
        if count_map[n] > 1:
            health_text.append(ANK_TRAITS["health"][str(n)]["negative"])
    missing_health_text = [ANK_TRAITS["health"][str(n)]["negative"] for n in missing_health]

    health_paragraph = (
        f"Your health and mindset are shaped by {', '.join(f'{n} ({PLANET_MAP[n]})' for n in present_health)}. "
        + " ".join(health_text)
        + (f" Missing {', '.join(f'{n} ({PLANET_MAP[n]})' for n in missing_health)} "
           f"can lead to {', '.join(missing_health_text)}." if missing_health else "")
    )

    # Remedy
    dominant_num = max(count_map, key=lambda k: count_map[k])
    remedy = ANK_TRAITS["remedies"].get(str(dominant_num), "5 Mukhi Rudraksha for balance.")

    return {
        "personality": personality_paragraph,
        "career_finance": career_paragraph,
        "love_relationships": love_paragraph,
        "health_mindset": health_paragraph,
        "remedy": remedy
    }

# ---------------------- DASHAS ----------------------
def get_mahadasha_sequence(birth_number, years=90):
    sequence, current, total = [], birth_number, 0
    while total < years:
        span = current
        if total + span > years:
            span = years - total
        sequence.append((current, span))
        total += span
        current = 1 if current == 9 else current + 1
    return sequence

def get_antardasha(dob, year, mahadasha):
    dob_parts = dob.split("-")
    date_obj = datetime.date(year, int(dob_parts[1]), int(dob_parts[2]))
    day_lord = get_day_lord_number(date_obj)
    day_sum = sum(int(x) for x in dob_parts[2])
    month_sum = sum(int(x) for x in dob_parts[1])
    year_sum = sum(int(x) for x in str(year)[-2:])
    antardasha = reduce_strict(day_sum + month_sum + year_sum + day_lord)
    return antardasha

def get_pratyantardasha(start_date, antardasha):
    duration_map = {1:8,2:16,3:24,4:32,5:41,6:49,7:57,8:65,9:73}
    days = duration_map[antardasha]
    praty_list = []
    current_number = antardasha
    current_date = start_date
    for i in range(12):  # 12 segments for 1 year approx.
        end_date = current_date + datetime.timedelta(days=days)
        praty_list.append({
            "number": current_number,
            "planet": PLANET_MAP.get(current_number, f"Unknown({current_number})"),
            "start": current_date.isoformat(),
            "end": end_date.isoformat()
        })
        current_number = 1 if current_number == 9 else current_number + 1
        current_date = end_date
    return praty_list

# ---------------------- PREDICTIONS ----------------------
def get_predictions(mahadasha, antardasha, praty_number):
    return {
        "mahadasha_prediction": f"Major life theme under {PLANET_MAP.get(mahadasha, 'Unknown')}.",
        "antardasha_prediction": f"Current sub-period ruled by {PLANET_MAP.get(antardasha, 'Unknown')}.",
        "pratyantardasha_prediction": f"Daily trends influenced by {PLANET_MAP.get(praty_number, 'Unknown')}"
    }

# ---------------------- MAIN FUNCTION ----------------------
def generate_vedic_kundali(name, dob):
    try:
        dob = dob.strip()
        birth_number = get_birth_number(dob)
        destiny_number = get_destiny_number(dob)
        combo_key = f"{birth_number}_{destiny_number}"
        combo_interpretation = BIRTH_DESTINY_TEXT.get(combo_key, {})
        ank_grid, missing_numbers = build_primary_ank_kundali(dob, birth_number, destiny_number)
        digits = {int(num) for row in ank_grid for cell in row for num in cell.split() if num}
        yogs = detect_yogs(digits)

        today = datetime.date.today()
        dob_date = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
        current_age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))

        mahadasha_seq = get_mahadasha_sequence(birth_number, years=90)
        start_year = today.year - 1
        dasha_timeline = []
        year_cursor = start_year

        for m_number, duration in mahadasha_seq:
            for _ in range(duration):
                antardasha = get_antardasha(dob, year_cursor, m_number)
                pratyantar = get_pratyantardasha(
                    datetime.date(year_cursor, dob_date.month, dob_date.day),
                    antardasha
                )
                dasha_timeline.append({
                    "year": year_cursor,
                    "mahadasha": m_number,
                    "mahadasha_planet": PLANET_MAP.get(m_number, f"Unknown({m_number})"),
                    "antardasha": antardasha,
                    "antardasha_planet": PLANET_MAP.get(antardasha, f"Unknown({antardasha})"),
                    "pratyantardasha": pratyantar
                })
                year_cursor += 1

        current_dasha = next((item for item in dasha_timeline if item["year"] == today.year), None)
        if current_dasha:
            predictions = get_predictions(
                current_dasha["mahadasha"],
                current_dasha["antardasha"],
                current_dasha["pratyantardasha"][0]["number"]
            )
        else:
            predictions = {}

        return {
            "tool": "vedic-numerology-kundali",
            "name": name,
            "dob": dob,
            "birth_number": birth_number,
            "birth_planet": PLANET_MAP[birth_number],
            "destiny_number": destiny_number,
            "destiny_planet": PLANET_MAP[destiny_number],
            "combo_interpretation": combo_interpretation,
            "ank_kundali": ank_grid,
            "missing_numbers": missing_numbers,
            "yogs": yogs,
            "current_dasha": current_dasha,
            "predictions": predictions,
            "mahadasha_chart": dasha_timeline[:10]

        }

    except Exception as e:
        import traceback
        print("ERROR in generate_vedic_kundali:", traceback.format_exc())
        return {"error": str(e)}


if __name__ == "__main__":
    print(json.dumps(generate_vedic_kundali("Ravi Kumar", "1985-03-31"), indent=2))
