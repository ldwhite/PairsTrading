# Pairs Trading Strategy in Python

<p align="center">
  <img src="https://media.istockphoto.com/photos/stock-market-price-display-picture-id509031122?k=6&m=509031122&s=612x612&w=0&h=SlN4D-0yMTc1XI64-cIajhXZYy0wRN2I8XWCrxvc_6Q=" />
</p>

Using Python to construct a Pairs Trading Strategy. This model pulls the current list of S&P 500 companies as listed on wikipedia and allows the user to easily filter them by Sector and Industry which then tests for correlation and cointegration between pairs of stocks, normalizes their standard deviations and constructs buy and sell signals.

## Required Packages

<img src="https://raw.githubusercontent.com/ldwhite/TradingStrategies/main/images/packages.png" 
     width="400" 
     />

We need to load NumPy and Pandas just about anytime we're dealing with data. The Datetime package is used when setting the start and end dates that we're using to determine the time interval in which our historical stock data will be picked. Pandas-Datareader is the package we will be using to obtain historical pricing data. Statsmodels is the package we will use for conducting our correlation and cointegration tests. Finally, Matplotlib and Seaborn are the packages we will use for data visualization, with Matplotlib being used for generating graphs and Seaborn used for constructing the correlation heatmap.

## Acknowledgements
A lot of inspiration came from [KidQuant](https://kidquant.com/project/pairs-trading-strategies-in-python/).
