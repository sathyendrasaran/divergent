# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:31:10 2016

@author: sathyendrasaran
"""

# pip install twython
from twython import Twython
import json
import sys
from pprint import pprint

#with open('gene_twitter_credentials.json', 'r') as f:
#    credentials = json.load(f)

# create your own app to get consumer key and secret
CONSUMER_KEY = "lpYZw7PE29VTskZe8FWXUI9Zn"
CONSUMER_SECRET = "l3p19ZX6b4ljP8AnoEpRGJI3AISEQx2058TGZ8P7GnSx1CHaH7"

def call_twitter_search_api(keyword):

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

    tweets = []
    for status in twitter.search(q='\"{}\"'.format(keyword),count=10000)['statuses']:
        user = status['user']['screen_name'].encode('utf-8')
        text = status['text'].encode('utf-8')
        #print user, ':', text
        #print
        tweets.append(status)
        #tweets.append(text)
        

    with open('tweet_search_{}.json'.format(keyword), 'w') as f:
        json.dump(tweets, f, indent=4)


call_twitter_search_api("Hillary")