#!/usr/bin/python3
"""
A flask web application
Routes
/states _> returns the lsit of state objects present in DB storage
/states<id> _> returns  all the cities of a particular state
"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def get_states():
    """
    return states
    """
    states = storage.all('State')
    return render_template('9-states.html', states_json=states, len=len)


@app.route('/states/<id>', strict_slashes=False)
def get_state_by_id(id):
    """A function to get state by id
    """
    states = storage.all('State')
    act_state = []
    print(id)
    for state in states.values():
        if state.id == id:
            act_state.append(state)
    
    return render_template('9-states.html', states_json=act_state, len=len)


@app.teardown_appcontext
def tear_context(Exception):
    """A function to tear down the context
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
