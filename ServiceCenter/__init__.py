import os

from flask import Flask


def create_app(test_config=None):
    # Create and configure the app.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="ServiceCenter",
        DATABASE=os.path.join(app.instance_path, 'ServiceCenter.sqlite')
    )

    # Load the instance config, if it exists.
    app.config.from_pyfile('config.py', silent=True)

    # Ensure the instance folder exists.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
