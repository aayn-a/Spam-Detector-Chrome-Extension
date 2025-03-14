from flask import Flask, jsonify
from training import train
import tensorflow as tf
from tensorflow import keras


app = Flask(__name__)


@app.route('/train-model', methods=['GET'])
def train_model():
    train()



@app.route("/detectSpam", methods=["GET"])
def use_model():
    model = tf.keras.models.load_model('spam_detector_model.h5')
