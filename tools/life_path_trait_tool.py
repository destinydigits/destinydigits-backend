# tools/life_path_trait_tool.py
from typing import Dict

# Use project core (tools/numerology_core.py)
from .numerology_core import extract_full_numerology

LIFE_PATH_TRAITS: Dict[int, str] = {
    1: "You never like to follow, you always want to lead and do it your way.",
    2: "Your emotional connections are too strong, you value bonds and harmony.",
    3: "You love to do things differently — creativity flows in your own style.",
    4: "Discipline is everything for you, a natural manager who builds with focus.",
    5: "Always searching for adventure, you get bored with routine easily.",
    6: "You are caring and always ready to help and protect others.",
    7: "A philosopher inside, yet social outside — wisdom and charm define you.",
    8: "If you decide to do something, you give 100% until it’s achieved.",
    9: "You are a good planner, but you don’t believe in showing off your purpose.",
    11: "Your intuition is strong, and you often inspire people without trying.",
    22: "You think big and have the power to turn vision into lasting reality.",
    33: "You heal and guide others with love — people feel safe with you."
}

def run(name: str, dob: str) -> Dict:
    try:
        data = extract_full_numerology(name, dob)
        lp = data.get("life_path")
    except Exception:
        lp = None

    if not lp or not isinstance(lp, int):
        msg = "We couldn’t calculate your Life Path number. Please check DOB (YYYY-MM-DD)."
        return {
            "tool": "life-path-trait",
            "title": "Life Path Trait",
            "name": name,
            "dob": dob,
            "lifePath": None,
            "trait": msg,
            "summary": msg,
            "mainNumber": 0,
            "mainPercentage": 100
        }

    trait = LIFE_PATH_TRAITS.get(lp, "Your energy is unique — keep exploring your path with confidence.")
    return {
        "tool": "life-path-trait",
        "title": "Life Path Trait",
        "name": name,
        "dob": dob,
        "lifePath": lp,
        "trait": trait,
        "summary": trait,
        "mainNumber": lp,
        "mainPercentage": 100
    }
