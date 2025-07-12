from flask import Flask, request, jsonify
from flask_cors import CORS
from tools.numerology_core import extract_full_numerology
import os

app = Flask(__name__)
CORS(app)

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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
