import tweepy
import time
import random
import twitter_credentials
from tweepy import OAuthHandler



#auth variables 
auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
            
def searchBotCount(hashtag_list=0, tweetNumber=5):
    hashtag = ["#Germanshepard", "#Doggo", "#Foster", "#cats", "#dogs"]
    hashtag_list=random.choice(hashtag)
    tweets = tweepy.Cursor(api.search, hashtag_list).items(tweetNumber)
    for tweet in tweets:
        try:
            tweet.retweet()
            tweet.favorite()
            #api.create_friendship(tweet.user.id)
            print("bork bork")
            time.sleep(1)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(1)

def followMyFollowers():
    follow_all=tweepy.Cursor(api.followers).items()
    for follower in follow_all:
        follower.follow()


searchBotCount()
#followMyFollowers()