from flask import Flask, jsonify, render_template
import tensorflow as tf
from tensorflow import keras


app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    return render_template('index.html')



@app.route("/detectSpam", methods=["GET"])
def use_model():
    model = tf.keras.models.load_model('spam_detector_model.h5')


if __name__ == '__main__':
    app.run(port=5000, debug=True)