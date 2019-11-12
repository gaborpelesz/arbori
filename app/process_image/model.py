import json
import numpy as np
from tensorflow.keras.models import load_model
from keras.applications.resnet50 import preprocess_input

from process_image.base64_img import base64_to_image

class ClassifyImage:
    def __init__(self,  input_size=(224,224),
                        model_path='model/object_classification.h5',
                        label_path='model/labels.json'):
        self.model = load_model(model_path)

        # load labels
        with open(label_path) as label_file:
            data = label_file.read().replace('\n', '').replace("'", '"')
            json_data = json.loads(data)

        self.labels = json_data
        self.input_size = input_size

    def predict_base64(base64_str):
        img = base64_to_image(base64_str)
        img = tf.image.resize(np.array([img]), input_size)[0]

        preprocessed_img = preprocess_input(img)

        predictions = self.model.predict(np.array([x]))[0]

        highest_pred_index = np.where(predictions == max(predictions))[0][0]

        # map the correct label with the highest prediction's index
        for label, label_num in self.labels.items():
            if label_num == highest_pred_index:
                return label_num
        raise Exception("Couldn't find matching prediction index and label number...")