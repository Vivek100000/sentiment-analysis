from textblob import TextBlob
import pandas as pd
import tweepy
import re

api_key = "MT10kr0ziWhLybSTZbb7WylqI"
api_secret_key = "xCLlXltqitl41HeUyM23gEAnuY7pZGHYa9s93ZzO9JV3DXhLAZ"
access_token = "1503960613793386500-2LdKlihZfpORNZ8NeuI0tpzmOPBFY0"
access_token_secret = "w70L0LrbqWfrvZuUzTo0PsBEfxVkkG3YmZUuWP3vCIAOo"

# establishing connection with the Twitter API using keys
auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_secret_key)
auth_handler.set_access_token(access_token, access_token_secret)
# Connection established
api = tweepy.API(auth_handler)
search_item = "technology"
tweet_amount = 200

tweets = tweepy.Cursor(api.search_tweets, q=search_item, lang="en").items(tweet_amount)
positive = 0
negative = 0
neutral = 0
column = ['Time', 'user', 'tweet', 'sentiment']
data = []

for tweet in tweets:
    final_text = tweet.text
    final_text = re.sub('@[^\s]+', '', final_text)
    final_text = re.sub('http[^\s]+', '', final_text)
    analysis = TextBlob(final_text)
    if analysis.polarity > 15:
        data.append([tweet.created_at,tweet.username,tweet.text,"positive"])
        positive += 1
    elif analysis.polarity < 15:
        data.append([tweet.created_at,tweet.username,tweet.text,"negative"])
        negative += 1
    elif analysis.polarity == 0:
        data.append([tweet.created_at,tweet.username,tweet.text,"neutral"])
        neutral += 1
df = pd.DataFrame(data, columns=column)
print(df)
print("total tweets taken into consideration: ", tweet_amount, "\n")
print("negative tweets: ", negative, "\n")
print("positive tweets: ", positive, "\n")
print("neutral tweets: ", neutral, "\n")




