from flask import Flask, template_rendered, request
from flask_cors import CORS

#Primer commit de flask

app = Flask(__name__)
CORS(app)

@app.route("/saludo", methods=['GET'])
def saludo():
    msg = request.args.get("msg", "Mundo")
    return f"Hola {msg}"

@app.route("/home")
def home():
    return template_rendered("<h1>Bienvenido</h1>")

if __name__ == "__main__":
    app.run(port=8080, debug=True)