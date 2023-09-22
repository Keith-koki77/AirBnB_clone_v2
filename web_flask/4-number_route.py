#!/usr/bin/python3
"""
script that starts a Flask web application
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
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythontext(text='is cool'):
    """
    returns python followed by <text>
    Replaces underscores with slashes
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays number 'n' only if it's an integer
    """
    return '{:d} is a number'.format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
