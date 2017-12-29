from twitter_bot import TwitterBot

def test_TwitterBot():
    bot = TwitterBot()
    assert bot != None, "Check twitter env variables"

def test_search_tweets():
    bot = TwitterBot()
    searches=bot.api.GetSearch('BTC',count=1)
    print("[o] Searching twitter for BTC")
    print(searches[0].text)
    
