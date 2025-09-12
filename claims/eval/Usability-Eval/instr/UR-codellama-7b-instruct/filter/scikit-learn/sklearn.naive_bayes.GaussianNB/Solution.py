
import numpy as np
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

# Train a Gaussian Naive Bayes (GaussianNB) model on the training set
gnb = GaussianNB()
gnb.fit(X, y)

# Evaluate the model on the test set
X_test = iris.data[50:100, :2]
y_test = iris.target[50:100]
accuracy = gnb.score(X_test, y_test)
print("Accuracy: %.2f" % accuracy)
