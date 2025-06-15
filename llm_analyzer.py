import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def build_prompt(transaction):
    return f"""
You are a specialised financial risk analyst.
Evaluate the transaction below and respond in JSON with:
- risk_score (0.0-1.0)
- risk_factors (list)
- reasoning (string)
- recommended_action (allow/review/block)

Transaction Data:
{json.dumps(transaction, indent=2)}
"""

def analyze_transaction_risk(transaction):
    prompt = build_prompt(transaction)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You're a financial risk expert."},
                  {"role": "user", "content": prompt}],
        temperature=0.2
    )

    text = response['choices'][0]['message']['content']
    try:
        analysis = json.loads(text)
        required_keys = {"risk_score", "risk_factors", "reasoning", "recommended_action"}
        if not required_keys.issubset(analysis):
            raise ValueError("Missing keys in LLM response.")
        return analysis
    except Exception as e:
        raise ValueError(f"Failed to parse LLM response: {e}")
