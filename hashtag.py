import twython
from twython import Twython


class Tweets():
    APP_KEY = "17m7fv2ydjEFr0WaQrZhbw"
    APP_SECRET = "ffZ63hQ9K1UM6FOpU6cDqMUvLQjlPttKDzBapGDKQU"
    ACCESS_TOKEN = None

    twitter = None

    def __init__( self ):
        self.twitter = Twython(self.APP_KEY, self.APP_SECRET, oauth_version=2)
        self.ACCESS_TOKEN = self.twitter.obtain_access_token()
        self.twitter = Twython(self.APP_KEY, access_token=self.ACCESS_TOKEN)

    def find_one( self, query ):
        return self.twitter.search( q = "#" + query )[ "statuses" ][0]
