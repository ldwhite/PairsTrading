# Pairs Trading Strategy in Python

<p align="center">
  <img src = "https://github.com/ldwhite/PairsTrading/blob/main/images/Stock%20Market.gif" />
</p>

Today, we use Python to construct a pairs trading strategy. This model pulls the current list of S&P 500 constituents from Wikipedia, allowing the user to easily filter companies by Sector and Industry, which then tests for correlation and cointegration between pairs of stocks, normalizes their standard deviations, and constructs buy and sell signals.

## Required Packages

<p align="center">
<img src = "https://raw.githubusercontent.com/ldwhite/TradingStrategies/main/images/packages.png" style = "width:50%" />
</p>

We need to load NumPy and Pandas just about anytime we're dealing with data. The Datetime package is used when setting the start and end dates that determine the time interval in which our historical stock data will be picked. Pandas-Datareader is the package we will be using to obtain historical pricing data. Statsmodels is the package we will use for conducting our correlation and cointegration tests. Finally, Matplotlib and Seaborn are the packages we will use for data visualization, with Matplotlib being used for generating graphs and Seaborn used for constructing the correlation heatmap.

## Data Gathering

<p align="center">
<img src = "https://raw.githubusercontent.com/ldwhite/PairsTrading/main/images/wikipedia.png" style = "width:80%" />
</p>

After we load our required packages, we want to pull a table containing all the companies that are currently listed on the S&P 500 index. I like to pull this from Wikipedia, firstly because the table is already formatted quite well and especially because of the list of Sectors and Industries, which is how we will be dividing the list of stocks we seek to investigate. Note that you might need to make changes to <code>sp500 = pd.DataFrame(tables[0])</code>, as Wikipedia pages sometimes get reformatted, thus it might become necessary to change which table number you are seeking to pull from the Wikipedia page.

## Heatmap

<p align="center">
<img src = "https://raw.githubusercontent.com/ldwhite/PairsTrading/main/images/heatmap.png" style = "width:80%" />
</p>

After we use the list of stocks from the S&P 500 to narrow down our choices, we want to find stocks with a high degree of correlation. As you will often end up with a long list of stocks, it can be difficult to identify stock pairs with a high correlation from a traditional correlation matrix. To ameliorate the problem of readability, first we take only the magnitude of correlation, <code>.abs()</code>, then ensure that we have a triangular correlation matrix. We accomplish this by creating a mask using the NumPy package which masks duplicate values in the correlation matrix using <code>mask = np.triu(np.ones_like(matrix, dtype = bool))</code>. The next thing we want to do is ensure the heatmap is set up to our specifications; with a large number of stocks in our correlation matrix, it is beneficial to limit each cell to only two significant figures, which we specify with <code>fmt = '.2f'</code>. Additionally, the color scheme is entirely up to personal preference; the one I chose for this heatmap, <code>cmap = 'RdYlBu_r'</code> is my personal favorite, but you can choose your own. The Seaborn package has great [documentation](https://seaborn.pydata.org/generated/seaborn.heatmap.html) for the various different options available with Seaborn heatmaps. From this, yields the following heatmap:

<p align="center">
<img src = "https://github.com/ldwhite/PairsTrading/blob/main/images/seaborn_heatmap.png" style = "width:80%" />
</p>
  
## Cointegration

<p align="center">
<img src= "https://github.com/ldwhite/PairsTrading/blob/main/images/cointegration.png" style = "width:80%" />
</p>

The next item on the agenda is confirming that the ratio of the stock pairs we have chosen is fluctuating around a stationary value. If the pair is fluctuating around a stationary value, then we can use that to execute trades: buying or selling the ratio when the pair has deviated a sufficient distance from that stationary value, with the expectation from historical data that it will eventually revert to the mean value. To determine this, we use cointegration. The function as written at the end of this snippet of code isn't strictly speaking necessary but it is a nice way of printing the p-values and the significance of the p-value of the cointegration.

## Buy and Sell Signals

<p align="center">
<img src = "https://github.com/ldwhite/PairsTrading/blob/main/images/buysellcode.png" style = "width:50%" />
</p>
  
Now that we have determined that our chosen stock pair is in fact cointegrated, we want to construct buy and sell signals. To visualize this, we generate a chart that incorporates buy and sell signal once the price ratio has deviated past our predefined Z-scores. If the ratio deviates more than 1 standard deviation (or past a Z-score of 1), then we either buy or sell the ratio, depending on the direction of the deviation. We will buy the ratio once it reaches 1 standard deviation below the mean, as we expect, from our data, that the ratio will appreciate in value; this is accomplished by buying stock S1 (the stock in the numerator of our ratio) and selling stock S2 (the stock in the denominator of our ratio), and vice-versa when the ratio reaches 1 standard deviation above the mean.

<p align="center">
<img src = "https://github.com/ldwhite/PairsTrading/blob/main/images/buysell.png" style = "width:80%" />
</p>

## Acknowledgements
Thanks to [KidQuant](https://kidquant.com/project/pairs-trading-strategies-in-python/) for providing the inspiration.
