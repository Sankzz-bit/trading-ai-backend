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
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5ENSEI"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return {"error": "API blocked"}

        data = response.json()

        nifty_price = data["quoteResponse"]["result"][0]["regularMarketPrice"]

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
