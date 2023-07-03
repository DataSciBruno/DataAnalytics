import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf
from datetime import datetime

# Streamlit configuration
st.set_page_config(layout="wide")

# Function to download stock data
def download_stock_data(ticker, start_date):
    end_date = datetime.today().strftime('%Y-%m-%d')
    data_downloaded = yf.download(ticker, start=start_date, end=end_date)
    return data_downloaded

# Function to preprocess data and plot the chart
def preprocess_and_plot(data):
    # Calculate additional indicators
    data["Returns"] = round((data["Adj Close"].pct_change()) * 100, 2)
    data["Log_Returns"] = round((np.log(data["Adj Close"]) - np.log(data["Adj Close"].shift(1))) * 100, 2)
    window_size = 30
    data['Historical_Volatility'] = round(data["Log_Returns"].rolling(window=window_size).std() * np.sqrt(252), 2)
    data['EMA8'] = round(data['Close'].ewm(span=9, adjust=False).mean(), 2)
    data['EMA21'] = round(data['Close'].ewm(span=21, adjust=False).mean(), 2)
    data['EMA50'] = round(data['Close'].ewm(span=50, adjust=False).mean(), 2)
    data['EMA72'] = round(data['Close'].ewm(span=72, adjust=False).mean(), 2)
    data['EMA144'] = round(data['Close'].ewm(span=144, adjust=False).mean(), 2)
    data['EMA200'] = round(data['Close'].ewm(span=200, adjust=False).mean(), 2)
    delta = data['Close'].diff()
    gain = delta.mask(delta < 0, 0)
    loss = -delta.mask(delta > 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = round(rsi, 2)
    data['SMA20'] = data['Close'].rolling(window=20).mean()
    data['StdDev'] = round(data['Close'].rolling(window=20).std(), 2)
    data['UpperBB'] = round(data['SMA20'] + (data['StdDev'] * 2), 2)
    data['LowerBB'] = round(data['SMA20'] - (data['StdDev'] * 2), 2)
    data = data.dropna()

    # Plot OHLC chart with indicators
    ohlc_data = data[['Open', 'High', 'Low', 'Close']]
    apds = [
        mpf.make_addplot(data['EMA8'], color='blue'),
        mpf.make_addplot(data['EMA21'], color='green'),
        mpf.make_addplot(data['EMA50'], color='orange'),
        mpf.make_addplot(data['EMA72'], color='purple'),
        mpf.make_addplot(data['EMA144'], color='red'),
        mpf.make_addplot(data['EMA200'], color='brown'),
        mpf.make_addplot(data['RSI'], panel=1, color='blue'),
        mpf.make_addplot(data['UpperBB'], panel=2, color='green'),
        mpf.make_addplot(data['LowerBB'], panel=2, color='red')
    ]

    fig, axes = mpf.plot(ohlc_data, type='candle', style='yahoo', title='OHLC Chart with Indicators', ylabel='Price',
                         addplot=apds, returnfig=True)

    # Customize the plot
    axes[0].grid(True)
    axes[1].grid(True)
    axes[2].grid(True)

    # Show the plot
    st.pyplot(fig)

# Main Streamlit app
def main():
    # App title
    st.title("Stock OHLC Chart with Indicators")

    # User input for stock ticker and start date
    ticker = st.text_input("Enter the stock ticker (e.g., AAPL):")
    start_date = st.text_input("Enter a start date (e.g., 2010-01-01):")

    if ticker and start_date:
        try:
            # Download stock data
            data_downloaded = download_stock_data(ticker, start_date)

            if not data_downloaded.empty:
                # Preprocess data and plot the chart
                preprocess_and_plot(data_downloaded)

                # Display the data table
                st.subheader("Stock Data")
                st.dataframe(data_downloaded)

            else:
                st.error("No data available for the provided stock ticker and start date.")

        except Exception as e:
            st.error(f"Error occurred: {e}")

    else:
        st.info("Please enter the stock ticker and start date.")

# Run the app
if __name__ == '__main__':
    main()
