from .numerology_core import extract_full_numerology
import datetime

# ✨ Sample logic: Use current year and essence/pinnacle for that year
def run(name, dob, businessName=None):
    try:
        full = extract_full_numerology(name, dob)
        essence_map = full.get("essenceMap", {})
        pinnacle_map = full.get("pinnacleMap", {})

        if not essence_map or not pinnacle_map:
            return {"error": "Essence or Pinnacle data missing"}

        current_year = datetime.datetime.now().year
        years_to_check = list(range(current_year, current_year + 5))

        suggestions = []

        for year in years_to_check:
            essence = essence_map.get(str(year))
            pinnacle = pinnacle_map.get(str(year))

            if not essence or not pinnacle:
                continue

            rating = 0
            if essence in [1, 5, 8]:  # Dynamic, Growth, Power
                rating += 1
            if pinnacle in [1, 3, 8]:  # Action, Creativity, Ambition
                rating += 1

            if rating == 2:
                comment = "🌟 Excellent year to launch or expand your business."
            elif rating == 1:
                comment = "⚖️ Decent year — favorable energy, but act with clarity."
            else:
                comment = "⛔ May not be ideal — wait or plan, not act."

            suggestions.append(f"{year}: Essence {essence}, Pinnacle {pinnacle} → {comment}")

        summary = (
            f"🧮 Analysis based on your personal Essence and Pinnacle cycles:\n\n" +
            "\n".join(suggestions) +
            "\n\n✅ Ideal years are those with Essence and Pinnacle energies that support action, growth, and leadership."
        )

        return return {
            "tool": "venture-timing",
            "name": name,
            "dob": dob,
            "title": "Your Wealth Personality",  # Frontend is using this title
            "summary": f"💼 Wealth Combo: Essence + Pinnacle\n\n{summary}",
            "mainNumber": 5,  # Dummy to avoid crash
            "score": "",      # Prevents 'Compatibility Score' from showing
        }

    except Exception as e:
        return {"error": str(e)}
