import tweepy
from textblob import TextBlob

# twitter app keys and tokens
consumer_key = '****'
consumer_secret = '****'
access_token = '****'
access_token_secret = '****'

# authentication
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

# search for tweets
public_tweets = api.search('World record egg')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('\n')
