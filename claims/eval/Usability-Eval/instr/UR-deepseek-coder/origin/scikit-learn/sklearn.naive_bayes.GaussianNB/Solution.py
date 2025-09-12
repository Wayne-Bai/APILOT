import numpy as np
from sklearn.naive_bayes import GaussianNB

# Example data
X_train = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y_train = np.array([0, 1, 0, 1])

# Initialize the Gaussian Naive Bayes model
gnb = GaussianNB()

# Fit the model with the initial training data
gnb.fit(X_train, y_train)

# Example new data for online updates
X_new = np.array([[9, 10]])
y_new = np.array([1])

# Perform online updates to the model parameters
gnb.partial_fit(X_new, y_new)

# Predict using the updated model
X_test = np.array([[1, 2], [9, 10]])
predictions = gnb.predict(X_test)

print(predictions)
