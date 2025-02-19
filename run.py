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
    lista = "<h3>Provincias del Ecuador</h3><ol><li>Guayas</li><li>Loja</li><li>Pichincha</li><li>Carchi</li><li>El Oro</li></ol>"  
    return lista

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
