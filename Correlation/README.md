"# Data_Analytics" 

# Stock Correlation Analysis
This project retrieves and analyzes historical stock data for user-specified stocks. 

It uses the yfinance library to download the stock data, pandas for data manipulation, and matplotlib and seaborn for data visualization. 

The correlation between the daily returns of the two stocks is calculated and visualized as a heatmap. 

The adjusted closing prices and daily returns of the stocks are also plotted over time.

## Dependencies

pandas

yfinance

numpy

matplotlib

seaborn

You can install all dependencies by running pip install pandas yfinance numpy matplotlib seaborn

## Usage
Run the script.

When prompted, type in the ticker symbols of the two stocks you want to analyze.

Then, input the start and end dates for the data retrieval in the format YYYY-MM-DD.

The script will then download the data for the specified stocks and dates.

It will calculate and print the correlation matrix of the daily returns of the two stocks.

It will also display a heatmap of the correlation matrix, a plot of the adjusted closing prices over time, and a plot of the daily returns over time.
