import tweepy as tw
import json

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

    for tweet in tw.Cursor(api.search, q=to_search, geocode='51.51702,-0.12701,10000km', lang='en', tweet_mode='extended', since='2020-12-01').items(count):
        if tweet._json['user']['location'] == '':
            pair = ('California', tweet._json['full_text'])
        else:
            pair = (tweet._json['user']['location'], tweet._json['full_text'])
        tweetsList.append(pair)
        # print(tweet._json['user']['location'])
    return tweetsList


if __name__ == '__main__':
    for tweet in get_tweets('#romania', 10):
        print(tweet)
        print()