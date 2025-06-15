from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from llm_analyzer import analyze_transaction_risk
from notify_admin import send_admin_notification
from utils import validate_transaction_json, is_authenticated

load_dotenv()

app = Flask(__name__)

# ✅ Add this route
@app.route('/')
def home():
    return "✅ Transaction Risk API is running. Use POST /webhook to send transactions."

@app.route('/webhook', methods=['POST'])
def webhook():
    if not is_authenticated(request):
        return jsonify({"error": "Unauthorized"}), 401

    transaction = request.get_json()
    if not validate_transaction_json(transaction):
        return jsonify({"error": "Invalid transaction data"}), 400

    try:
        analysis = analyze_transaction_risk(transaction)
        if analysis["risk_score"] >= 0.7:
            send_admin_notification(transaction, analysis)
        return jsonify({"status": "processed", "analysis": analysis}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
