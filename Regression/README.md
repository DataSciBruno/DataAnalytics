# Linear Regression Analysis of Stock Price Changes
This project focuses on performing a linear regression analysis on the historical stock price changes of a given ticker symbol. The goal is to explore the relationship between the opening price gap and the percentage change in adjusted closing price of the stock.

## Libraries
The following libraries are used in this project:

yfinance: For downloading historical stock price data.

pandas: For data manipulation and analysis.

plotly.express: For data visualization.

scipy.stats: For statistical analysis.

statsmodels.api: For regression analysis.

numpy: For numerical computations.

matplotlib.pyplot: For plotting charts.

## Input
The user is prompted to enter the ticker symbol of the stock they want to analyze and the start and end dates to download the corresponding historical price data.

## Downloading Data
The historical price data for the specified ticker symbol is downloaded using the yfinance library and stored in a pandas DataFrame named data.

## Preprocessing
To focus on the relevant features, the DataFrame data is reduced to only the 'Open' and 'Adj Close' columns, which represent the opening price and adjusted closing price of the stock, respectively.

Next, the percentage change in the adjusted closing price is calculated and stored in a new column named 'Pct_Change'. Additionally, the previous day's adjusted closing price and the opening price gap are calculated and added as 'Yesterday_s_Adj_Close' and 'Gap' columns, respectively.

Any rows with missing values are dropped from the DataFrame.

## Visualization
A scatter plot is created using the plotly.express library to visualize the relationship between the opening price gap ('Gap') and the percentage change in adjusted closing price ('Pct_Change') for the preprocessed data.

## Removing Outliers
Outliers in the percentage change data are identified using z-scores. Any data points with an absolute z-score above a threshold (default is 3.0) are considered outliers. These outliers are removed from the dataset, and the resulting DataFrame is stored in data_no_outliers.

## Linear Regression Model
A linear regression model is fitted to the data using the stats.linregress function from scipy.stats. The slope, intercept, r-value (correlation coefficient), p-value, and standard error of the regression are calculated.

## Results
The linear regression model reveals the following insights:

Slope: The estimated slope of the linear regression line is approximately 0.0199, indicating a positive relationship between the opening price gap and the percentage change in adjusted closing price.

Intercept: The estimated intercept of the linear regression line is approximately -0.0756, representing the expected percentage change in adjusted closing price when the opening price gap is zero.

R-squared: The coefficient of determination (R-squared) is approximately 0.0067, indicating that only a small proportion of the variation in the percentage change can be explained by the opening price gap.

p-value: The p-value is approximately 3.13e-06, suggesting that the relationship between the opening price gap and the percentage change in adjusted closing price is statistically significant.

## Visualization
A scatter plot with the regression line is plotted using the matplotlib.pyplot library to visualize the relationship between the opening price gap and the percentage change in adjusted closing price, as well as the linear regression line that represents the estimated relationship.

Feel free to explore the provided code and modify it according to your specific needs. Use this linear regression analysis to gain insights into the relationship between opening price gaps and percentage changes in adjusted closing prices for a given stock!
