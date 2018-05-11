import os
import secrets

from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture, resize=True):
    # rename file
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext

    # root path
    picture_path = os.path.join(
        current_app.root_path, 'static/profile_pics', picture_fn)

    if resize:
        output_size = (125, 125)
        i = Image.open(form_picture)
        i.thumbnail(output_size)
        i.save(picture_path)
    else:
        form_picture.save(picture_path)

    return picture_fn


def send_reset_email(user):
    """
    NOTE:
        if your gmail couldn't send an email, then:
        - Turn on less secure (https://myaccount.google.com/lesssecureapps?pli=1)
        - follow the step in https://www.google.com/accounts/DisplayUnlockCaptcha
        - for more https://support.google.com/mail/answer/7126229?visit_id=1-636616406666769328-657204447&rd=2#cantsignin
    """
    token = user.get_reset_token()
    msg = Message('Password reset request',
                  sender=current_app.config['APP_MAIL_SENDER'],
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request than simply ignore this email and no changes will be made.
'''
    mail.send(msg)


# def get_posts_data():
#     """get posts data from json file"""
#     SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
#     json_url = os.path.join(SITE_ROOT, 'static', 'posts.json')
#     data = json.load(open(json_url))

#     return data['posts']
