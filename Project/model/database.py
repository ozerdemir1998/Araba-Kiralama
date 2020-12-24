from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from Project import app, db
import os
from datetime import datetime


class Users(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    username = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    kiralikAracSayisi = db.Column(db.Integer)

class Cars(db.Model):
    __tablename__="cars"
    id = db.Column(db.Integer, primary_key=True)
    carName = db.Column(db.String(80))
    carAge = db.Column(db.String(4))
    carDetail = db.Column(db.String(100))
    carImage = db.Column(db.String(100))
    isRent = db.Column(db.Boolean)
    kiralanmaSayisi = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)

class RentCars(db.Model):
    __tablename__="rentcars"
    id = db.Column(db.Integer, primary_key=True)
    rentDate = db.Column(db.DateTime, default=datetime.utcnow)
    carId = db.Column(db.Integer, ForeignKey('cars.id'))
    userId = db.Column(db.Integer, ForeignKey('users.id'))
    