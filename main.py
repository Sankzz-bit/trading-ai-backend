from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

# ✅ CREATE APP FIRST
app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root route
@app.get("/")
def home():
    return {"message": "Trading AI Backend Running 🚀"}

# ✅ Analysis route
@app.get("/api/analysis")
def get_analysis():
    try:
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5ENSEI"
        response = requests.get(url, timeout=5)

        data = response.json()
        result = data.get("quoteResponse", {}).get("result", [])

        if not result:
            return {"error": "No data from API"}

        nifty_price = result[0].get("regularMarketPrice", 0)

        resistance = nifty_price + 50
        support = nifty_price - 50

        if nifty_price > resistance:
            bias = "Bullish"
            action = "BUY CALL 🚀"
        elif nifty_price < support:
            bias = "Bearish"
            action = "BUY PUT 🔻"
        else:
            bias = "Sideways"
            action = "NO TRADE ⚠️"

        return {
            "market": "NIFTY 50",
            "price": nifty_price,
            "bias": bias,
            "confidence": 85,
            "action": action
        }

    except Exception as e:
        return {"error": str(e)}
