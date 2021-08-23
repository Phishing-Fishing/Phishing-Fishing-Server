import pandas as pd
import numpy as np
import os

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from preprocessing import *
import joblib


def classify(url):
    clf = joblib.load("Phishing-Fishing-Server/model.joblib")
    data = preprocessing(url)

    y_pred = clf.predict(data)

    return y_pred[0]


# def train_random_forest_with_params(X, y, params):
#     model = RandomForestClassifier()
#     model.set_params(**params)
#     model = model.fit(X, y)
#     score = model.score(X, y)
#     return model