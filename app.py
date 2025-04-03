from flask import Flask, jsonify, render_template, request
from preprocessing import preprocessWText
from flask_cors import CORS
import os


os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU usage
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # Disable oneDNN optimizations
import tensorflow as tf
from tensorflow import keras


app = Flask(__name__, template_folder="templates")
MODEL_PATH = "spam_detector_model.h5"
model = None



CORS(app)


def get_model():
    global model
    if model is None:
        print("Loading model...")
        model = keras.models.load_model(MODEL_PATH)
        print("Model loaded.")
    return model
@app.route('/')
def index():
    return render_template('index.html')



@app.route("/detectSpam", methods=["POST"])
def use_model():
    try:
        input_text = request.json['text']
        print(f"Received input: {input_text}")  # Log the received input
        input_vectorized = preprocessWText(input_text)
        model = get_model()
        prediction = model.predict(input_vectorized)
        print(f"Prediction: {prediction}")  # Log the prediction
        result = "Spam" if prediction[0] > 0.5 else "Not Spam"
        print(f"Result: {result}")  # Log the result
        return jsonify({"prediction": result})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    PORT = int(os.getenv("PORT", 8080))  # Ensure port is an integer
    app.run(host="0.0.0.0", port=PORT, debug=False)