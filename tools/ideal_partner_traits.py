from .numerology_core import extract_full_numerology  

heart_traits = {
    1: "craves a partner who respects their independence and offers mutual admiration.",
    2: "seeks emotional bonding, harmony, and someone who truly listens.",
    3: "wants someone playful, creative, and emotionally expressive.",
    4: "needs someone dependable, honest, and stable.",
    5: "desires excitement and freedom in love; needs a flexible and adventurous partner.",
    6: "longs for nurturing, loyalty, and a strong family-oriented connection.",
    7: "seeks depth, silence, and spiritual compatibility.",
    8: "is drawn to confident, ambitious partners who offer security.",
    9: "wants someone compassionate, idealistic, and emotionally generous."
}

destiny_traits = {
    1: "Your ideal partner is strong-willed and supportive of your goals.",
    2: "You vibe best with someone diplomatic, loving, and emotionally intelligent.",
    3: "A fun-loving, communicative, and optimistic partner suits you well.",
    4: "Someone who values structure, trust, and simplicity would match your mindset.",
    5: "You align with someone spontaneous, adventurous, and mentally agile.",
    6: "You need someone with a warm heart and a sense of responsibility.",
    7: "You match best with someone introspective, peaceful, and intellectually curious.",
    8: "A powerful, practical, and success-driven partner completes your world.",
    9: "Someone kind, idealistic, and devoted to a higher cause is your soulmate."
}

def get_ideal_partner_traits(data):
    name = data.get("name", "").strip()
    dob = data.get("dob", "").strip()
    if not name or not dob:
        return {"error": "Name and DOB required."}

    numbers = extract_full_numerology(name, dob)
    heart = numbers.get("heartNumber")
    destiny = numbers.get("expressionNumber")
    life_path = numbers.get("lifePath")

    part1 = heart_traits.get(heart, "")
    part2 = destiny_traits.get(destiny, "")
    summary = f"{name}, you {part1} {part2}"

    return {
        "tool": "ideal-partner-traits",
        "name": name,
        "dob": dob,
        "heartNumber": heart,
        "destinyNumber": destiny,
        "lifePath": life_path,
        "summary": summary
    }
