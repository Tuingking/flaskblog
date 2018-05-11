from flask import Flask
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail

from flaskblog.config import config
from flaskblog.constants import SQLALCHEMY_METADATA_CONVENTION

metadata = MetaData(naming_convention=SQLALCHEMY_METADATA_CONVENTION)

# Initialize flask extention
db = SQLAlchemy(metadata=metadata)
bcrypt = Bcrypt()
moment = Moment()
login_manager = LoginManager()
login_manager.login_view = 'users.login'        # same like url_for('login')
login_manager.login_message_category = 'info'   # info is bootstrap class
mail = Mail()


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Bind extention to app
    db.init_app(app)
    bcrypt.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Register blueprint
    from flaskblog.users.routes import users
    app.register_blueprint(users)
    from flaskblog.posts.routes import posts
    app.register_blueprint(posts)
    from flaskblog.main.routes import main
    app.register_blueprint(main)
    from flaskblog.errors.handlers import errors
    app.register_blueprint(errors)

    return app
