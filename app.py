from flask import Flask, request, jsonify
from flask_cors import CORS
from tools.numerology_core import extract_full_numerology, generate_full_report
from tools.horoscope_api import load_horoscope
from tools.romantic_vibes import get_romantic_vibes
from tools.karmic_lesson_marriage import get_karmic_lesson_marriage
from tools.attraction_insight import get_attraction_insight
from tools.love_compatibility import get_love_compatibility 
from tools.heart_desire import get_heart_desire_match
from tools.soulmates_check import get_soulmate_score
from tools.marriage_compatibility import get_marriage_compatibility
from tools.best_year_to_marry import get_best_year_to_marry
from tools.ideal_partner_traits import get_ideal_partner_traits
from tools.money_vibration_today import run as money_vibration_today
from tools.wealth_potential_insight import run as wealth_potential_insight
from tools.business_name_numerology import run as business_name_numerology
from tools.venture_timing import run as venture_timing
from tools.business_partner_check import get_business_partner_compatibility
from tools.career_guidance import get_career_guidance
from tools.hidden_talents import get_hidden_talents
from tools.resume_booster import get_resume_booster
from tools.best_working_days import get_best_working_days
from tools.personal_core_numbers import get_personal_core_number
from tools.vedic_kundali import get_vedic_kundali
from tools.luck_engine import calculate_luck_score
from tools.flames import flames_result
from tools.numerology_core import extract_full_numerology
from tools.name_correction_engine import run_name_correction_tool
from string import ascii_uppercase
from tools.mobile_number_checker import run_mobile_number_checker
from flask import send_file
import os

app = Flask(__name__)
CORS(app, supports_credentials=True)

# ------------------- CORS HEADERS -------------------
@app.after_request
def apply_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "https://destinydigits.com"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

# OPTIONS route to handle CORS preflight
@app.route('/api/tool-result', methods=['OPTIONS'])
def tool_result_options():
    response = jsonify({'status': 'OK'})
    response.headers["Access-Control-Allow-Origin"] = "https://destinydigits.com"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

# ------------------- ROUTES -------------------
@app.route('/')
def home():
    return jsonify({"message": "DestinyDigits Backend Running!"})

@app.route('/api/extract-numbers')
def extract_numbers():
    name = request.args.get('name')
    dob = request.args.get('dob')
    try:
        if not name or not dob:
            return jsonify({"error": "Missing name or dob"}), 400
        result = extract_full_numerology(name, dob)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

@app.route("/api/dasha-effects")
def get_dasha_effects():
    return send_file("tools/dasha_effects.json", mimetype="application/json")

@app.route('/api/horoscope-message')
def get_horoscope_message():
    number = request.args.get("number")
    type_ = request.args.get("type")

    if not number or not type_:
        return jsonify({"error": "Missing number or type"}), 400

    result = load_horoscope(str(number), type_)
    if isinstance(result, tuple):  # error
        return jsonify(result[0]), result[1]

    return jsonify(result)

@app.route('/api/tool-result', methods=['POST'])
    def get_tool_result():
        data = request.get_json()
        tool = data.get("tool")
        print("Requested tool:", tool)

def get_money_vibration_today(data):
    name = data.get("name")
    dob = data.get("dob")
    return money_vibration_today(name, dob)

def get_wealth_potential_insight(data):
    name = data.get("name")
    dob = data.get("dob")
    return wealth_potential_insight(name, dob)

@app.route('/api/tool-result', methods=['POST'])
def get_tool_result():
    data = request.get_json()
    tool = data.get("tool")
    
    if tool == "life-prediction":
        name = data.get("name")
        dob = data.get("dob")
        if not name or not dob:
            return jsonify({"error": "Missing name or dob"}), 400

        numerology_data = extract_full_numerology(name, dob)
        full_report = generate_full_report(name, dob)

        result = {
            "tool": "life-prediction",
            "name": name,
            "dob": dob,
            "title": "🔮 Free Life Prediction Report",
            "summary": (full_report[:250] + "...") if len(full_report) > 250 else full_report,
            "mainNumber": numerology_data.get("life_path", 0),
            "fullReport": full_report
        }
        return jsonify(result)
        
    if tool == "luck-meter":
        return jsonify(calculate_luck_score(data.get("name"), data.get("dob")))
    if tool == "flames-check":
        return jsonify(flames_result(data.get("name1"), data.get("name2")))
    if tool == "romantic-vibes":
        return jsonify(get_romantic_vibes(data))
    if tool == "karmic-lessons-marriage":
        return jsonify(get_karmic_lesson_marriage(data))
    if tool == "attraction-insight":
        return jsonify(get_attraction_insight(data))
    if tool == "love-compatibility":
        return jsonify(get_love_compatibility(data))
    if tool == "heart-desire":
        return jsonify(get_heart_desire_match(data))
    if tool == "soulmates-check":
        return jsonify(get_soulmate_score(data))
    if tool == "marriage-compatibility":
        return jsonify(get_marriage_compatibility(data))
    if tool in ["best-year-to-marry", "marriage-year"]:
        return jsonify(get_best_year_to_marry(data))
    if tool == "name-correction":
        name = data.get("name")
        dob = data.get("dob")
        return jsonify(run_name_correction_tool(name, dob))
    if tool == "ideal-partner-traits":
        return jsonify(get_ideal_partner_traits(data))
    if tool in ["money-vibration-today", "money-today"]:
        return jsonify(get_money_vibration_today(data))
    if tool in ["wealth-potential-insight", "wealth-potential"]:
        return jsonify(get_wealth_potential_insight(data))
    if tool == "business-name-check":
        return jsonify(business_name_numerology(
            data.get("name"),
            data.get("dob"),
            data.get("businessName")
        ))
    if tool in ["venture-timing", "best-time-to-start-venture"]:
        return jsonify(venture_timing(data.get("name"), data.get("dob")))
    if tool == "business-partner-check":
        return jsonify(get_business_partner_compatibility(data))
    if tool == "career-guidance":
        return jsonify(get_career_guidance(data))
    if tool == "hidden-talents":
        return jsonify(get_hidden_talents(data))
    if tool == "resume-booster":
        return jsonify(get_resume_booster(data))
    if tool == "best-working-days":
        return jsonify(get_best_working_days(data))
    if tool in [
        "life-path", "expression-number", "soul-urge",
        "personality-number", "birthday-number", "maturity-number",
        "karmic-lessons", "hidden-passion"
    ]:
        return jsonify(get_personal_core_number(data, tool))
    if tool == "vedic-numerology":
        return jsonify(get_vedic_kundali(data))
    
    return jsonify({"error": "Unsupported tool"}), 400

    if tool == "mobile-number-checker":
        return jsonify(run_mobile_number_checker(
            data.get("mobileNumber"),
            name=data.get("name"),
            dob=data.get("dob")
        ))



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
