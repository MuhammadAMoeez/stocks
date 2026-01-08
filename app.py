import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import date

st.set_page_config(page_title='stock dashboard', page_icon='📈', layout='wide')

st.title("Stock Dashboard 📈")

st.sidebar.header("Setting for Stock")
ticker_symbol = st.sidebar.text_input("enter ticker symbol", "AAPL")
period = st.sidebar.selectbox("Select the period", ['1d', '1M', "6M", '1Y', "5Y"])
interval = st.sidebar.selectbox("Select the interval", ['1m', '5m', '15m', '1h', '1d'])

ticker = yf.Ticker(ticker_symbol)
data = ticker.history(period=period, interval=interval)

latest_price = data['Close'].iloc[-1] if not data.empty else "N/a"
st.metric(label=f"Current Price : {ticker_symbol}", value=f"${latest_price: .2f}" if latest_price != "N/a" else "No Data")

st.subheader(f"Price Chart for {ticker_symbol}")
if not data.empty:
    st.line_chart(data)
else:
    st.warning(f"No data available for {ticker_symbol}")


col1, col2, col3 = st.columns(3)

with col1:
    st.write(f"**Previous Close**", ticker.info.get("previousClose", "N/A") )
with col2:
    st.write(f"**Market Cap**", ticker.info.get("marketcap", "N/A") )
with col3:
    st.write(f"**52-Week high**", ticker.info.get("fiftyTwoWeekHigh", "N/A") )


st.info("Refresh to get latest data")
    