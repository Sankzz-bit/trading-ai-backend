@app.get("/api/analysis")
def get_analysis():
    try:
        import requests

        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5ENSEI"
        response = requests.get(url, timeout=5)

        data = response.json()

        # Safe extraction
        result = data.get("quoteResponse", {}).get("result", [])

        if not result:
            return {"error": "No data from API"}

        nifty_price = result[0].get("regularMarketPrice", 0)

        # Trading logic
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
