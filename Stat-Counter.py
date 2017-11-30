# Analysis of a browser page in order to get the tbale on page 5.

import pandas as pd
import datetime
import matplotlib.pyplot as plt

#browser usage data form Statounter Global Stats

#\url{http://gs.statcounter.com/#browser-ww-monthly-200807-201410
#read in comma-delimited text fields

# read in csv file
browser_usage=pd.read_csv('browser_usage_2008_2014.csv')

#examine the data frame object 
print(browser_usage.shape)
print(browser_usage.head())


#identify the date fields as dates with apply aand lambda function
browser_usage['Date'] = \
browser_usage['Date']\
	.apply(lambda d: datetime.datetime.strptime(str(d), '%Y-%m'))

#define other category 
browser_usage['Other']= 100-\
browser_usage['IE'] - browser_usage['Chrome'] -\
browser_usage['Firefox'] -browser_usage['Safari']


#examine selected colums of the data frame object

selected_browser_usage= pd.DataFrame(browser_usage, 
	columns = ['Date', 'IE', 'Chrome', 'Firefox', 'Safari', 'Other'])
print(selected_browser_usage.shape)
print(browser_usage.head())

#create multiple time series plot
selected_browser_usage.plot(subplots=True, 
	sharex= True, sharey= True, style = 'k-')
plt.legend(loc= 'best')
plt.xlabel('')
plt.savefig('fig_broswer_mts_Python_pdf',
bbox_inches= 'tight', dpi= None, facecolor ='w', edgecolor ='b', orientation='portrait', papertype=None,
format=None, transparent=True, pad_inches=0.25, frameon=None)
