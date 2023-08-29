#!/usr/bin/env python3
"""Flask Application"""
from babel import Locale
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)

babel = Babel(app)


class Config:
    """Config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

SUPPORTED_LOCALES = ['en', 'fr']


@babel.localeselector
def get_locale():
    """get_locale() method"""
    locale = request.args.get('locale')
    if locale and locale in SUPPORTED_LOCALES:
        return Locale(locale)
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Index Route"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port=5000)
