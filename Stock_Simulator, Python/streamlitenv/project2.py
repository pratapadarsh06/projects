import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""# Online Stock Price Ticker """)


tickerSymbol = "tsla"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-30', end='2021-03-8')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
