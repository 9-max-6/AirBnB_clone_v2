#!/usr/bin/python3
"""
Web framework app to server static files.
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def serve_hbnb_filters():
    """
    server hbnb
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", len=len, states=states, amenities=amenities)


@app.teardown_appcontext
def tear_context(Exception):
    """A function to tear down the context
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
