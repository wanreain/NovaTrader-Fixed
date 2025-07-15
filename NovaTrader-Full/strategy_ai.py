import pandas as pd
import numpy as np
import joblib
from strategy import compute_rsi

model = joblib.load("model_xgb.pkl")

def predict_trade_signal(df):
    df["ema_fast"] = df["close"].ewm(span=10).mean()
    df["ema_slow"] = df["close"].ewm(span=20).mean()
    df["ema_diff"] = df["ema_fast"] - df["ema_slow"]
    df["rsi"] = compute_rsi(df["close"])
    df["slope"] = df["close"].diff().rolling(window=5).mean()

    latest = df[["ema_diff", "rsi", "slope"]].iloc[-1:].dropna()
    if latest.empty:
        return "hold"
    prediction = model.predict(latest)[0]
    return "buy" if prediction == 1 else "sell"