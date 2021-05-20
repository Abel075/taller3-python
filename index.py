from flask import Flask
from flask import render_template #metodo para retornar la plantilla en template

#Archivo principal de la aplicacion
app = Flask(__name__)

#Rutas @
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')




#Archivo que arranca la aplicacion
if __name__ == '__main__':
    app.run(debug=True)