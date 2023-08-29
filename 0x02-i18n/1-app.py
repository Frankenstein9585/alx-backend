#!/usr/bin/env python3
"""Flask Application"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config:
    """Config class"""
    LANGUAGES = ['en', 'es']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """Index Route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=5000)
