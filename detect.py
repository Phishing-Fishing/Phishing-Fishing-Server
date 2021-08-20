import pandas as pd
import numpy as np
import os

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(train_data, target, test_size = 0.25, random_state = 123456)

clf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state = 123456)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

print('Model accuracy score with 10 decision-trees : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))