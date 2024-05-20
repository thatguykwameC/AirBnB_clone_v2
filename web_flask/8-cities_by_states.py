#!/usr/bin/python3

"""This module runs a Flask web application."""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

web_app = Flask(__name__)
web_app.jinja_env.trim_blocks = True
web_app.jinja_env.lstrip_blocks = True


@web_app.teardown_appcontext
def teardown_session(_):
    """Closes current session"""
    storage.close()


@web_app.route("/cities_by_states", strict_slashes=False)
def get_cities_by_state():
    """Renders all the City objects by State objects in storage."""
    states = storage.all(State).values()

    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
