import streamlit as st
import pandas as pd
from io import StringIO
from pathlib import Path

st.set_page_config(page_title="NovaTrader Dashboard", layout="wide")
st.title("📊 NovaTrader AI - Live Trade Dashboard")

log_file = Path("trade_log.csv")

if not log_file.exists():
    st.warning("📁 `trade_log.csv` not found. Showing sample data instead.")
    csv_data = """2025-07-15 09:00:00,BUY,65432.10,0.001
2025-07-15 09:05:00,SELL,65500.25,0.001
2025-07-15 10:00:00,BUY,65320.00,0.001
2025-07-15 10:45:00,SELL,65480.50,0.001
2025-07-15 11:15:00,BUY,65200.75,0.001
2025-07-15 11:30:00,SELL,65350.90,0.001"""
    df = pd.read_csv(StringIO(csv_data), names=["Time", "Signal", "Price", "Quantity"], parse_dates=["Time"])
else:
    df = pd.read_csv(log_file, names=["Time", "Signal", "Price", "Quantity"], parse_dates=["Time"])

df["Time"] = pd.to_datetime(df["Time"])
df.set_index("Time", inplace=True)

st.subheader("📈 Price Chart")
st.line_chart(df["Price"])

st.subheader("📃 Recent Trades")
st.dataframe(df.tail(20))

st.metric(label="Latest Price", value=f"${df['Price'].iloc[-1]:,.2f}")
st.metric(label="Last Signal", value=df['Signal'].iloc[-1])