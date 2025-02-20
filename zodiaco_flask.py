from flask import Flask, request, render_template
from wtforms import Form, StringField, IntegerField, RadioField, SubmitField
from wtforms.validators import InputRequired, NumberRange
from datetime import datetime

app = Flask(__name__)

animales_zodiaco = {
    0: "rata", 1: "buey", 2: "tigre", 3: "conejo", 4: "dragon",
    5: "serpiente", 6: "caballo", 7: "cabra", 8: "mono",
    9: "gallo", 10: "perro", 11: "cerdo"
}

class ZodiacoForm(Form):
    nombre = StringField("Nombre", validators=[InputRequired()])
    apellido_paterno = StringField("Apellido Paterno", validators=[InputRequired()])
    apellido_materno = StringField("Apellido Materno", validators=[InputRequired()])
    dia = IntegerField("Día", validators=[InputRequired(), NumberRange(1, 31)])
    mes = IntegerField("Mes", validators=[InputRequired(), NumberRange(1, 12)])
    anio = IntegerField("Año", validators=[InputRequired(), NumberRange(1900, 2100)])
    sexo = RadioField("Sexo", choices=[('H', 'Hombre'), ('M', 'Mujer')], validators=[InputRequired()])
    submit = SubmitField("Calcular")

@app.route("/", methods=["GET", "POST"])
def home():
    form = ZodiacoForm(request.form) 
    signo = None
    imagen = None
    mensaje = None

    if request.method == "POST" and form.validate():
        año = form.anio.data
        signo = animales_zodiaco[(año - 1912) % 12]
        imagen = f"/static/img/{signo}.jpg"

        fecha_nacimiento = datetime(año, form.mes.data, form.dia.data)
        hoy = datetime.today()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

        nombre_completo = f"{form.nombre.data} {form.apellido_paterno.data} {form.apellido_materno.data}"
        mensaje = f"Hola {nombre_completo}, tienes {edad} años."

    return render_template("zodiaco.html", form=form, zodiac_sign=signo, image_path=imagen, mensaje=mensaje)

if __name__ == "__main__":
    app.run(port=3000, debug=True)