import praw
from decouple import config
class RedditBot(object):
    def __init__(self):
        self.api = praw.Reddit(client_id=config('REDDIT_ID'),
                     client_secret=config('REDDIT_SECRET'), password=config('REDDIT_PASSWORD'),
                     user_agent=config('REDDIT_USERAGENT'), username=config('REDDIT_USERNAME'))


