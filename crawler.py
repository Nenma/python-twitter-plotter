import tweepy as tw
import json
import re

keys_json = open('config/keys.json', 'r').read()
keys = json.loads(keys_json)

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET_KEY = keys['consumer_secret_key']
ACCESS_TOKEN = keys['access_token']
ACCESS_SECRET_TOKEN = keys['access_secret_token']

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tw.API(auth, wait_on_rate_limit=True)


def get_tweets(to_search, count):
    tweetsList = list()
    pattern = re.compile('^[a-zA-Z]+$')

    for tweet in tw.Cursor(api.search, q=to_search, lang='en', tweet_mode='extended', since='2020-12-01').items(count):
        if pattern.match(tweet._json['user']['location']) != None:
            pair = (tweet._json['user']['location'], tweet._json['full_text'])
            tweetsList.append(pair)
    return tweetsList


if __name__ == '__main__':
    for tweet in get_tweets('#news', 30):
        print(tweet)
        print()