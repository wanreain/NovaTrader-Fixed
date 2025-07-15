import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="NovaTrader Dashboard", layout="wide")
st.title("📊 NovaTrader AI - Live Trade Dashboard")

log_file = Path("trade_log.csv")

if not log_file.exists():
    st.warning("📁 `trade_log.csv` not found.\n\nPlease make sure the bot has run and logged at least one trade.")
else:
    try:
        df = pd.read_csv(log_file, names=["Time", "Signal", "Price", "Quantity"], parse_dates=["Time"])
        df["Time"] = pd.to_datetime(df["Time"])
        df.set_index("Time", inplace=True)

        st.subheader("📈 Price Chart")
        st.line_chart(df["Price"])
        st.subheader("📃 Recent Trades")
        st.dataframe(df.tail(20))
        st.metric(label="Latest Price", value=f"${df['Price'].iloc[-1]:,.2f}")
        st.metric(label="Last Signal", value=df['Signal'].iloc[-1])
    except Exception as e:
        st.error(f"❌ Error loading trade data: {e}")
