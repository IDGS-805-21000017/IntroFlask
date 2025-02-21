from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, FloatField, EmailField
from wtforms.validators import InputRequired

class UserForm(Form):
    matricula = StringField("Matricula", validators=[InputRequired()])
    nombre = StringField("Nombre", validators=[InputRequired()])
    apellido = StringField("Nombre", validators=[InputRequired()])
    email = EmailField("Correo", validators=[InputRequired()])