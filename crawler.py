import json

import tweepy as tw


def initialize_twitter_api():
    """Return an object from which we can later make calls to the Twitter API.

    :return: The Twitter API object
    """

    keys_json = open('config/keys.json', 'r').read()
    keys = json.loads(keys_json)

    consumer_key = keys['consumer_key']
    consumer_secret_key = keys['consumer_secret_key']
    access_token = keys['access_token']
    access_secret_token = keys['access_secret_token']

    auth = tw.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_secret_token)
    api = tw.API(auth, wait_on_rate_limit=True)

    return api


def get_tweets(to_search: str, count: int):
    """Return a list of tuples each containing a tweet's location and text,
    that contains the hashtag <to_search> and is of <count> size.

    :param to_search: A hashtag.
    :param count: A natural number.
    :return: A list of (tweet_location, tweet_text) tuples.
    """

    api = initialize_twitter_api()
    tweets_list = list()

    for tweet in tw.Cursor(api.search, q=to_search, geocode='51.51702,-0.12701,10000km', lang='en',
                           tweet_mode='extended', since='2020-12-01', result_type='recent').items(count):
        if tweet._json['user']['location'] == '':
            pair = ('California', tweet._json['full_text'])
        else:
            pair = (tweet._json['user']['location'], tweet._json['full_text'])
        tweets_list.append(pair)

    return tweets_list
