# extracting info from the twitter API
# steam sales and webscrape every single web page (including wiki)
from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener # This is downloaded
import time 

#consumer key, consumer secret, access token, access secret
ckey='7hJsTCHYsi6dio5jkZIeWJiUB'
csecret='u6uLp27eITMGv3EbZf4VbgABI7NDRGq9zyYP4i7yXgjU1c6hRr'
atoken='481343324-WonDjGMVzjxxUDbY8rfSbjOzoxM0cScoJybqZLjc'
asecret='198CSXoYVi30s9NurkppiWPkUgDVBT9NRWbUNWWKuB3MJ'

# define your listener class 

class listener(StreamListener):  

	def on_data(self, data):
		try: # This is to trim the data, try and except look 
			print (data)

			tweet = data.split (', "text":"') [1]. split('","source"') #JSON Format
			print (tweet)
			saveThis=str(time.time()+'::::' + tweet ) # safest, not a comma because it's highlily likely that people are going to put a colon
			saveFile = open ('twitDB2.csv','a')
			saveFile.write (saveThis)
			saveFile.write ('\n')
			saveFile.close ()
			return (True)
		 except (BaseException), e: # don't stream twitter on wireless dumbass
			print 'failed ondata,',str(e)
			time.sleep(5)

	def on_error(self,status):
		print (status)

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken, asecret)
twitterStream= Stream (auth, listener ()) # referring to line 12
twitterStream.filter (track=["niantic labs"]) # you are streaming at least 8x the data you need
# Open and you can edit it with notepad. 
