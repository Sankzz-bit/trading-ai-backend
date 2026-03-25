from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/analysis")
def get_analysis():
    try:
        # Using free public API (no blocking)
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5ENSEI"
        response = requests.get(url)
        data = response.json()

        nifty_price = data["quoteResponse"]["result"][0]["regularMarketPrice"]

        # AI logic
        if nifty_price > 22000:
            bias = "Bullish"
            action = "BUY CALL"
        else:
            bias = "Bearish"
            action = "BUY PUT"

        return {
            "market": "NIFTY 50",
            "price": nifty_price,
            "bias": bias,
            "confidence": 80,
            "action": action
        }

    except Exception as e:
        return {"error": str(e)}
