from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Enterprise Ops Toolkit API is Live"}

# Topic 1: CRM Webhook Simulator
@app.post("/api/webhook/crm")
async def receive_crm_webhook(request: Request):
    payload = await request.json()
    return {"status": "Webhook received successfully", "logged_data": payload}

# Topic 2: Agile PRD & User Stories
@app.get("/api/agile/prd")
def get_prd():
    return {
        "feature": "Automated Account Renewal Tracker",
        "user_story": "As an Account Manager, I want automated churn alerts so I can retain enterprise clients.",
        "acceptance_criteria": ["Triggers when usage drops by 20%", "Sends high-priority push notification"]
    }

# Topic 3: Account Analytics & Churn Metrics
@app.get("/api/analytics/accounts")
def get_account_analytics():
    return {
        "total_accounts": 45,
        "avg_clv": "$120,000",
        "churn_rate_percentage": "4.2%",
        "health_status": "Stable"
    }

# Topic 4: AI Client Intelligence Pipeline Mock
@app.get("/api/ai/client-intelligence")
def ai_intelligence_scan():
    return {
        "client": "Global Logistics Corp",
        "sentiment": "Neutral to Positive",
        "ai_recommendation": "Schedule quarterly business review (QBR) to pitch enterprise expansion pack."
    }
  
