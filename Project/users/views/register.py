from flask import Blueprint, render_template, request
from Project.model.FormModel import RegisterForm
from passlib.hash import sha256_crypt
from Project import db
from Project.model.database import Users
from Project.auth import *

register = Blueprint('register',__name__,template_folder="../templates")

#kayıt sayfası
@register.route("/register",methods = ["GET","POST"])
def register_m():
    form = RegisterForm(request.form)

    if request.method=="POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        users = Users(name = name, username = username, email = email, password = password, kiralikAracSayisi = 0)
        db.session.add(users)
        db.session.commit()

        flash("Kayıt başarıyla gerçekleştirildi.","success")
        return redirect(url_for("login.login_m"))
    else:
        return render_template("register.html",form = form)
