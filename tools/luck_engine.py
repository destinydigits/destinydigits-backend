import datetime
import hashlib
import json
import os
import random
from .numerology_core import extract_full_numerology

# 📂 Load tips.json once
TIPS_PATH = os.path.join(os.path.dirname(__file__), "tips.json")
with open(TIPS_PATH, "r") as f:
    TIPS_DATA = json.load(f)

def get_luck_bucket(score):
    score = int(score)
    if score >= 90:
        return "90-100"
    elif score >= 80:
        return "80-89"
    elif score >= 70:
        return "70-79"
    elif score >= 60:
        return "60-69"
    elif score >= 50:
        return "50-59"
    else:
        return "30-49"

def get_daily_tip(name, dob, score, today_str):
    bucket = get_luck_bucket(score)
    tips = TIPS_DATA.get(bucket, [])

    if not tips:
        return "Stay balanced and trust your process."

    # Stable seed based on name + dob + score + date
    seed_str = f"{name.lower()}-{dob}-{score}-{today_str}"
    seed = int(hashlib.sha256(seed_str.encode()).hexdigest(), 16)
    random.seed(seed)
    return random.choice(tips)

def calculate_luck_score(data, today=None):
    name = data.get("name")
    dob = data.get("dob")
    if not today:
        today = datetime.date.today()
    today_str = today.strftime("%Y-%m-%d")

    # 📈 Extract numerology core data
    core = extract_full_numerology(name, dob)
    personal_day = core.get("personalDay", 1)
    expression_number = core.get("expression_number", 1)

    # 🔄 Day modifier (based on weekday)
    weekday = today.weekday()  # 0 = Monday, ..., 6 = Sunday
    day_modifiers = [1.05, 1.02, 1.08, 1.06, 1.1, 0.95, 1.12]
    day_multiplier = day_modifiers[weekday]

    base_score = personal_day * expression_number
    final_score = int(min(100, max(10, base_score * day_multiplier)))

    # 🧠 Build output
    return {
        "name": name,
        "dob": dob,
        "personalDay": personal_day,
        "luckScore": final_score,
        "emoji": get_luck_emoji(final_score),
        "tip": get_daily_tip(name, dob, final_score, today_str)
    }

def get_luck_emoji(score):
    if score >= 90:
        return "🔥"
    elif score >= 75:
        return "🌟"
    elif score >= 60:
        return "✨"
    else:
        return "🪶"
