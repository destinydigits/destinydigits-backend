import random
from datetime import datetime

def reduce_strict(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def sum_of_digits(date_str):
    return sum(int(d) for d in date_str if d.isdigit())

def get_romantic_vibes(data):
    name = data.get("name", "")
    dob = data.get("dob")
    partner_dob = data.get("partnerDOB")

    if not dob:
        return {"error": "DOB is required"}, 400

    today = datetime.today().strftime("%d-%m-%Y")
    user_total = sum_of_digits(dob)
    today_total = sum_of_digits(today)
    daily_vibe = reduce_strict(user_total + today_total)

    # 🎯 Randomized vibe messages
    vibe_messages = {
        1: ["🔥 Be bold today. Express your desires openly.",
            "🔥 Chase love, don’t wait for it."],
        2: ["💞 Deep connections form today. Time to nurture love.",
            "💞 Listen, not fix. That’s love today."],
        3: ["🎉 Flirt, laugh, and be spontaneous today.",
            "🎉 Share playful energy – joy attracts love."],
        4: ["🧘‍♀️ Stability and comfort rule. Plan your future.",
            "🧘‍♀️ Be the calm in your partner's storm."],
        5: ["🚀 Expect romantic surprises. Text them now!",
            "🚀 Today is made for spontaneity. Act fast!"],
        6: ["💝 Sweet, nurturing love surrounds you.",
            "💝 Home dates or cozy moments work best today."],
        7: ["🧿 Go deep or go solo. Trust your intuition.",
            "🧿 Romance has spiritual depth today. Listen within."],
        8: ["💼 Passion meets purpose – strong pair vibes.",
            "💼 Power couple moments are born today."],
        9: ["🕊 Healing day. Let go, make room for love.",
            "🕊 Give with an open heart – karma returns."]
    }

    # 🎨 Randomized colors per number
    colors = {
        1: ["Red", "Crimson"],
        2: ["Pink", "Blush"],
        3: ["Yellow", "Lemon"],
        4: ["Cream", "Beige"],
        5: ["Orange", "Coral"],
        6: ["Peach", "Rose"],
        7: ["Indigo", "Violet"],
        8: ["Wine", "Burgundy"],
        9: ["White", "Silver"]
    }

    # 💡 Randomized love tips per number
    love_tips = {
        1: ["Say what you feel – confidently.",
            "Initiate a bold move today."],
        2: ["Be emotionally present today.",
            "Listen with full heart – no fixes."],
        3: ["Send a funny reel or voice note.",
            "Flirt with charm and playfulness."],
        4: ["Cook together or discuss dreams.",
            "Write down shared goals today."],
        5: ["Plan a surprise call or DM.",
            "Go somewhere new – even virtually!"],
        6: ["Share how much they mean to you.",
            "Tell them one thing you love about them."],
        7: ["Reflect on your inner love language.",
            "Journal a message and maybe send it."],
        8: ["Talk about long-term vision.",
            "Support their ambitions today."],
        9: ["Do something selfless in love.",
            "Forgive and attract peace."]
    }

    summary = random.choice(vibe_messages.get(daily_vibe, ["Feel the love in the air."]))
    color = random.choice(colors.get(daily_vibe, ["Red"]))
    tip = random.choice(love_tips.get(daily_vibe, ["Say something nice."]))

    response = {
        "tool": "romantic-vibes",
        "name": name,
        "dob": dob,
        "mainNumber": daily_vibe,
        "title": f"Romantic Vibe Today is {daily_vibe}",
        "summary": summary,
        "colorOfTheDay": color,
        "loveTip": tip,
        "dateCalculated": today
    }

    # 🧮 Optional Partner Compatibility
    if partner_dob:
        partner_total = sum_of_digits(partner_dob)
        partner_vibe = reduce_strict(partner_total + today_total)
        sync_score = (daily_vibe + partner_vibe) % 9 or 9

        sync_map = {
            (1, 2, 3): "💖 Perfect day for bonding",
            (4, 5, 6): "💬 Communicate clearly",
            (7, 8, 9): "🌙 Give space and recharge"
        }

        for group, msg in sync_map.items():
            if sync_score in group:
                response["partnerVibe"] = partner_vibe
                response["syncScore"] = sync_score
                response["syncMessage"] = msg
                break

    return response
