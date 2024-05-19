#!/usr/bin/python3
""" Script to load all the cities of a State"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes = False)
def get_cities_by_states():
    """the actor function to be called at
    ath this particular endpoint"""
    all_states =  storage.all(State)
    states_json = get_json(all_states)
    tear_context()
    return (render_template(
        '8-cities_by_states.html',
        states_json=states_json))

def get_json(all_states=None):
    """custom function to create a json object for the template"""
    states_json = []
    if all_states:
        for state in all_states.values():
            new_dict = {}
            new_dict['state_name'] = state.__dict__['name']
            new_dict['state_id'] = state.__dict__['id']
            new_dict['cities'] = []
            for city in state.cities:
                new_city_dict = {}
                new_city_dict['name'] = city.__dict__['name']
                new_city_dict['id'] = city.__dict__['id']
                new_dict['cities'].append(new_city_dict)
            states_json.append(new_dict)
    return states_json

@app.teardown_appcontext
def tear_context():
    storage.close();


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
