#!/usr/bin/python3
"""
A script to start a flask web application-> 0.0.0.0:5000
Routes / -> "Hello HBNB!"
Routes /hbnb -> "HBNB"
Route /c/<text> -> returns "C {<text>}" (underscore-whitespace)
strict_slashes = False
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Function to be called under the route "/"
    """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Function to be called under the router "/hbnb"
    """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
    Function to be called under the router "/c/<text>"
    """

    new_text = text.replace("_", " ")
    return (f"C {new_text}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
