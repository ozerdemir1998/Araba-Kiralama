from flask import Flask,session,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object(os.environ.get('APP_SETTINGS') or 'config.ProductionConfig')

from .home.home import home
from .users.register import register
from .users.login import login
from .users.users import users
from .cars.views.cars import cars
from .cars.views.sureilerlet import sureilerlet
from .cars.views.arama import arama


app.register_blueprint(home)

app.register_blueprint(users)
app.register_blueprint(register)
app.register_blueprint(login)

app.register_blueprint(cars)
app.register_blueprint(sureilerlet)
app.register_blueprint(arama)


