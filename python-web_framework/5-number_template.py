#!/usr/bin/python3

"""
Flask and importing from flask
"""
from flask import Flask
from markupdown import escape
from flask import template_render

app = Flask(__name__)

#route created at the localhost
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

#Dislocating the previous setting
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

#creating route
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    text = escape(text).replace('_', ' ')
    return f"C {text}"

#creating the previous text using app route
@app.route('/python/<text>',strict_slashes=False)
def python_with_text(defaults="is cool"):
    text = escape(text).replace('_', ' ')
    return f"Python {text}"

# route created to by-pass the previous setting
@ap.route('/number/<n>', strict_slashes=False)
def n_integer(n):
    return template_render("5-number.html", n=n)


if __name__ == "__main__":
# activating the debug: ON
    app.run(debug=True)

