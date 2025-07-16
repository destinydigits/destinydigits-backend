from flask import Flask, request, jsonify
from flask_cors import CORS
from tools.numerology_core import extract_full_numerology
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
import os

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.after_request
def apply_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "https://destinydigits.com"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    return response

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
    if tool == "ideal-partner-traits":
        return jsonify(get_ideal_partner_traits(data))
    if tool in ["money-vibration-today", "money-today"]:
        return jsonify(get_money_vibration_today(data))
    if tool == "wealth-potential-insight":
        return jsonify(get_wealth_potential_insight(data))

    return jsonify({"error": "Unsupported tool"}), 400

    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
