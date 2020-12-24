from flask import Blueprint, render_template, request
from Project.model.FormModel import LoginForm
from passlib.hash import sha256_crypt
from Project.model.database import Users
from Project.auth import *

login = Blueprint('login',__name__,template_folder="../templates")

#giriş sayfası
@login.route("/login",methods = ["GET","POST"])
def login_m():
    form = LoginForm(request.form)

    if request.method == "POST":
        username = form.username.data
        password_entered = form.password.data  
        
        result = Users.query.filter_by(username = username).first()
        if result:
            real_password = result.password
            user_id = result.id
            if sha256_crypt.verify(password_entered,real_password):
                flash("Giriş başarılı.","success")

                session["logged_in"] = True
                session["username"] = username
                session["userId"] = user_id
                    
                return redirect(url_for("home.index_m"))
            else:
                flash("Girdiğiniz bilgileri kontrol edin.","danger")
                return redirect(url_for("login.login_m"))
        else:
            flash("Böyle bir kullanıcı bulunamadı.","danger")
            return redirect(url_for("login.login_m"))  
    else:
        return render_template("login.html",form = form)

#çıkış işlemi
@login.route("/logout")
def logout_m():
    session.clear()
    flash("Çıkış yaptınız.","info")
    return render_template("index.html")