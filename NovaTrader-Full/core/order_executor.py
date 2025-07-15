import ccxt

class TradeExecutor:
    def __init__(self, api_key, api_secret):
        self.exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': api_secret
        })

    def place_order(self, symbol, side, amount):
        return self.exchange.create_market_order(symbol=symbol, side=side.lower(), amount=amount)