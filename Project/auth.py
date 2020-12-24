
from flask import flash,redirect,url_for,session, render_template
from functools import wraps
from Project import app

#kullanıcı giriş decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntülemek için lütfen giriş yapın.","danger")
            return redirect(url_for("login.login_m"))
    return decorated_function

def admin_control(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session["username"] != "admin1":
            flash("Bu yetkiye sahip değilsiniz.","danger")
            return redirect(url_for("home.index_m"))
        else:
            return f(*args, **kwargs)
    return decorated_function
