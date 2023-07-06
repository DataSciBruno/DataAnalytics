# Exploratory Analysis for Stock Price
This project focuses on conducting exploratory analysis for stock price data. The goal is to gain insights into the stock's behavior and identify potential support and resistance levels.

## Libraries
The following libraries are used in this project:

yfinance: For downloading stock price data.

pandas: For data manipulation and analysis.

plotly.express: For interactive data visualization.

scipy.stats: For statistical functions.

statsmodels.api: For statistical modeling.

numpy: For numerical computations.

matplotlib.pyplot: For data visualization.

## Input
You will be prompted to enter the stock ticker symbol and the start and end dates for the data. The yfinance library is used to download the historical stock price data.

## Data Exploration
The project includes various exploratory analyses on the stock price data:

Visualize Stock Prices: The closing price of the stock is plotted over time.

Identify Support and Resistance Levels: Local minima (support) and local maxima (resistance) levels are identified based on the stock price. These levels are visualized on the stock price plot.

Determine Last Support and Resistance: The last support and resistance levels are determined based on the most recent data.

Make Trading Decision: Based on the last closing price and the proximity to the last support and resistance levels, a trading decision (buy or sell) is suggested.

## Results
Based on the analysis, a trading decision is provided:

If the last closing price is closer to the last support level than the last resistance level, a "Buy" recommendation is given.
If the last closing price is not closer to the last support level than the last resistance level, a "Sell" recommendation is given.
Feel free to explore the provided code and modify it according to your requirements. Use this exploratory analysis to gain insights into stock price behavior and support your trading decisions!
