# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 18:22:08 2016

@author: selva
"""
import json
from dateutil import parser
if __name__=='__main__':
    tweets=[]    
    tweets_time=[]
    with open("tweet_search_India.json","r") as json_file:
        json_object=json.load(json_file)
    for tweet in json_object:
        tweets.append(tweet['text'])
        time=tweet["created_at"]
        dt = parser.parse(time)
        tme=dt.strftime("%d-%m-%Y")
        tweets_time.append((tweet['text'],tme))
    print tweets
    print tweets_time