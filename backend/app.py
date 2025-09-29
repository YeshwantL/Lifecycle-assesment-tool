# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from calculator import perform_calculations # Ensure this function name matches calculator.py

app = Flask(__name__)
CORS(app)

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    if not data or 'tons' not in data or 'recycled_percent' not in data:
        return jsonify({"error": "Missing data in the input"}), 400
    
    try:
        tons = float(data['tons'])
        recycled_percent = float(data['recycled_percent'])
    except ValueError:
        return jsonify({"error": "Invalid data types please verify again!!"}), 400
    
    results = perform_calculations(tons, recycled_percent)
    
    if "error" in results:
        return jsonify(results), 500
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)