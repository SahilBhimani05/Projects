import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate_emi():
    try:
        data = request.get_json()

        p, r, n = [float(data[k]) if k == "rate" else int(data[k]) for k in ["principal", "rate", "tenure"]]
        tenure_type = data["tenure_type"].lower()

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
    port = int(os.environ.get("PORT", 8081))
    app.run(host='0.0.0.0', port=port)