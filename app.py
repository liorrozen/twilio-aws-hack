import site
import sys
import os
import subprocess

subprocess.call( "cat pid.lock | xargs kill", shell = True )


full_path = os.path.realpath(__file__)
path, file = os.path.split(full_path)
site.addsitedir( path + '/site-packages' )

from flask import Flask, request
from twilio.twiml import Response
import twilio.twiml

from hashtag import Tweets

app = Flask(__name__)

tweets = Tweets()

current_pid = os.getpid()
lock_target = os.path.dirname( os.path.realpath( __file__ ) )
lock_target += "/pid.lock"
target = open( lock_target, "w" )
target.write( str( current_pid ) )
target.close()

@app.route( "/voice/", methods = [ "GET", "POST" ] )
def hello_monkey():
    """Respond to incoming requests."""

    resp = Response()

    g = resp.gather( numDigits = 1, action = "/handle-key", method = "POST" )
    g.say( "For hashtag Tel Aviv, press 1" )
    g.pause( length = 1 )
    g.say( "For hashtag A.W.S., press 2" )
    g.pause( length = 1 )
    g.say( "For hashtag twilio, press 3" )

    return str( resp )


@app.route( "/handle-key", methods = [ "GET", "POST" ] )
def handle_key():

    resp = Response()
    digit_pressed = request.values.get( "Digits", None )

    tweet = {
        "1" : tweets.find_one( "telaviv" ),
        "2" : tweets.find_one( "aws" ),
        "3" : tweets.find_one( "twilio" )
    }[ digit_pressed ]

    text = tweet[ "text" ]

    resp.say( "The latest tweet for your selection is: %s" % text )

    return str( resp )

if __name__ == "__main__":
    app.run( host = "0.0.0.0", debug = True, port = 1337 )
