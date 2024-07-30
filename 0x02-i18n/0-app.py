#!/usr/bin/env python3
"""
Module for a Basic Flask app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Renders the 0-index.html page with a title and a header

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
