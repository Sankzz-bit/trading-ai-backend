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
        # Using stable API (no blocking)
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        data = response.json()

        # Using BTC price as demo (works 100%)
        price = data["bpi"]["USD"]["rate_float"]

        if price > 30000:
            bias = "Bullish"
            action = "BUY"
        else:
            bias = "Bearish"
            action = "SELL"

        return {
            "market": "Demo Market",
            "price": price,
            "bias": bias,
            "confidence": 85,
            "action": action
        }

    except Exception as e:
        return {"error": str(e)}
