from datetime import datetime
from tools.numerology_core import reduce_strict

day_meanings = {
    1: "💡 Fresh Start – Great for launching new ideas or taking initiative.",
    2: "🤝 Teamwork – Best for collaboration and partnership tasks.",
    3: "🎨 Creativity – Ideal for content, writing, or design work.",
    4: "📊 Productivity – Focus on execution, tasks, and structure.",
    5: "📞 Meetings & Pitching – High communication day.",
    6: "🛠 Responsibility – Handle important follow-ups or family tasks.",
    7: "🧘 Quiet Focus – Plan, analyze, research or deep solo work.",
    8: "💼 Success & Money – Excellent for deals, visibility, and bold moves.",
    9: "✅ Wrap-up – Finish tasks, reflect, and prepare for next cycle."
}

rotating_tips = {
    1: ["Start something new today — even if it's small.", "Stand out — don’t follow, lead.",
        "Don’t overthink — act on your instinct.", "Push forward on that delayed idea."],
    2: ["Work with a partner or support someone else.", "Listen more than you speak today.",
        "Choose harmony over ego.", "Send that follow-up message — it’ll help."],
    3: ["Express yourself creatively — through writing or speech.", "Make your workspace colorful or inspiring.",
        "Share your ideas — people will listen.", "Crack a joke. Lighten the day."],
    4: ["Focus on organizing your workspace.", "Complete long-pending admin tasks today.",
        "Use checklists to stay efficient.", "Don’t start new projects — finish existing ones."],
    5: ["Make calls, pitch ideas, or follow up.", "Try something new — break routine.",
        "Keep things moving — don't get stuck.", "Use your voice — speak your truth."],
    6: ["Support a colleague or loved one.", "Balance your home and work tasks.",
        "Take responsibility and own the outcome.", "Be of service — it will help you too."],
    7: ["Spend time thinking deeply — avoid distractions.", "Block calendar for solo work today.",
        "Seek knowledge or analyze a situation.", "Pause. Recharge. Think long-term."],
    8: ["Ask for what you're worth.", "Close deals or pitch boldly.",
        "Tackle big goals — you have power today.", "Make decisions with confidence."],
    9: ["End what’s no longer useful.", "Forgive. Release. Reflect.",
        "Review your past efforts — harvest the wisdom.", "Tie up loose ends. Rest is near."]
}

def get_best_working_days(data):
    name = data.get("name")
    dob = data.get("dob")

    if not name or not dob:
        return {
            "title": "Best Working Days",
            "summary": "⚠️ Please provide your name and birth date.",
            "mainNumber": 0,
            "mainPercentage": 0,
            "name": name or "—",
            "dob": dob or "—"
        }

    try:
        dob_dt = datetime.strptime(dob, "%Y-%m-%d")
        birth_day = dob_dt.day
        birth_month = dob_dt.month
        today = datetime.today()

        # Personal Day Calculation
        py = reduce_strict(birth_day + birth_month + today.year)
        pm = reduce_strict(py + today.month)
        pd = reduce_strict(pm + today.day)

        # Tip rotation based on day of month
        week_slot = min((today.day - 1) // 7, 3)
        tip = rotating_tips.get(pd, ["Be aware of your energy today."])[week_slot]
        meaning = day_meanings.get(pd, "Explore yourself today.")

        summary = (
            f"📆 Today’s Personal Day Number: **{pd}**\n\n"
            f"Meaning: {meaning}\n"
            f"Tip: {tip}\n\n"
            "✨ Come back tomorrow to unlock your next day's power vibe."
        )

        return {
            "tool": "best-working-days",
            "name": name,
            "dob": dob,
            "title": "Best Working Days",
            "mainNumber": pd,
            "mainPercentage": pd * 11,
            "summary": summary
        }

    except Exception as e:
        return {
            "title": "Best Working Days",
            "summary": f"⚠️ Error calculating: {str(e)}",
            "mainNumber": 0,
            "mainPercentage": 0,
            "name": name,
            "dob": dob
        }
