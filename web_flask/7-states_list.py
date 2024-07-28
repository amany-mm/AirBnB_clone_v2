#!/usr/bin/python3
"""
A script that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """After each request, flask app call to remove the current SQLAlchemy
    Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Function that displays States"""
    states = storage.all(State).values()
    # sorted() returns a new sorted list from the elements of states
    # according to the name attribute of each state object in the list
    sorted_states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
