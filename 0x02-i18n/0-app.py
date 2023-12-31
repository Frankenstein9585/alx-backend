#!/usr/bin/env python3
"""Flask Application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Index Route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=5000)
