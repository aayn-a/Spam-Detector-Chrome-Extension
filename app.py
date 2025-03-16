from flask import Flask, jsonify, render_template, request
import tensorflow as tf
from tensorflow import keras
from preprocessing import preprocessWText
from flask_cors import CORS


app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    global model
    model = keras.models.load_model('spam_detector_model.h5')
    return render_template('index.html')



@app.route("/detectSpam", methods=["POST"])
def use_model():
    input = request.json['text']
    input_vectorized = preprocessWText(input)
    prediction = model.predict(input_vectorized)
    print(prediction)
    print("Spam" if prediction > 0.5 else "Not Spam")
    return jsonify({"prediction": "Spam" if prediction[0] > 0.5 else "Not Spam"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)