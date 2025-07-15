from core.data_fetcher import get_binance_ohlcv
from core.strategy_engine import apply_indicators, generate_signal
from core.order_executor import TradeExecutor
from utils.logger import log_trade
import yaml
import time

with open("configs/settings.yaml", "r") as f:
    config = yaml.safe_load(f)

symbol = config['trade']['symbol'].replace("/", "")
interval = config['trade']['interval']
quantity = config['trade']['quantity']

executor = TradeExecutor(config['api']['binance_key'], config['api']['binance_secret'])

while True:
    try:
        df = get_binance_ohlcv(symbol=symbol, interval=interval)
        df = apply_indicators(df)
        signal = generate_signal(df)

        current_price = df['close'].iloc[-1]
        if signal in ["BUY", "SELL"]:
            executor.place_order(symbol=symbol, side=signal, amount=quantity)
            log_trade(signal, current_price, quantity)
        print(f"Signal: {signal}, Price: {current_price}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(60)