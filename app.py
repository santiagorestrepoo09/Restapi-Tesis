from flask import Flask, request
from Prediccion import predecir
import urllib.request

app = Flask(__name__)

@app.route("/predecirneumotorax", methods=["POST"])
def predecirPneumothorax():
    imagen = request.args.get("imagen")
    ruta = "/home/santiago/Documentos/Proyecto_Chatboot/rest-api/img/Neumotorax/imagen.jpg"
    urllib.request.urlretrieve(imagen,ruta)
    result = predecir.predecirPneumothorax(ruta)
    return result


@app.route("/predecirpneumonia", methods=["POST"])
def predecirPneumonia():
    imagen = request.args.get("imagen")
    ruta = "/home/santiago/Documentos/Proyecto_Chatboot/rest-api/img/Neumonia/imagen.jpg"
    urllib.request.urlretrieve(imagen,ruta)
    result = predecir.predecirneumonia(ruta)
    return result

if __name__=="__main__":
  app.run(debug=False) 