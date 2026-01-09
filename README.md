📈 Real-Time Stock Market Dashboard
A comprehensive financial visualization tool built to democratize access to market data through an intuitive, high-performance web interface.

🌟 Project Motivation
Traditional market data platforms are often either prohibitively expensive for retail investors or cluttered with advertisements and delayed data. This project was built to provide a clean, ad-free command center that consolidates live market indices, individual stock performance, and predictive trends into a single coherent interface.

🚀 Key Features
Live Market Monitoring: Real-time price tracking for major indices and individual equities with low-latency updates.

Interactive Data Visualization: Dynamic candlestick charts, moving averages (SMA/EMA), and RSI indicators powered by Plotly.

Custom Watchlists: Personalized tracking for specific stocks to monitor portfolio performance at a glance.

Historical Analysis: Fetch and visualize past price data (1 day to 5+ years) for deep-dive trend analysis.

Fundamental Insights: Instant access to key financial metrics including Market Cap, P/E Ratio, and Volume.

🛠️ Tech Stack
Frontend: Streamlit (Rapid UI prototyping & Python-native server).

Data Source: yfinance / Yahoo Finance API (Reliable financial data retrieval).

Analytics: Pandas for data manipulation and NumPy for mathematical indicators.

Visualization: Plotly for interactive, responsive charting.

Deployment: Streamlit Community Cloud.

🏗️ How It Works
Ingestion: The app fetches raw market data via RESTful API calls to financial providers.

Processing: Python scripts calculate technical indicators (like Moving Averages) on-the-fly.

Visualization: Data is rendered into high-fidelity charts using Plotly's engine.

Interaction: Streamlit widgets allow users to toggle indicators, change timeframes, and search for new tickers instantly.

📦 Installation & Usage
Clone the repository.

Install dependencies:

Bash

pip install streamlit yfinance plotly pandas
Launch the dashboard:

Bash

streamlit run app.py
