from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (important for frontend)
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

    nifty_price = 22450  # simulated value

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
        "confidence": 82,
        "action": action
    }
