from flask import Flask, request, url_for
import twilio.twiml
app = Flask(__name__)


@app.route("/")
def home():
    return "It's ALIVE!?"


@app.route("/voice/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()

    # resp.say("W.T.F?")

    # return str(resp)

    snd_file = url_for('static', filename='mario.mp3')
    resp.play( snd_file )
    g = resp.gather( numDigits = 1, action = "/handle-key", method = "POST" )
    g.say( "For foo press 1" )
    g.pause( length = 2 )
    g.say( "For bar press 2" )

    return str(resp)


@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():

    resp = twilio.twiml.Response()
    digit_pressed = request.values.get('Digits', None)

    resp.say( "You pressed %s" % digit_pressed )

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=1337)
