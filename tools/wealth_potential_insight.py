from .numerology_core import extract_full_numerology

wealth_insights = {
    (1, 1): "You are born to lead and build wealth through innovation and independence.",
    (1, 2): "You have leadership instincts with the ability to form powerful financial partnerships.",
    (1, 3): "You can create wealth through self-expression, media, or solo creative ventures.",
    (1, 4): "Discipline and initiative combine — great for long-term business building and management.",
    (1, 5): "Risk-taker and adventurer — wealth comes through bold moves, freedom-based careers.",
    (1, 6): "Responsible and assertive — ideal for leadership in service-based or healing professions.",
    (1, 7): "Analytical leader — suited for consulting, tech, or intellectual property-driven business.",
    (1, 8): "You are built for wealth and power. Strong potential for high-level success and investments.",
    (1, 9): "Mission-driven leader — wealth may follow when you lead with purpose and uplift others.",
    (2, 1): "You bring wealth through collaboration with strong leaders — success comes when you trust your voice.",
    (2, 2): "Master of harmony and partnerships — wealth flows through teamwork, mediation, or community building.",
    (2, 3): "Charming and expressive — your ability to connect emotionally creates wealth in creative or social industries.",
    (2, 4): "Structured and cooperative — ideal for wealth through system-building, admin roles, or steady enterprises.",
    (2, 5): "Adaptable and persuasive — success comes through social ventures, media, or travel-related work.",
    (2, 6): "Empathic and nurturing — wealth may grow in family-centered businesses, healing arts, or education.",
    (2, 7): "Quietly powerful — your intuition and insight can lead to wealth through research, counseling, or spiritual work.",
    (2, 8): "Supportive yet ambitious — perfect for strategic roles in business, finance, or partnership-based ventures.",
    (2, 9): "Service-oriented and wise — you attract wealth through humanitarian work, coaching, or conscious leadership.",
    (3, 1): "Your charisma and confidence combine — you create wealth through personal branding and bold ideas.",
    (3, 2): "Charming and emotionally intelligent — ideal for partnerships in media, events, or community-building.",
    (3, 3): "Creative powerhouse — you're made for wealth through arts, entertainment, or digital influence.",
    (3, 4): "Structured creativity — success comes when you turn ideas into organized, profitable projects.",
    (3, 5): "Dynamic and free-spirited — you attract wealth through adventure, marketing, or trend-based careers.",
    (3, 6): "Empathic artist — ideal for wealth in lifestyle, beauty, healing, or family-focused content.",
    (3, 7): "Spiritual communicator — your insights bring wealth through writing, teaching, or niche audiences.",
    (3, 8): "Creative and strategic — you build influence and income through smart branding and business savvy.",
    (3, 9): "Uplifting and visionary — you're meant to inspire and earn through messages that heal and empower.",
    (4, 1): "You’re a steady leader — wealth comes from building lasting foundations through discipline and drive.",
    (4, 2): "You excel in structured partnerships — ideal for business development, planning, or operations.",
    (4, 3): "Organized yet expressive — success comes from structured creative projects or teaching roles.",
    (4, 4): "Master of systems — you create wealth through architecture, engineering, finance, or long-term enterprises.",
    (4, 5): "Adventurous builder — best suited for entrepreneurial ventures with structure and risk balance.",
    (4, 6): "You bring harmony to systems — wealth may grow through education, wellness, or service-based leadership.",
    (4, 7): "Analytical and reliable — ideal for wealth through research, data, consulting, or strategy.",
    (4, 8): "Business-minded and methodical — built for long-term success in finance, real estate, or enterprise.",
    (4, 9): "Disciplined with purpose — wealth flows when you build systems that serve a greater mission.",
    (5, 1): "Independent and bold — you generate wealth through personal ventures, innovation, or public influence.",
    (5, 2): "Social and adaptable — ideal for wealth through partnerships in media, PR, or travel-based industries.",
    (5, 3): "Magnetic communicator — wealth flows through entertainment, sales, or trendsetting brands.",
    (5, 4): "Grounded adventurer — success comes when you balance freedom with structure in your business model.",
    (5, 5): "Ultimate explorer — you're made for entrepreneurship, global trade, or any fast-moving industry.",
    (5, 6): "Freedom-loving nurturer — ideal for wealth through wellness, relationships, or lifestyle design.",
    (5, 7): "Curious and insightful — suited for digital ventures, research-based consulting, or spiritual travel.",
    (5, 8): "Ambitious and daring — strong potential for wealth through high-stakes business or investing.",
    (5, 9): "Charismatic and visionary — your global thinking attracts wealth through causes, media, or social change.",
    (6, 1): "Caring leader — wealth grows when you lead in healing, education, or family-centered enterprises.",
    (6, 2): "Supportive and cooperative — ideal for wealth through partnerships in counseling, coaching, or design.",
    (6, 3): "Creative nurturer — money follows your ability to express beauty, harmony, and emotional intelligence.",
    (6, 4): "Grounded and devoted — you build wealth through consistent service, planning, or home-related ventures.",
    (6, 5): "Dynamic caregiver — ideal for success in wellness, events, or flexible service industries.",
    (6, 6): "Master of healing and harmony — perfect for wealth through care industries, community leadership, or arts.",
    (6, 7): "Intuitive and wise — suited for spiritual coaching, psychology, or conscious business.",
    (6, 8): "Business-minded nurturer — success comes through ethical leadership in service or health-based industries.",
    (6, 9): "Empathic visionary — wealth flows through humanitarian missions, creative therapy, or social impact work.",
    (7, 1): "Analytical leader — your inner wisdom supports wealth in consulting, research, or intellectual property.",
    (7, 2): "Intuitive collaborator — wealth may come through spiritual alliances, therapy, or partnership in niche fields.",
    (7, 3): "Expressive thinker — you succeed through writing, teaching, or digital platforms that share deep insights.",
    (7, 4): "Systematic seeker — ideal for wealth in tech, science, or structured spiritual frameworks.",
    (7, 5): "Adventurous analyst — you thrive in online business, media, or unique travel-based careers.",
    (7, 6): "Spiritual caretaker — suited for coaching, healing professions, or soulful content creation.",
    (7, 7): "Deep intuitive — you are designed for mastery in metaphysics, data, or high-level research.",
    (7, 8): "Spiritual strategist — wealth flows when you apply your insight to business, investment, or systems.",
    (7, 9): "Philosophical guide — you attract wealth through conscious leadership, writing, or teaching with impact.",
    (8, 1): "Powerful and driven — wealth comes from leadership in business, finance, or innovation-based ventures.",
    (8, 2): "Strategic partner — success flows when you combine ambition with emotional intelligence in partnerships.",
    (8, 3): "Magnetic and expressive — ideal for wealth through public influence, media empires, or luxury branding.",
    (8, 4): "Master builder — you're wired to create long-term wealth through structure, discipline, and enterprise.",
    (8, 5): "Bold and adaptable — strong potential in dynamic industries like real estate, sales, or global trade.",
    (8, 6): "Responsible and influential — you thrive in leadership roles within service-based or wellness industries.",
    (8, 7): "Visionary strategist — ideal for wealth through tech, data, metaphysics, or advisory roles.",
    (8, 8): "Double power — you're built for empire-building, major investments, and legacy-level wealth.",
    (8, 9): "Mission-driven magnate — you attract wealth when your success uplifts others or fuels global change.",
    (9, 1): "Purposeful leader — wealth comes when you lead movements, causes, or visionary businesses.",
    (9, 2): "Compassionate collaborator — ideal for partnerships in service, healing, or community-driven ventures.",
    (9, 3): "Inspirational communicator — you attract wealth through arts, speaking, or heart-centered storytelling.",
    (9, 4): "Disciplined humanitarian — you're suited for nonprofit leadership, sustainable businesses, or education.",
    (9, 5): "Global change-maker — success follows your ability to travel, teach, and transform lives.",
    (9, 6): "Service-driven guide — you thrive in roles that heal, nurture, or advocate for collective well-being.",
    (9, 7): "Spiritual humanitarian — wealth comes through wisdom-sharing, therapy, or philosophical work.",
    (9, 8): "Mission-led executive — ideal for high-impact business that serves humanity and builds legacy wealth.",
    (9, 9): "Universal giver — you're here to inspire, teach, and heal; wealth flows when aligned with global service."
    # 🪄 Add more combos (2,1) to (9,9) here...
}

def get_wealth_insight(lp, expr):
    return wealth_insights.get(
        (lp, expr),
        "Your unique combination suggests wealth may come from an unconventional or creative path. Trust your inner rhythm and long-term vision."
    )

def run(name, dob):
    try:
        full = extract_full_numerology(name, dob)
        lp = full.get("life_path")
        expr = full.get("expression_number")

        if not lp or not expr:
            return {"error": "Life Path or Expression Number missing"}

        paragraph = get_wealth_insight(lp, expr)

        return {
            "tool": "wealth-potential-insight",
            "name": name,
            "dob": dob,
            "title": "Your Wealth Personality",
            "summary": paragraph,
            "mainNumber": f"{lp}"  # to avoid undefined%
        }

    except Exception as e:
        return {"error": str(e)}
