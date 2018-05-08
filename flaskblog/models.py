import os
import secrets

from PIL import Image

from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin
from flaskblog import app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.png')
    password = db.Column(db.String(60), nullable=False)

    # One to many
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    @staticmethod
    def save_profile_picture(form_picture, resize=True):
        # rename file
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(form_picture.filename)
        picture_fn = random_hex + f_ext

        # root path
        picture_path = os.path.join(
            app.root_path, 'static/profile_pics', picture_fn)

        if resize:
            output_size = (125, 125)
            i = Image.open(form_picture)
            i.thumbnail(output_size)
            i.save(picture_path)
        else:
            form_picture.save(picture_path)

        return picture_fn


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    # One to one (belongs to)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
