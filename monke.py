import tweepy
import praw
from credentials import *

tw_auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
tw_auth.set_access_token(twitter_access_token, twitter_access_token_secret)
tw_api = tweepy.API(tw_auth)

my_reddit = praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, user_agent=reddit_user_agent)

sub_name = 'monke'

# use r/<hashtag> for reddit search
# and #<hashtag> for instagram search
hashtag = 'monke'
num_posts = 1

# tweet reddit info
reddit_posts = my_reddit.subreddit(hashtag).new(limit=num_posts)
for submission in reddit_posts:
 title = submission.title
 url = 'www.reddit.com{}'.format(submission.permalink) 
 tweet_str = "Hello, this is my first tweet!"
 tw_api.update_status(tweet_str)