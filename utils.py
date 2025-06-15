import os

def is_authenticated(request):
    auth_header = request.headers.get("Authorization")
    token = os.getenv("AUTH_TOKEN")
    return auth_header == f"Bearer {token}"

def validate_transaction_json(transaction):
    required_fields = ["transaction_id", "timestamp", "amount", "currency", "customer", "payment_method", "merchant"]
    if not transaction:
        return False
    for field in required_fields:
        if field not in transaction:
            return False
    return True
