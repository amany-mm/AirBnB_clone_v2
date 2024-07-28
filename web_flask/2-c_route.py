#!/usr/bin/python3
"""
A script that starts a Flask web application
listening on 0.0.0.0, port 5000
Routes:
- /: display “Hello HBNB!”
- /hbnb: display “HBNB”
- /c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
== You must use the option strict_slashes=False in your route definition
"""
from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Function that displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function that displays HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Function that displays C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
