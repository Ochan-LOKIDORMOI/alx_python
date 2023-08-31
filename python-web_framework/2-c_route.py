#!/usr/bin/python3
"""
Flask and imported from flask
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

#create the localhost
@app.route('/', strict_slashes=False)
def hello_hbnb():
# a defined function of hello_hbnb to return a string
    return "Hello HBNB!"

#Dislocate the previous setting
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

#route created to the previous route setting
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    text = escape(text).replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
# activating the debug: ON
    app.run(debug=True)
