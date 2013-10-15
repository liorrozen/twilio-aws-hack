from flask import Flask, request
import twilio.twiml
app = Flask(__name__)


@app.route("/")
def home():
    return "It's ALIVE!!!!!"


@app.route("/voice/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()

    # resp.say("W.T.F?")

    # return str(resp)

    g = resp.gather( numDigits = 1, action = "/handle-key", method = "POST" )
    g.say( "For foo press 1" )
    g.say( "For bar press 2" )

    return str(resp)


@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
    digit_pressed = request.values.get('Digits', None)

    return str( "You pressed %s" % digit_pressed )

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=1337)
