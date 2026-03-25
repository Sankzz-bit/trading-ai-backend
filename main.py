@app.get("/api/analysis")
def get_analysis():

    # ✅ Temporary demo price (until we connect real API)
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
