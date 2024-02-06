#!/usr/bin/env python3
"""
- In this task, implement a way to force a particular locale by passing the
        locale=fr parameter to your app’s URLs.
- In your get_locale function, detect if the incoming request contains
        locale argument and ifs value is a supported locale, return it. If not
        or if the parameter is not present, resort to the previous default
        behavior.
- should be able to test different translations by visiting
        http://127.0.0.1:5000?locale=[fr|en].
"""

from flask import Flask, render_template, request
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
