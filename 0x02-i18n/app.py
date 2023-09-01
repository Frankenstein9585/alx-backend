#!/usr/bin/env python3
"""Flask Application"""
from datetime import datetime
from typing import Dict

from babel import Locale
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, exceptions, utc

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
def get_locale():
    """get_locale() method"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    locale = request.headers.get('locale', None)
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Dict | None:
    """Returns a user dictionary if user ID is found"""
    user_id = request.args.get('login_as')
    if not user_id:
        return None
    return users.get(int(user_id))


@babel.timezoneselector
def get_timezone():
    """this function get timezone for the locale"""
    default_time_zone = app.config['BABEL_DEFAULT_TIMEZONE']
    local_time_zone = request.args.get('timezone', None)
    if local_time_zone:
        try:
            return timezone(local_time_zone).zone
        except exceptions.UnknownTimeZoneError:
            return default_time_zone
    if g.user:
        try:
            local_time_zone = g.user.get('timezone')
            return timezone(local_time_zone).zone
        except exceptions.UnknownTimeZoneError:
            return default_time_zone
    return request.accept_languages.best_match(default_time_zone)


@app.before_request
def before_request():
    """This runs before all other functions"""
    g.user = get_user()
    utc_now = utc.localize(datetime.utcnow())
    g.current_time = utc_now.astimezone(timezone(get_timezone()))


@app.route('/')
def index() -> str:
    """Index Route"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
