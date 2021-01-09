# retweetCyborgV2/bots/config.py
import tweepy
import logging
import os

def create_api():
    # Authenticate to Twitter
    
    CONSUMER_KEY = environ["CONSUMER_KEY"]
    CONSUMER_SECRET = environ["CONSUMER_SECRET"]
    ACCESS_KEY = environ["ACCESS_KEY"]
    ACCESS_SECRET = environ["ACCESS_SECRET"]
    
    auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
    auth.set_access_token("ACCESS_KEY","ACCESS_SECRET")
    
    
    #Verify API
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    # api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    return api
