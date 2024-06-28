from flask import Flask
from .config import Config
from .routes import main
from .oauth import oauth
from .models import init_db  # Import init_db function

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():  # Ensure application context
        init_db(app)  # Pass app instance to init_db function

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(oauth)

    return app
