
from .numerology_core import extract_full_numerology
import random

messages = {
    1: [
        "Today is a powerful day to take charge of your finances. Trust your instincts and don't hesitate to initiate action.",
        "Money matters may demand leadership today. If you’ve been delaying an investment or task, now is the time to move."
    ],
    2: [
        "Collaboration can open new financial doors. Seek guidance or work with a trusted partner.",
        "Not a day for solo decisions. Let others support your financial planning today — harmony will bring gain."
    ],
    3: [
        "Your creativity may lead to unexpected income. Express your ideas — people are listening.",
        "Avoid emotional spending. While the day feels light, keeping control will help you save."
    ],
    4: [
        "Today demands discipline. Focus on budgeting and avoid impulsive purchases.",
        "A grounded approach will protect your finances. Stick to the plan and be mindful of small expenses."
    ],
    5: [
        "You may experience financial ups and downs today. Stay flexible and avoid risky moves.",
        "A surprise opportunity might appear — be alert, but don’t rush decisions."
    ],
    6: [
        "Money may be spent on home or family needs today. Balance generosity with financial sense.",
        "A good day to settle dues or take care of loved ones. Emotional spending is likely — plan accordingly."
    ],
    7: [
        "Reflection is better than action today. Avoid major financial commitments or impulsive choices.",
        "Trust your inner voice. If something feels off financially, pause and reevaluate."
    ],
    8: [
        "Strong energy for success in career and money. Use this day to assert yourself professionally.",
        "Power and money are aligned today. A decision you make now could lead to future gain."
    ],
    9: [
        "Today is ideal for clearing old debts or letting go of past financial baggage.",
        "Acts of generosity can open up new money flow. Don’t cling to what needs to be released."
    ],
}

def run(name, dob):
    try:
        full = extract_full_numerology(name, dob)
        personal_day = full["personalDay"]
        name_number = full["expressionNumber"]

        paragraph = random.choice(messages.get(personal_day, ["No financial insight available for today."]))

        return {
            "tool": "money-vibration-today",
            "name": name,
            "dob": dob,
            "personalDay": personal_day,
            "nameNumber": name_number,
            "paragraph": paragraph
        }
    except Exception as e:
        return {"error": str(e)}
