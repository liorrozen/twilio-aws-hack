from flask import Flask, render_template, jsonify, request
import twilio.twiml
app = Flask(__name__)

@app.route("/")
def home():
    return "It Works!"

@app.route("/voice/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")
    return str(resp)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=1337)
