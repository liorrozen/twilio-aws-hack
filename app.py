from flask import Flask, request
import twilio.twiml

from hashtag import Tweets

app = Flask(__name__)

tweets = hashtag.Tweets()

@app.route( "/voice/", methods = [ "GET", "POST" ] )
def hello_monkey():
    """Respond to incoming requests."""

    resp = twilio.twiml.Response()

    g = resp.gather( numDigits = 1, action = "/handle-key", method = "POST" )
    g.say( "For hashtag A.W.S., press 1" )
    g.pause( length = 1 )
    g.say( "For hashtag twilio, press 2" )

    return str( resp )


@app.route( "/handle-key", methods = [ "GET", "POST" ] )
def handle_key():

    resp = twilio.twiml.Response()
    digit_pressed = request.values.get( "Digits", None )

    tweet = {
        "1" : tweets.find_one( "aws" ),
        "2" : tweets.find_one( "twilio" )
    }[ digit_pressed ]

    text = tweet[ "text" ]

    resp.say( "The latest tweet for your selection is: %s" % text )

    return str( resp )

if __name__ == "__main__":
    app.run( host = "0.0.0.0", debug = True, port = 1337 )
