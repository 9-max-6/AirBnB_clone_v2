#!/usr/bin/python3
""" Script to load all the cities of a State"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def get_cities_by_states():
    """the actor function to be called at
    ath this particular endpoint"""
    all_states = storage.all('State')
    return (render_template('8-cities_by_states.html', states_json=all_states))


@app.teardown_appcontext
def tear_context(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
