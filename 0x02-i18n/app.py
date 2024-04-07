#!/usr/bin/env python3
"""Creating a mock database
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config(object):
    """doc doc doc"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Return a user dict or None """
    id = request.args.get('login_as')
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """Function to execute before each is processed
    it retrieves the user and assigns it to the global variable g.user
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """ Return the locale pass in the agrument """
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Doc"""
    try:
        if request.args.get('timezone'):
            return pytz.timezone(request.args.get('timezone')).zone
        if g.user and g.user.get('timezone'):
            return pytz.timezone(g.user['timezone']).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return 'UTC'


@app.route('/')
def index():
    """Return the home page"""
    from datetime import datetime
    from flask_babel import format_datetime

    current_time = format_datetime(datetime.utcnow())
    return render_template('index.html', current_time=current_time)


if __name__ == "__main__":
    app.run()
