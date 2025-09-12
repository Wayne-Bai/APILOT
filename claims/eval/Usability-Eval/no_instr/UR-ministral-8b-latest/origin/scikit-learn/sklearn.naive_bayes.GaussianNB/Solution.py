from sklearn.naive_bayes import GaussianNB
import numpy as np

# Initialize the Gaussian Naive Bayes model
model = GaussianNB()

# Example training data
X_train = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]])
y_train = np.array([0, 1, 0])

# Fit the model with the training data
model.partial_fit(X_train, y_train, classes=np.unique(y_train))
