from reddit_bot import RedditBot

def test_obtain_posts():
    bot = RedditBot()
    iota = bot.api.subreddit('Iota')
    print("[o] Getting 5 submissions from r/IOTA")
    for submission in iota.hot(limit=5):
        print(submission.title)
    assert len(submission.title) > 0
    