from flask import Flask,render_template, request
import jinja2
import forms

app=Flask(__name__)

class Boleto:
    __precioBoleto: int = 12

    def __init__(self, nombre: str, numPersonas: int, cantidad: int, tieneTarjeta: bool):
        self.nombre = nombre
        self.numPersonas = numPersonas
        self.cantidad = cantidad
        self.tieneTarjeta = tieneTarjeta
        self.total = 0.0

    def validar_cantidad(self):
        max_boletos = self.numPersonas * 7
        if self.cantidad > max_boletos:
            return False, f"No se pueden comprar más de {max_boletos} boletos (7 por persona)."
        if self.cantidad < 1:
            return False, "La cantidad debe ser al menos 1."
        return True, ""

    def calcular_total(self) -> float:
        if self.cantidad > 5:
            self.total = self.__precioBoleto * self.cantidad * 0.85
        elif 3 <= self.cantidad <= 5:
            self.total = self.__precioBoleto * self.cantidad * 0.90
        else:
            self.total = self.__precioBoleto * self.cantidad

        if self.tieneTarjeta:
            self.total *= 0.9

        return self.total

@app.route("/")
def index():
    titulo="IDGS805"
    lista=["Pedro,juan,Mario"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")


@app.route("/Hola")
def hola():
    return "<h1>Hola mundooo</h1>"


@app.route("/user/<string:user>")
def user(user):
    return f"hola,{user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"El numeri es: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"El usuario es: {username} con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es: {n1+n2}"

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}"

@app.route("/form1")
def form1():
    return '''
            <form>
            <label for="nombre">Nombre:</label>
            </form>
    
           '''

@app.route("/page2")
def operas():
    return render_template("index.html", value=0, num1=1, num2=1)


@app.route("/resultado", methods=['POST', 'GET'])
def resultados():
    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        tipo = (request.form.get("group1"))
        print(tipo)
        total = 0
        if tipo == "+":
            total=num1+num2
        elif tipo == "-":
            total=num1-num2
        elif tipo == "x":
            total=num1*num2
        elif tipo == "/":
            total=num1/num2
        else:
            total = 0
        print(total)
        return render_template("index.html", value=total, num1=num1, num2=num2)

@app.route('/cinepolis', methods=['GET'])
def cinepolis():
    return render_template('cinepolis.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form.get('nombre')
    numPersonas = int(request.form.get('numPersonas', 1))
    cantidad = int(request.form.get('cantidad', 1))
    tieneTarjeta = request.form.get('tieneTarjeta') == 'on'
    
    boleto = Boleto(nombre, numPersonas, cantidad, tieneTarjeta)
    valido, mensaje = boleto.validar_cantidad()
    total = None
    if valido:
        total = boleto.calcular_total()
    
    return render_template('cinepolis.html', mensaje=mensaje, total=total) 

@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    mat=''
    nom=''
    ape=''
    email=''
    alumno_clase = forms.UserForm(request.form)
    if request.method == "POST":
        mat = alumno_clase.matricula.data
        nom = alumno_clase.nombre.data
        ape = alumno_clase.apellido.data
        email = alumno_clase.email.data

        print(f'Nombre: {nom}')
    return render_template("Alumnos.html", form=alumno_clase)

# Cinepolis Flask
if __name__=="__main__":
    app.run(debug=True,port=3000)