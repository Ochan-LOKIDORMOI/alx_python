#!/usr/bin/python3

"""
This script import from flask
"""
from flask import Flask
from markupsafe import escape

"""
Looking up resources
"""
app = Flask(__name__)

"""
Triggering the flask URL
"""


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>/", strict_slashes=False)
def c(text):
    # replace all underscores with spaces
    return f"C {text.replace('_', ' ')}"

@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>")
def python(text):
    # replace all underscores with spaces
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
