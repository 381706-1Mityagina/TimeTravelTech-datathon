import numpy as np
import cv2
import tensorflow as tf

from PIL import Image

saved_model_path = "../../cv_module/models/inception_v3"
LOADED = tf.saved_model.load(saved_model_path)
IMAGE_SIZE = (299, 299)
normalization_layer = tf.keras.layers.Rescaling(1. / 255)

CLASS_NAMES = {
        "camille pissarro": "Impressionism",
        "claude monet": "Impressionism",
        "edgar degas": "Impressionism",
        "ivan aivazovsky": "Romanticism",
        "vincent van gogh": "Realism",
    }

def get_author_and_genre(image_path):
    # image preparation
    img = cv2.imread(image_path)
    # Convert the image to RGB format
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    image = tf.image.resize(img, IMAGE_SIZE)

    # Apply normalization if needed
    normalization = normalization_layer(image)
    img_array = tf.expand_dims(normalization, 0)

    # inference classification model
    prediction_scores = LOADED(img_array)
    predicted_index = np.argmax(prediction_scores)
    
    artist, genre = list(CLASS_NAMES.items())[predicted_index]

    return artist, genre
