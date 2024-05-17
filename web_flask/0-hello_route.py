#!/usr/bin/python3
"""
A script to start a flask web application-> 0.0.0.0:5000
Routes / -> displays "Hello HBNB!"
strict_slashes = False
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False, )
def hello_word():
    """
    Function to be called under the route "/"
    """
    return ("Hello HBNB!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
