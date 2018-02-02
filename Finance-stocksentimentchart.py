import sys
import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob 


#function for the percentage
def percentage(part,whole):
	return 100*Float(part)/float(whole)

#Twitter API credentials
consumer_key = "OMtzXiVSufYfpia0UxdZsBsWb"
consumer_secret = "4GdxHCrCJngyrQZhVflTzCv4zZEr3e7RJaGmwzToTeTYk6upnU"
access_token_key = "481343324-rppQzYvi0tp6GOW5Qxy3LUmi6zYbGVti4jZV1BLI"
access_token_secret = "1wk9IDdWwH8BGFnemsh7J74UH8O5rUJNU6658P9mQm5Y0"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)


api = tweepy.API(auth)

#This is cute, it's a pop up for your search term using the input function

searchTerm= input("Enter the keyword you want to search about: ")
noOfSearchTerms= int(input("Enter how many tweets you want to analyse: "))

tweets = tweepy.Cursor(api.search, q=searchTerm,lang="English").items(noOfSearchTerms) #Farsi/French

positive = 0
negative = 0
neutral = 0
polarity = 0
subjectivity= 0

for tweet in tweets:
	print(tweet.text)
	analysis=TextBlob(tweet.text)
	print(analysis)
	polarity += analysis.sentiment.polarity
	subjectivity += analysis.sentiment.subjectivity

	if (analysis.sentiment.polarity == 0):
		neutral +=1 
	elif (analysis.sentiment.polarity < 0.00):
		negative +=1
	elif (analysis.sentiment.polarity > 0.00):
		positive +=1
		
positive = percentage (positive,noOfSearchTerms)

neutral = percentage (neutral,noOfSearchTerms)

negative = percentage (negative,noOfSearchTerms)

positive = format(positive, '2f')
neutral = format(neutral, '2f')
negative = format(negative, '2f')

print("How people are reacting on" + searchTerm + "by analysing" + str(noOfSearchTerms) + "Tweets.")

if (polarity == 0):
	print("Neutral")
elif (polarity < 0):
	print ("Negative")
elif (polarity > 0):
	print ("Positive")

# 1 Create your labels, 2 define your sizes, 3 select your colours, 4 plot legend 5 plot title 
labels = ['Positive['+str(positive)+'%]', 'Neutral['+str(neutral)+'%]', 'Negative['+str(negative)+'%]']
sizes=[positive, neutral, negative]
colours['yellowgreen', 'gold','red']
patches, texts= plt.pie(sizes, colors=colours, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("How people are reacting on" + searchTerm + "by analysing" + str(noOfSearchTerms) + "Tweets.")
plt.axis('equal')
plt.show()

