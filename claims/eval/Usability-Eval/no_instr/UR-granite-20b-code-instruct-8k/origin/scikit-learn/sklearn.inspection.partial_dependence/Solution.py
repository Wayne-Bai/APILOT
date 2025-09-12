from sklearn.inspection import plot_partial_dependence
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import numpy as np

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train a logistic regression model on the dataset
clf = LogisticRegression()
clf.fit(X, y)

# Compute partial dependence plots for the first and second features
features = [0, 1]
plot_partial_dependence(clf, X, features)
