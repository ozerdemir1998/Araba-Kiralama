from flask import Blueprint, render_template, redirect
from Project import db, app
from sqlalchemy import func
from Project.model.database import Cars

home = Blueprint('home',__name__,template_folder="templates")

@home.route("/")
def index_m():
    max_car = db.session.query(func.max(Cars.kiralanmaSayisi))
    data = Cars.query.filter_by(kiralanmaSayisi = max_car).all()
    return render_template("index.html",data = data)