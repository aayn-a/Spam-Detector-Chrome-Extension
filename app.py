from flask import Flask, jsonify
from training import train



app = Flask(__name__)


@app.route('/train-model', methods=['GET'])
def train_model():
    train()
    return jsonify({"message": "Model training complete"})