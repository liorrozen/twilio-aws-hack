from flask import Flask, request
import twilio.twiml
app = Flask(__name__)


@app.route("/")
def home():
    return "It's ALIVE!!!!!"


@app.route("/voice/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    # resp = twilio.twiml.Response()
    # resp.say("Hello Monkey")
    # return str(resp)

    resp = twilio.twiml.Gather()
    ans = resp.say("Enter something")
    return str(ans)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=1337)
