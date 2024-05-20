#!/usr/bin/python3
"""This module runs a Flask web application."""

from models import storage
from flask import Flask
from flask import render_template

web_app = Flask(__name__)


@web_app.route("/states", strict_slashes=False)
def states():
    """Displays a page with a list of all States."""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@web_app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays a page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@web_app.teardown_appcontext
def teardown(exc):
    """Remove the current session."""
    storage.close()


if __name__ == "__main__":
    web_app.run(host="0.0.0.0")