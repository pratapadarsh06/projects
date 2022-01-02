#Description: This is a stock market dashboard to show some charts and data on some stock 

#Import the libraries
import streamlit as st
from PIL import Image
import yfinance as yf



#Add a title and an image 
st.write("""
#stock Market Web Application
***visually show data on a stock! Data range from Jan 1, 2021-April 30, 2021
""")

st.title('Stock Market Simulator')

image = Image.open("E:/learning/various technololgy learned/computer simulation project/Preview_Stock_Market_Data.jpg")
st.image(image, use_column_width=True)


#create a sidebar header
st.sidebar.header('User Input')


#create a function to get the users input 
def get_input():
	start_date = st.sidebar.text_input("Start Date", "2021-01-01")
	end_date = st.sidebar.text_input("End Date", "2021-04-30")
	stock_symbol = st.sidebar.text_input("Stock Symbol", "tsla")
	return start_date, end_date, stock_symbol

#Get the users input 
start, end, symbol = get_input()


tickerSymbol = symbol
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start=start, end=end)



#Display the close price
st.header(tickerSymbol+" Volume\n")
st.line_chart(tickerDf['Volume'])
	
# Get statistics ont he data
st.header('Data Statistics')
st.write(tickerDf.describe())

st.header('Company Calander')  #“calendar” function can be used to know about the earnings and revenue of the company.
st.write(tickerData.calendar)

st.header('Company Divident Data')  #A dividend can be described as a reward that publicly-listed companies extend to their shareholders. Dividends are sourced from company's net profits. 
st.write(tickerData.dividends)

st.header('Company Share Holders')
st.write(tickerData.major_holders)

st.header('Company Institutional Investors')
st.write(tickerData.institutional_holders) #Institutional investors are legal entities that participate in trading in the financial markets. Institutional investors include the following organizations: credit unions, banks, large funds such as a mutual or hedge fund, venture capital funds, insurance companies, and pension funds.

st.header('Company Recommendations')
st.write(tickerData.recommendations) # recommend different company share to buy, sell, Hold, strong buy etc

st.header('Json Format Company Data')
st.write(tickerData.info)


#stock symbol list
#https://stockanalysis.com/stocks/

#AAPL
#MSFT
#tsla
