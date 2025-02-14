from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, FloatField, EmailField

class UserForm(Form):
    matricula = StringField("Matricula")
    nombre = StringField("Nombre")
    apellido = StringField("Nombre")
    email = EmailField("Correo")