from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/analysis")
def get_analysis():
    return {
        "market": "NIFTY 50",
        "bias": "Bullish",
        "confidence": 70,
        "resistance": "22450",
        "support": "22300",
        "reasoning": [
            "Demo data",
            "Backend working",
            "Next step: real data"
        ],
        "optionsInsight": "PCR ~1",
        "action": "NO TRADE",
        "risk": "Medium",
        "invalidation": "Below support"
    } 
