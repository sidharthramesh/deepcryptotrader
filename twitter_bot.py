import twitter
from decouple import config

class TwitterBot(object):
    def __init__(self):
        """Provide the CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN and
        ACCESS_TOKEN_SECRET in the environment variables or a .env file"""
        self.api = twitter.Api(
            config('CONSUMER_KEY'),
            config('CONSUMER_SECRET'),
            config('ACCESS_TOKEN'),
            config('ACCESS_TOKEN_SECRET')
            )
        self.test_valid()

    def test_valid(self):
        try:
            user = self.api.VerifyCredentials()
            print('[+] Creadentials valid: {}'.format(user.name))
        except Exception as e:
            print('[-] Invalid Credentials: {}'.format(e))

bot = TwitterBot()
