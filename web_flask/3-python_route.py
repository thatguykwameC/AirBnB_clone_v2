#!/usr/bin/python3

"""This module starts a Flask web application."""

from markupsafe import escape
from flask import Flask

web_app = Flask(__name__)


@web_app.route("/", strict_slashes=False)
def home():
    """Returns a string to the homepage."""
    return "Hello HBNB!"


@web_app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Handles the /hbnb route."""
    return "HBNB"


@web_app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Returns Python followed by a text."""
    return f"C {escape(text.replace('_', ' '))}"


@web_app.route("/python/", strict_slashes=False)
@web_app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Returns Python followed by a text."""
    return f"Python {escape(text.replace('_', ' '))}"


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
