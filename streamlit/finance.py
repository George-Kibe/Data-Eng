import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price Application

#### Shown are the stock closing price and volume of Google!
""")

# Define the ticker symbol
tickerSymbol = "GOOGL"
#Get Data on This Ticker
tickerData = yf.Ticker(tickerSymbol)
# Get the historical prices for this ticker
tickerDf = tickerData.history(period="id", start="2010-5-31", end="2020-5-31")
# open high low close volume dividends stock splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


















