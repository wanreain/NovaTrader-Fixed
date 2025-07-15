import streamlit as st
from strategy import fetch_data, apply_strategy
from config import SYMBOL

st.title("📊 NovaTrader Dashboard")
df = fetch_data(SYMBOL)
df = apply_strategy(df)
st.line_chart(df[['close', 'ema_fast', 'ema_slow']])
st.dataframe(df.tail(10))