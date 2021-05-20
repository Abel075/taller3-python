from flask import Flask
from flask import render_template #metodo para retornar la plantilla en template
#from flask_sqlalchemy import SQLAlchemy  #Libreria de base de datos

# import os

#dbdir = "sqlite:///" +os.path.abspath(os.gtwcwd()) + "/database.db"

#Archivo principal de la aplicacion
app = Flask(__name__)
#Base de datos
# app.config["SQLAlchemy_DATABASE_URI"] = dbdir
# db = SQLAlchemy(app)

#Rutas @
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hardware')
def hardware():
    return render_template('hardware.html')

@app.route('/armado_de_pc')
def armado():
    return render_template('arma_tu_pc.html')

@app.route('/pc_armadas')
def armadas():
    return render_template('pc_armadas.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/mi_cuenta')
def mi_cuenta():
    return render_template('mi_cuenta.html')

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')

@app.route('/acceso')
def acceso():
    return render_template('acceso.html')

#Archivo que arranca la aplicacion
if __name__ == '__main__':
    app.run(debug=True)