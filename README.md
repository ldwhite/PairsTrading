# Pairs Trading Strategy in Python

<p align="center">
  <img src="https://media.istockphoto.com/photos/stock-market-price-display-picture-id509031122?k=6&m=509031122&s=612x612&w=0&h=SlN4D-0yMTc1XI64-cIajhXZYy0wRN2I8XWCrxvc_6Q=" />
</p>

Using Python to construct a Pairs Trading Strategy. This model pulls the current list of S&P 500 companies as listed on wikipedia and allows the user to easily filter them by Sector and Industry which then tests for correlation and cointegration between pairs of stocks, normalizes their standard deviations and constructs buy and sell signals.

## Required Packages

<img src="https://raw.githubusercontent.com/ldwhite/TradingStrategies/main/images/packages.png" style="width:50%" 
     />

We need to load NumPy and Pandas just about anytime we're dealing with data. The Datetime package is used when setting the start and end dates that we're using to determine the time interval in which our historical stock data will be picked. Pandas-Datareader is the package we will be using to obtain historical pricing data. Statsmodels is the package we will use for conducting our correlation and cointegration tests. Finally, Matplotlib and Seaborn are the packages we will use for data visualization, with Matplotlib being used for generating graphs and Seaborn used for constructing the correlation heatmap.

## Data Gathering  

<img src="https://raw.githubusercontent.com/ldwhite/PairsTrading/main/images/wikipedia.png" style="width:80%" />

After we load our required packages, we want to pull a table containing all the companies that are currently listed on the S&P 500 index. I like to pull this from Wikipedia, firstly because the table is already formatted quite well and especially because of the list of Sectors and Industries, which is how we will be dividing the list of stocks we seek to investigate. Note that you might need to make changes to <code>sp500 = pd.DataFrame(tables[0])</code>, as Wikipedia pages sometimes get reformatted, thus it might become necessary to change which table number you are seeking to pull from the Wikipedia page.

## Acknowledgements
A lot of inspiration came from [KidQuant](https://kidquant.com/project/pairs-trading-strategies-in-python/).
