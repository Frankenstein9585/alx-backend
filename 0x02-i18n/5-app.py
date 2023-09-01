#!/usr/bin/env python3
"""Flask Application"""
from typing import Dict

from babel import Locale
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)

babel = Babel(app)


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

SUPPORTED_LOCALES = ['en', 'fr']


@babel.localeselector
def get_locale() -> str:
    """get_locale() method"""
    locale = request.args.get('locale')
    if locale and locale in SUPPORTED_LOCALES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Dict | None:
    """Returns a user dictionary if user ID is found"""
    user_id = request.args.get('login_as')
    if not user_id:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """This runs before all other functions"""
    g.user = get_user()


@app.route('/')
def index() -> str:
    """Index Route"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
