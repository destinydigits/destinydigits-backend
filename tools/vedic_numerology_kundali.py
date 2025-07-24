import datetime
import json
from dateutil.relativedelta import relativedelta

# ---------------------- TRAITS ----------------------
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

PRATYANTAR_DAYS = {1: 8, 2: 16, 3: 24, 4: 32, 5: 41, 6: 49, 7: 57, 8: 65, 9: 73}

DAY_LORD_MAP = {
    6: 1,  # Sunday → Sun
    0: 2,  # Monday → Moon
    1: 9,  # Tuesday → Mars
    2: 5,  # Wednesday → Mercury
    3: 3,  # Thursday → Jupiter
    4: 6,  # Friday → Venus
    5: 8   # Saturday → Saturn
}

# ---------------------- UTIL FUNCTIONS ----------------------
def reduce_strict(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def get_birth_number(dob):
    return reduce_strict(int(dob.split("-")[2]))

def get_destiny_number(dob):
    parts = dob.split("-")  # [YYYY, MM, DD]
    digits = [int(d) for d in parts[2] + parts[1] + parts[0]]  # DDMMYYYY ke sabhi digits
    total = sum(digits)
    return reduce_strict(total)
    
def get_day_lord_number(date_obj):
    """Return day lord number based on weekday."""
    return DAY_LORD_MAP[date_obj.weekday()]

# ---------------------- ANK GRID ----------------------
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

# ---------------------- ANK INTERPRETATION ----------------------
def generate_ank_interpretation(grid, missing_numbers):
    count_map = {n: 0 for n in range(1, 10)}
    for row in grid:
        for cell in row:
            for num in cell.split():
                if num.isdigit():
                    count_map[int(num)] += 1

    present_personality = [n for n in [1, 3, 5, 9] if count_map[n] > 0]
    missing_personality = [n for n in [1, 3, 5, 9] if n not in present_personality]
    personality_text = (
        f"Your personality is shaped by {', '.join(f'{n} ({PLANET_MAP[n]})' for n in present_personality)}, "
        + (
            "bringing traits like " + ', '.join(
                ANK_TRAITS['personality'][str(n)]['positive'] for n in present_personality
            ) + ". " if present_personality else ""
        )
        + (
            f"However, missing {', '.join(f'{n} ({PLANET_MAP[n]})' for n in missing_personality)} "
            f"can lead to {', '.join(
                ANK_TRAITS['personality'][str(n)]['negative'] for n in missing_personality
            )}." if missing_personality else ""
        )
    )

    present_career = [n for n in [4, 5, 8] if count_map[n] > 0]
    missing_career = [n for n in [4, 5, 8] if n not in present_career]
    career_text = (
        f"Career and finances are influenced by {', '.join(f'{n} ({PLANET_MAP[n]})' for n in present_career)}. "
        + ', '.join(ANK_TRAITS['career'][str(n)]['positive'] for n in present_career)
        + (
            f" Missing {', '.join(f'{n} ({PLANET_MAP[n]})' for n in missing_career)} "
            f"may cause {', '.join(ANK_TRAITS['career'][str(n)]['negative'] for n in missing_career)}."
            if missing_career else ""
        )
    )

    present_love = [n for n in [2, 6] if count_map[n] > 0]
    missing_love = [n for n in [2, 6] if n not in present_love]
    love_text = (
        f"In love and relationships, {', '.join(f'{n} ({PLANET_MAP[n]})' for n in present_love)} "
        + ', '.join(ANK_TRAITS['love'][str(n)]['positive'] for n in present_love)
        + (
            f" Missing {', '.join(f'{n} ({PLANET_MAP[n]})' for n in missing_love)} "
            f"may bring {', '.join(ANK_TRAITS['love'][str(n)]['negative'] for n in missing_love)}."
            if missing_love else ""
        )
    )

    present_health = [n for n in [1, 9, 7, 8] if count_map[n] > 0]
    missing_health = [n for n in [1, 9, 7, 8] if n not in present_health]
    health_text = (
        f"Your health and mindset are shaped by {', '.join(f'{n} ({PLANET_MAP[n]})' for n in present_health)}. "
        + ', '.join(ANK_TRAITS['health'][str(n)]['positive'] for n in present_health)
        + (
            f" Missing {', '.join(f'{n} ({PLANET_MAP[n]})' for n in missing_health)} "
            f"can lead to {', '.join(ANK_TRAITS['health'][str(n)]['negative'] for n in missing_health)}."
            if missing_health else ""
        )
    )

    dominant_num = max(count_map, key=lambda k: count_map[k])
    remedy = ANK_TRAITS['remedies'].get(str(dominant_num), "5 Mukhi Rudraksha for balance.")

    return {
        "personality": personality_text.strip(),
        "career_finance": career_text.strip(),
        "love_relationships": love_text.strip(),
        "health_mindset": health_text.strip(),
        "remedy": remedy
    }

