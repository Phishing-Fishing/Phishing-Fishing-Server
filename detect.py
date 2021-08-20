import pandas as pd
import numpy as np
import os

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from preprocessing import *

# x_train, x_test, y_train, y_test = train_test_split(train_data, target, test_size = 0.25, random_state = 123456)
# print('Model accuracy score with 10 decision-trees : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

params = {"bootstrap":"True", "ccp_alpha":0.0, "class_weight":"None",
    "criterion":'gini', "max_depth":"None", "max_features":'auto',
    "max_leaf_nodes":"None", "max_samples":"None",
    "min_impurity_decrease":0.0, "min_impurity_split":"None",
    "min_samples_leaf":1, "min_samples_split":2,
    "min_weight_fraction_leaf":0.0, "n_estimators":100,
    "n_jobs":"None", "oob_score":"True", "random_state":123456,
    "verbose":0, "warm_start":"False"}

def classify(url):
    clf = RandomForestClassifier()
    clf.set_params(**params)

    data = preprocessing(url)
    # clf.fit(x_train, y_train)

    y_pred = clf.predict(data)
    # score = clf.score(testing_points, testing_labels)

    return y_pred


def train_random_forest_with_params(X, y, params):
    model = RandomForestClassifier()
    model.set_params(params)
    model = model.fit(X, y)
    score = model.score(X, y)
    return model