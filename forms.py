from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, FloatField, EmailField
from wtforms.validators import validators

class UserForm(Form):
    matricula = StringField("Matricula", [
        validators.DataRequired(message='El campo es requerido'),
        validators.lenght(min=3, max=10, message='El campo debe tener entre 3 y 10 caracteres.')
    ])
    nombre = StringField("Nombre")
    apellido = StringField("Nombre")
    email = EmailField("Correo", [
        validators.Email(message='Ingrese un correo válido')
    ])