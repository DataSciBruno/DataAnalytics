# Stock Correlation Analyzer - Pearson

This Python script downloads historical stock data using Yahoo Finance (using the `yfinance` library) and calculates the Pearson correlation coefficient between two given stocks. It also determines the statistical significance of the correlation.

## Usage

1. Make sure you have the necessary dependencies installed: `pandas`, `yfinance`, and `scipy`.
2. Run the script and provide the required inputs:
   - Enter the first stock ticker.
   - Enter the second stock ticker.
   - Enter the start date for the historical data.
   - Enter the end date for the historical data.
3. The script will download the historical data for the specified stocks, calculate the correlation coefficient, and provide the statistical significance at different significance levels (0.10, 0.05, and 0.01).
4. The correlation coefficient and statistical significance will be printed to the console.

## Example

```python
import pandas as pd
import yfinance as yf
from scipy.stats import pearsonr

# Function to calculate the correlation coefficient and statistical significance
def historical_data(ticker_1, ticker_2, start_date, end_date):
    # Download historical data for the given ticker
    stock_data_1 = yf.download(ticker_1, start=start_date, end=end_date, progress=False)
    stock_data_2 = yf.download(ticker_2, start=start_date, end=end_date, progress=False)

    # Create a pct change column
    stock_data_1 = stock_data_1['Adj Close']
    stock_data_2 = stock_data_2['Adj Close']

    # Combine the data into a single DataFrame
    df = pd.concat([stock_data_1, stock_data_2], axis=1)
    df.columns = [ticker_1, ticker_2]

    # Remove any rows with missing data
    df.dropna(inplace=True)

    # Calculate the Pearson correlation coefficient and p-value
    corr_coef, p_value = pearsonr(df[ticker_1], df[ticker_2])

    # Print the correlation coefficient
    print("\nCorrelation Coefficient:", corr_coef)

    # Calculate and print the p-values for different significance levels
    p_value_0_10 = 1 - corr_coef
    p_value_0_05 = 1.96 * (1 - corr_coef)
    p_value_0_01 = 2.58 * (1 - corr_coef)

    print("\nP-value:",p_value)

    if p_value > 0.1:
        print('0.10: Not statistically significant')
    else:
        print('0.10: Statistically significant')

    if p_value > 0.05:
        print('0.05: Not statistically significant')
    else:
        print('0.05: Statistically significant')

    if p_value > 0.01:
        print('0.01: Not statistically significant')
    else:
        print('0.01: Statistically significant')

    # Return the correlation coefficient
    return corr_coef

# Example usage
ticker_1 = input("Enter stock ticker: ")
ticker_2 = input("Enter the other stock ticker: ")
start_date = input("Start date: ")
end_date = input("End date: ")

data = historical_data(ticker_1, ticker_2, start_date, end_date)
