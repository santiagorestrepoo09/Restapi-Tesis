from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from PIL import Image
import urllib.request
import tensorflow as tf
import numpy as np

def predecirPneumothorax(url):
    model = load_model("/home/santiago/Documentos/Proyecto_Chatboot/rest-api/modelNeumotorax.h5",compile=False)
    img = image.load_img(url, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    img_data = preprocess_input(x)
    classes = model.predict(img_data)
    result = int(classes[0][0])
    resultado = classes[0]
    respuesta = np.argmax(resultado)  ##[1]
    predict = ""
    if result == 0:
        predict = "Neumotorax"
    else:
        predict = "Normal"
    return predict

def predecirneumonia(url):
    model = load_model("/home/santiago/Documentos/Proyecto_Chatboot/rest-api/model_Neumonia_vgg16.h5")
    img = image.load_img(url, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    img_data = preprocess_input(x)
    classes = model.predict(img_data)
    result = int(classes[0][0])
    resultado = classes[0]
    respuesta = np.argmax(resultado)  ##[1]
    predict = ""
    if result == 0:
        predict = "Neumonia"
    else:
        predict = "Normal"
    return predict