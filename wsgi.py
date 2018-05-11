import os

from flaskblog import create_app
from flaskblog.config import Config

app = create_app('dev')

if __name__ == '__main__':
    app.run()
