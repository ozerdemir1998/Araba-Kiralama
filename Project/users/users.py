from flask import Blueprint, render_template
from Project.auth import *
from Project.model.database import Users

users = Blueprint('users',__name__,template_folder="templates")

#kullanıcı listesi
@users.route("/users")
@login_required
@admin_control
def users_m():
    users_data = Users.query.all()
    return render_template("users.html",users_data = users_data)