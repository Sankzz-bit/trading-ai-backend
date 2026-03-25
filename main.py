from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def home():
    return {"message": "Trading AI Backend Running 🚀"}

# Analysis route
@app.get("/api/analysis")
def get_analysis():

    # Demo price (temporary)
    nifty_price = 22450

    # Trading zones
    resistance = 22500
    support = 22300

    if nifty_price > resistance:
        bias = "Strong Bullish"
        action = "BUY CALL 🚀"
        reason = "Breakout above resistance"

    elif nifty_price < support:
        bias = "Strong Bearish"
        action = "BUY PUT 🔻"
        reason = "Breakdown below support"

    else:
        bias = "Sideways"
        action = "NO TRADE ⚠️"
        reason = f"Price between {support} and {resistance}"

    return {
        "market": "NIFTY 50",
        "price": nifty_price,
        "bias": bias,
        "confidence": 85,
        "action": action,
        "reason": reason
    }
