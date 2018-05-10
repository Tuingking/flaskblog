import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '700517db4bdbce253020d799be8c11c8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
moment = Moment(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'  # same like url_for('login')
login_manager.login_message_category = 'info'  # info is bootstrap class

# Mail config
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = '587'
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_USERNAME'] = 'courtesyna@gmail.com'
app.config['MAIL_PASSWORD'] = '890ApPle.com'
mail = Mail(app)


from flaskblog import routes
