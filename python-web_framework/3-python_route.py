#!/usr/bin/python3

"""
This is the script that import from flask
"""
from flask import Flask
from markupsafe import escape

"""
Looking for resources from flask
"""
app = Flask(__name__)

"""
showing flask what URL it'll trigger
"""


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


#This format "/c/<text>/", it won't render in your browser rather it'll be 404
@app.route("/c/<text>/", strict_slashes=False)
def c(text):
    # replace all underscores with spaces
    return f"C {text.replace('_', ' ')}"


# added default parameter to be "is cool"
@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>")
def python(text):
    # replace all underscores with spaces
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
