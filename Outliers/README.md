# Outlier Analysis for Stock Price
This project focuses on analyzing and handling outliers in stock price data. The goal is to identify and remove any outliers that may significantly affect the analysis or modeling process.

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

## Data Preprocessing
The initial data is preprocessed to calculate the percentage change in the adjusted closing price (Pct_Change). Any rows with missing values are dropped from the dataset.

## Outlier Analysis
Outliers in the percentage change data are identified using the z-score method. The z-scores are calculated for each data point, and a threshold value is set to determine outliers. Data points with z-scores above the threshold are considered outliers.

## Handling Outliers
The identified outliers are removed from the dataset to ensure they do not skew the analysis. The rows corresponding to the outliers are dropped, resulting in a new dataset (data_no_outliers) without the outliers.

## Results
The scatter plot of the percentage change in the stock price is displayed before and after removing the outliers. This allows for a visual comparison of the distribution and the impact of the outliers on the data.

Feel free to explore the provided code and modify it according to your requirements. Use this outlier analysis to ensure robust and reliable analysis of stock price data!
