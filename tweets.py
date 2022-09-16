# Load packages for analysis
import snscrape.modules.twitter as sntwitter
import pandas as pd

# set query constraints using a scrape. This
# still needs to be modified to loop for some list of stocks
query = "(from:elonmusk) until:2020-01-01 since:2010-01-01"
tweets = []
limit = 5000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
# df.to_csv('tweets.csv')
