import os

from flask import Flask
from flask_bootstrap import Bootstrap


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

    # Add Bootstrap to the app.
    Bootstrap(app)

    # Import and initialize the DatabaseManager.
    from . import DatabaseManager
    DatabaseManager.init_app(app)

    # Import and register the AuthenticationManager (Blueprint).
    from . import AuthenticationManager
    app.register_blueprint(AuthenticationManager.bp)

    # Import and register the Dashboard (Blueprint).
    from . import Dashboard
    app.register_blueprint(Dashboard.bp)
    app.add_url_rule('/', endpoint='dashboard')

    return app
