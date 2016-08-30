import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import time
 
class MyListener(StreamListener):
 
    def __init__(self):
        self.i = 0

    def on_data(self, data):
        #Put the number of tweets you want, here it's 10,000
        while (self.i <9999):
            try:
                with open('data_ger.json', 'a') as f:
                    f.write(data)
                    self.i = self.i +1
                    return True
            except BaseException as e:
                print("Error on_data: %s" % str(e))
            return True
        return False
 
    def on_error(self, status):
        print(status)
        return True

#This script gathers all the tweets that are now tweeted 

consumer_key = '67JviKGXrIJiCnVv8V6kOjUOZ'
consumer_secret = 'po5RZzEDUaAUByVOwPdYRA6iycjWEgyoXp480e2JR3MVKijV2L'
access_token = '395126661-suDOBHGfAbsjzKyHmxajvrgnFHfgUkcLVJNPxkJW'
access_secret = 'n1exsvQMjOLCy9Ol0YPxNTox8usDiSnSVQ1A5ZxB5QwRt'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth) 
twitter_stream = Stream(auth, MyListener())
#Change the language if you want to
twitter_stream.filter(track = ["a", "e", "u", "n"],languages=['de'])

