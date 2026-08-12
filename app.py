from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola contratenme  funcionoooooooo conecte servicio circle con aws ahora si estoy en la cima Y LO HICE DENUEVOOO CONTRATENMEEEE DIOS MIO PORFIN AUTOMATIZE TODOODODODODODOD!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)