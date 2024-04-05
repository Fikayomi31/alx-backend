#!/usr/bin/env python3
"""A simple flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


@app.route('/')
def index():
    """Return 0-index.html home page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)