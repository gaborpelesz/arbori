import time
import json
from flask import Flask, request, redirect, jsonify
from flask_api import FlaskAPI, status
from process_image.model import ClassifyImage
from process_image.base64_img import base64_to_image

app = FlaskAPI(__name__)
model = ClassifyImage()

@app.route("/predict", methods=["POST"])
def predict():

    if request.method == "POST" and request.is_json:
        content = request.get_json()

        try:
            base64_image = content["image"]
        except KeyError as e:
            return {
                "status": "Failed",
                "status_message": "Missing the 'image' property of the JSON object.",
                "error_message": str(e)
            }, status.HTTP_400_BAD_REQUEST

        if model:
            inference_start = time.time()
            img = base64_to_image(base64_image)
            label, prob = model.predict(img)
            print(label, prob)
            inference_end = time.time()
            return json.dumps({
                    "status": "Success",
                    "prediction": {
                        "class": str(label),
                        "probability": str(prob)
                    },
                    "processing_runtime": '{:.3f}ms'.format((inference_end - inference_start)*1000)
                })

        return {
                "status": "Failed",
                "error_message": "The model wasn't initialized properly. There might be a bug in the code.",
            }, status.HTTP_500_INTERNAL_SERVER_ERROR
        
        

def main():
    app.run(host='0.0.0.0', port=3000)