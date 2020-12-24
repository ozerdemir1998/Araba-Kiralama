from wtforms import Form,StringField,TextAreaField,PasswordField,FileField,validators
from wtforms.validators import ValidationError, DataRequired
from passlib.hash import sha256_crypt
from wtforms import SelectField

#WTF kullanıcı kayıt formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim",validators=[validators.Length(min=5,max=30)])
    username = StringField("Kullanıcı Adı",validators=[validators.Length(min=5,max=25)])
    email = StringField("Email Adresi",validators=[validators.Email(message="Email geçerli bir email adresi girin.")])
    password = PasswordField("Parola",validators=[
        validators.DataRequired(message="Lütfen bir parola belirleyin"),
        validators.EqualTo(fieldname = "confirm",message="Parolanız uyuşmuyor.")
    ])
    confirm = PasswordField("Parola Doğrula")

#WTF kullanıcı giriş formu
class LoginForm(Form):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")

    #araba form
class carForm(Form):
    year_choises = [("1","2007"),("2","2008"),("3","2009"),("4","2010"),("5","2011"),("6","2012"),("7","2013"),("8","2014"),("9","2015"),("10","2016"),("11","2017"),("12","2018"),("13","2019"),("14","2020")]
    carName = StringField("Araba Marka ve Model",validators=[validators.Length(min=5,max=40)])
    carAge = SelectField("Araba Yıl", choices=year_choises, validate_choice=True)
    carDetail = TextAreaField("Araba Hakkında",validators=[validators.Length(min=10,max=80)])
    carImage = FileField("Araba Resim",_name='file1')
    
