from flask import Flask, request, jsonify
from flask_cors import CORS
from tools.numerology_core import extract_full_numerology
from tools.horoscope_api import load_horoscope
from tools.tool_engine import process_tool
import os

app = Flask(__name__)
CORS(app, origins=["https://destinydigits.com"])

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

@app.route('/api/tool-result', methods=['POST'])
def get_tool_result():
    data = request.get_json()
    result = process_tool(data)
    return jsonify(result)
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
