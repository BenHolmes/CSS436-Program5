from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():

    return "Hello, World!" + function()


def function():
    return "what is up"

