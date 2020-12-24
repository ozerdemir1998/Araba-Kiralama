from flask import Blueprint, render_template, request, flash
from Project.model.database import Cars, Users, RentCars
from Project.model.FormModel import carForm
from Project import db
from datetime import datetime, timedelta
from Project.auth import *
import os

cars = Blueprint('cars',__name__,template_folder="../templates")

#araç listesi
@cars.route("/cars")
def cars_m():
    cars_data = Cars.query.all()
    return render_template("cars.html",cars_data = cars_data)

#araba ekleme
@cars.route("/addcar",methods=["GET","POST"])
@login_required
@admin_control
def addcar_m():
    form = carForm(request.form)
    if request.method == "POST" and form.validate():
        carName = form.carName.data
        carAge = dict(form.carAge.choices).get(form.carAge.data)
        carDetail = form.carDetail.data

        if form.carImage.name not in request.files:
            flash("Lütfen araç resmi ekleyin.","danger")
            return redirect(url_for("cars.addcar_m"))
        form.carImage.name = request.files[form.carImage.name]
        path = os.path.join(app.config['UPLOAD_FOLDER'], form.carImage.name.filename)
        f=form.carImage.name.filename
        form.carImage.name.save(path)

        cars_data = Cars(carName = carName, carAge = carAge, carDetail = carDetail, carImage = f, isRent = False, kiralanmaSayisi = 0, date = datetime.today())
        db.session.add(cars_data)
        db.session.commit()

        flash("Araba başarıyla eklendi.","success")
        return redirect(url_for("cars.cars_m"))
    return render_template("addcar.html",form = form)


#araç kiralama
@cars.route("/kirala/<string:carId>")
@login_required
def kirala_m(carId):

    users = Users.query.filter_by(id = session["userId"]).first()
    if users:
            if users.kiralikAracSayisi >= 3:
                flash("Bir kullanıcı en fazla 3 araç kiralayabilir.","danger")
                return redirect(url_for("cars.mycars_m"))
            else:
                cars_data = Cars.query.filter_by(id = carId).first()
                if cars_data.isRent == 1:
                    flash("Aracı kiralayamazsınız, bu araç zaten kiralanmış.","danger")
                    return redirect(url_for("home.index_m"))
                else:
                    rentcars = RentCars(userId = session["userId"], carId = carId, rentDate = datetime.today())
                    db.session.add(rentcars)
                    
                    cars_data.isRent = True
                    users.kiralikAracSayisi +=1
                    cars_data.kiralanmaSayisi +=1
                    db.session.commit()

                    flash("Araba başarıyla kiralandı.","success")
                    return redirect(url_for("cars.mycars_m"))
    else:
        flash("Araba kiralama işlemi yapılamadı.","danger")
        return redirect(url_for("home.index_m"))

#araç teslim et
@cars.route("/teslimet/<string:carId>")
@login_required
def teslimet_m(carId):
    
    rentcars = RentCars.query.filter_by(carId = carId).first()
    db.session.delete(rentcars)

    cars_data = Cars.query.filter_by(id = carId).first()
    cars_data.isRent = False

    users = Users.query.filter_by(id = rentcars.userId).first()
    users.kiralikAracSayisi -=1

    db.session.commit()

    flash("Araba başarıyla teslim edildi.","success")
    return redirect(url_for("cars.mycars_m"))


#kiraladığım araçlar
@cars.route("/mycars")
@login_required
def mycars_m():
        mycars = db.session.query(Cars, RentCars).join(RentCars).filter(Cars.id == RentCars.carId, RentCars.userId == session["userId"]).all()
        days = datetime.today() - timedelta(days=7)
        return render_template("mycars.html",mycars = mycars, days = days)

#araba sil
@cars.route("/deletecar/<string:carId>")
@login_required
@admin_control
def deletecar_m(carId):
    cars_data = Cars.query.filter_by(id = carId).first()
    if cars_data:
        path = os.path.join(app.config['UPLOAD_FOLDER'], cars_data.carImage)
        os.remove(path)
        db.session.delete(cars_data)

    rentcars = RentCars.query.filter_by(carId = carId).first()
    if rentcars:
        db.session.delete(rentcars)

    db.session.commit()
    flash("Araç başarıyla silindi.","success")
    return redirect(url_for("cars.cars_m"))

