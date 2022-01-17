#Importamos flask, render_template y los modulos
from flask import Flask, render_template #Render_template sirve para poder conectar un template a la app
import Dolar_oficial
import Dolar_blue
import Dolar_turista

#Creamos la app
app = Flask(__name__)

#Usamos el decorador para decirle que es la pagina principal, siempre a acompañado de la funcion que tiene que ejecutar
@app.route("/")
def index():
    return render_template("index.html", poc = Dolar_oficial.decimeDolar(), pov= Dolar_oficial.decimeDolarVenta(), pbc= Dolar_blue.decimeDolar(), pbv= Dolar_blue.decimeDolarVenta(), ptv = Dolar_turista.decimeDolarVenta())

#Corremos la app
if __name__ == '__main__':
    app.run(debug=True)