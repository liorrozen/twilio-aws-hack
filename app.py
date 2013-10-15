from flask import Flask, request
import twilio.twiml
import hashtag
app = Flask(__name__)

import hashtag
from hashtag import Tweets

tweets = hashtag.Tweets()


@app.route("/voice/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""

    resp = twilio.twiml.Response()

    g = resp.gather( numDigits = 1, action = "/handle-key", method = "POST" )
    g.say( "For hashtag A.W.S., press 1" )
    g.pause( length = 1 )
    g.say( "For hashtag twilio, press 2" )

    return str(resp)


@app.route( "/handle-key", methods=[ "GET", "POST" ] )
def handle_key():

    resp = twilio.twiml.Response()
    digit_pressed = request.values.get( "Digits", None )

    if digit_pressed == "1":
        tweet = tweets.find_one( "aws" )

    if digit_pressed == "2":
        tweet = tweets.find_one( "twilio" )

    text = tweet[ "text" ]

    resp.say( "The latest tweet for your selection is: " + text )

    return str(resp)

if __name__ == "__main__":
    app.run( host = "0.0.0.0", debug = True, port = 1337 )
