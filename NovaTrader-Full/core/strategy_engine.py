import ta

def apply_indicators(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    macd = ta.trend.MACD(df['close'])
    df['macd'] = macd.macd_diff()
    df['ema_fast'] = ta.trend.EMAIndicator(df['close'], window=12).ema_indicator()
    df['ema_slow'] = ta.trend.EMAIndicator(df['close'], window=26).ema_indicator()
    return df

def generate_signal(df):
    latest = df.iloc[-1]
    if latest['rsi'] < 30 and latest['macd'] > 0 and latest['ema_fast'] > latest['ema_slow']:
        return "BUY"
    elif latest['rsi'] > 70 and latest['macd'] < 0 and latest['ema_fast'] < latest['ema_slow']:
        return "SELL"
    return "HOLD"