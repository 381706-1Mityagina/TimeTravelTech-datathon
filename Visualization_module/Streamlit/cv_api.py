import numpy as np
from flask import Flask, request
import cv2
import tensorflow as tf

flask_app = Flask(__name__)

saved_model_path = "../../CV preparation/models/inception_v3"
LOADED = tf.saved_model.load(saved_model_path)
IMAGE_SIZE = (299, 299)
normalization_layer = tf.keras.layers.Rescaling(1. / 255)

api_prefix = "/predict"


@flask_app.route("/")
def home():
    return "Artist classification"


@flask_app.route(api_prefix + "/artist", methods=['POST'])
def predict():

    # image preparation
    img = np.frombuffer(request.data, np.uint8)
    img = cv2.imdecode(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = tf.image.resize(img, IMAGE_SIZE)
    normalization = normalization_layer(image)
    img_array = tf.expand_dims(normalization, 0)

    # inference classification model
    prediction_scores = LOADED(img_array)
    predicted_index = np.argmax(prediction_scores)
    return str(predicted_index)


if __name__ == "__main__":
    flask_app.run('localhost', 7777)
