#!/usr/bin/python3

"""
Flask and imported from flask
"""
from flask import Flask

app = Flask(__name__)

#create the localhost
@app.route('/', strict_slashes=False)
def hello_hbnb():
# a defined function of hello_hbnb to return a string
    return "Hello HBNB!"

#create the route to dislocate the previous setting
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == "__main__":
# activating the debug: ON
    app.run(debug=True)
