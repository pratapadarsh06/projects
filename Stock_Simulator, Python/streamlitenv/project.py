#Description: This is a stock market dashboard to show some charts and data on some stock 

#Import the libraries
import streamlit as st
import pandas as pd
from PIL import Image
from alpha_vantage.timeseries import TimeSeries
import time


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
	start_date = st.sidebar.text_input("Start Date", "2021-10-25")
	end_date = st.sidebar.text_input("End Date", "2021-11-05")
	stock_symbol = st.sidebar.text_input("Stock Symbol", "MSFT")
	return start_date, end_date, stock_symbol

#create a function to get the company name
def get_company_name(symbol):   
   if symbol == 'AXIS':
      return 'AXIS BANK'
   elif symbol == 'ICICI':
    	return 'ICICI BANK'
   elif symbol == 'KOTAK':
      return 'KOTAK BANK'
   else:
      'None'

#create a function to get the proper company data and the proper timeframe from the user start date to the user end date.
def get_data(comp_name, start, end):
      #Load the data

      api_key='2ZQ7F65CN9W34EV1'

      ts = TimeSeries(key=api_key, output_format='pandas')
      df, meta_data = ts.get_intraday(symbol=comp_name, outputsize = 'full')
      #print(df)

      # if symbol.upper() == 'AXIS':
      #    df = pd.read_csv("E:/learning/various technololgy learned/computer simulation project/edited_csv file/AXIS_BANK.csv")
      # elif symbol.upper() == 'ICICI':
      #    df = pd.read_csv("E:/learning/various technololgy learned/computer simulation project/edited_csv file/ICICI_BANK.csv")
      # elif symbol.upper() == 'KOTAK':
      #    df = pd.read_csv("E:/learning/various technololgy learned/computer simulation project/edited_csv file/KOTAK_BANK.csv")
      # else:
      #    df = pd.DataFrame(columns=['Date', 'Close', 'Open', 'Prev Close', 'High', 'Low'])

      #get the date range 
      start = pd.to_datetime(start)
      end = pd.to_datetime(end)
      print(start)
      print(pd.to_datetime(df['date'][0]))
          
      #set the start and end index rows both to 0
      start_row = 0
      end_row = 0

      #Start the date from the top of the data set and go down to see if the users start date is less than or equal to the date in the dataset.
      for i in range(0, len(df)):
      	if start <= pd.to_datetime(df['Date'][i]):
                  start_row = i
                  break

      #Start from the bottom of the dataset and go up to see if the users end date is greater than or equal to the date in the dataset.

      for j in range(0, len(df)):
      	if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
                  end_row = len(df)-1-j
                  break

      #set the index to be the date
      df = df.set_index(pd.DatetimeIndex(df['Date'].values))

      return df.iloc[start_row:end_row +1, :]


#Get the users input 
start, end, symbol = get_input()
#getthe data
df = get_data(symbol, start, end)
#Get the company name
#company_name = get_company_name(symbol.upper())
company_name = symbol

#Display the close price
st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])

# Get statistics ont he data
st.header('Data Statistics')
st.write(df.describe())