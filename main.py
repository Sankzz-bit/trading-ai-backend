@app.get("/api/analysis")
def get_analysis():

    # ✅ Static + simulated real logic
    nifty_price = 22450  # simulate live value

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
        "action": action,
        "note": "Stable mode (no API dependency)"
    }
