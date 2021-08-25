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
    clf = joblib.load("model.joblib")
    data = preprocessing(url)

    y_pred = clf.predict(data)

    return y_pred[0]