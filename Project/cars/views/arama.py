from flask import Blueprint, render_template, request, flash, redirect, url_for
from Project.model.database import Cars
from Project import db

arama = Blueprint('arama',__name__,template_folder="templates")

#filireli arama
@arama.route("/filitrearama",methods=["GET","POST"])
def filitrearama_m():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        search_type = request.form.get("searchType")

        if search_type == "carName":
            cars_data = Cars.query.filter(Cars.carName.like("%"+ keyword +"%"))
        else:
            cars_data = Cars.query.filter(Cars.carAge.like("%"+ keyword +"%"))
        
        if cars_data:
            return render_template("filitrearama.html",cars_data = cars_data)
        else:
            flash("Aranan araç bulunamadı.","warning")
            return redirect(url_for("arama.filitrearama_m"))
    return render_template("filitrearama.html")