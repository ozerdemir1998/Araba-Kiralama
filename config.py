from Project import app, db

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(dir_path, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY="arackiralama"
    UPLOAD_FOLDER = 'Project/static/images/'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True