from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_user import UserManager
from flask_mail import Mail

login_manager = LoginManager()
db = SQLAlchemy()
admin = Admin()
mail = Mail()

def create_app(config_name='config.py'):

    app = Flask(__name__)

    # Lee la configuración desde el archivo config.py
    app.config.from_pyfile(config_name)

    login_manager.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    from .restricted.routes import MyAdminIndexView
    admin.init_app(app, index_view=MyAdminIndexView())

    from .auth.models import User
    user_manager = UserManager(app, db, User)

    # Registro de los BluePrints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .errors import errors_bp
    app.register_blueprint(errors_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)

    from .restricted import restricted_bp
    app.register_blueprint(restricted_bp)

    return app