import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # On Vercel, only /tmp is writable; point SQLite there when no DATABASE_URL is set.
    if not os.environ.get("DATABASE_URL") and os.environ.get("VERCEL"):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/egate.db"

    db.init_app(app)
    login_manager.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    from app.auth.routes import auth_bp
    from app.main.routes import main_bp
    from app.challenges.routes import challenges_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(challenges_bp)

    with app.app_context():
        db.create_all()

    return app
