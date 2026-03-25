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
        url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
        
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "en-US,en;q=0.9"
        }

        session = requests.Session()
        session.get("https://www.nseindia.com", headers=headers)
        response = session.get(url, headers=headers)
        data = response.json()

        nifty_price = data["records"]["underlyingValue"]

        # Simple AI logic
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
            "confidence": 75,
            "action": action
        }

    except Exception as e:
        return {"error": str(e)}
