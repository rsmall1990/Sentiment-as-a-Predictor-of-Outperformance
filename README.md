# Sentiment and Market Outperformance

This project functions as an example of a deployed fully-functional "data product." It will look at whether Twitter sentiment can serve as a predictor of market outperformance. Although the topic has been covered extensively in [relevant literature](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0138441#:~:text=In%20%5B%2031%20%5D%2C%20the%20authors%20show%20that,terms%20of%20their%20influence%20on%20future%20stock%20prices.}), it can serve as a useful demonstration of the power of data products to influence decisions of consequence. The product will be deployed live to a microsoft azure environment for public access.

The initial phase will gather data from the twitter api alone. This data will be analysed to determine if there is a correlation between sentiment and security specific alpha.

The next step is to place trades using an application programming interface with a broker.

Therefore, the steps are as follows:

1.  Aggregate historical market data
    1.1. Validate if lowest institutional ownership has relationship to twitter mentions. If so, low institutional ownership (I.e. high retail ownership) may exhibit a relationship between identified sentiment and price. 
2.  Aggregate historical media sentiment training files
3.  determine if sentiment is a statistically significant predictor of price over meaningful time periods (day, week, weeks, month, year)
4.  Create mechanism for live streaming of sentiment data
5.  create algorithm to evaluate sentiment in real or near real time
6.  Predict market returns
7.  place trades by api on TDA or IB platforms

Here's to hoping we all get rich.

*Ryan*
