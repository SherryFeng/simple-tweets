import tweepy
from secrets import consumer_key, consumer_secret, access_token, access_token_secret

# OAuth process, using the keys and tokens
# hello 2
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to print my info
# hello! 
print api.me()
