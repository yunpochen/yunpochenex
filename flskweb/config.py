import os

basedir = os.path.abspath(os.path.dirname(__file__))

#SECRET KEY


SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KET'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
