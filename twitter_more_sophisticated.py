import tweepy
import re
import pandas as pd
from textblob import TextBlob
client = tweepy.Client(bearer_token= "AAAAAAAAAAAAAAAAAAAAAFFgewEAAAAA9sqnI%2B0WaeCzZeUTJekSmzmywB4%3D5j44Ow70Kl9spy6SokMZiRdGyPTmV5BSNL9lVItW2WypMFOzcC")
query = 'tech'
column = ['author-id','created_at','tweet','sentiment']
#response = client.search_recent_tweets(query=query,max_results=100)
response = tweepy.Paginator(client.search_recent_tweets, query=query,tweet_fields=['created_at','author_id','id'], max_results=50).flatten(limit=200)
data = []
sentiment=''
for tweet in response:
    final_text=tweet.text
    final_text = re.sub('@[^\s]+', '', final_text)
    final_text = re.sub('http[^\s]+', '', final_text)
    analysis = TextBlob(final_text)
    if analysis.polarity>0:
        sentiment = "positive"
    elif analysis.polarity<0:
        sentiment = "negative"
    elif analysis.polarity == 0:
        sentiment = "neutral"
    data.append(tweet)

for i in range(30):
    print(data[i].includes['users'][2])


