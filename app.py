from flask import Flask, request, jsonify
from tools.numerology_core import extract_full_numerology
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "DestinyDigits Backend Running!"})

@app.route('/api/extract-numbers')
def extract_numbers():
    name = request.args.get('name')
    dob = request.args.get('dob')  # format: DD-MM-YYYY
    if not name or not dob:
        return jsonify({"error": "Missing name or dob"}), 400
    result = extract_full_numerology(name, dob)
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
