#!/usr/bin/env python3
"""
- Creating a user login system.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instantiate and configure the Flask app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# Define get_user handler function
def get_user():
    """
    - function returns a user dictionary or None if the ID cannot be found or
        if login_as was not passed
    """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
        else:
            return None


# Define a before_request handler function
@app.before_request
def before_request():
    """Find a user if any, and set it as a global on flask.g.user"""
    user = get_user()
    if user:
        g.user = user


@babel.localeselector
def get_locale():
    """Get locale from request"""
    locale_request = request.args.get('locale')
    if locale_request and locale_request in app.config['LANGUAGES']:
        return locale_request

    """Determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """Returns a string"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
