#!/usr/bin/python
import praw
import pdb
import re
import os
import time


reddit = praw.Reddit('bot1')

subreddits = ['pythonforengineers','funny']
pos=0

title = "Funny programmar joke"
url = "https://imgur.com/r/programmarhumor/5OUd8yZ"

def post():
	global subreddits
	global pos
	global errors
	
	try:
		subreddit = reddit.subreddit(subreddits[pos])
		subreddit.submit(title, url=url)
		print("Posted to "+ subreddits[pos])
		
		pos=pos+1
		
		if(pos<=len(subreddits)-1):
		   post()
		else:
			print "Done"
		
	except praw.exceptions.APIException as e:
		if(e.error_type=="RATELIMIT"):
		   delay=re.search("(\d+) minutes",e.message)
		   
		   if delay:
		   		delay_seconds=float(int(delay.group(1))*60)
		   		time.sleep(delay_seconds)
		   		post()
		   else:
		   		delay=re.search("(\d+) seconds",e.message)
		   		delay_seconds=float(delay.group(1))
		   		time.sleep(delay_seconds)
		   		post()
	except:
		errors=errors+1
		if(errors>5):
			print("Crashed")
		

		
post()

