from .numerology_core import extract_full_numerology

def classify_relationship(n1, n2):
    lp1, lp2 = n1["life_path"], n2["life_path"]
    heart1, heart2 = n1["heartNumber"], n2["heartNumber"]
    destiny1, destiny2 = n1["expressionNumber"], n2["expressionNumber"]

    lp_combo = (lp1, lp2)
    twin_flame_pairs = [(1, 9), (9, 1), (3, 7), (7, 3), (2, 8), (8, 2)]

    if lp_combo in twin_flame_pairs and heart1 == heart2:
        return "Twin Flame"
    elif lp1 == lp2 and destiny1 != destiny2:
        return "Karmic"
    else:
        return "Compatible"

def get_relationship_type(data):
    name1 = data.get("name", "").strip()
    dob1 = data.get("dob", "").strip()
    name2 = data.get("partnerName", "").strip()
    dob2 = data.get("partnerDOB", "").strip()

    if not name1 or not dob1 or not name2 or not dob2:
        return {"error": "Both names and DOBs are required."}

    p1 = extract_full_numerology(name1, dob1)
    p2 = extract_full_numerology(name2, dob2)
    result_type = classify_relationship(p1, p2)

    summary_map = {
        "Twin Flame": f"{name1} and {name2} share opposing Life Paths with strong heart sync, showing signs of a rare Twin Flame connection — intense, transformative, and soul-driven.",
        "Karmic": f"{name1} and {name2} share similar life direction but face personality friction, indicating a Karmic bond meant to teach deep life lessons.",
        "Compatible": f"{name1} and {name2} share a balanced, flowing energy — ideal for long-term compatibility and emotional growth."
    }

    return {
    "tool": "union-type-check",
    "name": name1,
    "dob": dob1,
    "relationshipType": result_type,
    "summary": summary_map[result_type]
}
