from time import sleep
import re

import tweepy
from textblob import TextBlob
#from our keys module (keys.py), import the keys dictionary
from keys import keys
from moodring_display import mood_ring

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

moodTotal= -2
numTweets = 2

mood_ring(moodTotal / numTweets)

def sentiment_search(query):
    '''
    '''
    global moodTotal
    global numTweets

    moodTotal = 0
    numTweets = 0
    limit = 100

    results = api.search(query)

    while numTweets < limit and numTweets < len(results):
        cleaned_tweet = clean_tweet(results[numTweets].text)
        blob = TextBlob(cleaned_tweet)

        numTweets += 1
        moodTotal += blob.sentiment.polarity

        print("DEBUG Tweet:", cleaned_tweet)
        print("DEBUG Sentiment:", blob.sentiment)
        print("DEBUG: moodTotal:", moodTotal, "numTweets:", numTweets)
        print()

    return moodTotal / numTweets

def clean_tweet(tweet):
    '''
    '''
    cleaned_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    return cleaned_tweet

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        global moodTotal
        global numTweets

        handle = status.user.screen_name
        twt = status.text
        cleaned_tweet = clean_tweet(twt)
        blob = TextBlob(cleaned_tweet)

        numTweets += 1
        moodTotal += blob.sentiment.polarity
        mood_ring(moodTotal / numTweets)

        print("DEBUG Tweet:", handle, twt)
        print("DEBUG Sentiment:", blob.sentiment)
        print("DEBUG: moodTotal:", moodTotal, "numTweets:", numTweets)
        print()
        sleep(1)
        

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        
if __name__ == "__main__":
    myStream = tweepy.Stream(api.auth, MyStreamListener())
    myStream.filter(track=['#secretvariable'])
