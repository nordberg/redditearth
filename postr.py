from __future__ import print_function
from twython import Twython
import praw
import time
import datetime
import requests
import os

APP_KEY = ''  # Customer Key here
APP_SECRET = ''  # Customer secret here
OAUTH_TOKEN = ''  # Access Token here
OAUTH_TOKEN_SECRET = ''  # Access Token Secret here

r = praw.Reddit(user_agent='EarthPornLurker')
if os.path.isfile('subm_pic.jpg'):
	os.remove('subm_pic.jpg')
while True:
	top_subm = r.get_subreddit('EarthPorn').get_top_from_week(limit=10)
	for subm in top_subm:
		if 'reddit.com' not in subm.url:
			if 'imgur' in subm.url:
				status_to_post = '%s %s %s' %(subm, subm.url, '#EarthPorn')
				twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
				r = requests.get(subm.url)
				with open('subm_pic.jpg', 'a') as the_file:
					the_file.write(r.content)
				image_open = open('subm_pic.jpg', 'r')
				image_ids = twitter.upload_media(media=image_open)
				twitter.update_status(status=str(status_to_post), media_ids=image_ids['media_id'])
				print('Posted to twitter')
				print('Sleeping %s' %str(datetime.datetime.now()))
				time.sleep(60)
				break			