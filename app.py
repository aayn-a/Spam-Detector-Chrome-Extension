from flask import Flask, jsonify, render_template, request
import tensorflow as tf
from tensorflow import keras
from preprocessing import preprocessWText
from flask_cors import CORS


tf.config.set_visible_devices([], "GPU")  # Disable GPU use
tf.config.experimental.set_memory_growth(tf.config.list_physical_devices('CPU')[0], True)
app = Flask(__name__, template_folder="templates")
model = None

def get_model():
    global model
    if model is None:
        model = keras.models.load_model('spam_detector_model.h5')
    return model


@app.route('/')
def index():
    return render_template('index.html')



@app.route("/detectSpam", methods=["POST"])
def use_model():
    input = request.json['text']
    input_vectorized = preprocessWText(input)
    prediction = get_model().predict(input_vectorized)
    print(prediction)
    print("Spam" if prediction > 0.5 else "Not Spam")
    return jsonify({"prediction": "Spam" if prediction[0] > 0.5 else "Not Spam"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)