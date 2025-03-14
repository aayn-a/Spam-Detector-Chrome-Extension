from sklearn.utils import compute_class_weight
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from preprocessing import preprocess


X, y = preprocess()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = keras.Sequential([
    keras.layers.Input(shape=(50,)),
    keras.layers.Embedding(15000, 32),
    keras.layers.Bidirectional(keras.layers.LSTM(64, return_sequences=False)),  
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(32, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid"),
])


class_labels = np.unique(y)
class_weights = compute_class_weight(class_weight="balanced", classes=class_labels, y=y)
class_weight_dict = {i: class_weights[i] for i in range(len(class_weights))}
optimizer = keras.optimizers.Adam(learning_rate = 0.001)
model.compile(optimizer=optimizer, loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=20)
