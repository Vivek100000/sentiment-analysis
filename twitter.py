import tweepy
import re
import pandas as pd
from textblob import TextBlob
client = tweepy.Client(bearer_token= "AAAAAAAAAAAAAAAAAAAAAFFgewEAAAAA9sqnI%2B0WaeCzZeUTJekSmzmywB4%3D5j44Ow70Kl9spy6SokMZiRdGyPTmV5BSNL9lVItW2WypMFOzcC")
query = 'technology'
column = ['author-id','created_at','tweet','sentiment']

response = tweepy.Paginator(client.search_recent_tweets, query=query,tweet_fields=['created_at','author_id','id'], max_results=100).flatten(limit=120)
data = []
sentiment = ""
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
    data.append([tweet.id,tweet.created_at,tweet.text,sentiment])

df = pd.DataFrame(data, columns=column)
print(df)
df.to_csv('tweets.csv')