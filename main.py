
from flask import Flask
from flask import render_template
from flask import request
import re

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html')

@app.route('/buscar_por_nombre', methods=['POST', 'GET'])
def mostrar_por_nombre():

    patron1 = re.compile("'\s?--|.*'\s?(OR|or)\s.+=.+$") #' OR '1'=1

    patron2 = re.compile(".+';\s(DROP|drop)\s(TABLE|table)\s.+\s?--$") #Juan Perez'; DROP TABLE Cliente; --

    if request.method == 'POST':
        nombre = request.form['nombre']
        if patron1.match(nombre):
            print("patron1")
            return render_template('error_busqueda.html', dato=nombre)
        elif patron2.match(nombre):
            print("patron2")
            return render_template('error_busqueda.html', dato=nombre)
        else:
            return render_template('busqueda.html', dato=nombre)

@app.route('/buscar_por_id', methods=['POST', 'GET'])
def buscar_por_id():

    patron = re.compile("\d;\s(DROP|drop)\s(TABLE|table)\s.+$") #1; DROP TABLE cliente

    if request.method == 'POST':
        numero = request.form['id']
        if patron.match(numero):
            print("true")
            return render_template('error_busqueda.html', dato=numero)
        else:
            print("false")
            return render_template('busqueda.html', dato=numero)


if __name__ == '__main__':
    app.run(debug=True)
