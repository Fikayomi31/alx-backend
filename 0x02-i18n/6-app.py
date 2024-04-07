#!/usr/bin/env python3
"""Creating a mock database
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


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
    locale_url = request.args.get('locale')
    user_setting_locale = g.user.get('locale')
    locale_header = request.headers.get('Accept-Language')
    if locale_url in app.config['LANGUAGES']:
        return locale_url
    if (g.user and user_setting_locale in app.config['LANGUAGES']):
        return user_setting_locale
    if (locale_header and locale_header in app.config['LANGUAGES']):
        return request.accept_languages.best_match(app.config['LANGAUGES'])
    return app.config['LANGAUGES'][0]


@app.route('/')
def index():
    """Return the home page"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
