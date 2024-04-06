#!/usr/bin/env python3
"""Instantiate Babel object in app"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """The configuration class for babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """Return 1-index.html home page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
