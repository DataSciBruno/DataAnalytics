# Descriptive Analysis for Stock Price
This project focuses on conducting descriptive analysis for stock price data. Various statistical measures and visualizations are used to gain insights into the behavior and characteristics of the stock price.

## Libraries
The following libraries are used in this project:

yfinance: For downloading stock price data.

pandas: For data manipulation and analysis.

plotly.express: For interactive data visualization.

scipy.stats: For statistical functions.

statsmodels.api: For statistical modeling.

numpy: For numerical computations.

matplotlib.pyplot: For data visualization.

mplfinance: For plotting candlestick charts.

## Input
You will be prompted to enter the stock ticker symbol and the start and end dates for the data. The yfinance library is used to download the historical stock price data.

## Data Visualization
The project includes several visualizations of the stock price data:

Line Plot: A line plot of the adjusted closing price over time.

Candlestick Chart: A candlestick chart that shows the open, high, low, and close prices for each day.

Close and Volume Plot: A combination plot showing the closing price and volume.

Histogram: A histogram plot showing the distribution of daily returns.

Accumulated Returns: A line plot showing the accumulated returns over time.

## Preprocessing
The data is preprocessed to calculate additional columns:

Percentage Change: The percentage change in the adjusted closing price from the previous day.

Rolling Means: The rolling mean of the daily returns using different window sizes.

Volatility: The rolling standard deviation of the daily returns using different window sizes.

## Descriptive Statistics

Various descriptive statistics are calculated:

Mean: The average daily return.

Median: The median daily return.

Standard Deviation: The measure of the spread or volatility of the daily returns.

Minimum and Maximum: The minimum and maximum daily returns.

Quartiles: The first, second (median), and third quartiles of the daily returns.

## Data Distribution
The distribution of daily returns is visualized using a histogram.

## Accumulated Returns
The accumulated returns over time are calculated and plotted.

Feel free to explore the provided code and modify it according to your requirements. Have fun performing descriptive analysis on stock price data!
