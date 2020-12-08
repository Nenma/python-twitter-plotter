import tweepy as tw
import json

CONSUMER_KEY = 'pDyDjcwzNtFJHvAXHNJuhoPXk'
CONSUMER_SECRET_KEY = 'gy6edffCSdyrp1JY2WGoimrnS1HZ4ugJZxGaFBZLwA3c4O3kwj'
ACCESS_TOKEN = '1222796143-zlU5KHz0epkhpxQ3UAGxXgfaF0SFV2pdpHZs41C'
ACCESS_SECRET_TOKEN = 'W4X23DV12AJIpIVYzWfMTnlxKZbCcTj0d9KMIKHdXTxfb'

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tw.API(auth, wait_on_rate_limit=True)


def get_tweets():
    tweetsList = list()
    # filtering for the specified tweets
    return tweetsList


if __name__ == '__main__':
    get_tweets()