from flask import Flask, request, url_for
import twilio.twiml
import hashtag
app = Flask(__name__)

from twitter import *


@app.route("/")
def home():

    # create twitter API object
    twitter = Twitter()

    # perform a basic search
    # twitter API docs: https://dev.twitter.com/docs/api/1/get/search
    query = twitter.search(q = "lazy dog")

    # print how quickly the search completed
    print "Search complete (%f seconds)" % (query["completed_in"])

    # loop through each of my statuses, and print its content
    for result in query["results"]:
        print "(%s) @%s %s" % (result["created_at"], result["from_user"], result["text"])


@app.route("/voice/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""

    resp = twilio.twiml.Response()

    g = resp.gather( numDigits = 1, action = "/handle-key", method = "POST" )
    g.say( "For hashtag aws, press 1" )
    g.say( "For hashtag twilio, press 2" )

    return str(resp)


@app.route( "/handle-key", methods=[ "GET", "POST" ] )
def handle_key():

    resp = twilio.twiml.Response()
    digit_pressed = request.values.get( "Digits", None )

    resp.say( "You pressed %s" % digit_pressed )

    return str(resp)

if __name__ == "__main__":
    app.run( host = "0.0.0.0", debug = True, port = 1337 )
