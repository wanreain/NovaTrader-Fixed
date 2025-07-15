import os
import pandas as pd

# Ensure trade_log.csv exists
if not os.path.exists("trade_log.csv"):
    df = pd.DataFrame(columns=["time", "symbol", "action", "price", "volume", "result"])
    df.to_csv("trade_log.csv", index=False)

import streamlit as st
from strategy import fetch_data, apply_strategy
from config import SYMBOL

st.title("📊 NovaTrader Dashboard")
df = fetch_data(SYMBOL)
df = apply_strategy(df)
st.line_chart(df[['close', 'ema_fast', 'ema_slow']])
st.dataframe(df.tail(10))