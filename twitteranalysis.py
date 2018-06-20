import tweepy
from textblob import TextBlob

consumer_key = 'duV2ZqMebwokuBt8Y3Dt7yAVH'
consumer_seceret = 'ivCOsaIGvILtdPvDvHloJc5azzI77AuQTc0wfGCyXZeLjQcXFT'

access_token = '592359921-yAqUyN45QPLg3OiwTm9yd5ePiwf1VJFAH4O5iKNy'
access_token_seceret = 'DFEP5YKWWXiDyByJb5RfMrvX8j2E9slrQQhcV4nj1PEpk'

#Authentification
auth = tweepy.OAuthHandler(consumer_key, consumer_seceret)
auth.set_access_token(access_token, access_token_seceret)

#
api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
