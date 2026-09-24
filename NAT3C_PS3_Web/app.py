from flask import Flask, render_template

app = Flask(__name__)

SERVICIOS = [
    ("Instalación de HEN", "$15.000", "Configuración del sistema HEN para PS3 compatibles."),
    ("Reinstalación / reparación de HEN", "$10.000", "Revisión y reinstalación del entorno."),
    ("Instalación de todas las tiendas", "$5.000", "Configuración de las tiendas indicadas por el cliente."),
    ("HEN + tiendas", "$20.000", "Pack de configuración de HEN y tiendas."),
    ("1 juego", "$3.000", "Instalación de un juego proporcionado o autorizado por el cliente."),
    ("3 juegos", "$9.000", "Instalación de hasta tres juegos proporcionados o autorizados."),
    ("5 juegos", "$15.000", "Instalación de hasta cinco juegos proporcionados o autorizados."),
    ("10 juegos", "$30.000", "Instalación de hasta diez juegos proporcionados o autorizados."),
    ("HEN + tiendas + 5 juegos", "$35.000", "Pack completo de configuración."),
    ("HEN + tiendas + 10 juegos", "$50.000", "Pack completo de configuración."),
]

@app.route("/")
def inicio():
    return render_template("index.html", servicios=SERVICIOS)

if __name__ == "__main__":
    app.run(debug=True)
