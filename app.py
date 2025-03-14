from flask import Flask, jsonify, render_template, request
import tensorflow as tf
from tensorflow import keras


app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    return render_template('index.html')



@app.route("/detectSpam", methods=["POST"])
def use_model():
    model = keras.models.load_model('spam_detector_model.h5')
    input = request.json['text']
    print(input)


if __name__ == '__main__':
    app.run(port=5000, debug=True)