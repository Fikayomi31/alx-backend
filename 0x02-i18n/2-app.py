#!/usr/bin/env python3
""" function with the babel.localeselector decorator
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """The configuration class for babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Return best match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Return home page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
