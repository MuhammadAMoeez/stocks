import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Stock Dashboard 📊")

# Sidebar inputs
st.sidebar.header("Setting for Stock")
ticker = st.sidebar.text_input("enter ticker symbol", "AAPL")
period = st.sidebar.selectbox("Select the period", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "5y"])
interval = st.sidebar.selectbox("Select the Interval", ["1m", "5m", "15m", "1h", "1d"])

# Cache data to reduce API calls
@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_stock_data(ticker, period, interval):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period, interval=interval)
        return data, stock.info
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None, None

# Fetch data
data, info = get_stock_data(ticker, period, interval)

if data is not None and not data.empty:
    # Display current price
    st.subheader(f"Current Price: {ticker}")
    current_price = data['Close'].iloc[-1]
    st.metric("Price", f"$ {current_price:.2f}")
    
    # Display chart
    st.subheader(f"Price Chart for {ticker}")
    st.line_chart(data['Close'])
    
    # Display data table
    st.subheader("Historical Data")
    st.dataframe(data)
else:
    st.warning("Unable to fetch stock data. Please try again later.")
