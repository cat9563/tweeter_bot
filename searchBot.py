import tweepy
import time
import twitter_credentials
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# class TwitterUpdater():

#     """
#     update twitter status on Bella bot
#     """

#     def __init__(self):
#         pass



auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

hashtag = "#GermanShepherd"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("bork bork")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchBot()
#api.update_status("bork bork")

