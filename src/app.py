import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from flask import Flask, request, jsonify
import cv2

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('path/to/your/model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    img = image.load_img(file, target_size=(300, 300))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    result = 'Pneumonia' if prediction[0][0] >= 0.5 else 'Normal'

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)