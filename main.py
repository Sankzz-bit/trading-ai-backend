# Store previous price (simple memory)
previous_price = 0

@app.get("/api/analysis")
def get_analysis():
    global previous_price

    try:
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5ENSEI"
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            return {"error": "API not responding"}

        data = response.json()
        result = data.get("quoteResponse", {}).get("result", [])

        if not result:
            return {"error": "No data"}

        nifty_price = result[0].get("regularMarketPrice", 0)

        # 🔥 TREND LOGIC
        if previous_price == 0:
            trend = "Neutral"
        elif nifty_price > previous_price:
            trend = "Uptrend 📈"
        elif nifty_price < previous_price:
            trend = "Downtrend 📉"
        else:
            trend = "Sideways"

        previous_price = nifty_price

        # 🔥 SMART DECISION
        if trend == "Uptrend 📈":
            action = "BUY CALL 🚀"
        elif trend == "Downtrend 📉":
            action = "BUY PUT 🔻"
        else:
            action = "WAIT ⚠️"

        return {
            "market": "NIFTY 50",
            "price": nifty_price,
            "trend": trend,
            "confidence": 80,
            "action": action
        }

    except Exception as e:
        return {"error": str(e)}
