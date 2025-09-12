import numpy as np
from sklearn.naive_bayes import GaussianNB

# Initialize the Gaussian Naive Bayes model
gnb = GaussianNB()

# Example data
X_train = np.array([[1, 2], [3, 4], [5, 6]])
y_train = np.array([0, 1, 0])

# Fit the model with initial data
gnb.fit(X_train, y_train)

# Example new data for online update
X_new = np.array([[7, 8]])
y_new = np.array([1])

# Perform online update using partial_fit
gnb.partial_fit(X_new, y_new)

# Predict on new data
X_test = np.array([[1, 2], [7, 8]])
predictions = gnb.predict(X_test)

print(predictions)
