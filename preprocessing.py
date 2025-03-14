import pandas as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np


def preprocess():
    df = pd.read_csv("spam_or_not_spam.csv")
    emails = df["email"].to_numpy().astype(str)
    vectorizer = keras.layers.TextVectorization(max_tokens = 15000, output_sequence_length=50, output_mode="int")
    vectorizer.adapt(emails)
    X = vectorizer(emails)
    X = X.numpy()
    y = df["label"].to_numpy().astype(int)
    return X, y


def preprocessWText(text):
    df = pd.read_csv("spam_or_not_spam.csv")
    emails = df["email"].to_numpy().astype(str)
    vectorizer = keras.layers.TextVectorization(max_tokens = 15000, output_sequence_length=50, output_mode="int")
    vectorizer.adapt(emails)
    text_vectorized = vectorizer(tf.constant([text]))
    return text_vectorized.numpy()