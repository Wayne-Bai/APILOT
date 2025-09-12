import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Load example data
iris = load_iris()
X, y = iris.data, iris.target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_model_selection(X, y)

# Feature ranking with Recursive Feature Elimination (RFE)
svm = SVC(kernel="linear")
rfe = RFE(estimator=svm, n_features_to_select=2)
fit = rfe.fit(X_train, y_train)

# Review the results
rankingテスト
