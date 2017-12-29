from twitter_bot import TwitterBot

def test_TwitterBot():
    bot = TwitterBot()
    assert bot != None, "Check twitter env variables"
