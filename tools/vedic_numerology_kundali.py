# File: tools/vedic_numerology_kundali.py
import datetime
import json

# ---------------------- LOAD TRAITS ----------------------
with open("tools/ank_kundali_traits.json", "r", encoding="utf-8") as f:
    ANK_TRAITS = json.load(f)

with open("tools/birth_destiny_interpretations.json", "r", encoding="utf-8") as f:
    BIRTH_DESTINY_TEXT = json.load(f)

# ---------------------- PLANET MAP -----------------------
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

# ---------------------- CORE UTILS -----------------------
def reduce_strict(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def get_birth_number(dob):
    return reduce_strict(int(dob.split("-")[2]))

def get_destiny_number(dob):
    return reduce_strict(sum(int(d) for d in dob.replace("-", "")))

# ---------------------- ANK GRID -------------------------
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

# ---------------------- ANK INTERPRETATION ----------------
def generate_ank_interpretation(grid, missing_numbers):
    count_map = {n: 0 for n in range(1, 10)}
    for row in grid:
        for cell in row:
            for num in cell.split():
                if num.isdigit():
                    count_map[int(num)] += 1

    # Personality
    present_personality = [n for n in [1, 3, 5, 9] if count_map[n] > 0]
    missing_personality = [n for n in [1, 3, 5, 9] if n not in present_personality]
    personality_paragraph = (
        f"Your personality is shaped by {', '.join(f'{n} ({PLANET_MAP[n]})' for n in present_personality)}, "
        + (
            "bringing traits like "
            + ', '.join(ANK_TRAITS['personality'][str(n)]['positive'] for n in present_personality)
            + ". "
            if present_personality else ""
        )
        + (
            f"However, missing {', '.join(f'{n} ({PLANET_MAP[n]})' for n in missing_personality)} "
            f"can lead to {', '.join(ANK_TRAITS['personality'][str(n)]['negative'] for n in missing_personality)}."
            if missing_personality else ""
        )
    )

    # Career
    present_career = [n for n in [4, 5, 8] if count_map[n] > 0]
    missing_career = [n for n in [4, 5, 8] if n not in present_career]
    career_paragraph = (
        f"Career and finances are influenced by {', '.join(f'{n} ({PLANET_MAP[n]})' for n in present_career)}. "
        + ', '.join(ANK_TRAITS['career'][str(n)]['positive'] for n in present_career)
        + (
            f" Missing {', '.join(f'{n} ({PLANET_MAP[n]})' for n in missing_career)} "
            f"may cause {', '.join(ANK_TRAITS['career'][str(n)]['negative'] for n in missing_career)}."
            if missing_career else ""
        )
    )

    # Love
    present_love = [n for n in [2, 6] if count_map[n] > 0]
    missing_love = [n for n in [2, 6] if n not in present_love]
    love_paragraph = (
        f"In love and relationships, {', '.join(f'{n} ({PLANET_MAP[n]})' for n in present_love)} "
        + ', '.join(ANK_TRAITS['love'][str(n)]['positive'] for n in present_love)
        + (
            f" Missing {', '.join(f'{n} ({PLANET_MAP[n]})' for n in missing_love)} "
            f"may bring {', '.join(ANK_TRAITS['love'][str(n)]['negative'] for n in missing_love)}."
            if missing_love else ""
        )
    )

    # Health
    present_health = [n for n in [1, 9, 7, 8] if count_map[n] > 0]
    missing_health = [n for n in [1, 9, 7, 8] if n not in present_health]
    health_paragraph = (
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
        "personality": personality_paragraph.strip(),
        "career_finance": career_paragraph.strip(),
        "love_relationships": love_paragraph.strip(),
        "health_mindset": health_paragraph.strip(),
        "remedy": remedy
    }

# ---------------------- MAHADASHA TIMELINE -----------------
def generate_mahadasha_timeline(dob, future_years=20):
    dob_date = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
    today = datetime.date.today()
    end_limit = today.replace(year=today.year + future_years)

    birth_number = get_birth_number(dob)
    current_number = birth_number
    start_date = dob_date

    mahadashas = []

    while start_date <= end_limit:
        duration = current_number
        end_date = start_date.replace(year=start_date.year + duration) - datetime.timedelta(days=1)

        mahadashas.append({
            "number": current_number,
            "planet": PLANET_MAP[current_number],
            "start_date": start_date.strftime("%d-%m-%Y"),
            "end_date": end_date.strftime("%d-%m-%Y")
        })

        start_date = end_date + datetime.timedelta(days=1)
        current_number = 1 if current_number == 9 else current_number + 1

    return mahadashas

# ---------------------- PREDICTIONS ------------------------
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

        # Mahadasha Timeline
        mahadasha_seq = generate_mahadasha_timeline(dob, total_years=50)

        # Find current Mahadasha
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
