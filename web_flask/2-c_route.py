#!/usr/bin/python3
"""
script that starts a Flask web apllication
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    return Hello HBNB
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """
    returns a text message
    """
    text = text.replace("_", " ")
    return "c {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
