import MetaTrader5 as mt5
import pandas as pd
import numpy as np

def fetch_data(symbol='XAUUSD', timeframe=mt5.TIMEFRAME_M15, bars=1000):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
    return df

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def apply_strategy(df):
    df['ema_fast'] = df['close'].ewm(span=10).mean()
    df['ema_slow'] = df['close'].ewm(span=20).mean()
    df['rsi'] = compute_rsi(df['close'])

    df['signal'] = np.where(
        (df['ema_fast'] > df['ema_slow']) & (df['rsi'] > 50), 'buy',
        np.where((df['ema_fast'] < df['ema_slow']) & (df['rsi'] < 50), 'sell', '')
    )
    return df