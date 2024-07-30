#!/usr/bin/env python3
"""
Module for a Basic Flask app with Babel setup and mock login
"""

from flask_babel import Babel, _
from flask import Flask, render_template, request, g
from typing import Union, Dict


class Config:
    """Configuration class for Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Mock function to retrieve a user based on login_as parameter.

    Returns:
        dict or None: User dictionary or None if not found or not logged in.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Function to run before each request to set the user.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match with supported languages.

    Checks if the request has a locale parameter and uses it if valid.
    Otherwise, uses the best match from the Accept-Language header.

    Returns:
        str: Locale to use for the request.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Renders the index.html page with a title and a header.

    Returns:
        str: Rendered HTML content of the index page.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
