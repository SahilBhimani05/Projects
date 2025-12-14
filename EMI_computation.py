from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate_emi():
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ["principal", "rate", "tenure", "tenure_type"]
        missing_fields = [f for f in required_fields if f not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        # Convert and validate types
        try:
            p, r, n = [float(data[k]) if k != "tenure" else int(data[k]) for k in ["principal", "rate", "tenure"]]
            tenure_type = data["tenure_type"].lower()
        except (ValueError, TypeError):
            return jsonify({
                "error": "Invalid data types. Principal and rate must be numbers, tenure must be integer."}), 400

        # Validate values
        if p <= 0:
            return jsonify({"error": "Principal must be greater than 0"}), 400
        if n <= 0:
            return jsonify({"error": "Tenure must be greater than 0"}), 400
        if r < 0:
            return jsonify({"error": "Interest rate cannot be negative"}), 400
        if tenure_type not in ["years", "months"]:
            return jsonify({"error": "tenure_type must be 'years' or 'months'"}), 400

        months = [n * 12 if tenure_type == "years" else n][0]

        monthly_rate = r / 12 / 100

        # EMI calculation
        if monthly_rate == 0:
            EMI = p / months
        else:
            denominator = (1 + monthly_rate) ** months - 1
            if denominator == 0:
                return jsonify({"error": "Invalid input causing division by zero"}), 400
            EMI = p * monthly_rate * (1 + monthly_rate) ** months / denominator

        total_payment = EMI * months
        total_interest = total_payment - p

        return jsonify({
            "emi": round(EMI, 2),
            "total_payment": round(total_payment, 2),
            "total_interest": round(total_interest, 2)
        })

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
