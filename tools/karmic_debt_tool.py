import datetime
from tools.numerology_core import numerology_values

KARMIC_DEBT_INFO = (
    "Karmic Debt Numbers reflect lessons from past lives. "
    "If present, they indicate specific challenges you are here to overcome and grow from."
)

def get_karmic_debt_numbers(name, dob_str):
    try:
        dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d")
        day, month, year = dob.day, dob.month, dob.year

        all_sources = []

        # Raw DOB components
        all_sources.extend([day, month, year])

        # Life Path raw total
        raw_total = sum(int(d) for d in dob_str if d.isdigit())
        all_sources.append(raw_total)

        # Name-based numbers
        name_data = numerology_values(name)
        all_sources.extend([
            name_data.get("expressionNumber"),
            name_data.get("personalityNumber")
        ])

        karmic_debts = []
        for num in all_sources:
            if num in [13, 14, 16, 19] and num not in karmic_debts:
                karmic_debts.append(num)

        return karmic_debts

    except Exception as e:
        return []

def run_karmic_debt_tool(name, dob):
    karmic = get_karmic_debt_numbers(name, dob)

    if karmic:
        return {
            "tool": "karmic-debt-check",
            "name": name,
            "dob": dob,
            "mainNumber": karmic[0],
            "mainPercentage": 0,
            "emoji": "🌿",
            "title": "Karmic Debt Check",
            "summary": f"You carry Karmic Debt Number(s): {', '.join(str(k) for k in karmic)}.\n{KARMIC_DEBT_INFO}",
            "debtNumbers": karmic
        }
    else:
        return {
            "tool": "karmic-debt-check",
            "name": name,
            "dob": dob,
            "mainNumber": 0,
            "mainPercentage": 0,
            "emoji": "✅",
            "title": "Karmic Debt Check",
            "summary": "You do not carry any major Karmic Debt. Your path is more fluid and self-directed.",
            "debtNumbers": []
        }
