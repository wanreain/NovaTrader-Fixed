# NovaTrader App

Automated trading bot using MetaTrader 5 with EMA + RSI strategy and a Streamlit dashboard.

## Features
- EMA Crossover + RSI Filter
- Auto trading every 15 minutes
- Streamlit dashboard
- Telegram alerts (configurable)

## Setup
1. Install dependencies:
```
pip install -r requirements.txt
```
2. Create a `.env` file from `.env.template`.
3. Run the bot:
```
python main.py
```
4. Launch the dashboard:
```
streamlit run dashboard.py
```