# ---------------------- PRATYANTARDASHA ----------------------
def generate_pratyantardasha(antardasha_num, start_date):
    pratyantar_list = []
    current_num = antardasha_num
    current_start = start_date

    for _ in range(9):
        days = PRATYANTAR_DAYS[current_num]
        end_date = current_start + datetime.timedelta(days=days - 1)
        pratyantar_list.append({
            "number": current_num,
            "planet": PLANET_MAP[current_num],
            "start_date": current_start.strftime("%d-%m-%Y"),
            "end_date": end_date.strftime("%d-%m-%Y")
        })
        current_num = 1 if current_num == 9 else current_num + 1
        current_start = end_date + datetime.timedelta(days=1)

    return pratyantar_list

# ---------------------- ANTARDASHA ----------------------
def generate_antardasha_for_mahadasha(dob, mahadasha_start, mahadasha_years):
    antardashas = []
    day = int(dob.split("-")[2])
    month = int(dob.split("-")[1])
    current_start = mahadasha_start

    for _ in range(mahadasha_years):
        birthday_this_year = datetime.date(current_start.year, month, day)
        day_lord_no = get_day_lord_number(birthday_this_year)

        calc_sum = day + month + (current_start.year % 100) + day_lord_no
        antardasha_num = reduce_strict(calc_sum)

        next_year = current_start + relativedelta(years=1) - datetime.timedelta(days=1)
        pratyantar_list = generate_pratyantardasha(antardasha_num, current_start)

        antardashas.append({
            "year": current_start.year,
            "number": antardasha_num,
            "planet": PLANET_MAP[antardasha_num],
            "start_date": current_start.strftime("%d-%m-%Y"),
            "end_date": next_year.strftime("%d-%m-%Y"),
            "pratyantardasha": pratyantar_list
        })
        current_start = next_year + datetime.timedelta(days=1)

    return antardashas

# ---------------------- MAHADASHA TIMELINE ----------------------
def generate_mahadasha_timeline(dob, future_years=20):
    dob_date = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
    today = datetime.date.today()
    end_limit = today + relativedelta(years=future_years)

    birth_number = get_birth_number(dob)
    current_number = birth_number
    start_date = dob_date
    mahadashas = []

    while start_date <= end_limit:
        duration = current_number
        end_date = start_date + relativedelta(years=duration) - datetime.timedelta(days=1)

        antardashas = generate_antardasha_for_mahadasha(dob, start_date, duration)

        mahadashas.append({
            "number": current_number,
            "planet": PLANET_MAP[current_number],
            "start_date": start_date.strftime("%d-%m-%Y"),
            "end_date": end_date.strftime("%d-%m-%Y"),
            "antardasha": antardashas
        })

        start_date = end_date + datetime.timedelta(days=1)
        current_number = 1 if current_number == 9 else current_number + 1

    return mahadashas

# ---------------------- PREDICTIONS ----------------------
def get_predictions(current_dasha):
    if not current_dasha:
        return {}
    return {
        "mahadasha_prediction": f"Major life theme under {current_dasha['planet']}."
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
        ank_interpretation = generate_ank_interpretation(ank_grid, missing_numbers)

        mahadasha_seq = generate_mahadasha_timeline(dob, future_years=20)
        today = datetime.date.today()
        current_dasha = next(
            (m for m in mahadasha_seq
             if datetime.datetime.strptime(m["start_date"], "%d-%m-%Y").date() <= today <= datetime.datetime.strptime(m["end_date"], "%d-%m-%Y").date()),
            None
        )

        predictions = get_predictions(current_dasha)

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
            "ank_interpretation": ank_interpretation,
            "current_dasha": current_dasha,
            "predictions": predictions,
            "mahadasha_chart": mahadasha_seq
        }

    except Exception as e:
        import traceback
        print("ERROR in generate_vedic_kundali:", traceback.format_exc())
        return {"error": str(e)}

if __name__ == "__main__":
    print(json.dumps(generate_vedic_kundali("Ravi Kumar", "1985-03-31"), indent=2))
