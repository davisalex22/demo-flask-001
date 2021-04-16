"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo con Flask</h1>"

@app.route('/suma')
def suma():
    resultado = 10 + 10
    return "<h3>10 + 10 = %d</h3>" % (resultado)


@app.route('/listado')
def listado():
    lista = "Guayas \n + Loja\n + Azuay\n + Pichincha\n + El Oro\n + Manabí\n + Carchi\n "
    return lista

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
