#!/usr/bin/env python
# encoding: utf-8

import tweepy
import csv
from textblob import TextBlob


#Twitter API credentials
yadayadayada

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('tweets.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q="#$VWO",count=1000000,\
                           lang="en",\
                           since_id=2018-01-01).items():
    print tweet.created_at, tweet.text,tweet.retweet_count, 
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.retweet_count,])
    
    
    #only prints out 20 in past 7 days due to API rate limits  :/

print("THIS IS A HUGGGE AMOUNT OF DATA")    

# sentiment 
for tweet in tweepy.Cursor(api.search,q="#$VWO",count=1000000,\
                           lang="en",\
                           since_id=2018-01-01).items():
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
