from twython import Twython
import praw
import time
import datetime

APP_KEY = ''  # Customer Key here
APP_SECRET = ''  # Customer secret here
OAUTH_TOKEN = ''  # Access Token here
OAUTH_TOKEN_SECRET = ''  # Access Token Secret here

r = praw.Reddit(user_agent='EarthPornLurker')
while True:
	top_subm = r.get_subreddit('earthporn').get_top_from_hour(limit=3)
	for subm in top_subm:
		if 'reddit.com' not in subm.url:
				status_to_post = '%s %s' %(subm, subm.url)
				twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
				twitter.update_status(status=str(status_to_post))
				print 'Posted to twitter'
				print 'Sleeping %s' %str(datetime.datetime.now())
				time.sleep(60 * 60)
		break