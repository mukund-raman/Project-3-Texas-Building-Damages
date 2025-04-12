from flask import Flask, request
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)
model = tf.keras.models.load_model('vgg_16_model.keras')

@app.route('/summary', methods=['GET'])
def model_info():
    return {
        'name': 'Texas Building Damage Classification',
        'model_architecture': 'VGG-16',
        'version': 'v1',
        'description': 'Classify images of buildings as damaged or ' + \
            'not damaged.',
        'number_of_parameters': model.count_params()
    }

@app.route('/inference', methods=['POST'])
def classify_building_image():
    # Check if the post request has the file part
    if 'image' not in request.files:
      # If the user did not pass the image under `image`, return an error.
      return '{"error": "Invalid request; pass a binary image file as a \
              multi-part form under the image key."}'
    # Get the data
    data = request.files['image']
    
    # Preprocess the image data as needed
    image = Image.open(data).convert('RGB')
    image = image.resize((150, 150))
    img_array = np.expand_dims(np.array(image) / 255.0, axis=0)
    
    # Run the model on the image and return the prediction
    predicted_class = np.argmax(model.predict(img_array)[0])
    predicted_label = ['damage', 'no_damage'][predicted_class]
    return { 'prediction': predicted_label }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')