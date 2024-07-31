#!/usr/bin/env python3
"""
Module for a Basic Flask app with Babel setup
Configurtions and translations set
"""

from flask_babel import Babel, _
from flask import Flask, render_template, request


class Config:
    """Configuration class for Flask app to translate different languages."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match with the supported languages
    based on the Accept-Language header.

    Returns:
        str: Locale selected based on the best match
        from the Accept-Language header.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    """
    Renders the index.html page with a title and a header.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
