#!/usr/bin/python3
"""
A script to start a flask web application-> 0.0.0.0:5000
Routes / -> "Hello HBNB!"
Routes /hbnb -> "HBNB"
Route /c/<text> -> returns "C {<text>}" (underscore-whitespace)
Route /python/<text> -> returns "Python {<text>}" (underscore-whitespace)
Route /number/<n>: -> “n is a number” only if n is an integer
Route /number_odd_or_even/<int:n>: -> “n is a even|odd" only if n is an
integer
strict_slashes = False
"""
from flask import Flask
from flask import render_template
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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def py_route(text="is cool"):
    """
    Function to be called under the router "/python/<text>"
    """

    new_text = text.replace("_", " ")
    return (f"Python {new_text}")


@app.route("/number/<int:n>", strict_slashes=False)
def num_route(n):
    """
    Function to be called under the router "/number/<int:n>"
    """
    return (f"{n} is a number")


@app.route("/number_template/<int:n>", strict_slashes=False)
def temp_route(n):
    """
    Function to be called under the router "/number_template/<int:n>"
    """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even_temp_route(n):
    """
    Function to be called under the router "/number_odd_or_even/<int:n>"
    """
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
