import os


class Config:
    # App config
    SECRET_KEY = os.getenv('SECRET_KEY')

    # SQLAlchemy config
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail config
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('EMAIL_USER')
    MAIL_PASSWORD = os.getenv('EMAIL_PASS')

    APP_MAIL_SUBJECT_PREFIX = '[Flaskblog]'
    APP_MAIL_SENDER = 'Flaskblog <courtesyna@gmail.com>'
    APP_ADMIN = os.environ.get('FLASKBLOG_ADMIN')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/flaskblog'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,

    'default': DevelopmentConfig
}
