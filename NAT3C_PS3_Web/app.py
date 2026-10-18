from flask import Flask, render_template

app = Flask(__name__)

SERVICIOS = [
    ("Instalación de HEN", "$12.000", "Configuración del sistema HEN para PS3 compatibles."),
    ("Reinstalación / reparación de HEN", "$7.000", "Revisión y reinstalación del entorno."),
    ("Instalación de todas las tiendas", "$5.000", "Configuración de las tiendas indicadas por el cliente."),
    ("HEN + tiendas", "$17.000", "Pack de configuración de HEN y tiendas."),
    ("1 juego", "$1.500", "Instalación de un juego proporcionado o autorizado por el cliente."),
    ("3 juegos", "$4.500", "Instalación de hasta tres juegos proporcionados o autorizados."),
    ("5 juegos", "$7.500", "Instalación de hasta cinco juegos proporcionados o autorizados."),
    ("10 juegos", "$15.000", "Instalación de hasta diez juegos proporcionados o autorizados."),
    ("HEN + tiendas + 5 juegos", "$24.5000", "Pack completo de configuración."),
    ("HEN + tiendas + 10 juegos", "$32.000", "Pack completo de configuración."),
]

@app.route("/")
def inicio():
    return render_template("index.html", servicios=SERVICIOS)

if __name__ == "__main__":
    app.run(debug=True)
