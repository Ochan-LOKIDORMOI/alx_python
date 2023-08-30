#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root path.

    Returns:
        str: The message "Hello HBNB!"
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    """
    Main entry point of the application.
    Starts the Flask development server.
    """
    app.run(host='0.0.0.0', port=5000)
