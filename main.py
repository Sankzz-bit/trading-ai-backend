@app.get("/api/analysis")
def get_analysis():

    try:
        # Real NIFTY data
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5ENSEI"
        response = requests.get(url)
        data = response.json()

        nifty_price = data["quoteResponse"]["result"][0]["regularMarketPrice"]

        # Trading zones
        resistance = nifty_price + 50
        support = nifty_price - 50

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
            reason = "Market in range"

        return {
            "market": "NIFTY 50",
            "price": nifty_price,
            "bias": bias,
            "confidence": 88,
            "action": action,
            "reason": reason
        }

    except Exception as e:
        return {"error": str(e)}
