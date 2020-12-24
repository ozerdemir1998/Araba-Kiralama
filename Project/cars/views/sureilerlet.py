from flask import Blueprint, render_template
from Project.auth import *
from Project.model.database import Users, Cars, RentCars
from Project import db
from datetime import datetime, timedelta
from Project.cars.views.cars import teslimet_m

sureilerlet = Blueprint('sureilerlet',__name__,template_folder="../templates")

#süre ilerlet page
@sureilerlet.route("/sureyiilerlet")
@login_required
@admin_control
def sureilerlet_m():
        userCars = db.session.query(
            Cars, Users, RentCars,
        ).filter(
            Cars.id == RentCars.carId,
        ).filter(
            Users.id == RentCars.userId,
        ).all()
        return render_template("sureyiilerlet.html",userCars = userCars)        

#süre ilerle
@sureilerlet.route("/sureilerle/<string:id>")
@login_required
@admin_control
def sureilerle(id):
    rentCars = RentCars.query.filter_by(id = id).first()
    carId = rentCars.carId
    rentDate = rentCars.rentDate

    new_date = rentDate - timedelta(days = 1)
    back_time = datetime.today() - timedelta(days = 7)
    
    if new_date < back_time:
        teslimet_m(carId)
        return redirect(url_for("cars.cars_m"))
    else:
        rentCars.rentDate = new_date
        db.session.commit()
        flash("Teslim saati 1 gün ilerletildi.","success")
        return redirect(url_for("cars.cars_m"))