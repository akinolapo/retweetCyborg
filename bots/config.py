# retweetCyborgV2/bots/config.py
import tweepy
import logging
import os

def create_api():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("olTw7jBNhKwFmMFegs9QX1Amz",
    "A8tOOyAszr9aKzlI8qFMeENHAqJQJosIMoU6DCn8RacDCR7MUT")
    auth.set_access_token("1287921782545092610-hvLaUz2oxVIbV4XnjfU2QhmYrIpviP",
                      "GipJF0YfxMSpFZ6UxH8LGUynorOu3uKWi9aqscrzvI4bw")
    #Verify API
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    # api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    return api