def send_admin_notification(transaction, analysis):
    alert = {
        "alert_type": "high_risk_transaction",
        "transaction_id": transaction["transaction_id"],
        "risk_score": analysis["risk_score"],
        "risk_factors": analysis["risk_factors"],
        "transaction_details": transaction,
        "llm_analysis": analysis["reasoning"]
    }
    # In real system, send this to an admin channel (email, Slack, etc.)
    print("🚨 Admin Alert:\n", json.dumps(alert, indent=2))
