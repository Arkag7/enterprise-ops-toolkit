import os
from fastapi import FastAPI
from google import genai

app = FastAPI()
client = genai.Client()

@app.get("/")
def read_root():
    return {"status": "Enterprise Ops Toolkit API is Live"}

@app.get("/api/agile/prd")
def agile_prd():
    return {
        "feature": "Automated Account Renewal Tracker",
        "user_story": "As an Account Manager, I want automated churn alerts so I can retain enterprise clients.",
        "acceptance_criteria": [
            "Triggers when usage drops by 20%",
            "Sends high-priority push notification"
        ]
    }

@app.get("/api/analytics/accounts")
def account_analytics():
    return {
        "total_accounts": 45,
        "avg_clv": "$120,000",
        "churn_rate_percentage": "4.2%",
        "health_status": "Stable"
    }

@app.get("/api/ai/client-intelligence")
def live_ai_intelligence():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Analyze an enterprise client account with a 20% drop in usage and generate a concise QBR recommendation for executive retention."
    )
    return {
        "client": "Global Logistics Corp", 
        "ai_analysis": response.text
    }
