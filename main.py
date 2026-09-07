import os
from fastapi import FastAPI, Request
from google import genai

app = FastAPI()
client = genai.Client()

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
