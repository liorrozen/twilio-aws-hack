from twython import Twython


class Tweets():
    APP_KEY = "17m7fv2ydjEFr0WaQrZhbw"
    APP_SECRET = "ffZ63hQ9K1UM6FOpU6cDqMUvLQjlPttKDzBapGDKQU"
    ACCESS_TOKEN = None

    api = None

    def __init__( self ):
        self.api = Twython( self.APP_KEY, self.APP_SECRET, oauth_version = 2 )
        self.ACCESS_TOKEN = self.api.obtain_access_token()
        self.api = Twython( self.APP_KEY, access_token = self.ACCESS_TOKEN )

    def find_one( self, query ):
        return self.api.search( q = "#" + query )[ "statuses" ][ 0 ]
